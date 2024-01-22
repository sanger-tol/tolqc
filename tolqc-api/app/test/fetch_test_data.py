import gzip
import pathlib
import pickle

import click

from sqlalchemy import create_engine, select
from sqlalchemy.orm import selectinload, sessionmaker

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

data_dir = pathlib.Path(__file__).parents / 'data'

db_uri = click.option(
    '--db-uri',
    envvar='DB_URI',
    help=(
        'URI of the ToLQC test database.'
        ' Uses DB_URI environment variable if not specified'
    ),
    required=True,
)

pickled_data = click.option(
    '--pickled-data',
    help='File of pickled and gzipped data for test database',
    type=click.Path(
        dir_okay=False,
        exists=True,
        readable=True,
        path_type=pathlib.Path,
    ),
    default=data_dir / 'test_db.pkl.gz',
    required=True,
    show_default=True,
)


@click.command(
    help='Dump sample data from the production ToLQC database',
)
@db_uri
@pickled_data
@click.option(
    '--echo-sql/--no-echo-sql',
    help='Echo SQLAlchemy SQL to STDERR',
    default=False,
    show_default=True,
)
def cli(db_uri, pickled_data, echo_sql):
    engine = create_engine(db_uri, echo=echo_sql)
    ssn_maker = sessionmaker(bind=engine)
    session = ssn_maker()
    fetched = []

    # Fetch data from the dictionary-like tables
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

    with gzip.open(pickled_data, 'wb') as pkl:
        pickle.dump(fetched, pkl)
    click.echo(f"Wrote data for test DB to: '{pickled_data}'")


def data_dir():
    return pathlib.Path(__file__).parent / 'data'


def fetch_species_data(session, species_list):
    """
    Fetches a list of Species from the database, with all their data that
    we're interested in pre-fetched and attached via SELECT IN loads.
    """

    statement = (
        select(Species)
        .filter(Species.species_id.in_(species_list))
        # Specify a `selectinload` path to each leaf we want
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
