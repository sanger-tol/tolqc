# SPDX-FileCopyrightText: 2024 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

import json
from datetime import datetime

import pytest

from tolqc.marshal.status import store_status, store_status_row
from tolqc.schema.sample_data_models import Specimen, SpecimenStatus, SpecimenStatusType

from .conftest import SKIP_IF_NO_DB_URI_ENV as pytestmark  # noqa: F401, N811


@pytest.fixture
def session(db_session):
    """Adds test Datasets to db_session"""
    for obj in status_test_data():
        db_session.merge(obj)
    db_session.commit()

    return db_session


def test_store_status(session):
    sp_obj = session.get(Specimen, 'rTyrRex1')
    status = store_status(
        session,
        'specimen',
        sp_obj,
        SpecimenStatus,
        status_name='Data Generation',
    )
    assert isinstance(status.status_time, datetime)
    assert sp_obj.status is not None


def test_store_status_row(session):
    row = {
        'specimen.id': 'rTyrRex1',
        'status_type.id': 'Data Generation',
        'status_time': '1993-06-09T12:30:00',
    }
    key, status = store_status_row(session, 'specimen', row)
    assert key == 'new'

    # Matches current status so is existing
    key, status = store_status_row(
        session,
        'specimen',
        {
            'specimen.id': 'rTyrRex1',
            'status_type.id': 'Data Generation',
        },
    )
    assert key == 'existing'

    # Make a new status
    key, status = store_status_row(
        session,
        'specimen',
        {
            'specimen.id': 'rTyrRex1',
            'status_type.id': 'Data Issue',
        },
    )
    assert key == 'new'

    # No longer matches current status, so a new status is stored
    # (Even though it does match a prevous status in the history.)
    key, status = store_status_row(
        session,
        'specimen',
        {
            'specimen.id': 'rTyrRex1',
            'status_type.id': 'Data Generation',
        },
    )
    assert key == 'new'

    spcmn = session.get(Specimen, 'rTyrRex1')
    assert spcmn.status.status_type_id == 'Data Generation'
    assert len(spcmn.status_history) == 3


def test_store_status_api(client, api_path, session):
    data_json = ''.join(
        [
            json.dumps(x, separators=(',', ':')) + '\n'
            for x in [
                {
                    'specimen.id': 'rTyrRex1',
                    'status_type.id': 'Data Generation',
                    'status_time': '1993-06-09T12:30:00',
                },
                {
                    'specimen.id': 'rTyrRex1',
                    'status_type.id': 'Data Generation',
                },
            ]
        ]
    )

    response = client.post(api_path + '/loader/status/specimen', data=data_json)
    assert response.status == '200 OK'
    assert response.json == {
        'new': [
            {
                'specimen.id': 'rTyrRex1',
                'status_type.id': 'Data Generation',
                'status_time': '1993-06-09T12:30:00',
            }
        ],
        # The second row matches the first, so we get the first row back as an
        # existing row with the time filled in.
        'existing': [
            {
                'specimen.id': 'rTyrRex1',
                'status_type.id': 'Data Generation',
                'status_time': '1993-06-09T12:30:00',
            }
        ],
    }


def status_test_data():
    return [
        SpecimenStatusType(
            status_type_id='Data Generation',
            assign_order=10,
        ),
        SpecimenStatusType(
            status_type_id='Data Issue',
            assign_order=20,
        ),
        SpecimenStatusType(
            status_type_id='Data Complete',
            assign_order=30,
        ),
        SpecimenStatusType(
            status_type_id='Curation',
            assign_order=40,
        ),
        SpecimenStatusType(
            status_type_id='Curated',
            assign_order=50,
        ),
        SpecimenStatusType(
            status_type_id='Submitted',
            assign_order=60,
        ),
        Specimen(specimen_id='rTyrRex1'),
    ]
