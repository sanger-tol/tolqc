# SPDX-FileCopyrightText: 2024 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

import pathlib
import subprocess
import sys

import click

from psycopg2.errors import DuplicateDatabase

from sqlalchemy import create_engine, select, text
from sqlalchemy.engine import make_url
from sqlalchemy.exc import ProgrammingError
from sqlalchemy.orm import selectinload, sessionmaker

from tolqc.model import Base
from tolqc.sample_data_models import (
    AccessionTypeDict,
    Allocation,
    Centre,
    Data,
    LibraryType,
    Platform,
    QCDict,
    Run,
    Sample,
    Sex,
    Species,
    Specimen,
    VisibilityDict,
)

data_dir = pathlib.Path(__file__).parent / 'data'


@click.command(
    help='Dump sample data from the production ToLQC database',
)
@click.option(
    '--db-uri',
    envvar='DB_URI',
    help=(
        'URI of the ToLQC source database.'
        ' Uses DB_URI environment variable if not specified'
    ),
    required=True,
)
@click.option(
    '--sql-data-file',
    help='File of pickled and gzipped data for test database',
    type=click.Path(
        dir_okay=False,
        readable=True,
        path_type=pathlib.Path,
    ),
    default=data_dir / 'test_data.sql',
    required=True,
    show_default=True,
)
@click.option(
    '--build-db-uri',
    envvar='BUILD_DB_URI',
    help=(
        'URI of the a database for building SQL dump which will be created'
        ' and dropped.'
        " Defaults to the --db-uri with the database name 'test_data_build'"
    ),
)
@click.option(
    '--echo-sql/--no-echo-sql',
    help='Echo SQLAlchemy SQL to STDERR',
    default=False,
    show_default=True,
)
@click.option(
    '--delete-build-db/--keep-build-db',
    help='Delete or keep database of sample data after creating SQL dump',
    default=True,
    show_default=True,
)
def cli(db_uri, build_db_uri, sql_data_file, echo_sql, delete_build_db):
    # Create empty database to receive test data
    build_url = make_build_url(db_uri, build_db_uri)
    create_build_db(build_url)
    build_engine = create_engine(build_url, echo=echo_sql)
    Base.metadata.create_all(build_engine)

    # Fetch sample data
    engine = create_engine(db_uri, echo=echo_sql)
    sample_data = build_sample_data(sessionmaker(bind=engine))

    # Populate build database
    populate_database(sessionmaker(bind=build_engine), sample_data)

    # Dump SQL data file
    make_sql_data_file(build_url, sql_data_file)
    click.echo(f"Wrote sample data to file: '{sql_data_file}'")

    # Cleanup build database unless it's wanted
    if delete_build_db:
        build_engine.dispose()
        drop_build_db(build_url)


def make_sql_data_file(build_url, sql_data_file):
    with open(sql_data_file, 'w') as sql_fh:
        sql_dump = subprocess.run(
            (
                'pg_dump',
                '--data-only',
                '--inserts',
                build_url.render_as_string(),
            ),
            stdout=sql_fh,
        )
        sql_dump.check_returncode()


def build_sample_data(ssn_maker):
    fetched = []
    with ssn_maker() as session:
        # Fetch data from all of the dictionary-like tables
        for cls in (
            AccessionTypeDict,
            LibraryType,
            Platform,
            Centre,
            QCDict,
            Sex,
            VisibilityDict,
        ):
            entries = session.scalars(select(cls)).all()
            fetched.extend(entries)

        # Fetch data for a list of test species
        species_list = 'Adalia bipunctata', 'Quercus robur', 'Juncus effusus'
        fetched.extend(fetch_species_data(session, species_list))
    return fetched


def populate_database(ssn_maker, sample_data):
    with ssn_maker() as session:
        for obj in sample_data:
            session.merge(obj)
        session.commit()


def make_build_url(db_uri, build_db_uri):
    if build_db_uri:
        url = make_url(db_uri)
    else:
        url = make_url(db_uri).set(database='test_data_build')
    return url


def create_build_db(build_url):
    engine = pg_engine(build_url)
    try:
        with engine.begin() as conn:
            conn.execute(text(f'CREATE DATABASE {build_url.database}'))
    except ProgrammingError as e:
        if isinstance(e.orig, DuplicateDatabase):
            url_str = build_url.render_as_string(hide_password=True)
            click.echo(f"Error: database '{url_str}' already exists")
            sys.exit(1)
        else:
            raise e


def drop_build_db(build_url):
    engine = pg_engine(build_url)
    with engine.begin() as conn:
        conn.execute(text(f'DROP DATABASE {build_url.database}'))


def pg_engine(url):
    pg_url = url.set(database='postgres')
    return create_engine(pg_url, isolation_level='AUTOCOMMIT')


def fetch_species_data(session, species_list):
    """
    Fetches a list of Species from the database, with all their data that
    we're interested in pre-fetched and attached via SELECT IN loads.
    """

    statement = (
        select(Species)
        .where(Species.species_id.in_(species_list))
        # Specify a `selectinload` path to each leaf we want fetched
        .options(
            selectinload(Species.specimens).selectinload(Specimen.accession)
        )
        .options(
            selectinload(Species.specimens)
            .selectinload(Specimen.samples)
            .selectinload(Sample.accession)
        )
        .options(
            selectinload(Species.specimens)
            .selectinload(Specimen.samples)
            .selectinload(Sample.data)
            .selectinload(Data.project_assn)
            .selectinload(Allocation.project)
        )
        .options(
            selectinload(Species.specimens)
            .selectinload(Specimen.samples)
            .selectinload(Sample.data)
            .selectinload(Data.library)
        )
        .options(
            selectinload(Species.specimens)
            .selectinload(Specimen.samples)
            .selectinload(Sample.data)
            .selectinload(Data.run)
            .selectinload(Run.pacbio_run_metrics)
        )
        .options(
            selectinload(Species.specimens)
            .selectinload(Specimen.samples)
            .selectinload(Sample.data)
            .selectinload(Data.files)
        )
    )
    species_data = session.scalars(statement).all()

    # Check that we found all the requested species
    requested = set(species_list)
    fetched = {s.species_id for s in species_data}
    if miss := requested - fetched:
        msg = f'Failed to fetch species: {miss}'
        raise ValueError(msg)

    return species_data


if __name__ == '__main__':
    cli()
