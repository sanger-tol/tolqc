"""Add public_path and insdc_path to file table

Revision ID: 5617d7b038a6
Revises: 87b655ac9298
Create Date: 2026-03-06 17:32:21.672451

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5617d7b038a6'
down_revision = '87b655ac9298'
branch_labels = None
depends_on = None


def upgrade() -> None:
    with op.batch_alter_table('file', recreate='always') as batch_op:
        batch_op.add_column(
            sa.Column('public_path', sa.String(), nullable=True),
            insert_before='size_bytes',
        )
        batch_op.add_column(
            sa.Column('insdc_path', sa.String(), nullable=True),
            insert_before='size_bytes',
        )


def downgrade() -> None:
    pass
