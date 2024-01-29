import gzip
import os
import pathlib
import pickle

import pytest

from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from tol.sql.database import DefaultDatabase

from tolqc import application, models_list
from tolqc.model import Base


SKIP_IF_NO_DB_URI_ENV = pytest.mark.skipif(
    os.getenv('DB_URI') is None,
    reason='No database. Environment variable DB_URI not set',
)


@pytest.fixture(scope='session')
def data_dir():
    """
    The directory where test data checked in to version control is stored.
    """
    return pathlib.Path(__file__).parent / 'data'


@pytest.fixture(scope='session')
def pkl_gz_file(data_dir):
    """
    The file containing sample test data as SQLAlchemy ORM data objects,
    pickled and gzipped.
    """
    return data_dir / 'test_db.pkl.gz'


@pytest.fixture(scope='session')
def unpickled_data(pkl_gz_file):
    """
    Returns the list of unpickled SQLAlchemy ORM data objects.
    """
    with gzip.open(pkl_gz_file, 'rb') as pkl_fh:
        test_data = pickle.load(pkl_fh)
    return test_data


@pytest.fixture(scope='module')
def db_connection():
    """
    Creates a connection to the database specified in the `DB_URI` environment
    variable, creates the database schema, starts a transaction, and yields
    the connection. The transaction is rolled back after the yield, leaving
    an empty database with no tables.
    """
    db_uri = os.getenv('DB_URI')
    assert db_uri
    engine = create_engine(db_uri, echo=True)
    connection = engine.connect()
    txn = connection.begin()

    # Create the database schema
    Base.metadata.create_all(connection)

    yield connection
    txn.rollback()
    connection.close()


@pytest.fixture(scope='module')
def make_session(db_connection, unpickled_data):
    """
    Creates a `sessionmaker` bound to the `db_connection` which created the
    database, uses a `Session` to populate the test database using the
    pickled ORM objects, and returns the `sessionmaker`.
    """
    maker = sessionmaker(
        # Bind to the single connection that created and populated the
        # database with test data.
        bind=db_connection,
        # `create_savepoint` makes new transactions nested via SAVEPOINT
        # instructions which can then be rolled back within the
        # db_connection's existing transaction.
        join_transaction_mode='create_savepoint',
    )
    with maker() as session:
        for obj in unpickled_data:
            session.merge(obj)
        session.commit()
    return maker


@pytest.fixture
def db_session(make_session):
    """
    Yields a session for each test function (the default scope), which by
    default is rolled back after the function returns. Note: changes which
    have been committed will remain after the function returns.
    """
    with make_session() as session:
        yield session
        session.rollback()


@pytest.fixture(scope='module')
def database_factory(make_session):

    @contextmanager
    def session_factory():
        with make_session() as session:
            yield session
            session.rollback()

    def db_factory_for_testing(_, __):
        return DefaultDatabase(
            session_factory=session_factory, models=models_list()
        )

    return db_factory_for_testing


@pytest.fixture
def flask_app(database_factory):
    app = application(database_factory=database_factory)
    app.config.update(
        {
            'TESTING': True,
        }
    )

    return app


@pytest.fixture()
def client(flask_app):
    return flask_app.test_client()
