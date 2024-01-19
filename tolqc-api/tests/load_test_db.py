import gzip
import pathlib
import pickle

import click

from sqlalchemy import create_engine, select
from sqlalchemy.orm import selectinload, sessionmaker

from tolqc.model import Base


@click.command(help='Create and load test database')
@click.option(
    '--db-uri',
    envvar='DB_URI',
    help=('URI of the ToLQC test database to write to'),
    required=True,
    show_default=True,
)
@click.option(
    '--echo-sql/--no-echo-sql',
    help='Echo SQLAlchemy SQL to STDERR',
    default=False,
    show_default=True,
)
@click.option(
    '--pickled-data',
    help='File containing pickled and gzipped data',
    type=click.Path(
        dir_okay=False,
        exists=True,
        readable=True,
        path_type=pathlib.Path,
    ),
    required=True,
)
def cli(db_uri, echo_sql, pickled_data):
    engine = create_engine(db_uri, echo=echo_sql)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    with gzip.open(pickled_data, 'rb') as pkl_file:
        test_data = pickle.load(pkl_file)
    with Session() as session:
        for obj in test_data:
            session.merge(obj)
        session.commit()



if __name__ == '__main__':
    cli()
