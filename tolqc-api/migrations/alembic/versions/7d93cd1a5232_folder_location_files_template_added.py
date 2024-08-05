"""folder_location.files_template added

Revision ID: 7d93cd1a5232
Revises: 0f9299d6970b
Create Date: 2024-08-05 11:40:17.652048

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '7d93cd1a5232'
down_revision = '0f9299d6970b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('folder_location', sa.Column('files_template', postgresql.JSONB(astext_type=sa.Text()), nullable=True))


def downgrade() -> None:
    pass
