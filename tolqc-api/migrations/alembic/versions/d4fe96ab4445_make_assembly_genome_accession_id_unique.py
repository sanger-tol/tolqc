"""Make assembly.genome_accession_id unique

Revision ID: d4fe96ab4445
Revises: 3e71a12802d1
Create Date: 2026-05-26 14:18:14.830303

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd4fe96ab4445'
down_revision = '3e71a12802d1'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_unique_constraint(None, 'assembly', ['genome_accession_id'])


def downgrade() -> None:
    pass
