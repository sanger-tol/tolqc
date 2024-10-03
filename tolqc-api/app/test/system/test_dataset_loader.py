# SPDX-FileCopyrightText: 2024 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

import json
import logging

import pytest

from sqlalchemy.exc import IntegrityError

from tolqc.marshal.dataset import (
    dataset_row_by_data_ids,
    dataset_row_by_dataset_id,
    load_dataset_stream,
    store_dataset_row,
)
from tolqc.schema.assembly_models import Dataset, DatasetElement
from tolqc.schema.sample_data_models import Data, File

from .conftest import SKIP_IF_NO_DB_URI_ENV as pytestmark  # noqa: F401, N811


@pytest.fixture
def session(db_session):
    """Adds test Datasets to db_session"""
    for obj in dataset_test_data():
        db_session.merge(obj)
    db_session.commit()

    return db_session


def test_fetch_dataset(session):
    dsid = 'DSET_001'
    dsr = dataset_row_by_dataset_id(session, dsid)
    logging.debug('Found: ' + json.dumps(dsr, indent=2))
    assert dsr['dataset.id'] == dsid
    assert len(dsr['elements']) == 4


def test_fetch_dataset_by_data_ids(session):
    dsr = dataset_row_by_data_ids(
        session,
        [
            'DATA_11#2025',
            'DATA_22#2039',
            'DATA_33#2068',
            '46916_2#2',
        ],
    )
    logging.debug('Found: ' + json.dumps(dsr, indent=2))
    assert dsr['dataset.id'] == 'DSET_001'
    assert len(dsr['elements']) == 4

    dsr = dataset_row_by_data_ids(
        session,
        [
            'DATA_11#2025',
            'DATA_22#2039',
            '46916_2#2',
        ],
    )
    logging.debug('Found: ' + json.dumps(dsr, indent=2))
    assert dsr['dataset.id'] == 'DSET_002'
    assert len(dsr['elements']) == 3

    assert (
        dataset_row_by_data_ids(
            session,
            [
                'DATA_11#2025',
                'DATA_22#2039',
                'DATA_33#2068',
            ],
        )
        is None
    )


def test_store_exisiting_dataset_row(session):
    dsr = {
        'dataset.id': 'DSET_NEW',
        'elements': [
            {
                'data.id': 'DATA_11#2025',
            },
            {
                'remote_path': 'irods:/seq/pacbio/DATA_22.hifi_reads.bc2039.bam',
            },
            {
                'data.id': '46916_2#2',
            },
        ],
    }
    new_dsr, xst_dsr = store_dataset_row(session, dsr)
    assert new_dsr is None
    assert xst_dsr['dataset.id'] == 'DSET_002'


def test_store_new_dataset_row(session):
    dsr = {
        'dataset.id': 'DSET_NEW',
        'elements': [
            {
                'data.id': 'DATA_11#2025',
            },
            {
                'remote_path': 'irods:/seq/pacbio/DATA_22.hifi_reads.bc2039.bam',
            },
        ],
    }
    new_dsr, xst_dsr = store_dataset_row(session, dsr)
    assert xst_dsr is None
    logging.debug('New dataset row: ' + json.dumps(new_dsr, indent=2))
    assert new_dsr['dataset.id'] == 'DSET_NEW'


def test_store_rows_ok(session):
    row_data = [
        json.dumps(row)
        for row in (
            {
                'dataset.id': 'DSET_NEW_01',
                'elements': [
                    {
                        'data.id': 'DATA_11#2025',
                    },
                    {
                        'data.id': 'DATA_22#2039',
                    },
                ],
            },
            # Test that get with only the dataset.id works
            {'dataset.id': 'DSET_001'},
        )
    ]
    res = load_dataset_stream(session, row_data)
    logging.debug(f'Result: {res}')
    assert res.get('new') == [
        {
            'dataset.id': 'DSET_NEW_01',
            'elements': [
                {
                    'data.id': 'DATA_11#2025',
                    'remote_path': 'irods:/seq/pacbio/DATA_11.hifi_reads.bc2025.bam',
                },
                {
                    'data.id': 'DATA_22#2039',
                    'remote_path': 'irods:/seq/pacbio/DATA_22.hifi_reads.bc2039.bam',
                },
            ],
        }
    ]
    assert res.get('existing') == [
        {
            'dataset.id': 'DSET_001',
            'elements': [
                {
                    'data.id': 'DATA_22#2039',
                    'remote_path': 'irods:/seq/pacbio/DATA_22.hifi_reads.bc2039.bam',
                },
                {
                    'data.id': 'DATA_11#2025',
                    'remote_path': 'irods:/seq/pacbio/DATA_11.hifi_reads.bc2025.bam',
                },
                {
                    'data.id': 'DATA_33#2068',
                    'remote_path': 'irods:/seq/pacbio/DATA_33.hifi_reads.bc2068.bam',
                },
                {'data.id': '46916_2#2', 'remote_path': None},
            ],
        }
    ]


