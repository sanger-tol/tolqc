"""family_taxon_id and sts_priority columns

Revision ID: f5c78f517f05
Revises: a79168bbc430
Create Date: 2025-08-14 12:18:49.721076

"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'f5c78f517f05'
down_revision = 'a79168bbc430'
branch_labels = None
depends_on = None


def upgrade() -> None:
    species_rel_tables = (
        'edit_species',
        'specimen',
        'metagenome',
        'metagenome_bin',
    )
    for tbl in species_rel_tables:
        op.drop_constraint(f'{tbl}_species_id_fkey', tbl)
    with op.batch_alter_table('species', recreate='always') as sp_op:
        sp_op.add_column(
            sa.Column('family_taxon_id', sa.Integer(), nullable=True),
            insert_after='taxon_id',
        )
    op.create_index(None, 'species', ['family_taxon_id'], unique=False)
    for tbl in species_rel_tables:
        op.create_foreign_key(
            None,
            tbl,
            'species',
            ['species_id'],
            ['species_id'],
        )

    # Drop foreign key constraint for all tables pointing at specimen
    specimen_rel_tables = (
        'assembly',
        'edit_specimen',
        'offspring',
        'sample',
        'specimen_status',
    )
    for tbl in specimen_rel_tables:
        op.drop_constraint(f'{tbl}_specimen_id_fkey', tbl)
    op.drop_constraint('offspring_offspring_specimen_id_fkey', 'offspring')
    op.drop_constraint('metagenome_host_specimen_id_fkey', 'metagenome')
    op.drop_constraint('specimen_cobiont_specimen_id_fkey', 'specimen')

    # Batch alter table to place columns in desired order
    with op.batch_alter_table('specimen', recreate='always') as batch_op:
        batch_op.add_column(
            sa.Column('sts_priority', sa.Integer(), nullable=True),
            insert_after='sts_specimen',
        )
    op.create_index(None, 'specimen', ['sts_priority'], unique=False)

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
    op.create_foreign_key(
        None,
        'metagenome',
        'specimen',
        ['host_specimen_id'],
        ['specimen_id'],
    )
    op.create_foreign_key(
        None,
        'specimen',
        'specimen',
        ['cobiont_specimen_id'],
        ['specimen_id'],
    )

    # Default project for studies
    op.add_column('study', sa.Column('default_project_id', sa.String(), nullable=True))
    op.create_foreign_key(
        None,
        'study',
        'project',
        ['default_project_id'],
        ['project_id'],
    )


def downgrade() -> None:
    pass
