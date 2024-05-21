"""BigInt JSONB and data.name

Revision ID: 7088fcbeadcd
Revises: b6a23971491c
Create Date: 2024-05-21 13:43:08.715450

"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '7088fcbeadcd'
down_revision = 'b6a23971491c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Rename data.name_root to data.name and give it a unique constraint
    op.drop_index('ix_data_name_root', table_name='data')
    op.alter_column('data', 'name_root', new_column_name='name')
    op.create_unique_constraint(None, 'data', ['name'])

    # Columns which need to be BIGINT
    for table, column in (
        ('assembly_metrics', 'contig_length'),
        ('assembly_metrics', 'contig_n50'),
        ('assembly_metrics', 'contig_longest'),
        ('assembly_metrics', 'contig_shortest'),
        ('assembly_metrics', 'scaffold_n50'),
        ('assembly_metrics', 'gap_n50'),
        ('data', 'reads'),
        ('data', 'read_length_n50'),
        ('dataset', 'reads'),
        ('dataset', 'read_length_n50'),
    ):
        op.alter_column(
            table,
            column,
            existing_type=sa.INTEGER(),
            type_=sa.BigInteger(),
            existing_nullable=True,
        )

    # Change results columns to JSONB
    for table in (
        'contigviz_metrics',
        'genomescope_metrics',
        'markerscan_metrics',
    ):
        op.alter_column(
            table,
            'results',
            existing_type=postgresql.JSON(astext_type=sa.Text()),
            type_=postgresql.JSONB(astext_type=sa.Text()),
            existing_nullable=True,
        )


def downgrade() -> None:
    pass
