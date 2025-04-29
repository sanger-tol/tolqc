"""Add run.chemistry and ChemistryDict

Revision ID: 2871303688df
Revises: 9671771d4ad5
Create Date: 2025-04-28 18:13:36.997367

"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '2871303688df'
down_revision = '9671771d4ad5'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'chemistry_dict',
        sa.Column('chemistry', sa.String(), nullable=False),
        sa.Column('description', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('chemistry'),
    )
    op.create_index(op.f('ix_data_processed'), 'data', ['processed'], unique=False)
    op.add_column('run', sa.Column('chemistry', sa.String(), nullable=True))
    op.create_foreign_key(None, 'run', 'chemistry_dict', ['chemistry'], ['chemistry'])


def downgrade() -> None:
    pass
