import os
from logging.config import fileConfig

from alembic import context

from sqlalchemy import create_engine

from tolqc.model import Base

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

DB_URI = os.environ['DB_URI']

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = [Base.metadata]

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.s


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    Setting compare_type=True instructs autogenerate to compare column types.
    """
    connectable = create_engine(DB_URI)
    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
        )

        with context.begin_transaction():
            context.run_migrations()


run_migrations_online()