def test_store_rows_fail(session):
    row_data = [
        json.dumps(row)
        for row in (
            {
                'dataset.id': 'DSET_NEW_02',
                'elements': [
                    {
                        'data.id': 'DATA_11#2025',
                    },
                    {
                        'data.id': 'DATA_22#2039',
                    },
                ],
            },
            {
                'dataset.id': 'DSET_FAIL_01',
                'elements': [
                    {
                        'data.id': 'DATA_11#2025',
                    },
                    {
                        # This entry will error
                        'data.id': 'DOES_NOT_EXIST',
                    },
                ],
            },
        )
    ]
    with pytest.raises(IntegrityError, match='violates foreign key'):
        load_dataset_stream(session, row_data)

    # Check that neither the first, good Dataset nor the fail Dataset were
    # saved.
    session.flush()
    assert session.get(Dataset, 'DSET_NEW_02') is None
    assert session.get(Dataset, 'DSET_FAIL_01') is None


def test_loader_api(client, api_path, session):
    assert session.get(Data, 'DATA_11#2025')
    assert session.get(Data, 'DATA_22#2039')

    new_ds_json = (
        json.dumps(
            {
                'dataset.id': 'DSET_API_01',
                'elements': [
                    {
                        'data.id': 'DATA_11#2025',
                    },
                    {
                        'data.id': 'DATA_22#2039',
                    },
                ],
            },
            separators=(',', ':'),
        )
        + '\n'
    )
    response = client.post(api_path + '/loader/dataset', data=new_ds_json)
    assert response.status == '200 OK'
    assert response.json == {
        'new': [
            {
                'dataset.id': 'DSET_API_01',
                'elements': [
                    {
                        'data.id': 'DATA_11#2025',
                        'remote_path': 'irods:/seq/pacbio/DATA_11.hifi_reads.bc2025.bam',
                    },
                    {
                        'data.id': 'DATA_22#2039',
                        'remote_path': 'irods:/seq/pacbio/DATA_22.hifi_reads.bc2039.bam',
                    },
                ],
            },
        ],
    }


def dataset_test_data():
    return [
        Dataset(
            dataset_id='DSET_001',
            data_assn=[
                DatasetElement(
                    data_id='DATA_22#2039',
                    dataset_id='DSET_001',
                    data=Data(
                        data_id='DATA_22#2039',
                        files=[
                            File(
                                data_id='DATA_22#2039',
                                remote_path=(
                                    'irods:/seq/pacbio/DATA_22.hifi_reads.bc2039.bam'
                                ),
                            )
                        ],
                    ),
                ),
                DatasetElement(
                    data_id='DATA_11#2025',
                    dataset_id='DSET_001',
                    data=Data(
                        data_id='DATA_11#2025',
                        files=[
                            File(
                                data_id='DATA_11#2025',
                                remote_path=(
                                    'irods:/seq/pacbio/DATA_11.hifi_reads.bc2025.bam'
                                ),
                            )
                        ],
                    ),
                ),
                DatasetElement(
                    data_id='DATA_33#2068',
                    dataset_id='DSET_001',
                    data=Data(
                        data_id='DATA_33#2068',
                        files=[
                            File(
                                data_id='DATA_33#2068',
                                remote_path=(
                                    'irods:/seq/pacbio/DATA_33.hifi_reads.bc2068.bam'
                                ),
                            )
                        ],
                    ),
                ),
                DatasetElement(
                    data_id='46916_2#2',
                    dataset_id='DSET_001',
                    data=Data(
                        data_id='46916_2#2',
                        # No files attached to test that File is not required
                    ),
                ),
            ],
        ),
        Dataset(
            dataset_id='DSET_002',
            data_assn=[
                # DatasetElement(data_id='DATA_22#2039', dataset_id='DSET_002'),
                # DatasetElement(data_id='DATA_11#2025', dataset_id='DSET_002'),
                # DatasetElement(data_id='46916_2#2', dataset_id='DSET_002'),
                DatasetElement(data_id='DATA_22#2039'),
                DatasetElement(data_id='DATA_11#2025'),
                DatasetElement(data_id='46916_2#2'),
            ],
        ),
    ]
