"""New data table stats columns

Revision ID: bbcd2bbe983a
Revises: 7088fcbeadcd
Create Date: 2024-05-22 14:23:54.543570

"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'bbcd2bbe983a'
down_revision = '7088fcbeadcd'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.drop_column('data', 'elastic_mlwh_cksum')
    op.add_column('data', sa.Column('bases_a', sa.BigInteger(), nullable=True))
    op.add_column('data', sa.Column('bases_c', sa.BigInteger(), nullable=True))
    op.add_column('data', sa.Column('bases_g', sa.BigInteger(), nullable=True))
    op.add_column('data', sa.Column('bases_t', sa.BigInteger(), nullable=True))
    op.add_column('data', sa.Column('read_length_longest', sa.Integer(), nullable=True))
    op.add_column(
        'data', sa.Column('read_length_shortest', sa.Integer(), nullable=True)
    )
    op.add_column('data', sa.Column('reads_duplicated', sa.BigInteger(), nullable=True))
    op.add_column('data', sa.Column('reads_filtered', sa.BigInteger(), nullable=True))
    op.add_column('data', sa.Column('average_quality', sa.Float(), nullable=True))
    op.add_column('data', sa.Column('bases_duplicated', sa.BigInteger(), nullable=True))
    op.add_column('data', sa.Column('bases_mapped', sa.BigInteger(), nullable=True))
    op.add_column(
        'data', sa.Column('bases_mapped_cigar', sa.BigInteger(), nullable=True)
    )
    op.add_column('data', sa.Column('bases_trimmed', sa.BigInteger(), nullable=True))
    op.add_column('data', sa.Column('error_rate', sa.Float(), nullable=True))
    op.add_column('data', sa.Column('insert_size_average', sa.Float(), nullable=True))
    op.add_column(
        'data', sa.Column('insert_size_standard_deviation', sa.Float(), nullable=True)
    )
    op.add_column(
        'data', sa.Column('inward_oriented_pairs', sa.BigInteger(), nullable=True)
    )
    op.add_column('data', sa.Column('mismatches', sa.BigInteger(), nullable=True))
    op.add_column(
        'data', sa.Column('outward_oriented_pairs', sa.BigInteger(), nullable=True)
    )
    op.add_column(
        'data',
        sa.Column('pairs_on_different_chromosomes', sa.BigInteger(), nullable=True),
    )
    op.add_column(
        'data',
        sa.Column('pairs_with_other_orientation', sa.BigInteger(), nullable=True),
    )
    op.add_column('data', sa.Column('reads_mapped', sa.BigInteger(), nullable=True))
    op.add_column(
        'data', sa.Column('reads_mapped_and_paired', sa.BigInteger(), nullable=True)
    )
    op.add_column('data', sa.Column('reads_mq0', sa.BigInteger(), nullable=True))
    op.add_column(
        'data', sa.Column('reads_properly_paired', sa.BigInteger(), nullable=True)
    )
    op.add_column('data', sa.Column('reads_unmapped', sa.BigInteger(), nullable=True))


def downgrade() -> None:
    pass
