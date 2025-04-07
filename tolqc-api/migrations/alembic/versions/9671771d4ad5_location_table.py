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
    # New location table
    op.create_table(
        'location',
        sa.Column('location_id', sa.Integer(), nullable=False),
        sa.Column('path', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('location_id'),
    )
    op.create_index(op.f('ix_location_path'), 'location', ['path'], unique=False)

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
        'location',
        ['location_id'],
        ['location_id'],
    )

    # specimen.hierarchy_name column to location_id
    # and add epithet and taxon_id columns
    op.alter_column('specimen', 'hierarchy_name', nullable=True)
    op.execute(sa.text('UPDATE specimen SET hierarchy_name = NULL'))

    # Drop foreign key constraint for all tables pointing at specimen
    specimen_rel_tables = (
        'edit_specimen',
        'offspring',
        'sample',
        'specimen_status',
    )
    for tbl in specimen_rel_tables:
        op.drop_constraint(f'{tbl}_specimen_id_fkey', tbl)
    op.drop_constraint('offspring_offspring_specimen_id_fkey', 'offspring')

    # Batch alter table to place columns in desired order
    with op.batch_alter_table('specimen', recreate='always') as batch_op:
        batch_op.alter_column(
            'hierarchy_name',
            new_column_name='location_id',
            type_=sa.Integer(),
            postgresql_using='hierarchy_name::integer',
        )
        batch_op.add_column(
            sa.Column('epithet', sa.String(), nullable=True),
            insert_before='lims_id',
        )
        batch_op.add_column(
            sa.Column('taxon_id', sa.Integer(), nullable=True),
            insert_before='lims_id',
        )

    op.create_index(op.f('ix_specimen_epithet'), 'specimen', ['epithet'], unique=False)
    op.create_index(
        op.f('ix_specimen_taxon_id'), 'specimen', ['taxon_id'], unique=False
    )
    op.create_foreign_key(
        None,
        'specimen',
        'location',
        ['location_id'],
        ['location_id'],
    )

    # Recreate specimen table foreign key constraints
    for tbl in specimen_rel_tables:
        op.create_foreign_key(
            None,
            tbl,
            'specimen',
            ['specimen_id'],
            ['specimen_id'],
        )
    op.create_foreign_key(
        None,
        'offspring',
        'specimen',
        ['offspring_specimen_id'],
        ['specimen_id'],
    )

    # category name changes
    op.alter_column('data', 'hierarchy_name', new_column_name='category')
    op.alter_column('library_type', 'category', new_column_name='default_category')

    # category_dict table to restrict vocabulary
    op.create_table(
        'category_dict',
        sa.Column('category', sa.String(), nullable=False),
        sa.Column('description', sa.String()),
        sa.PrimaryKeyConstraint('category'),
    )
    op.create_foreign_key(
        None,
        'data',
        'category_dict',
        ['category'],
        ['category'],
    )

    for sql in [
        # Populate category_dict table
        """
        INSERT INTO category_dict (category)
        SELECT DISTINCT default_category
        FROM library_type
        WHERE default_category IS NOT NULL
        ON CONFLICT DO NOTHING
        """,
        # Populate data.category column
        """
        UPDATE data AS d
        SET category = lt.default_category
        FROM library AS lib
          , library_type AS lt
        WHERE d.library_id = lib.library_id
          AND lib.library_type_id = lt.library_type_id
          AND d.category IS NULL
        """,
        # Create species_dir function
        """
        CREATE FUNCTION species_dir(taxon_id INTEGER, species_id VARCHAR)
        RETURNS VARCHAR
        STABLE
        LANGUAGE SQL
        AS $$
          SELECT array_to_string(
              ((string_to_array(md5(taxon_id::VARCHAR), NULL))[: 6])
              , '/'
            )
            || '/' ||
            trim((regexp_replace(species_id, '\\W+', '_', 'g')), '_')
        $$
        """,
        # Populate location table
        """
        INSERT INTO location (path)
        SELECT species_dir(taxon_id, species_id)
        FROM species
        WHERE strain IS NULL
          AND species_id != 'unidentified'
        ORDER BY taxon_id
        """,
        # Fill in location_id in species table
        """
        UPDATE species AS s
        SET location_id = loc.location_id
        FROM location AS loc
        WHERE species_dir(s.taxon_id, s.species_id) = loc.path
          AND s.location_id IS NULL
        """,
        # Fill in location_id in specimen table
        """
        UPDATE specimen AS spmn
        SET location_id = loc.location_id
        FROM species AS s
          , location AS loc
        WHERE spmn.species_id = s.species_id
          AND s.location_id = loc.location_id
          AND spmn.location_id IS NULL
        """,
        # Copy strain and taxon_id to specimen table when strain is set
        """
        UPDATE specimen AS spmn
        SET epithet = s.strain
          , taxon_id = s.taxon_id
        FROM species AS s
        WHERE spmn.species_id = s.species_id
          AND s.strain IS NOT NULL
          AND spmn.epithet IS NULL
        """,
        # Remove temporary species_dir function
        'DROP FUNCTION species_dir',
    ]:
        op.execute(sa.text(sql))

    op.drop_column('species', 'strain')


def downgrade() -> None:
    pass
