"""Add new columns

Revision ID: 168603975dd1
Revises: 106250dfc9e0
Create Date: 2023-05-11 17:55:24.503076

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '168603975dd1'
down_revision = '106250dfc9e0'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('run', sa.Column('complete_date', sa.DateTime(), nullable=True))
    op.add_column('data', sa.Column('tag_index', sa.String(), nullable=False))
    op.add_column('data', sa.Column('checksum_from_mlwh', sa.String(), nullable=False))


def downgrade() -> None:
    pass
