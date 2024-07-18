# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

import datetime
import json

from flask import Blueprint, request

from sqlalchemy import select
from sqlalchemy.orm import Bundle

from tol.api_base2 import custom_blueprint
from tol.sql.session import create_session_factory

from tolqc.sample_data_models import (
    Allocation,
    Data,
    File,
    Library,
    PacbioRunMetrics,
    Platform,
    Project,
    Run,
    Sample,
    Species,
    Specimen,
)

from werkzeug.exceptions import BadRequest


def reports_blueprint(
    db_uri=None,
    session_factory=None,
    url_prefix: str = '/report',
) -> Blueprint:
    rep = custom_blueprint(name='reports', url_prefix=url_prefix)
    if not session_factory:
        session_factory = create_session_factory(db_uri)

    @rep.route('/pacbio-data')
    def pacbio_run_data():
        return tolqc_report(
            session_factory,
            'pacbio_data',
            pacbio_data_report_query,
        )

    @rep.route('/pipeline-data')
    def pipeline_data():
        return tolqc_report(
            session_factory,
            'pipeline_data',
            pipeline_data_report_query,
        )

    @rep.route('/mlwh-data')
    def mlwh_data():
        return tolqc_report(
            session_factory,
            'mlwh_data',
            mlwh_data_report_query,
        )

    @rep.errorhandler(BadRequest)
    def handle_bad_request(e):
        return {'error': e.description}, 400

    return rep


def tsv_rows(row_itr, query):
    yield '\t'.join(d['name'] for d in query.column_descriptions) + '\n'
    for row in row_itr:
        yield '\t'.join('' if x is None else str(x) for x in row) + '\n'


def ndjson_rows(row_itr, _):
    for row in row_itr:
        yield json.dumps(row._asdict(), separators=(',', ':')) + '\n'


FORMATTERS = {
    'ndjson': (ndjson_rows, 'application/x-ndjson'),
    'tsv': (tsv_rows, 'text/tab-separated-values'),
}


def tolqc_report(session_factory, report_name, build_query):
    # File format if requested; defaults to TSV
    req_fmt = request.args.get('format', 'tsv').lower()
    fmt_mime = FORMATTERS.get(req_fmt)
    if not fmt_mime:
        valid = tuple(FORMATTERS)
        msg = f'format parameter must be one of: {valid}'
        raise BadRequest(msg)
    out_formatter, mime_type = fmt_mime

    # Suggested filename for web browsers
    today = datetime.date.today().isoformat()
    filename = f'{report_name}_{today}.{req_fmt}'
    headers = {
        'Content-Type': mime_type,
        'Content-Disposition': f'attachment; filename="{filename}"',
    }

    # Must either (as here) use session as a context manager or call
    # session.close() to avoid SELECT statements accumulating on server
    # with 'idle in transaction' state.
    with session_factory() as session:
        query = build_query()
        row_itr = session.execute(query)

    # Streams formatted data from the SQL query to the client
    return out_formatter(row_itr, query), 200, headers


def pipeline_data_report_query():
    query = (
        select(
            Data.data_id,
            File.remote_path,
            Species.species_id.label('species'),
            Species.hierarchy_name.label('species_hierarchy'),
            Specimen.specimen_id.label('specimen'),
            Library.library_type_id.label('pipeline'),
            Data.study_id,
            Data.visibility,
            Data.lims_qc,
            Data.processed,
        )
        .select_from(Data)
        .outerjoin(Sample)
        .outerjoin(Specimen)
        .outerjoin(Species)
        .join(File)
        .join(Library)
        .order_by(Data.data_id.desc())
    )

    query = add_argument(
        query,
        Data.processed,
        lookup={
            'null': None,
            '0': 0,
            '1': 1,
        },
    )
    query = add_argument(query, Data.visibility)
    query = add_argument(query, Data.lims_qc)
    query = add_argument(query, Library.library_type_id, name='pipeline')
    query = add_argument(query, Data.study_id)

    return query


def add_argument(query, column, name=None, lookup=None):
    if not name:
        name = column.name

    arg = request.args.get(name)
    if not arg:
        return query

    # Guard against being passed excessively long param values
    val = arg[:256]

    if lookup:
        try:
            val = lookup[arg]
        except KeyError:
            valid = tuple(lookup)
            msg = f"'{name}' parameter must be one of: {valid}"
            raise BadRequest(msg) from None

    return query.where(column == val)


def pacbio_data_report_query():
    return (
        select(
            ProjectGroupBundle(
                'group',
                Project.hierarchy_name,
                Species.taxon_group,
            ),
            Species.species_id.label('species'),
            Specimen.specimen_id.label('specimen'),
            Sample.sample_id.label('sample'),
            Library.library_type_id.label('pipeline'),
            Platform.name.label('platform'),
            Platform.model,
            IsoDayBundle('date', Run.start),
            Data.lims_qc,
            Run.lims_id.label('run'),
            Run.run_id.label('movie_name'),
            Run.element.label('well'),
            Run.instrument_name.label('instrument'),
            Run.plex_count,
            PacbioRunMetrics.movie_minutes.label('movie_length'),
            Data.tag_index,
            Data.tag1_id.label('tag'),
            Sample.accession_id.label('sample_accession'),
            Data.accession_id.label('run_accession'),
            Data.library_id.label('library'),
            Data.reads,
            Data.read_length_mean,
            Data.read_length_n50,
            Data.read_length_longest,
            Data.read_length_shortest,
            Data.reads_duplicated,
            Data.reads_filtered,
            Data.bases.label('bases'),
            Data.bases_a,
            Data.bases_c,
            Data.bases_g,
            Data.bases_t,
            PacbioRunMetrics.loading_conc.label('loading_concentration'),
            PacbioRunMetrics.binding_kit,
            PacbioRunMetrics.sequencing_kit,
            PacbioRunMetrics.productive_zmws_num,
            PacbioRunMetrics.p0_num,
            PacbioRunMetrics.p1_num,
            PacbioRunMetrics.p2_num,
        )
        .select_from(Data)
        .outerjoin(Sample)
        .outerjoin(Specimen)
        .outerjoin(Species)
        .join(Run)
        .join(Platform)
        .outerjoin(Library)
        .outerjoin(PacbioRunMetrics)
        # Cannot do many-to-many join between Data and Project directly.
        # Must explicitly go through Allocation:
        .join(Allocation)
        .join(Project)
        .where(Platform.name == 'PacBio')
        .order_by(
            Data.date.desc(),
            Specimen.specimen_id,
        )
    )


