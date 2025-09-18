"""Assignee for specimens and assemblies

Revision ID: c8babd30b9f1
Revises: e3ec79e6f3be
Create Date: 2025-09-18 16:13:08.745789

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'c8babd30b9f1'
down_revision = 'e3ec79e6f3be'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        'specimen',
        sa.Column('assigned_user_id', sa.Integer(), nullable=True),
    )
    op.create_foreign_key(None, 'specimen', 'user', ['assigned_user_id'], ['id'])

    op.add_column(
        'assembly',
        sa.Column('assigned_user_id', sa.Integer(), nullable=True),
    )
    op.add_column(
        'assembly',
        sa.Column('folder_ulid', sa.String(), nullable=True),
    )
    op.create_foreign_key(None, 'assembly', 'user', ['assigned_user_id'], ['id'])
    op.create_foreign_key(None, 'assembly', 'folder', ['folder_ulid'], ['folder_ulid'])

    op.execute(sa.text('UPDATE metagenome_bin SET n_16s = ssu_count WHERE n_16s IS NULL'))
    op.drop_column('metagenome_bin', 'ssu_count')


def downgrade() -> None:
    pass
