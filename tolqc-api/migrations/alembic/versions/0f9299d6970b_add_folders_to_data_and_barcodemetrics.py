"""Add folders to Data and BarcodeMetrics

Revision ID: 0f9299d6970b
Revises: 2b092ba4a3e9
Create Date: 2024-06-24 14:01:59.747943

"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '0f9299d6970b'
down_revision = '2b092ba4a3e9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    for tbl in ('barcode_metrics', 'data'):
        op.add_column(tbl, sa.Column('folder_ulid', sa.String(), nullable=True))
        op.create_foreign_key(None, tbl, 'folder', ['folder_ulid'], ['folder_ulid'])


def downgrade() -> None:
    pass
