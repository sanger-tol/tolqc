# SPDX-FileCopyrightText: 2024 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from functools import cache

from sqlalchemy.exc import SQLAlchemyError

from tolqc.marshal.ndjson import (
    must_get_row_value,
    ndjson_rows_from_stream,
)
from tolqc.schema.assembly_models import (
    Assembly,
    AssemblyStatus,
    Dataset,
    DatasetStatus,
)
from tolqc.schema.base import now_with_local_tz
from tolqc.schema.sample_data_models import Specimen, SpecimenStatus


@cache
def model_status_model(table):
    tbl_to_mdl = {
        'assembly': (
            Assembly,
            AssemblyStatus,
        ),
        'dataset': (
            Dataset,
            DatasetStatus,
        ),
        'specimen': (
            Specimen,
            SpecimenStatus,
        ),
    }
    if mdl := tbl_to_mdl.get(table):
        return mdl
    else:
        msg = f'No ...Status model for table {table!r}'
        raise ValueError(msg)


def load_status_stream(session, stream, table):
    datasets = {}
    try:
        for row in ndjson_rows_from_stream(stream):
            key, status = store_status_row(session, table, row)
            datasets.setdefault(key, []).append(status_row(table, status))
    except SQLAlchemyError:
        session.rollback()
        raise

    return datasets


def store_status_row(session, table, row):
    model, status_model = model_status_model(table)
    oid = must_get_row_value(row, table + '.id')
    status_type = must_get_row_value(row, 'status_type.id')
    status_time = row.get('status_time')  # *** Make timezone aware ***

    obj = session.get(model, oid)
    if not obj:
        msg = r'No such {model.__name__} {oid!r}'
        raise ValueError(msg)

    # Check that the current status isn't the same
    if (xst := obj.status) and xst.status_type_id == status_type:
        return 'existing', xst

    # Store a new status
    new = store_status(
        session,
        table,
        obj,
        model=status_model,
        status_name=status_type,
        time=status_time,
    )
    return 'new', new


def status_row(table, status):
    return {
        f'{table}.id': getattr(status, f'{table}_id'),
        'status_type.id': status.status_type_id,
        'status_time': status.status_time,
    }


def store_status(session, table, obj, model=None, status_name=None, time=None):
    if not time:
        time = now_with_local_tz()
    status = model(
        status_type_id=status_name,
        status_time=time,
    )

    # Set the related object this is the status of
    setattr(status, table, obj)

    session.add(status)

    # This flush:
    session.flush()
    # allows us to set the current status in the related object without
    # running into circular reference issues:
    obj.status = status

    return status
