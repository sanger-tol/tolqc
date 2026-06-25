"""assembly.category and library.is_pcr

Revision ID: 127e17ed1743
Revises: 7b92949913ed
Create Date: 2026-06-10 11:55:33.789981

"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.schema import CreateSequence, DropSequence, Sequence


# revision identifiers, used by Alembic.
revision = '127e17ed1743'
down_revision = '7b92949913ed'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'assembly_category',
        sa.Column('category_id', sa.String(), nullable=False),
        sa.Column('hierarchy_name', sa.String(), nullable=True),
        sa.Column('descrption', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('category_id'),
    )

    # Drop foreign key constraint for all tables pointing at assembly
    assembly_rel_tables = (
        'assembly_dataset',
        'assembly_source',
        'assembly_status',
        'busco_metrics',
        'contigviz_metrics',
        'edit_assembly',
        'mapping_metrics',
        'markerscan_metrics',
        'merqury_metrics',
    )
    for tbl in assembly_rel_tables:
        op.drop_constraint(f'{tbl}_assembly_id_fkey', tbl)
    op.drop_constraint('assembly_source_source_assembly_id_fkey', 'assembly_source')

    # Drop `assembly_id` sequence to avoid it being trashed by alembic
    # `batch_alter_table()`
    op.alter_column('assembly', 'assembly_id', server_default=None)
    sqn_name = 'assembly_assembly_id_seq'
    op.execute(DropSequence(Sequence(sqn_name)))

    # Alter assembly table
    with op.batch_alter_table('assembly', recreate='always') as batch_op:
        batch_op.add_column(
            sa.Column('category_id', sa.String(), nullable=True),
            insert_after='level',
        )

    # Recreate and reset `assembly_id` sequence
    op.execute(CreateSequence(Sequence(sqn_name)))
    op.alter_column(
        'assembly',
        'assembly_id',
        server_default=sa.text(f"nextval('{sqn_name}'::regclass)"),
    )
    op.execute(
        sa.text(f"""
          SELECT setval('{sqn_name}',
            (SELECT MAX(assembly_id) FROM assembly))
        """)  # noqa: S608
    )

    # Recreate assembly table foreign key constraints
    for tbl in assembly_rel_tables:
        op.create_foreign_key(
            None,
            tbl,
            'assembly',
            ['assembly_id'],
            ['assembly_id'],
        )
    op.create_foreign_key(
        None,
        'assembly_source',
        'assembly',
        ['source_assembly_id'],
        ['assembly_id'],
    )
    op.create_foreign_key(
        None,
        'assembly',
        'assembly_category',
        ['category_id'],
        ['category_id'],
    )

    # Add new `is_pcr` column to the `library_type` table, and move the
    # `reporting_category` column next to `default_category`.
    op.drop_constraint('library_library_type_id_fkey', 'library')
    op.drop_index('ix_library_type_reporting_category', table_name='library_type')
    with op.batch_alter_table('library_type', recreate='always') as batch_op:
        batch_op.add_column(
            sa.Column(
                'reporting_category_new',
                sa.String(),
                nullable=True,
            ),
            insert_after='default_category',
        )
        batch_op.add_column(
            sa.Column(
                'is_pcr',
                sa.Boolean(),
                server_default=sa.text('false'),
                nullable=True,
            ),
        )
    op.execute(
        sa.text('UPDATE library_type SET reporting_category_new = reporting_category')
    )
    op.execute(
        sa.text("""
          UPDATE library_type
          SET is_pcr = 'true'
          WHERE library_type_id IN (
              'PacBio - HiFi (Ampli-Fi)',
              'PacBio - HiFi (PiMmS)',
              'PacBio - HiFi (ULI)'
          )
        """)
    )
    op.drop_column('library_type', 'reporting_category')
    op.alter_column(
        'library_type', 'reporting_category_new', new_column_name='reporting_category'
    )
    op.create_foreign_key(
        None,
        'library',
        'library_type',
        ['library_type_id'],
        ['library_type_id'],
    )
    op.create_index(
        op.f('ix_library_type_reporting_category'),
        'library_type',
        ['reporting_category'],
        unique=False,
    )
    op.create_index(
        op.f('ix_library_type_is_pcr'),
        'library_type',
        ['is_pcr'],
        unique=False,
    )

    # New ENA controlled vocabulary columns
    op.create_table(
        'library_selection_dict',
        sa.Column('selection', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('selection'),
    )
    op.create_table(
        'library_source_dict',
        sa.Column('source', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('source'),
    )
    op.create_table(
        'library_strategy_dict',
        sa.Column('strategy', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('strategy'),
    )

    op.add_column('library', sa.Column('description', sa.String(), nullable=True))

    # Three ENA controlled vocab columns
    op.add_column(
        'library_type',
        sa.Column('source', sa.String(), nullable=True),
    )
    op.add_column(
        'library_type',
        sa.Column('selection', sa.String(), nullable=True),
    )
    op.add_column(
        'library_type',
        sa.Column('strategy', sa.String(), nullable=True),
    )

    # Three ENA controlled vocab foreign keys
    op.create_foreign_key(
        None, 'library_type', 'library_source_dict', ['source'], ['source']
    )
    op.create_foreign_key(
        None, 'library_type', 'library_selection_dict', ['selection'], ['selection']
    )
    op.create_foreign_key(
        None, 'library_type', 'library_strategy_dict', ['strategy'], ['strategy']
    )

    op.add_column(
        'library_type', sa.Column('description_template', sa.String(), nullable=True)
    )

    # Drop foreign key constraint for all tables pointing at project
    project_rel_tables = (
        'allocation',
        'edit_project',
    )
    for tbl in project_rel_tables:
        op.drop_constraint(f'{tbl}_project_id_fkey', tbl)
    op.drop_constraint('study_default_project_id_fkey', 'study')

    # Batch alter table to place columns in desired order
    with op.batch_alter_table('project', recreate='always') as batch_op:
        batch_op.add_column(
            sa.Column('sts_alias', sa.String(), nullable=True),
            insert_after='project_id',
        )
    op.create_index(
        op.f('ix_project_sts_alias'), 'project', ['sts_alias'], unique=False
    )

    # Recreate project table foreign key constraints
    for tbl in project_rel_tables:
        op.create_foreign_key(
            None,
            tbl,
            'project',
            ['project_id'],
            ['project_id'],
        )
    op.create_foreign_key(
        None,
        'study',
        'project',
        ['default_project_id'],
        ['project_id'],
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
            sa.Column('priority', sa.Integer(), nullable=True),
            insert_after='sts_priority',
        )
    op.create_index(
        op.f('ix_specimen_priority'), 'specimen', ['priority'], unique=False
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


def downgrade() -> None:
    pass
