# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

import datetime
import json
from typing import Optional

from flask import Blueprint, request

from sqlalchemy import select
from sqlalchemy.orm import Bundle

from tol.api_base2 import custom_blueprint
from tol.api_base2.misc import Authenticator

from tolqc.sample_data_models import (
    Allocation,
    Data,
    Library,
    PacbioRunMetrics,
    Platform,
    Project,
    Run,
    Sample,
    Species,
    Specimen,
)


def reports_blueprint(
    session_factory,
    url_prefix: str = '/reports',
    authenticator: Optional[Authenticator] = None,
) -> Blueprint:
    rep = custom_blueprint(
        name='reports', url_prefix=url_prefix, authenticator=authenticator
    )
    # session_factory = create_session_factory(db_uri)

    @rep.route('/pacbio-run-data')
    def pacbio_run_data():
        # File format if requested; defaults to TSV
        req_fmt = request.args.get('format', 'tsv').lower()
        fmt_mime = FORMATTERS.get(req_fmt)
        if not fmt_mime:
            valid = tuple(FORMATTERS)
            return {'error': f'format parameter must be one of: {valid}'}, 400
        out_formatter, mime_type = fmt_mime

        # Suggested filename for web browsers
        today = datetime.date.today().isoformat()
        filename = f'pacbio_run_data_{today}.{req_fmt}'
        headers = {
            'Content-Type': mime_type,
            'Content-Disposition': f'attachment; filename="{filename}"',
        }

        # Must either (as here) use session as a context manager or call
        # session.close() to avoid SELECT statements accumulating on server
        # with 'idle in transaction' state.
        with session_factory() as session:
            query = pacbio_run_report_query()
            row_itr = session.execute(query)

        # Streams formatted data from the SQL query to the client
        return out_formatter(row_itr, query), 200, headers

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


def pacbio_run_report_query():
    return (
        select(
            ProjectGroupBundle(
                'group',
                Project.hierarchy_name,
                Species.taxon_group,
            ),
            Specimen.specimen_id.label('specimen'),
            Library.library_type_id.label('pipeline'),
            Platform.name.label('platform'),
            Platform.model,
            Sample.sample_id.label('sanger_id'),
            IsoDayBundle('date', Run.start),
            Data.lims_qc,
            Run.lims_id.label('run'),
            Run.run_id.label('movie_name'),
            Run.element.label('well'),
            Run.instrument_name.label('instrument'),
            PacbioRunMetrics.movie_minutes.label('movie_length'),
            Data.tag_index,
            Data.tag1_id.label('tag'),
            Sample.accession_id.label('sample_accession'),
            Data.accession_id.label('run_accession'),
            Data.library_id.label('library_load_name'),
            PacbioRunMetrics.hifi_num_reads.label('reads'),
            PacbioRunMetrics.hifi_read_bases.label('bases'),
            PacbioRunMetrics.insert_length_mean.label('mean'),
            PacbioRunMetrics.insert_length_n50.label('n50'),
            Species.species_id.label('species'),
            PacbioRunMetrics.loading_conc,
            PacbioRunMetrics.binding_kit,
            PacbioRunMetrics.sequencing_kit,
            PacbioRunMetrics.include_kinetics,
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
