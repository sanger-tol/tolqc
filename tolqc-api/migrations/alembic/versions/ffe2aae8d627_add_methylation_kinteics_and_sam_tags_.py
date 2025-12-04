"""Add methylation, kinteics and SAM tags fields to file table

Revision ID: ffe2aae8d627
Revises: 81bf8897c7c6
Create Date: 2025-12-01 12:08:06.456989

"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
from sqlalchemy.schema import CreateSequence, DropSequence, Sequence

# revision identifiers, used by Alembic.
revision = 'ffe2aae8d627'
down_revision = '81bf8897c7c6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Add columns to file table
    op.add_column('file', sa.Column('has_methylation', sa.Boolean(), nullable=True))
    op.add_column('file', sa.Column('has_kinetics', sa.Boolean(), nullable=True))
    op.add_column(
        'file',
        sa.Column('sam_tags', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    )
    op.create_index(
        op.f('ix_file_has_kinetics'), 'file', ['has_kinetics'], unique=False
    )
    op.create_index(
        op.f('ix_file_has_methylation'), 'file', ['has_methylation'], unique=False
    )

    # Schema changes from TOLP-9082 and TOLP-9248
    op.create_table(
        'loader',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('source_object_type', sa.String(), nullable=False),
        sa.Column('destination_object_type', sa.String(), nullable=False),
        sa.Column(
            'object_filters', postgresql.JSONB(astext_type=sa.Text()), nullable=True
        ),
        sa.Column('prefix', sa.String(), nullable=False),
        sa.Column('convert_class', sa.String(), nullable=True),
        sa.Column(
            'candidate_key', postgresql.JSONB(astext_type=sa.Text()), nullable=True
        ),
        sa.Column('ids_object_type', sa.String(), nullable=True),
        sa.Column('ids_attribute', sa.String(), nullable=True),
        sa.Column(
            'ids_object_filters', postgresql.JSONB(astext_type=sa.Text()), nullable=True
        ),
        sa.Column('ids_sort_by', sa.String(), nullable=True),
        sa.Column('ids_attribute_in_source', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_table(
        'loader_instance',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('frequency_weekly', sa.Boolean(), nullable=True),
        sa.Column('frequency_daily', sa.Boolean(), nullable=True),
        sa.Column('frequency_hourly', sa.Boolean(), nullable=True),
        sa.Column('frequency_quarter_hourly', sa.Boolean(), nullable=True),
        sa.Column('date_last_run', sa.DateTime(), nullable=True),
        sa.Column('loader_id', sa.Integer(), nullable=False),
        sa.Column('source_data_source_instance_id', sa.String(), nullable=False),
        sa.Column('destination_data_source_instance_id', sa.String(), nullable=False),
        sa.Column('ids_data_source_instance_id', sa.String(), nullable=True),
        sa.ForeignKeyConstraint(
            ['destination_data_source_instance_id'],
            ['data_source_instance.id'],
        ),
        sa.ForeignKeyConstraint(
            ['ids_data_source_instance_id'],
            ['data_source_instance.id'],
        ),
        sa.ForeignKeyConstraint(
            ['loader_id'],
            ['loader.id'],
        ),
        sa.ForeignKeyConstraint(
            ['source_data_source_instance_id'],
            ['data_source_instance.id'],
        ),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_table(
        'data_source_config_summary',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('source_object_type', sa.String(), nullable=False),
        sa.Column('destination_object_type', sa.String(), nullable=True),
        sa.Column(
            'object_filters',
            postgresql.JSONB(astext_type=sa.Text()),
            nullable=False,
        ),
        sa.Column(
            'group_by',
            postgresql.JSONB(astext_type=sa.Text()),
            nullable=False,
        ),
        sa.Column(
            'stats_fields',
            postgresql.JSONB(astext_type=sa.Text()),
            nullable=False,
        ),
        sa.Column(
            'stats',
            postgresql.JSONB(astext_type=sa.Text()),
            nullable=False,
        ),
        sa.Column('prefix', sa.String(), nullable=False),
        sa.Column('data_source_config_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ['data_source_config_id'],
            ['data_source_config.id'],
        ),
        sa.PrimaryKeyConstraint('id'),
    )

    # Rename sequences with temporary names from previous Alembic migration
    for tbl in ('assembly', 'study'):
        id_seq = f'{tbl}_{tbl}_id_seq'

        # Remove the old sequence
        op.alter_column(tbl, f'{tbl}_id', server_default=None)
        op.execute(DropSequence(Sequence(f'_alembic_tmp_{id_seq}')))

        # Create the new sequence
        op.execute(CreateSequence(Sequence(id_seq)))
        op.alter_column(
            'data',
            'data_id',
            server_default=sa.text(f"nextval('{id_seq}'::regclass)"),
        )

        # Set sequence to correct current value
        set_sql = sa.text(
            f"SELECT setval('{id_seq}', (SELECT MAX({tbl}_id) FROM {tbl}))"  # noqa: S608
        )
        op.execute(set_sql)


def downgrade() -> None:
    pass
