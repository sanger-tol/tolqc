"""Move assembly metrics into assembly table

Index library_type.reporting_category

Add constraints to allocation table

Revision ID: 2d56a365736e
Revises: 5617d7b038a6
Create Date: 2026-03-11 15:11:08.123612

"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB

# revision identifiers, used by Alembic.
revision = '2d56a365736e'
down_revision = '5617d7b038a6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_index(
        op.f('ix_library_type_reporting_category'),
        'library_type',
        ['reporting_category'],
        unique=False,
    )

    op.create_unique_constraint(
        'allocation_project_id_data_id_key',
        'allocation',
        [
            'project_id',
            'data_id',
        ],
    )
    op.create_unique_constraint(
        'allocation_data_id_is_primary_key',
        'allocation',
        [
            'data_id',
            'is_primary',
        ],
    )

    op.drop_table('assembly_metrics')

    op.add_column('assembly', sa.Column('bases_count', sa.BigInteger(), nullable=True))
    op.add_column('assembly', sa.Column('bases_a', sa.BigInteger(), nullable=True))
    op.add_column('assembly', sa.Column('bases_c', sa.BigInteger(), nullable=True))
    op.add_column('assembly', sa.Column('bases_g', sa.BigInteger(), nullable=True))
    op.add_column('assembly', sa.Column('bases_t', sa.BigInteger(), nullable=True))
    op.add_column('assembly', sa.Column('bases_n', sa.BigInteger(), nullable=True))
    op.add_column('assembly', sa.Column('bases_cpg', sa.BigInteger(), nullable=True))

    op.add_column('assembly', sa.Column('contig_count', sa.Integer(), nullable=True))
    op.add_column('assembly', sa.Column('contig_length', sa.BigInteger(), nullable=True))
    op.add_column('assembly', sa.Column('contig_longest', sa.BigInteger(), nullable=True))
    op.add_column('assembly', sa.Column('contig_shortest', sa.BigInteger(), nullable=True))
    op.add_column('assembly', sa.Column('contig_length_mean', sa.Float(), nullable=True))
    op.add_column('assembly', sa.Column('contig_n50', sa.BigInteger(), nullable=True))
    op.add_column('assembly', sa.Column('contig_l50', sa.BigInteger(), nullable=True))
    op.add_column('assembly', sa.Column('contig_aun', sa.Float(), nullable=True))

    op.add_column('assembly', sa.Column('scaffold_count', sa.Integer(), nullable=True))
    op.add_column('assembly', sa.Column('scaffold_length', sa.BigInteger(), nullable=True))
    op.add_column('assembly', sa.Column('scaffold_longest', sa.BigInteger(), nullable=True))
    op.add_column('assembly', sa.Column('scaffold_shortest', sa.BigInteger(), nullable=True))
    op.add_column('assembly', sa.Column('scaffold_length_mean', sa.Float(), nullable=True))
    op.add_column('assembly', sa.Column('scaffold_n50', sa.BigInteger(), nullable=True))
    op.add_column('assembly', sa.Column('scaffold_l50', sa.BigInteger(), nullable=True))
    op.add_column('assembly', sa.Column('scaffold_aun', sa.Float(), nullable=True))

    op.add_column('assembly', sa.Column('gap_count', sa.Integer(), nullable=True))
    op.add_column('assembly', sa.Column('gap_length', sa.BigInteger(), nullable=True))
    op.add_column('assembly', sa.Column('gap_longest', sa.BigInteger(), nullable=True))
    op.add_column('assembly', sa.Column('gap_shortest', sa.BigInteger(), nullable=True))
    op.add_column('assembly', sa.Column('gap_length_mean', sa.Float(), nullable=True))
    op.add_column('assembly', sa.Column('gap_n50', sa.BigInteger(), nullable=True))
    op.add_column('assembly', sa.Column('gap_l50', sa.BigInteger(), nullable=True))
    op.add_column('assembly', sa.Column('gap_aun', sa.Float(), nullable=True))

    op.add_column('assembly', sa.Column('metrics', JSONB(astext_type=sa.Text()), nullable=True))

    op.add_column('busco_metrics', sa.Column('stop_codons', sa.Integer(), nullable=True))
    op.add_column('busco_metrics', sa.Column('results', JSONB(astext_type=sa.Text()), nullable=True))



def downgrade() -> None:
    pass
