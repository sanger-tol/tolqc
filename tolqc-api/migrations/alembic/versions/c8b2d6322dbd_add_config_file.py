"""add config file

Revision ID: c8b2d6322dbd
Revises: 1bec7c07ef1f
Create Date: 2022-07-05 11:15:56.470758

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import orm


# revision identifiers, used by Alembic.
revision = 'c8b2d6322dbd'
down_revision = '1bec7c07ef1f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('track_config',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('lims_id', sa.INTEGER(), autoincrement=False),
    sa.Column('name', sa.String()),
    sa.Column('hierarchy_name', sa.String()),
    )


def downgrade() -> None:
    pass
