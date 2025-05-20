"""tiara table and trim summary columns for data table

Revision ID: a66e18edc0e5
Revises: 06cdf4c6ea30
Create Date: 2025-05-16 13:11:52.498637

"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'a66e18edc0e5'
down_revision = '06cdf4c6ea30'
branch_labels = None
depends_on = None


def upgrade() -> None:
    data_fk_tables = (
        'allocation',
        'barcode_metrics',
        'data_submission',
        'dataset_element',
        'edit_data',
        'file',
        'mapping_metrics',
    )
    for tbl in data_fk_tables:
        op.drop_constraint(f'{tbl}_data_id_fkey', tbl)
    with op.batch_alter_table('data', recreate='always') as batch_op:
        batch_op.drop_column('reads_filtered')
        batch_op.add_column(
            sa.Column('reads_discarded', sa.BigInteger(), nullable=True),
            insert_after='reads_duplicated',
        )
        batch_op.add_column(
            sa.Column('reads_trimmed', sa.BigInteger(), nullable=True),
            insert_after='reads_discarded',
        )
        batch_op.add_column(
            sa.Column('bases_removed', sa.BigInteger(), nullable=True),
            insert_after='reads_trimmed',
        )
    for tbl in data_fk_tables:
        op.create_foreign_key(None, tbl, 'data', ['data_id'], ['data_id'])

    op.create_table(
        'tiara_metrics',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('data_id', sa.String(), nullable=True),
        sa.Column('division', sa.String(), nullable=True),
        sa.Column('reads', sa.BigInteger(), nullable=True),
        sa.Column('bases', sa.BigInteger(), nullable=True),
        sa.Column('read_length_n50', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ['data_id'],
            ['data.data_id'],
        ),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('division', 'data_id'),
    )

    # UniqeContraints which were missed in previous alembic migrations
    for table, col1, col2 in (
        ('allocation', 'project_id', 'data_id'),
        ('assembly_source', 'assembly_id', 'source_assembly_id'),
        ('dataset_element', 'data_id', 'dataset_id'),
        ('offspring', 'specimen_id', 'offspring_specimen_id'),
        ('software_version', 'name', 'version'),
        ('umbrella', 'project_id', 'species_id'),
    ):
        op.create_index(f'{table}_{col1}_{col2}_key', table, [col1, col2], unique=True)


def downgrade() -> None:
    pass
