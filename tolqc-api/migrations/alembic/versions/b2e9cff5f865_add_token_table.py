"""add Token table

Revision ID: b2e9cff5f865
Revises: 652eb8a9e934
Create Date: 2024-03-28 13:01:57.627213

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b2e9cff5f865'
down_revision = '652eb8a9e934'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.drop_column('user', 'token')

    op.create_table(
        'oidc_token',
        sa.Column(
            'id',
            sa.Integer(),
            primary_key=True,
            autoincrement=True
        ),
        sa.Column(
            'token',
            sa.String(),
            nullable=False,
            unique=True
        ),
        sa.Column(
            'user_id',
            sa.Integer(),
            nullable=False
        )
    )
    op.create_foreign_key(
        None,
        'oidc_token',
        'user',
        ['user_id'],
        ['id']
    )


def downgrade() -> None:
    pass
