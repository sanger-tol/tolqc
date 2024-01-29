import io
import pytest

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from tolqc.sample_data_models import VisibilityDict

from .conftest import SKIP_IF_NO_DB_URI_ENV as pytestmark


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
    dubious = VisibilityDict(
        visibility='Dubious',
        description='Data under investigation',
    )
    db_session.add(dubious)
    # commit() instead of flush() here would make it visible to the next
    # function / session
    assert db_session.flush() is None


def test_fetch_visibility_dubious_is_none(db_session):
    assert db_session.get(VisibilityDict, 'Dubious') == None


def test_pacbio_run_data_report(client):
    response = client.get('/reports/pacbio-run-data')
    tsv_lines = io.StringIO(response.text).readlines()

    assert len(tsv_lines) == 89

