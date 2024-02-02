# SPDX-FileCopyrightText: 2024 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

import io
import re

import pytest

from sqlalchemy.exc import IntegrityError

from tolqc.sample_data_models import Data, Platform, Run, VisibilityDict

from .conftest import SKIP_IF_NO_DB_URI_ENV as pytestmark  # noqa: F401, N811


def test_fetch_visibility_always(db_session):
    """
    Test fetching the 'Always' entry from the VisibilityDict, which will
    invariably be present if a ToLQC database has been created and
    populated.
    """
    always = db_session.get(VisibilityDict, 'Always')
    assert always.visibility == 'Always'


def test_delete_visibility_always(db_session):
    """
    Deleting the 'Always' entry from the VisibilityDict will raise an
    IntegrityError
    """
    always = db_session.get(VisibilityDict, 'Always')
    db_session.delete(always)
    with pytest.raises(IntegrityError):
        db_session.flush()


def test_insert_visibility_dubious(db_session):
    """
    Test adding a new entry to a table.
    """
    dubious = VisibilityDict(
        visibility='Dubious',
        description='Data under investigation',
    )
    db_session.add(dubious)
    # Even though we commit() here, it will not be visible in the next test
    # function called
    assert db_session.commit() is None


def test_fetch_visibility_dubious_is_now_none(db_session):
    """
    Dubious should now be absent from VisibilityDict, despite being committed
    by test_insert_visibility_dubious()
    """
    assert db_session.get(VisibilityDict, 'Dubious') is None


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


def test_pacbio_run_data_report_tsv(client, pacbio_row_count):
    """
    Test PacBio run report with default format
    """
    response = client.get('/reports/pacbio-run-data')
    assert response.status == '200 OK'

    # Check Content-Disposition header
    dspstn = response.headers.get('Content-Disposition')
    assert re.fullmatch(
        r'attachment; filename="pacbio_run_data_\d{4}-\d\d-\d\d\.tsv"',
        dspstn,
    )

    tsv_lines = io.StringIO(response.text).readlines()
    assert len(tsv_lines) == 1 + pacbio_row_count


def test_pacbio_run_data_report_ndjson(client, pacbio_row_count):
    """
    Test NDJSON format request.
    """
    response = client.get('/reports/pacbio-run-data?format=NDJSON')
    assert response.status == '200 OK'

    tsv_lines = io.StringIO(response.text).readlines()
    assert len(tsv_lines) == pacbio_row_count


def test_pacbio_run_data_report_csv(client):
    """
    Requesting an unsupported format should be a 400
    """
    response = client.get('/reports/pacbio-run-data?format=CSV')
    assert response.status == '400 BAD REQUEST'