def mlwh_data_report_query():
    query = (
        mlwh_data_report_query_select()
        .select_from(Data)
        .outerjoin(Sample)
        .outerjoin(Specimen)
        .outerjoin(Species)
        .join(Run)
        .join(Platform)
        .outerjoin(File)
        .outerjoin(Library)
        .outerjoin(PacbioRunMetrics)
        .where(Data.study_id != None)  # noqa: E711
        .order_by(
            Data.date.desc(),
        )
    )
    query = add_argument(query, Data.study_id)
    return query


def mlwh_data_report_query_select():
    return select(
        Data.data_id,
        Data.study_id,
        Sample.sample_id.label('sample_name'),
        Specimen.supplied_name.label('supplier_name'),
        Specimen.specimen_id.label('tol_specimen_id'),
        Sample.accession_id.label('biosample_accession'),
        Specimen.accession_id.label('biospecimen_accession'),
        Species.species_id.label('scientific_name'),
        Species.taxon_id,
        Platform.name.label('platform_type'),
        Platform.model.label('instrument_model'),
        Run.instrument_name,
        Library.library_type_id.label('pipeline_id_lims'),
        Run.run_id,
        Data.tag_index,
        Run.lims_id.label('lims_run_id'),
        Run.element,
        IsoDateTimeBundle('run_start', Run.start),
        IsoDateTimeBundle('run_complete', Run.complete),
        Run.plex_count,
        Data.lims_qc,
        IsoDateTimeBundle('qc_date', Data.date),
        Data.tag1_id,
        Data.tag2_id,
        Library.library_id,
        PacbioRunMetrics.movie_minutes,
        PacbioRunMetrics.binding_kit,
        PacbioRunMetrics.sequencing_kit,
        PacbioRunMetrics.sequencing_kit_lot_number,
        PacbioRunMetrics.cell_lot_number,
        PacbioRunMetrics.include_kinetics,
        PacbioRunMetrics.loading_conc,
        PacbioRunMetrics.control_num_reads,
        PacbioRunMetrics.control_read_length_mean,
        PacbioRunMetrics.control_concordance_mean,
        PacbioRunMetrics.control_concordance_mode,
        PacbioRunMetrics.local_base_rate,
        PacbioRunMetrics.polymerase_read_bases,
        PacbioRunMetrics.polymerase_num_reads,
        PacbioRunMetrics.polymerase_read_length_mean,
        PacbioRunMetrics.polymerase_read_length_n50,
        PacbioRunMetrics.insert_length_mean,
        PacbioRunMetrics.insert_length_n50,
        PacbioRunMetrics.unique_molecular_bases,
        PacbioRunMetrics.productive_zmws_num,
        PacbioRunMetrics.p0_num,
        PacbioRunMetrics.p1_num,
        PacbioRunMetrics.p2_num,
        PacbioRunMetrics.adapter_dimer_percent,
        PacbioRunMetrics.short_insert_percent,
        PacbioRunMetrics.hifi_read_bases,
        PacbioRunMetrics.hifi_num_reads,
        PacbioRunMetrics.hifi_read_length_mean,
        PacbioRunMetrics.hifi_read_quality_median,
        PacbioRunMetrics.hifi_number_passes_mean,
        PacbioRunMetrics.hifi_low_quality_read_bases,
        PacbioRunMetrics.hifi_low_quality_num_reads,
        PacbioRunMetrics.hifi_low_quality_read_length_mean,
        PacbioRunMetrics.hifi_low_quality_read_quality_median,
        PacbioRunMetrics.hifi_barcoded_reads,
        PacbioRunMetrics.hifi_bases_in_barcoded_reads,
        File.remote_path,
    )


class ProjectGroupBundle(Bundle):
    """
    Combine the "proj" and "taxon_group" columns if the "proj" column
    contains "{}", else returns the "proj" itself.
    e.g. ("darwin/{}", "birds") becomes "darwin/birds"
    """  # noqa: P102

    def create_row_processor(self, query, getters, _):
        get_proj, get_taxon_group = getters

        def processor(row):
            proj = get_proj(row)
            taxon_group = get_taxon_group(row)
            group = None
            if proj is not None:
                if '{}' in proj and taxon_group is not None:  # noqa: P103
                    group = proj.format(taxon_group)
                else:
                    group = proj
            return group

        return processor


class IsoDayBundle(Bundle):
    """
    Returns just the day portion of a datetime column
    in ISO 8601 format, if it contains a value.
    """

    def create_row_processor(self, query, getters, _):
        (get_datetime,) = getters

        def processor(row):
            dt = get_datetime(row)
            return dt.date().isoformat() if dt else None

        return processor


class IsoDateTimeBundle(Bundle):
    """
    Returns datetime column in ISO 8601 format, if it contains a value.
    """

    def create_row_processor(self, query, getters, _):
        (get_datetime,) = getters

        def processor(row):
            dt = get_datetime(row)
            return dt.isoformat() if dt else None

        return processor
