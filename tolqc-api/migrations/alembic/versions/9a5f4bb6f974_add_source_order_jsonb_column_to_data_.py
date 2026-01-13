"""Add source_order JSONB column to data_source_config_relationship

Revision ID: 9a5f4bb6f974
Revises: ffe2aae8d627
Create Date: 2026-01-13 13:52:35.952307

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9a5f4bb6f974'
down_revision = 'ffe2aae8d627'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        'data_source_config_relationship',
        sa.Column('source_order', sa.JSON(), nullable=True)
    )


def downgrade() -> None:
    op.drop_column('data_source_config_relationship', 'source_order')
