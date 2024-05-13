"""Add run.plex_count

Revision ID: b6a23971491c
Revises: 8c7475da7d56
Create Date: 2024-05-13 14:31:53.881973

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'b6a23971491c'
down_revision = '8c7475da7d56'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('run', sa.Column('plex_count', sa.Integer(), nullable=True))


def downgrade() -> None:
    op.drop_column('run', 'plex_count')
