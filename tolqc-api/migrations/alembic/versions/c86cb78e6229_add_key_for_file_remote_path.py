"""Add key for file.remote_path

Revision ID: c86cb78e6229
Revises: c49ecfc326e4
Create Date: 2024-10-09 17:14:10.622013

"""
from alembic import op

# revision identifiers, used by Alembic.
revision = 'c86cb78e6229'
down_revision = 'c49ecfc326e4'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_index(op.f('ix_file_remote_path'), 'file', ['remote_path'], unique=False)


def downgrade() -> None:
    pass
