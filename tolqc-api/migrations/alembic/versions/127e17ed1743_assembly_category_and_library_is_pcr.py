"""assembly.category and library.is_pcr

Revision ID: 127e17ed1743
Revises: d4fe96ab4445
Create Date: 2026-06-10 11:55:33.789981

"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.schema import CreateSequence, DropSequence, Sequence


# revision identifiers, used by Alembic.
revision = '127e17ed1743'
down_revision = 'd4fe96ab4445'
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
    op.execute(sa.text('UPDATE library_type SET reporting_category_new = reporting_category'))
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
    op.alter_column('library_type', 'reporting_category_new', new_column_name='reporting_category')
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


def downgrade() -> None:
    pass
