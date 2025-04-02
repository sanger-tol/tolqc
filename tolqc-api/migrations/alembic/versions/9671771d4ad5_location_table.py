"""Location table

Revision ID: 9671771d4ad5
Revises: 593122eb1742
Create Date: 2025-04-02 13:10:09.288976

"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '9671771d4ad5'
down_revision = '593122eb1742'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # New species_location table
    op.create_table(
        'species_location',
        sa.Column('location_id', sa.Integer(), nullable=False),
        sa.Column('path', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('location_id'),
    )
    op.create_index(op.f('ix_location_path'), 'species_location', ['path'], unique=False)

    # species.hierarchy_name column to location_id
    op.drop_constraint('species_hierarchy_name_key', 'species', type_='unique')
    op.alter_column('species', 'hierarchy_name', nullable=True)
    op.execute(sa.text('UPDATE species SET hierarchy_name = NULL'))
    op.alter_column(
        'species',
        'hierarchy_name',
        new_column_name='location_id',
        type_=sa.Integer(),
        postgresql_using='hierarchy_name::integer',
    )
    op.create_foreign_key(
        None,
        'species',
        'species_location',
        ['location_id'],
        ['location_id'],
    )

    # specimen.hierarchy_name column to location_id
    op.alter_column('specimen', 'hierarchy_name', nullable=True)
    op.execute(sa.text('UPDATE specimen SET hierarchy_name = NULL'))
    op.alter_column(
        'specimen',
        'hierarchy_name',
        new_column_name='location_id',
        type_=sa.Integer(),
        postgresql_using='hierarchy_name::integer',
    )
    op.create_foreign_key(
        None,
        'specimen',
        'species_location',
        ['location_id'],
        ['location_id'],
    )

    # category_dict table to restrict vocabulary
    op.create_table(
        'category_dict',
        sa.Column('category', sa.String(), nullable=False),
        sa.Column('description', sa.String()),
        sa.PrimaryKeyConstraint('category'),
    )

    # category name changes
    op.alter_column('data', 'hierarchy_name', new_column_name='category')
    op.alter_column('library_type', 'category', new_column_name='default_category')
    op.create_foreign_key(
        None,
        'data',
        'category',
        ['category'],
        ['category'],
    )


def downgrade() -> None:
    pass
