# SPDX-FileCopyrightText: 2024 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

import logging
import os
import pathlib

import pytest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from tol.sql.database import DefaultDatabase

from tolqc import application, models_list
from tolqc.model import Base

from .data_objects import TEST_DATA

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


@pytest.fixture
def session_factory():
    """
    Creates a connection to the database specified in the `DB_URI` environment
    variable, creates the database schema, starts a transaction, and yields
    the session_factory. The transaction is rolled back after the yield,
    leaving an empty database with no tables.
    """
    db_uri = os.getenv('DB_URI')
    assert db_uri
    engine = create_engine(db_uri)
    if os.getenv('SQL_ECHO'):
        logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
    connection = engine.connect()
    txn = connection.begin()
    Base.metadata.create_all(engine)

    """
    # Create a `sessionmaker` bound to the `connection` which created the
    database.
    """
    ssn_fctry = sessionmaker(
        # Bind to the single connection that created and populated the
        # database with test data.
        bind=connection,
        # `create_savepoint` makes new transactions nested via SAVEPOINT
        # instructions which can then be rolled back within the
        # connection's existing transaction.
        join_transaction_mode='create_savepoint',
    )

    with ssn_fctry() as session:
        # Create the database schema
        for obj in TEST_DATA:
            session.merge(obj)
        session.commit()

    yield ssn_fctry
    txn.rollback()
    connection.close()


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
