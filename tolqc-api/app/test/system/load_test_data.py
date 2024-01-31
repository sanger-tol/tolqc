# SPDX-FileCopyrightText: 2024 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

import gzip
import pickle

import click

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from tolqc.model import Base

from .fetch_test_data import db_uri, echo_sql, pickled_data


@click.command(
    help=('Create and load a test database from pickled, gzipped data')
)
@db_uri
@echo_sql
@pickled_data
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
