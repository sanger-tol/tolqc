"""Link submitter_dict and centre

Revision ID: f27ea749a621
Revises: af49aa9a22d4
Create Date: 2026-11-19 10:56:09.756716

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f27ea749a621'
down_revision = 'af49aa9a22d4'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('submitter_dict', sa.Column('centre_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'submitter_dict', 'centre', ['centre_id'], ['id'])


def downgrade() -> None:
    pass
