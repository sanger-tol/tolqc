# SPDX-FileCopyrightText: 2024 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

import os
import pathlib

import pytest

from sqlalchemy import create_engine, text
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
def sql_data_file(data_dir):
    """
    The file containing sample test data as SQLAlchemy ORM data objects,
    pickled and gzipped.
    """
    return data_dir / 'test_data.sql'


@pytest.fixture(scope='session')
def sql_data(sql_data_file):
    """
    Returns the list of unpickled SQLAlchemy ORM data objects.
    """
    with open(sql_data_file, 'r') as sql_fh:
        test_data = sql_fh.read()
    return text(test_data)


@pytest.fixture
def db_connection(sql_data):
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
    connection.execute(sql_data)
    connection.execute(text('SET search_path TO public'))

    yield connection
    txn.rollback()
    connection.close()


@pytest.fixture
def session_factory(db_connection):
    """
    Creates a `sessionmaker` bound to the `db_connection` which created the
    database.
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
    return maker


@pytest.fixture
def db_session(session_factory):
    """
    Yields a session for each test function (the default scope), which by
    default is rolled back after the function returns.
    """
    with session_factory() as session:
        yield session


@pytest.fixture
def database_factory_and_session(session_factory):
    def db_factory_for_testing(*_):
        return DefaultDatabase(
            session_factory=session_factory, models=models_list()
        )

    return db_factory_for_testing, session_factory


@pytest.fixture
def flask_app(database_factory_and_session):
    database_factory, session_factory = database_factory_and_session
    app = application(
        session_factory=session_factory,
        database_factory=database_factory,
    )
    app.config.update(
        {
            'TESTING': True,
        }
    )

    return app


@pytest.fixture()
def client(flask_app):
    return flask_app.test_client()
