import gzip
import pathlib

import click

from sqlalchemy import create_engine, select
from sqlalchemy.ext.serializer import dumps
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


@click.command(
    help='Dump sample data from the production ToLQC database',
)
@click.option(
    '--db-uri',
    envvar='DB_URI',
    help=(
        'URI of the ToLQC source database to use.'
        ' Uses DB_URI environment variable if not specified'
    ),
    required=True,
    show_default=True,
)
@click.option(
    '--echo-sql/--no-echo-sql',
    help='Echo SQLAlchemy SQL to STDERR',
    default=False,
    show_default=True,
)
def cli(db_uri, echo_sql):
    engine = create_engine(db_uri, echo=echo_sql)
    ssn_maker = sessionmaker(bind=engine)
    session = ssn_maker()
    fetched = []

    # Fetch data from
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
        fetched.append(entries)

    species_list = 'Adalia bipunctata', 'Quercus robur', 'Juncus effusus'
    fetched.append(fetch_species_data(session, species_list))
    pkl_file = data_dir() / 'test_db.pkl.gz'
    with gzip.open(pkl_file, 'wb') as pkl:
        pkl.write(dumps(fetched))
    click.echo(f"Wrote to: '{pkl_file}'")


def data_dir():
    return pathlib.Path(__file__).parent / 'data'


def fetch_species_data(session, species_list):
    statement = (
        # Enumerate a `selectinload` path to each leaf we want
        select(Species)
        .filter(Species.species_id.in_(species_list))
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
