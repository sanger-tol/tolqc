"""Index library_type.reporting_category

Revision ID: 2d56a365736e
Revises: 5617d7b038a6
Create Date: 2026-03-11 15:11:08.123612

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2d56a365736e'
down_revision = '5617d7b038a6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_index(
        op.f('ix_library_type_reporting_category'),
        'library_type',
        ['reporting_category'],
        unique=False,
    )
    op.create_unique_constraint(
        'allocation_project_id_data_id_key',
        'allocation',
        [
            'project_id',
            'data_id',
        ],
    )


def downgrade() -> None:
    pass
