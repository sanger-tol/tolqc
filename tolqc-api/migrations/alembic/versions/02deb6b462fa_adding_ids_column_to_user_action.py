"""adding_ids_column_to_user_action

Revision ID: 02deb6b462fa
Revises: 63272687e730
Create Date: 2026-04-14 09:48:58.079317

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB


# revision identifiers, used by Alembic.
revision = '02deb6b462fa'
down_revision = '63272687e730'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        'user_action',
        sa.Column('ids', JSONB, nullable=True)
    )
    op.add_column(
        'user_action',
        sa.Column('filters', JSONB, nullable=True)
    )
    op.create_check_constraint(
        None,
        'user_action',
        'NOT(ids IS NULL AND filters IS NULL)'
    )


def downgrade() -> None:
    pass
