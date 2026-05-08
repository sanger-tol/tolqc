# SPDX-FileCopyrightText: 2024 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

import io
import json
import logging
import re
from urllib.parse import urlencode

import pytest

from tolqc.reports import ReportEngine
from tolqc.schema import models_list
from tolqc.schema.sample_data_models import Data, Platform, Run

from werkzeug.exceptions import BadRequest

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


@pytest.fixture
def report_engine(session_factory):
    return ReportEngine(session_factory=session_factory, models=models_list())


def test_pacbio_run_data_report_tsv(client, api_path, pacbio_row_count):
    """
    Test PacBio run report with default format
    """
    response = client.get(api_path + '/report/pacbio-data')
    assert response.status == '200 OK'

    # Check Content-Disposition header
    dspstn = response.headers.get('Content-Disposition')
    assert re.fullmatch(
        r'attachment; filename="pacbio_data_\d{4}-\d\d-\d\d\.tsv"',
        dspstn,
    )

    tsv_lines = io.StringIO(response.text).readlines()
    assert len(tsv_lines) == 1 + pacbio_row_count


def test_pacbio_run_data_report_ndjson(client, api_path, pacbio_row_count):
    """
    Test NDJSON format request.
    """
    response = client.get(api_path + '/report/pacbio-data?format=NDJSON')
    assert response.status == '200 OK'

    tsv_lines = io.StringIO(response.text).readlines()
    assert len(tsv_lines) == pacbio_row_count


def test_pacbio_run_data_report_csv(client, api_path):
    """
    Requesting an unsupported format should be a 400
    """
    response = client.get(api_path + '/report/pacbio-data?format=CSV')
    assert response.status == '400 BAD REQUEST'


def test_illumna_data_report(client, api_path):
    response = client.get(api_path + '/report/illumina-data')
    assert response.status == '200 OK'


def test_pipeline_data_report(client, api_path):
    response = client.get(api_path + '/report/pipeline-data')
    assert response.status == '200 OK'


def test_mlwh_data_report(client, api_path):
    response = client.get(api_path + '/report/mlwh-data')
    assert response.status == '200 OK'


def test_report_engine_bad_requests(report_engine):
    with pytest.raises(BadRequest, match='No such report'):
        report_engine.report('x')
    with pytest.raises(BadRequest, match='No such table'):
        report_engine.folder_report('x')
    with pytest.raises(BadRequest, match='not a folder table'):
        report_engine.folder_report('species')


def test_report_engine_indexes(report_engine):
    with report_engine.session_factory() as session:
        # Primary key
        assert report_engine.is_indexed_column(session, Data.data_id) is True
        # Foregin key
        assert report_engine.is_indexed_column(session, Data.sample_id) is True
        # Indexed column
        assert report_engine.is_indexed_column(session, Data.processed) is True
        # No index
        assert report_engine.is_indexed_column(session, Data.bases) is False


def test_folder_report(client, api_path):
    response = client.get(api_path + '/report/folder/data?format=NDJSON')
    assert response.status == '200 OK'

    json_lines = [json.loads(x) for x in io.StringIO(response.text).readlines()]
    assert json_lines

    files_count = 0
    for jl in json_lines:
        for key in ('image_file_list', 'other_file_list'):
            files = jl[key]
            if files is not None:
                files_count += 1
                for spec in files:
                    assert spec['file'].startswith('https://')
    assert files_count > 0


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
        {'study_id': '5901'},
        # Combinations:
        {'processed': 'null', 'lims_qc': 'fail'},
        {'visibility': 'Always', 'lims_qc': 'pass'},
        {'study_id': '5901', 'lims_qc': 'fail'},
    ):
        yield {'format': 'NDJSON', **param}


def report_response_json(client, api_path, report, params):
    url = f'{api_path}/report/{report}?' + urlencode(params)
    logging.warning(f'{url = }')
    response = client.get(url)
    assert response.status == '200 OK'
    return [json.loads(x) for x in io.StringIO(response.text).readlines()]


@pytest.mark.parametrize('params', good_param_combinations())
def test_data_report_good_params(client, api_path, params):
    json_lines = report_response_json(client, api_path, 'pipeline-data', params)

    # Check that values match those requested
    expected = expected_values(params)
    for row in json_lines:
        for col, val in expected.items():
            assert row.get(col) == val


def test_pipeline_data_location(client, api_path):
    for param, expected in (
        ('true', r'/test/loc_root/.+'),  # Uses default from metadata table test data
        ('/my/loc/root', r'/my/loc/root/.+'),
    ):
        json_lines = report_response_json(
            client,
            api_path,
            'pipeline-data',
            {
                'format': 'NDJSON',
                'root': param,
            },
        )
        for row in json_lines:
            for col in (
                'location_root',
                'location',
                'file_location',
            ):
                assert re.fullmatch(expected, row[col])


def test_ont_data_report(client, api_path):
    all_ont = report_response_json(
        client,
        api_path,
        'ont-data',
        {
            'format': 'NDJSON',
        },
    )
    meth_ont = report_response_json(
        client,
        api_path,
        'ont-data',
        {
            'format': 'NDJSON',
            'has_methylation': 'true',
        },
    )
    assert len(meth_ont) < len(all_ont)


def test_pacbio_data_report(client, api_path):
    all_pacbio = report_response_json(
        client,
        api_path,
        'pacbio-data',
        {
            'format': 'NDJSON',
        },
    )
    null_meth_pacbio = report_response_json(
        client,
        api_path,
        'pacbio-data',
        {
            'format': 'NDJSON',
            'has_methylation': 'null',
        },
    )
    assert len(null_meth_pacbio) < len(all_pacbio)


def test_bioproject_report(client, api_path):
    species_bioprojects = report_response_json(
        client,
        api_path,
        'species-bioproject',
        {
            'format': 'NDJSON',
        },
    )
    assert len(species_bioprojects) == 3
    proj_links = 0
    prod_links = 0
    for row in species_bioprojects:
        if p := row['project_accessions']:
            proj_links += len(p)
        if d := row['product_accessions']:
            prod_links += len(d)
    assert proj_links > 1
    assert prod_links > 1

    tol_bioprojects = report_response_json(
        client,
        api_path,
        'species-bioproject',
        {
            'format': 'NDJSON',
            'accession': 'PRJEB40665',
        },
    )
    assert len(tol_bioprojects) == 2


@pytest.fixture
def max_bases(client, api_path):
    json_lines = report_response_json(
        client, api_path, 'specimen-status', {'format': 'NDJSON'}
    )
    assert json_lines
    return sum_species_data_bases(json_lines)


def sum_species_data_bases(json_lines):
    bases = 0
    for obj in json_lines:
        for dtm in obj['species_data']:
            bases += dtm['bases']
    return bases


def specimen_status_param_combinations():
    for param in (
        {'processed': '1'},
        {'processed': '0'},
        {'processed': 'null'},
        {'project': 'protist-microalgae'},
        {'qc': 'pass'},
        {'qc': 'null'},
        {'visibility': 'Always'},
        {'assignee': 'tester'},
        {'assignee': 'null'},
    ):
        yield {'format': 'NDJSON', **param}


@pytest.mark.parametrize('params', specimen_status_param_combinations())
def test_specimen_status_report(max_bases, client, api_path, params):
    json_lines = report_response_json(client, api_path, 'specimen-status', params)

    bases = sum_species_data_bases(json_lines)
    assert 0 < bases < max_bases


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
    assert response.status == '500 INTERNAL SERVER ERROR'
