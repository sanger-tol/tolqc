"""datetime timezones and more BigInteger columns

Revision ID: 6f373edef955
Revises: b54733d21719
Create Date: 2023-09-28 16:41:31.283922

"""
from alembic import op

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '6f373edef955'
down_revision = 'b54733d21719'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Add timezone to TIMESTAMP columns
    for tbl_col in (
        ('accession', 'date_submitted'),
        ('assembly_status', 'status_time'),
        ('busco_lineage', 'date_created'),
        ('data', 'date'),
        ('dataset_status', 'status_time'),
        ('run', 'complete'),
        ('run', 'start'),
        ('specimen_status', 'status_time'),
    ):
        op.alter_column(
            *tbl_col,
            existing_type=postgresql.TIMESTAMP(),
            type_=sa.DateTime(timezone=True),
            existing_nullable=False,
        )

    # Add timezone to the LogBase TIMESTAMP columns
    for tbl in (
        'assembly',
        'assembly_status',
        'data',
        'dataset',
        'dataset_status',
        'genomescope_metrics',
        'sample',
        'species',
        'specimen',
        'specimen_status',
    ):
        for col in (
            'created_at',
            'last_modified_at',
        ):
            op.alter_column(
                tbl,
                col,
                existing_type=postgresql.TIMESTAMP(),
                type_=sa.DateTime(timezone=True),
                existing_nullable=False,
            )

    # file.size and GenomeScope metrics that need to be a BIGINT
    for tbl_col in (
        ('file', 'size_bytes'),
        ('genomescope_metrics', 'haploid_length'),
        ('genomescope_metrics', 'repeat_length'),
        ('genomescope_metrics', 'unique_length'),
    ):
        op.alter_column(
            *tbl_col,
            existing_type=sa.INTEGER(),
            type_=sa.BigInteger(),
            existing_nullable=True,
        )

    # species.hierarchy_name is not always unique
    op.drop_constraint('species_hierarchy_name_key', 'species', type_='unique')
    op.create_index(
        op.f('ix_species_hierarchy_name'),
        'species',
        ['hierarchy_name'],
        unique=False,
    )
