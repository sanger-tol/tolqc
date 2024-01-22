import gzip
import pathlib
import pickle

import click

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from tolqc.model import Base

from .fetch_test_data import db_uri, pickled_data


@click.command(help='Create and load test database')
@db_uri
@pickled_data
@click.option(
    '--echo-sql/--no-echo-sql',
    help='Echo SQLAlchemy SQL to STDERR',
    default=False,
    show_default=True,
)
def cli(db_uri, echo_sql, pickled_data):
    engine = create_engine(db_uri, echo=echo_sql)
    Base.metadata.create_all(engine)
    make_session = sessionmaker(bind=engine)
    with gzip.open(pickled_data, 'rb') as pkl_file:
        test_data = pickle.load(pkl_file)
    with make_session() as session:
        for obj in test_data:
            session.merge(obj)
        session.commit()


if __name__ == '__main__':
    cli()
