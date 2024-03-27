# SPDX-FileCopyrightText: 2024 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

import logging
import os
import pathlib

from flask import testing

import pytest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from tol.sql.database import DefaultDatabase

from tolqc.flask import application, models_list
from tolqc.model import Base
from tolqc.system_models import User

from werkzeug.datastructures import Headers

from .data_objects import test_data

SKIP_IF_NO_DB_URI_ENV = pytest.mark.skipif(
    os.getenv('DB_URI') is None,
    reason='No database. Environment variable DB_URI not set',
)


@pytest.fixture(scope='session')
def api_path():
    return os.getenv('TOLQC_API_PATH', os.getenv('API_PATH', '/api/v1'))


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
    Base.metadata.create_all(connection)

    # Create a `sessionmaker` bound to the `connection` which created the
    # database.
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
        for obj in test_data():
            session.merge(obj)
        session.add(
            User(
                id=100,
                email='skdsjdkj',
                token=os.environ['API_TOKEN'],
                name='lol'
            )
        )
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
    app.testing = True

    return app


class TestClient(testing.FlaskClient):
    def open(self, *args, **kwargs):  # noqa: A003
        headers = kwargs.setdefault('headers', Headers())
        headers.add('token', os.getenv('API_TOKEN'))
        return super().open(*args, **kwargs)


@pytest.fixture()
def client(flask_app):
    flask_app.test_client_class = TestClient
    return flask_app.test_client()
