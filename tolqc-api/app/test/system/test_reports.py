# SPDX-FileCopyrightText: 2024 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

import io
import json
import re
from urllib.parse import urlencode

import pytest

from tolqc.sample_data_models import Data, Platform, Run

from .conftest import SKIP_IF_NO_DB_URI_ENV as pytestmark  # noqa: F401, N811


@pytest.fixture
def pacbio_row_count(db_session):
    """
    To avoid hard coding a number, query for the number of PacBio data rows in
    the test database.
    """
    n = (
        db_session.query(Platform)
        .join(Run)
        .join(Data)
        .where(Platform.name == 'PacBio')
        .count()
    )

    # Guard against tests being run on an empty database
    if not n > 1:
        msg = f"Expected more than one row of PacBio data but got '{n}'"
        raise ValueError(msg)

    return n


def test_pacbio_run_data_report_tsv(client, api_path, pacbio_row_count):
    """
    Test PacBio run report with default format
    """
    response = client.get(api_path + '/report/pacbio-run-data')
    assert response.status == '200 OK'

    # Check Content-Disposition header
    dspstn = response.headers.get('Content-Disposition')
    assert re.fullmatch(
        r'attachment; filename="pacbio_run_data_\d{4}-\d\d-\d\d\.tsv"',
        dspstn,
    )

    tsv_lines = io.StringIO(response.text).readlines()
    assert len(tsv_lines) == 1 + pacbio_row_count


def test_pacbio_run_data_report_ndjson(client, api_path, pacbio_row_count):
    """
    Test NDJSON format request.
    """
    response = client.get(api_path + '/report/pacbio-run-data?format=NDJSON')
    assert response.status == '200 OK'

    tsv_lines = io.StringIO(response.text).readlines()
    assert len(tsv_lines) == pacbio_row_count


def test_pacbio_run_data_report_csv(client, api_path):
    """
    Requesting an unsupported format should be a 400
    """
    response = client.get(api_path + '/report/pacbio-run-data?format=CSV')
    assert response.status == '400 BAD REQUEST'


def test_pipeline_data_report(client, api_path):
    response = client.get(api_path + '/report/pipeline-data')
    assert response.status == '200 OK'


def good_param_combinations():
    for param in (
        {'processed': '1'},
        {'processed': '0'},
        {'processed': 'null'},
        {'lims_qc': 'pass'},
        {'lims_qc': 'fail'},
        {'pipeline': 'Chromium genome'},
        {'pipeline': 'RNA PolyA'},
        {'pipeline': 'Hi-C - Arima v2'},
        {'visibility': 'Always'},
        {'visibility': 'Testing'},
        {'project_lims_id': '5901'},
        # Combinations:
        {'processed': 'null', 'lims_qc': 'fail'},
        {'visibility': 'Always', 'lims_qc': 'pass'},
        {'project_lims_id': '5901', 'lims_qc': 'fail'},
    ):
        yield {'format': 'NDJSON', **param}


@pytest.mark.parametrize('params', good_param_combinations())
def test_data_report_good_params(client, api_path, params):
    response = client.get(api_path + '/report/pipeline-data?' + urlencode(params))
    assert response.status == '200 OK'

    json_lines = [json.loads(x) for x in io.StringIO(response.text).readlines()]
    assert json_lines

    # Check that values match those requested
    expected = expected_values(params)
    for row in json_lines:
        for col, val in expected.items():
            assert row.get(col) == val


def expected_values(params):
    expected = {}
    for col, val in params.items():
        if col == 'format':
            continue

        if val == 'null':
            exp = None
        else:
            try:
                exp = int(val)
            except ValueError:
                exp = val
        expected[col] = exp

    return expected


def test_data_report_bad_params(client, api_path):
    response = client.get(
        api_path + '/report/pipeline-data?' + urlencode({'processed': 'x'})
    )
    assert response.status == '400 BAD REQUEST'
