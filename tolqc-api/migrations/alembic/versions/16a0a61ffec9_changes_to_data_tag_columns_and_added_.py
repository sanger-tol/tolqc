"""Changes to Data tag columns and added index

Revision ID: 16a0a61ffec9
Revises: 8e8a011a1b10
Create Date: 2023-07-04 15:38:01.209573

"""
from alembic import op

import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '16a0a61ffec9'
down_revision = '8e8a011a1b10'
branch_labels = None
depends_on = None


def upgrade() -> None:
    data_rel_tables = (
        'allocation',
        'barcode_metrics',
        'dataset_element',
        'file',
    )
    for tbl in data_rel_tables:
        op.drop_constraint(f'{tbl}_data_id_fkey', tbl)
    with op.batch_alter_table('data', recreate='always') as batch_op:
        batch_op.add_column(
            sa.Column('tag_index', sa.String(), nullable=True),
            insert_after='processed',
        )
        batch_op.alter_column('tag1_sequence', new_column_name='tag1_id')
        batch_op.alter_column('tag2_sequence', new_column_name='tag2_id')
        batch_op.create_index('ix_data_name_root', ['name_root'])
    for tbl in data_rel_tables:
        op.create_foreign_key(
            f'{tbl}_data_id_fkey', tbl, 'data', ['data_id'], ['data_id']
        )


def downgrade() -> None:
    op.drop_column('data', 'tag_index')
    op.alter_column('data', 'tag1_id', new_column_name='tag1_sequence')
    op.alter_column('data', 'tag2_id', new_column_name='tag2_sequence')
    op.drop_index('ix_data_name_root')
