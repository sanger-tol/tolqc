"""rename token

Revision ID: c3457e9954df
Revises: b6a23971491c
Create Date: 2024-05-21 13:27:21.363014

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c3457e9954df'
down_revision = 'b6a23971491c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.drop_constraint('oidc_token_user_id_fkey', 'oidc_token', type_='foreignkey')

    op.rename_table('oidc_token', 'token')

    op.create_foreign_key(None, 'token', 'user', ['user_id'], ['id'])


def downgrade() -> None:
    op.drop_constraint('token_user_id_fkey', 'token', type_='foreignkey')

    op.rename_table('token', 'oidc_token')
    
    op.create_foreign_key(None, 'oidc_token', 'user', ['user_id'], ['id'])
