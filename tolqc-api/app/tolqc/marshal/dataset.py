from tolqc.marshal.ndjson import must_get_row_value, ndjson_rows_from_stream
from tolqc.schema.assembly_models import Dataset, DatasetElement
from tolqc.schema.sample_data_models import Data


def load_dataset_stream(session, stream):
    new_datasets = []
    for row in ndjson_rows_from_stream(stream):
        new_datasets.append(store_dataset_row(session, row))
    return {'new': new_datasets}


def store_dataset_row(session, row):
    dataset_id = must_get_row_value(row, 'dataset.id')
    elements = must_get_row_value(row, 'elements')

