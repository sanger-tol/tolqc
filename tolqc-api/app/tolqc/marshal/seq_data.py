# SPDX-FileCopyrightText: 2024 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

import json
import logging
import re
from datetime import datetime

from sqlalchemy import and_, inspect, select

from tolqc.sample_data_models import (
    Accession,
    AccessionTypeDict,
    Allocation,
    Centre,
    Data,
    File,
    Library,
    LibraryType,
    PacbioRunMetrics,
    Platform,
    Project,
    Run,
    Sample,
    Species,
    Specimen,
)


def load_seq_data_stream(
    session,
    stream,
    centre_name='Wellcome Sanger Institute',
):
    centre = get_centre(session, centre_name)
    new_data = []
    upd_data = []
    for row in ndjson_rows(stream):
        new, upd = store_seq_data_row(session, centre, row)
        if new:
            new_data.append(headline_data_fields(new))
        if upd:
            upd_data.append(updated_data_fields(upd))
    return {
        'new': new_data,
        'updated': upd_data,
    }


def ndjson_rows(stream):
    for line in stream:
        yield parse_ndjson_row(line)


def parse_ndjson_row(line):
    if len(line) > 100_000:
        # Don't get hung up parsing excessively large strings
        msg = f'Unexpectedly long line ({len(line):_d} characters) in input'
        raise ValueError(msg)
    row = json.loads(line)
    if type(row) is not dict:  # noqa: E721
        msg = f'JSON must decode to a dict, not a {type(row)}'
        raise ValueError(msg)
    for k, v in row.items():
        if type(v) in (dict, list):
            # Don't allow collections to be smuggled in the values
            msg = 'Values of JSON row must all be scalars'
            raise ValueError(msg)
        if type(v) is str:  # noqa: E721
            # Avoid empty strings
            stripped = v.strip()
            row[k] = None if stripped == '' else stripped
    return row


def headline_data_fields(data):
    # Specimen and species may not always be present
    specimen_id = None
    species_id = None
    sample_id = None
    if smpl := data.sample:
        sample_id = smpl.sample_id
        if spcmn := smpl.specimen:
            specimen_id = spcmn.specimen_id
            species_id = spcmn.species_id

    return {
        'name': data.name,
        'specimen': specimen_id,
        'species': species_id,
        'library_type': data.library.library_type_id,
        'sample': sample_id,
        # Project will always be present for data loaded from the MLWH
        'project': data.projects[0].description,
    }


def updated_data_fields(data):
    state = inspect(data)
    changes = {}
    for col_name in state.mapper.columns.keys():  # noqa: SIM118
        attr = state.attrs[col_name]
        hist = attr.history
        if hist.has_changes():
            changes[col_name] = hist.deleted[0], hist.added[0]

    fields = headline_data_fields(data)
    fields['changes'] = changes
    return fields


def store_seq_data_row(session, centre, row) -> (None | Data, None | Data):
    data = get_data(session, row)
    if data:
        # The QC decisions *might* have changed so update these fields
        data.lims_qc = row['lims_qc']
        data.date = maybe_datetime(row, 'qc_date')
        if session.is_modified(data, include_collections=False):
            return None, data
        else:
            return None, None

    # No need to flush until we've built the Data object and attached
    # everything to it. If autoflush is on, warnings are generated about some
    # of the attached objects which haven't been added to the Session.
    with session.no_autoflush:
        data = build_data(session, centre, row)
        session.add(data)
        session.flush()

    return data, None


def build_data(session, centre, row):
    alloc = build_project_allocation(session, row)
    run = build_run(session, row, centre)

    data = Data(
        # Data fields
        name=row['name'],
        processed=0,  # Setting processed to 0 flags new data
        tag_index=row.get('tag_index'),  # Illumina only field
        tag1_id=row['tag1_id'],
        tag2_id=row['tag2_id'],
        lims_qc=row['lims_qc'],
        date=maybe_datetime(row, 'qc_date'),
        # Related objects
        project_assn=alloc,
        run=run,
    )
    if sample := build_sample(session, row):
        data.sample = sample
    if library := build_library(session, row):
        data.library = library
    if files := build_files(row):
        data.files = files

    return data


def build_files(row):
    path = row['irods_path']
    if not path:
        return None
    file_name = row['irods_file']
    if not file_name:
        msg = row_message(row, "'irods_path' set but no 'irods_file' field in row")
        raise ValueError(msg)

    rp = 'irods:' + path.rstrip('/') + '/' + file_name
    file = File(remote_path=rp)
    return [file]


def build_pacbio_run_metrics(row):
    pbrm = PacbioRunMetrics()
    for fld in (
        'movie_minutes',
        'binding_kit',
        'sequencing_kit',
        'include_kinetics',
        'loading_conc',
        'control_num_reads',
        'control_read_length_mean',
        'polymerase_read_bases',
        'polymerase_num_reads',
        'polymerase_read_length_mean',
        'polymerase_read_length_n50',
        'insert_length_mean',
        'insert_length_n50',
        'unique_molecular_bases',
        'p0_num',
        'p1_num',
        'p2_num',
        'hifi_read_bases',
        'hifi_num_reads',
        'hifi_low_quality_num_reads',
    ):
        setattr(pbrm, fld, row[fld])
    return [pbrm]


def build_project_allocation(session, row):
    project = session.scalars(
        select(Project).where(Project.lims_id == row['study_id'])
    ).one()
    return [Allocation(project=project)]


