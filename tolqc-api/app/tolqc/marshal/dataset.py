# SPDX-FileCopyrightText: 2024 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

from tolqc.marshal.ndjson import (
    must_get_row_value,
    ndjson_rows_from_stream,
    row_message,
)
from tolqc.schema.assembly_models import Dataset, DatasetElement
from tolqc.schema.sample_data_models import Data, File


def load_dataset_stream(session, stream):
    datasets = {}
    with session.no_autoflush:
        try:
            for row in ndjson_rows_from_stream(stream):
                new, xst = store_dataset_row(session, row)
                if new:
                    datasets.setdefault('new', []).append(new)
                if xst:
                    datasets.setdefault('existing', []).append(xst)
        except SQLAlchemyError:
            session.rollback()
            raise

    return datasets


def store_dataset_row(session, row):
    # First try fetching Dataset by it's ID
    dataset_id = must_get_row_value(row, 'dataset.id')
    if dsr := dataset_row_by_dataset_id(session, dataset_id):
        return None, dsr

    # Get the data_id for each element of the Dataset
    elements = must_get_row_value(row, 'elements')

    element_data_ids = []
    for ele in elements:
        data_id = ele.get('data.id')
        if not data_id:
            # Is there are remote_path value we can use for lookup?
            if rp := ele.get('remote_path'):
                (data_id,) = session.execute(
                    select(File.data_id).where(File.remote_path == rp)
                ).one_or_none()
                if not data_id:
                    msg = row_message(
                        ele, "No 'data.id' field and no File matching 'remote_path' field"
                    )
                    raise ValueError(msg)
            else:
                msg = row_message(ele, "No 'data.id' or 'remote_path' field in element")
                raise ValueError(msg)
        element_data_ids.append(data_id)

    # Return existing dataset row if we already have it
    if dsr := dataset_row_by_data_ids(session, element_data_ids):
        return None, dsr

    # Create a new dataset
    session.merge(
        Dataset(
            dataset_id=dataset_id,
            data_assn=[DatasetElement(data_id=x) for x in element_data_ids],
        )
    )
    session.flush()
    return dataset_row_by_dataset_id(session, dataset_id), None


def dataset_row_by_dataset_id(session, dataset_id):
    rows = __build_dataset_rows(
        session, dataset_rows_query().where(Dataset.dataset_id == dataset_id)
    )
    return rows[0] if rows else None


def dataset_row_by_data_ids(session, data_id_list):
    data_id_set = set(data_id_list)
    ds = None
    for maybe in __build_dataset_rows(
        session,
        dataset_rows_query().where(
            Dataset.dataset_id.in_(
                select(DatasetElement.dataset_id)
                .where(DatasetElement.data_id.in_(data_id_list))
                .distinct()
            )
        ),
    ):
        if data_id_set == {x['data.id'] for x in maybe['elements']}:
            ds = maybe
            break

    return ds


def __build_dataset_rows(session, query):
    ds_rows = []
    ds = None
    for row in session.execute(query):
        dataset_id, data_id, remote_path = row

        if ds is None or ds['dataset.id'] != dataset_id:
            # Make a new dataset row
            ds = {
                'dataset.id': dataset_id,
                'elements': [],
            }
            ds_rows.append(ds)

        # Append element to the current dataset
        ds['elements'].append(
            {
                'data.id': data_id,
                'remote_path': remote_path,
            }
        )

    return ds_rows


def dataset_rows_query():
    return (
        select(
            Dataset.dataset_id,
            Data.data_id,
            File.remote_path,
        )
        .select_from(Dataset)
        .join(DatasetElement)
        .join(Data)
        .outerjoin(File)  # Do not necessarily have a File
        .order_by(Dataset.dataset_id, DatasetElement.id)
    )
