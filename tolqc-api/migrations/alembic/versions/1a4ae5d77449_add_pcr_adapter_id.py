"""Add pcr adapter id

Revision ID: 1a4ae5d77449
Revises: c86cb78e6229
Create Date: 2024-12-13 13:22:30.622053

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '1a4ae5d77449'
down_revision = 'c86cb78e6229'
branch_labels = None
depends_on = None


def upgrade() -> None:
    data_rel_tables = (
        'allocation',
        'barcode_metrics',
        'mapping_metrics',
        'dataset_element',
        'edit_data',
        'file',
    )
    for tbl in data_rel_tables:
        op.drop_constraint(f'{tbl}_data_id_fkey', tbl)

    with op.batch_alter_table('data', recreate='always') as data_op:
        data_op.add_column(
            sa.Column('pcr_adapter_id', sa.String(), nullable=True),
            insert_after='tag2_id',
        )
        data_op.drop_column('tag_index')

    for tbl in data_rel_tables:
        op.create_foreign_key(
            f'{tbl}_data_id_fkey', tbl, 'data', ['data_id'], ['data_id']
        )

    update_pcr_adapter_sql = sa.text(
        """
            UPDATE data
            SET pcr_adapter_id = tag2_id, tag2_id = NULL
            FROM run as r
              , platform as p
            WHERE data.run_id = r.run_id
              AND r.platform_id = p.id
              AND p.name = 'PacBio'
        """)
    op.execute(update_pcr_adapter_sql)


def downgrade() -> None:
    pass
