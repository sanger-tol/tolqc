"""Some columns need BigInteger

Revision ID: 3936f8476e07
Revises: 16a0a61ffec9
Create Date: 2023-07-11 11:52:39.457713

"""
from alembic import op

import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3936f8476e07'
down_revision = '16a0a61ffec9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column(
        'assembly_metrics',
        'bases',
        existing_type=sa.INTEGER(),
        type_=sa.BigInteger(),
        existing_nullable=True,
    )
    op.alter_column(
        'assembly_metrics',
        'a',
        existing_type=sa.INTEGER(),
        type_=sa.BigInteger(),
        existing_nullable=True,
    )
    op.alter_column(
        'assembly_metrics',
        'c',
        existing_type=sa.INTEGER(),
        type_=sa.BigInteger(),
        existing_nullable=True,
    )
    op.alter_column(
        'assembly_metrics',
        'g',
        existing_type=sa.INTEGER(),
        type_=sa.BigInteger(),
        existing_nullable=True,
    )
    op.alter_column(
        'assembly_metrics',
        't',
        existing_type=sa.INTEGER(),
        type_=sa.BigInteger(),
        existing_nullable=True,
    )
    op.alter_column(
        'assembly_metrics',
        'n',
        existing_type=sa.INTEGER(),
        type_=sa.BigInteger(),
        existing_nullable=True,
    )
    op.alter_column(
        'assembly_metrics',
        'cpg',
        existing_type=sa.INTEGER(),
        type_=sa.BigInteger(),
        existing_nullable=True,
    )
    op.alter_column(
        'data',
        'bases',
        existing_type=sa.INTEGER(),
        type_=sa.BigInteger(),
        existing_nullable=True,
    )
    op.alter_column(
        'dataset',
        'bases',
        existing_type=sa.INTEGER(),
        type_=sa.BigInteger(),
        existing_nullable=True,
    )
    op.alter_column(
        'pacbio_run_metrics',
        'total_bases',
        existing_type=sa.INTEGER(),
        type_=sa.BigInteger(),
        existing_nullable=True,
    )
    op.alter_column(
        'species',
        'genome_size',
        existing_type=sa.INTEGER(),
        type_=sa.BigInteger(),
        existing_nullable=True,
    )
    op.alter_column(
        'specimen',
        'hierarchy_name',
        existing_type=sa.VARCHAR(),
        nullable=True,
    )
    op.drop_constraint(
        'specimen_hierarchy_name_key',
        'specimen',
        type_='unique',
    )


def downgrade() -> None:
    op.create_unique_constraint(
        'specimen_hierarchy_name_key',
        'specimen',
        ['hierarchy_name'],
    )
    op.alter_column(
        'specimen',
        'hierarchy_name',
        existing_type=sa.VARCHAR(),
        nullable=False,
    )
    op.alter_column(
        'species',
        'genome_size',
        existing_type=sa.BigInteger(),
        type_=sa.INTEGER(),
        existing_nullable=True,
    )
    op.alter_column(
        'pacbio_run_metrics',
        'total_bases',
        existing_type=sa.BigInteger(),
        type_=sa.INTEGER(),
        existing_nullable=True,
    )
    op.alter_column(
        'dataset',
        'bases',
        existing_type=sa.BigInteger(),
        type_=sa.INTEGER(),
        existing_nullable=True,
    )
    op.alter_column(
        'data',
        'bases',
        existing_type=sa.BigInteger(),
        type_=sa.INTEGER(),
        existing_nullable=True,
    )
    op.alter_column(
        'assembly_metrics',
        'cpg',
        existing_type=sa.BigInteger(),
        type_=sa.INTEGER(),
        existing_nullable=True,
    )
    op.alter_column(
        'assembly_metrics',
        'n',
        existing_type=sa.BigInteger(),
        type_=sa.INTEGER(),
        existing_nullable=True,
    )
    op.alter_column(
        'assembly_metrics',
        't',
        existing_type=sa.BigInteger(),
        type_=sa.INTEGER(),
        existing_nullable=True,
    )
    op.alter_column(
        'assembly_metrics',
        'g',
        existing_type=sa.BigInteger(),
        type_=sa.INTEGER(),
        existing_nullable=True,
    )
    op.alter_column(
        'assembly_metrics',
        'c',
        existing_type=sa.BigInteger(),
        type_=sa.INTEGER(),
        existing_nullable=True,
    )
    op.alter_column(
        'assembly_metrics',
        'a',
        existing_type=sa.BigInteger(),
        type_=sa.INTEGER(),
        existing_nullable=True,
    )
    op.alter_column(
        'assembly_metrics',
        'bases',
        existing_type=sa.BigInteger(),
        type_=sa.INTEGER(),
        existing_nullable=True,
    )
