# SPDX-FileCopyrightText: 2024 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

import logging
import re
from datetime import datetime

from sqlalchemy import and_, inspect, select
from sqlalchemy.exc import SQLAlchemyError

from tolqc.marshal.ndjson import must_get_row_value, ndjson_rows_from_stream
from tolqc.schema.sample_data_models import (
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
    rspns = {}
    for row in ndjson_rows_from_stream(stream):
        label, row = store_seq_data_row(session, centre, row)
        if row:
            rspns_row = (
                updated_data_fields(row)
                if label == 'updated'
                else headline_data_fields(row)
            )
            rspns.setdefault(label, []).append(rspns_row)
    return rspns


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

    lib_type_id = None
    if lib := data.library:
        lib_type_id = lib.library_type_id

    proj_desc = 'No assigned project'
    if proj_list := data.projects:
        proj_desc = proj_list[0].description

    return {
        'data_id': data.data_id,
        'specimen': specimen_id,
        'species': species_id,
        'library_type': lib_type_id,
        'sample': sample_id,
        'project': proj_desc,
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
        data.lims_qc = row.get('lims_qc')
        data.date = maybe_datetime(row, 'qc_date')
        if session.is_modified(data, include_collections=False):
            return 'updated', data
        else:
            return None, None

    # No need to flush until we've built the Data object and attached
    # everything to it. If autoflush is on, warnings are generated about some
    # of the attached objects which haven't been added to the Session.
    with session.no_autoflush:
        try:
            data = build_data(session, centre, row)
        except SQLAlchemyError:
            session.rollback()
            raise
        session.add(data)
        session.flush()

    return 'new', data


def build_data(session, centre, row):
    data = Data(
        # Data fields
        data_id=row.get('data_id'),
        study_id=row.get('study_id'),
        processed=0,  # Setting processed to 0 flags new data
        tag_index=row.get('tag_index'),  # Illumina only field
        tag1_id=row.get('tag1_id'),
        tag2_id=row.get('tag2_id'),
        lims_qc=row.get('lims_qc'),
        date=maybe_datetime(row, 'qc_date'),
    )
    if alloc := build_project_allocation(session, row):
        data.project_assn = alloc
    if sample := build_sample(session, row):
        data.sample = sample
    if library := build_library(session, row):
        data.library = library
    if files := build_files(row):
        data.files = files
    if run := build_run(session, row, centre):
        data.run = run

    return data


def build_files(row):
    if path := row.get('remote_path'):
        return [File(remote_path=path)]
    return None


def build_pacbio_run_metrics(row):
    pbrm = PacbioRunMetrics()
    have_value = False
    for fld in (
        'movie_minutes',
        'binding_kit',
        'sequencing_kit',
        'sequencing_kit_lot_number',
        'cell_lot_number',
        'include_kinetics',
        'loading_conc',
        'control_num_reads',
        'control_read_length_mean',
        'control_concordance_mean',
        'control_concordance_mode',
        'local_base_rate',
        'polymerase_read_bases',
        'polymerase_num_reads',
        'polymerase_read_length_mean',
        'polymerase_read_length_n50',
        'insert_length_mean',
        'insert_length_n50',
        'unique_molecular_bases',
        'productive_zmws_num',
        'p0_num',
        'p1_num',
        'p2_num',
        'adapter_dimer_percent',
        'short_insert_percent',
        'hifi_read_bases',
        'hifi_num_reads',
        'hifi_read_length_mean',
        'hifi_read_quality_median',
        'hifi_number_passes_mean',
        'hifi_low_quality_read_bases',
        'hifi_low_quality_num_reads',
        'hifi_low_quality_read_length_mean',
        'hifi_low_quality_read_quality_median',
        'hifi_barcoded_reads',
        'hifi_bases_in_barcoded_reads',
    ):
        v = row.get(fld)
        if v is not None:
            have_value = True
            setattr(pbrm, fld, v)
    return [pbrm] if have_value else None


def build_project_allocation(session, row):
    if study_id := row.get('study_id'):
        project = session.scalars(
            select(Project).where(Project.study_id == study_id)
        ).one()
        return [Allocation(project=project)]
    else:
        return None


def build_library_type(session, row):
    ltid = row.get('pipeline_id_lims')
    if ltid is None:
        return None
    if lib_type := session.get(LibraryType, ltid):
        return lib_type
    return LibraryType(library_type_id=ltid)


def build_library(session, row):
    lib_id = row.get('library_id')
    if not lib_id:
        return None
    if lib := session.get(Library, lib_id):
        return lib
    lib_type = build_library_type(session, row)
    return Library(library_id=lib_id, library_type=lib_type)


def build_run(session, row, centre):
    run_id = row.get('run_id')
    if not run_id:
        return None
    if run := get_by_pk_if_value(session, Run, run_id):
        return run

    platform = build_platform(session, row)
    run = Run(
        run_id=run_id,
        instrument_name=row.get('instrument_name'),
        start=maybe_datetime(row, 'run_start'),  # PacBio only field
        complete=maybe_datetime(row, 'run_complete'),
        lims_id=row.get('lims_run_id'),  # PacBio only field
        element=row.get('element'),
        plex_count=row.get('plex_count'),
        centre=centre,
        platform=platform,
    )

    if platform.name == 'PacBio' and (run_metrics := build_pacbio_run_metrics(row)):
        run.pacbio_run_metrics = run_metrics

    return run


def build_sample(session, row):
    sample_name = row.get('sample_name')
    if not sample_name:
        return None
    if smpl := session.get(Sample, sample_name):
        return smpl

    spcmn = None
    specimen_acc = None
    if spcmn_id := row.get('tol_specimen_id'):
        spcmn = session.get(Specimen, spcmn_id)
        if not spcmn and re.match(r'[a-z]{1,2}[A-Z][a-z]', spcmn_id):
            # Beginning of specimen ID looks like a ToL ID
            specimen_acc = accession_if_valid(
                session,
                'BioSample',
                row.get('biospecimen_accession'),
            )
            species = build_species(session, row)
            spcmn = Specimen(
                specimen_id=spcmn_id,
                accession=specimen_acc,
                supplied_name=row.get('supplier_name'),
                species=species,
            )

    sample_acc = accession_if_valid(
        session,
        'BioSample',
        row.get('biosample_accession'),
    )

    # Avoid trying to create two Accession objects with the same
    # accession if `biosample_accession` = `biospecimen_accession`
    if (
        sample_acc
        and specimen_acc
        and sample_acc.accession_id == specimen_acc.accession_id
    ):
        sample_acc = specimen_acc

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
    data_id = must_get_row_value(row, 'data_id')
    return session.get(Data, data_id)


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
