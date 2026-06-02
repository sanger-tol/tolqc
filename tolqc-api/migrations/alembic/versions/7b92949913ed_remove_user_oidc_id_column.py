"""remove user.oidc_id column

Revision ID: 7b92949913ed
Revises: d4fe96ab4445
Create Date: 2026-06-02 11:45:09.984916

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7b92949913ed'
down_revision = 'd4fe96ab4445'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.drop_column('user', 'oidc_id')


def downgrade() -> None:
    pass
