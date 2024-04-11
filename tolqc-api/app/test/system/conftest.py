# SPDX-FileCopyrightText: 2024 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

import logging
import os
import pathlib

from flask import testing

import pytest

from sqlalchemy import and_, create_engine, select
from sqlalchemy.event import listen, remove
from sqlalchemy.orm import configure_mappers, sessionmaker

from tolqc.flask import application
from tolqc.model import Base, update_logbase_closure
from tolqc.system_models import Token, User

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


@pytest.fixture(scope='session')
def token() -> str:
    return 'I love tokens!!!'


@pytest.fixture
def session_factory(token: str):
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
    configure_mappers()  # Required for creation of EditBase subclasses
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
        with session.no_autoflush:
            for obj in test_data(token):
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
def flask_app(session_factory):
    app = application(
        session_factory=session_factory,
    )
    app.testing = True

    return app


@pytest.fixture
def logbase_db_session(session_factory, token):
    with session_factory() as ssn:
        user_id = ssn.scalar(
            select(User.id)
            .join(Token)
            .where(
                and_(
                    User.registered == True,  # noqa: E712
                    Token.token == token,
                )
            )
        )
        hook_params = ssn, 'before_flush', update_logbase_closure(user_id)
        listen(*hook_params)
        yield ssn
        remove(*hook_params)


@pytest.fixture()
def client(flask_app, token):
    class TestClient(testing.FlaskClient):
        def open(self, *args, **kwargs):  # noqa: A003
            headers = kwargs.setdefault('headers', Headers())
            headers.add('token', token)
            return super().open(*args, **kwargs)

    flask_app.test_client_class = TestClient
    return flask_app.test_client()