# Should this mapping be done on the client side?
PIPELINE_TO_LIBRARY_TYPE = {
    'PacBio_Ultra_Low_Input': 'PacBio - HiFi (ULI)',
    'PacBio_Ultra_Low_Input_mplx': 'PacBio - HiFi (ULI)',
    'Pacbio_HiFi': 'PacBio - HiFi',
    'Pacbio_HiFi_mplx': 'PacBio - HiFi',
    'Pacbio_IsoSeq': 'PacBio - IsoSeq',
    'PacBio_IsoSeq_mplx': 'PacBio - IsoSeq',
    'Pacbio_Microbial_mplx': 'PacBio - HiFi (Microbial)',
}


def build_library_type(session, row):
    pipeline_id_lims = row['pipeline_id_lims']
    if pipeline_id_lims is None:
        return None
    ltid = PIPELINE_TO_LIBRARY_TYPE.get(pipeline_id_lims, pipeline_id_lims)
    if lib_type := session.get(LibraryType, ltid):
        return lib_type
    return LibraryType(library_type_id=ltid)


def build_library(session, row):
    lib_id = row['library_id']
    if not lib_id:
        return None
    if lib := session.get(Library, lib_id):
        return lib
    lib_type = build_library_type(session, row)
    return Library(library_id=lib_id, library_type=lib_type)


def build_run(session, row, centre):
    run_id = row['run_id']
    if not run_id:
        msg = row_message(row, "Missing 'run_id' field in row")
        raise ValueError(msg)
    if run := get_by_pk_if_value(session, Run, run_id):
        return run
    platform = build_platform(session, row)
    run_metrics = []
    if platform.name == 'PacBio':
        run_metrics = build_pacbio_run_metrics(row)

    return Run(
        run_id=row['run_id'],
        instrument_name=row['instrument_name'],
        start=maybe_datetime(row, 'run_start'),  # PacBio only field
        complete=maybe_datetime(row, 'run_complete'),
        lims_id=row.get('lims_run_id'),  # PacBio only field
        element=row.get('well_label'),  # PacBio only field
        plex_count=row.get('plex_count'),
        centre=centre,
        platform=platform,
        pacbio_run_metrics=run_metrics,
    )


def build_sample(session, row):
    sample_name = row['sample_name']
    if not sample_name:
        return None
    if smpl := session.get(Sample, sample_name):
        return smpl

    spcmn = None
    if spcmn_id := row['tol_specimen_id']:
        spcmn = session.get(Specimen, spcmn_id)
        if not spcmn and re.match(r'[a-z]{1,2}[A-Z][a-z]', spcmn_id):
            # Beginning of specimen ID looks like a ToL ID
            specimen_acc = accession_if_valid(
                session,
                'Bio Sample',
                row['biospecimen_accession'],
            )
            species = build_species(session, row)
            spcmn = Specimen(
                specimen_id=spcmn_id,
                accession=specimen_acc,
                supplied_name=row['supplier_name'],
                species=species,
            )

    sample_acc = accession_if_valid(
        session,
        'Bio Sample',
        row['biosample_accession'],
    )

    # Create a new Sample
    smpl = Sample(
        sample_id=sample_name,
        specimen=spcmn,
        accession=sample_acc,
    )
    return smpl


def build_species(session, row):
    sci_name = row['scientific_name']
    if not sci_name:
        return None

    if species := session.get(Species, sci_name):
        return species

    hn = re.sub(r'\W+', '_', sci_name).strip('_')
    return Species(
        species_id=sci_name,
        hierarchy_name=hn,
        taxon_id=row['taxon_id'],
    )


def build_platform(session, row):
    name = row['platform_type']
    model = row['instrument_model']

    if platform := session.scalars(
        select(Platform).where(
            and_(
                Platform.name == name,
                Platform.model == model,
            )
        )
    ).one_or_none():
        return platform
    return Platform(name=name, model=model)


def get_by_pk_if_value(session, cls, pk_value):
    if pk_value:
        return session.get(cls, pk_value)
    return None


def get_centre(session, centre_name):
    return session.scalars(select(Centre).where(Centre.name == centre_name)).one()


def get_data(session, row):
    if name := row.get('name'):
        return session.scalars(
            select(Data).where(Data.name == name)
        ).one_or_none()
    msg = row_message(row, "Missing 'name' field in row")
    raise ValueError(msg)


def maybe_datetime(row, field):
    if dt_str := row.get(field):
        return datetime.fromisoformat(dt_str)
    return None


def accession_if_valid(session, accn_type, accn_str):
    """
    Returns an Accession object if supplied with a valid accession string.
    Creates a new Accession object if it is not in the database.
    """
    if valid_accession(session, accn_type, accn_str):
        if acc_obj := session.get(Accession, accn_str):
            return acc_obj
        acc_obj = Accession(
            accession_id=accn_str,
            accession_type_id=accn_type,
        )
        # session.add(acc_obj)
        return acc_obj
    return None


def valid_accession(session, accn_type, accn_str):
    if accn_str:
        atd = session.get(AccessionTypeDict, accn_type)
        if not atd:
            msg = f"No such AccessionTypeDict in database: '{accn_type}'"
            raise ValueError(msg)
        if atd.valid_accession(accn_str):
            return True
        else:
            logging.debug(f"Invalid '{accn_type}': '{accn_str}'")
    return False


def row_message(row, msg):
    return f'{msg}:\n{format_row(row)}'


def format_row(row):
    name_max = max(len(name) for name in row)
    return ''.join(
        f"  {name:>{name_max}} = {'' if row[name] is None else row[name]}\n"
        for name in row
    )
