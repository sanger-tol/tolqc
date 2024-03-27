"""create user

Revision ID: 652eb8a9e934
Revises: f2d17797a753
Create Date: 2024-03-27 07:51:09.631170

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '652eb8a9e934'
down_revision = 'f2d17797a753'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        'user',
        sa.Column(
            'token',
            sa.String(),
            nullable=True,
            unique=True,
        ),
    )
    op.add_column(
        'user',
        sa.Column(
            'registered',
            sa.Boolean(),
            nullable=False,
            default=False,
            server_default='False',
        ),
    )


def downgrade() -> None:
    pass
