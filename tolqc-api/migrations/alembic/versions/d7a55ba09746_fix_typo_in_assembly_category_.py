"""Fix typo in assembly_category.description

Revision ID: d7a55ba09746
Revises: 127e17ed1743
Create Date: 2026-06-26 09:40:47.792441

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd7a55ba09746'
down_revision = '127e17ed1743'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('assembly_category', sa.Column('description', sa.String(), nullable=True))
    op.execute(sa.text('UPDATE assembly_category SET description = descrption'))
    op.drop_column('assembly_category', 'descrption')


def downgrade() -> None:
    pass
