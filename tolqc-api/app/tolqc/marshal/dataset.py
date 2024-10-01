from sqlalchemy import func, select
from sqlalchemy.exc import SQLAlchemyError

from tolqc.marshal.ndjson import (
    must_get_row_value,
    ndjson_rows_from_stream,
    row_message,
)
from tolqc.schema.assembly_models import Dataset, DatasetElement
from tolqc.schema.sample_data_models import Data, File


def load_dataset_stream(session, stream):
    datasets = []
    with session.no_autoflush:
        try:
            for row in ndjson_rows_from_stream(stream):
                datasets.append(store_dataset_row(session, row))
        except SQLAlchemyError:
            session.rollback()
            raise
    session.flush()

    return {'datasets': datasets}


def store_dataset_row(session, row):
    dataset_id = must_get_row_value(row, 'dataset.id')
    if dsr := dataset_row_by_dataset_id(session, dataset_id):
        return {'existing': dsr}
    elements = must_get_row_value(row, 'elements')
    datas = []
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
        datas.append(data_id)
    if dsr := dataset_row_by_data_ids(session, datas):
        return {'existing': dsr}


def dataset_row_by_dataset_id(session, dataset_id):
    rows = __build_dataset_rows(
        session, ds_row_data_query().where(Dataset.datset_id == dataset_id)
    )
    return rows[0] if rows else None


def dataset_row_by_data_ids(session, data_id_list):
    data_id_set = set(data_id_list)
    ds = None
    for maybe in __build_dataset_rows(
        session,
        ds_row_data_query().where(
            Dataset.dataset_id.in_(
                select(DatasetElement.dataset_id)
                .where(DatasetElement.data_id.in_(data_id_list))
                .distinct()
            )
        ),
    ):
        if data_id_set == {x['data.id'] for x in maybe.elements}:
            ds = maybe
            break

    return ds


def __build_dataset_rows(session, query):
    ds_rows = []
    for row in session.execute(query):
        dataset_id, data_ids, remote_paths = row
        elements = [
            {'data.id': did, 'remote_path': rp}
            for did, rp in zip(data_ids, remote_paths, strict=True)
        ]
        ds_rows.append(
            {
                'dataset.id': dataset_id,
                'elements': elements,
            }
        )

    return ds_rows if ds_rows else None


def ds_row_data_query():
    return (
        select(
            Dataset.dataset_id,
            func.array_agg(Data.data_id).label('data_ids'),
            func.array_agg(File.remote_path).label('remote_paths'),
        )
        .select_from(Dataset)
        .join(DatasetElement)
        .join(Data)
        .outerjoin(File)
        .group_by(Dataset.dataset_id)
        .order_by(DatasetElement.id)
    )
