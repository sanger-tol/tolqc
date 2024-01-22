import gzip
import os
import pathlib
import pickle
import pytest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from tolqc.model import Base


connection = pytest.mark.skipif(
    os.getenv('DB_URI') is None,
    reason='Missing environment variable DB_URI',
)


@pytest.fixture(scope='session')
def data_dir():
    return pathlib.Path(__file__).parent / 'data'


@pytest.fixture(scope='session')
def pkl_gz_file(data_dir):
    return data_dir / 'test_db.pkl.gz'


@pytest.fixture(scope='session')
def unpickled_data(pkl_gz_file):
    with gzip.open(pkl_gz_file, 'rb') as pkl_fh:
        test_data = pickle.load(pkl_fh)
    return test_data


@pytest.fixture(scope='session')
def db_engine():
    db_uri = os.getenv('DB_URI')
    assert db_uri
    engine = create_engine(db_uri)
    connection = engine.connect()
    trnsctn = connection.begin()
    Base.metadata.create_all(connection)
    yield connection
    trnsctn.rollback()


@pytest.fixture(scope='session')
def make_session(db_engine, unpickled_data):
    maker = sessionmaker(
        bind=db_engine,
        join_transaction_mode='create_savepoint',
    )
    with maker() as session:
        for obj in unpickled_data:
            session.merge(obj)
        session.commit()
    return maker


@pytest.fixture
def db_session(make_session):
    with make_session() as session:
        yield session
        session.rollback()
