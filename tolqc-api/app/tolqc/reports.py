# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

import datetime

from flask import Blueprint

from sqlalchemy import Column, inspect, select
from sqlalchemy.orm import Bundle
from sqlalchemy.orm.attributes import InstrumentedAttribute
from sqlalchemy.sql.elements import Label

from tol.api_base import custom_blueprint

from tolqc.json import json_dumps
from tolqc.report.bundles import FolderBundle, IsoDateTimeBundle
from tolqc.report.queries.sequence_data import (
    illumina_data_report_query,
    mlwh_data_report_query,
    ont_data_report_query,
    pacbio_data_report_query,
    pipeline_data_report_query,
)
from tolqc.report.queries.species_data import (
    ena_assembly_report_query,
    metagenome_bin_report_query,
    metagenome_report_query,
    species_bioproject_query,
    specimen_status_report_query,
)
from tolqc.report.request_args import RequestArgs
from tolqc.schema.folder_models import Folder, FolderLocation, HasFolder


from werkzeug.exceptions import BadRequest


def reports_blueprint(
    session_factory,
    models,
    url_prefix: str = '/report',
) -> Blueprint:
    rep = custom_blueprint(name='reports', url_prefix=url_prefix)

    rep_eng = ReportEngine(session_factory=session_factory, models=models)

    @rep.route('/<report_path>')
    def tolqc_report(report_path):
        return rep_eng.report(report_path)

    @rep.route('/folder/<folder_table>')
    def folder_data(folder_table):
        return rep_eng.folder_report(folder_table)

    return rep


def tsv_rows(row_itr, query):
    yield '\t'.join(d['name'] for d in query.column_descriptions) + '\n'
    for row in row_itr:
        yield '\t'.join('' if x is None else str(x) for x in row) + '\n'


def ndjson_rows(row_itr, _):
    for row in row_itr:
        yield json_dumps(row._asdict()) + '\n'


class ReportEngine:
    def __init__(self, session_factory=None, models=None):
        self.session_factory = session_factory
        self.models = models
        self.table_to_model = {x.__tablename__: x for x in models}
        self.indexed_columns = {}

    FORMATTERS = {
        'ndjson': (ndjson_rows, 'application/x-ndjson'),
        'tsv': (tsv_rows, 'text/tab-separated-values'),
    }

    QUERY_FUNCS = {
        'ena-assembly': ena_assembly_report_query,
        'illumina-data': illumina_data_report_query,
        'metagenome': metagenome_report_query,
        'metagenome-bin': metagenome_bin_report_query,
        'mlwh-data': mlwh_data_report_query,
        'ont-data': ont_data_report_query,
        'pacbio-data': pacbio_data_report_query,
        'pipeline-data': pipeline_data_report_query,
        'species-bioproject': species_bioproject_query,
        'specimen-status': specimen_status_report_query,
    }

    def do_report(self, report_name, query, req_args: RequestArgs | None = None):
        # File format if requested; defaults to TSV
        if req_args is None:
            req_args = RequestArgs()
        req_fmt = req_args.pop_default('format', 'tsv').lower()
        fmt_mime = self.FORMATTERS.get(req_fmt)
        if not fmt_mime:
            valid = tuple(self.FORMATTERS)
            msg = f'format parameter must be one of: {valid}'
            raise BadRequest(msg)
        out_formatter, mime_type = fmt_mime

        # Suggested filename for web browsers
        today = datetime.date.today().isoformat()  # noqa: DTZ011
        filename = f'{report_name}_{today}.{req_fmt}'
        headers = {
            'Content-Type': mime_type,
            'Content-Disposition': f'attachment; filename="{filename}"',
        }

        # Must either (as here) use session as a context manager or call
        # session.close() to avoid SELECT statements accumulating on server
        # with 'idle in transaction' state.
        with self.session_factory() as session:
            query = self.add_arguments(session, query, req_args)
            row_itr = session.execute(query)

        # Streams formatted data from the SQL query to the client
        return out_formatter(row_itr, query), 200, headers

    def report(self, report_path):
        query_gen = self.QUERY_FUNCS.get(report_path)
        if not query_gen:
            msg = f"No such report '{report_path}'"
            raise BadRequest(msg)

        report_name = report_path.replace('-', '_')
        req_args = RequestArgs()
        return self.do_report(report_name, query_gen(req_args), req_args)

    def folder_report(self, folder_table):
        model = self.table_to_model.get(folder_table)
        if not model:
            msg = f'No such table {folder_table!r}'
            raise BadRequest(msg)

        if not issubclass(model, HasFolder):
            msg = f'Table {folder_table!r} is not a folder table'
            raise BadRequest(msg)

        tbl_select = []
        ignore = {'folder_ulid', 'modified_at', 'modified_by'}
        for col in inspect(model).columns:
            if col.name not in ignore:
                if col.type.python_type == datetime.datetime:
                    tbl_select.append(IsoDateTimeBundle(col.name, col))
                else:
                    tbl_select.append(col)

        query = (
            select(
                *tbl_select,
                FolderBundle(
                    'image_file_list',
                    FolderLocation.http_prefix,
                    Folder.folder_ulid,
                    Folder.image_file_list,
                ),
                FolderBundle(
                    'other_file_list',
                    FolderLocation.http_prefix,
                    Folder.folder_ulid,
                    Folder.other_file_list,
                ),
            )
            .select_from(model)
            .outerjoin(Folder)
            .outerjoin(FolderLocation)
        )

        return self.do_report(f'{folder_table}_folders', query)

    def add_arguments(self, session, query, req_args: RequestArgs):
        """
        All remaining request arguments are treated as report column names to
        be selected on.
        """

        query_cols = {x['name']: x['expr'] for x in query.column_descriptions}

        for arg, val in req_args.pop_all().items():
            # Is the column in the report?
            expr = query_cols.get(arg)
            if expr is None:
                msg = f"No such column '{arg}' in report"
                raise BadRequest(msg)

            # Check that there's only one column in the expression
            columns = self.columns_from_expr(expr)
            if len(columns) == 1:
                sel_col = columns[0]
            else:
                msg = (
                    f"Cannot select on report column '{arg}' which contains {len(columns)} columns"
                )
                raise BadRequest(msg)

            # Check that the column is indexed
            if not self.is_indexed_column(session, sel_col):
                msg = f"Cannot select on unindexed column '{sel_col.table.name}.{sel_col.name}'"
                raise BadRequest(msg)

            query = query.where(sel_col == val)

        return query

    def is_indexed_column(self, session, column) -> bool:
        if column.primary_key or column.foreign_keys:
            return True

        # Column may have a non primary or foreign key index
        table_name = column.table.name
        idx_dict = self.indexed_columns.get(table_name)
        if not idx_dict:
            insp = inspect(session.connection())
            self.indexed_columns = idx_dict = {}
            for idx in insp.get_indexes(table_name):
                idx_cols = idx['column_names']
                if len(idx_cols) == 1:
                    idx_dict[idx_cols[0]] = True

        return idx_dict.get(column.name, False)

    def columns_from_expr(self, expr) -> tuple[Column | InstrumentedAttribute]:
        if isinstance(expr, Column | InstrumentedAttribute):
            return (expr,)
        elif isinstance(expr, Label):
            return tuple(expr.base_columns)
        elif isinstance(expr, Bundle):
            err = f"Cannot select on Bundle column '{expr.name}'"
        else:
            err = f"Do not know how to get columns from '{expr.name}': {expr!r}"
        raise BadRequest(err)
