"""Add is_principal to assembly table

Revision ID: 1203fe3dac4c
Revises: ed76b468c147
Create Date: 2026-09-27 11:40:40.692693

"""

from sqlalchemy.schema import CreateSequence, DropSequence, Sequence

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1203fe3dac4c'
down_revision = 'ed76b468c147'
branch_labels = None
depends_on = None


def upgrade() -> None:
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
        batch_op.add_column(
            sa.Column(
                'is_principal',
                sa.Boolean(),
                server_default=sa.text('false'),
                nullable=True,
            ),
            insert_after='file_path',
        )
    op.create_index(
        op.f('ix_assembly_is_principal'),
        'assembly',
        ['is_principal'],
        unique=False,
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


def downgrade() -> None:
    pass
