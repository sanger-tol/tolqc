"""Add assembly.level

Revision ID: 3e71a12802d1
Revises: 2acc2f8257a0
Create Date: 2026-05-08 16:17:19.219191

"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.schema import CreateSequence, DropSequence, Sequence


# revision identifiers, used by Alembic.
revision = '3e71a12802d1'
down_revision = '2acc2f8257a0'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # New assembly level restricted vocab
    op.create_table(
        'assembly_level_dict',
        sa.Column('level', sa.String(), nullable=False),
        sa.Column('description', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('level'),
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

    # Alter assembly table
    seq = 'assembly_assembly_id_seq'
    op.execute(DropSequence(Sequence(seq)))
    with op.batch_alter_table('assembly', recreate='always') as batch_op:
        batch_op.add_column(
            sa.Column('level', sa.String(), nullable=True),
            insert_after='description',
        )
        batch_op.add_column(
            sa.Column('is_reference', sa.Boolean(), nullable=True),
            insert_after='level',
        )
    op.execute(CreateSequence(Sequence(seq)))
    op.alter_column(
        'assembly',
        'assembly_id',
        server_default=sa.text(f"nextval('{seq}'::regclass)"),
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
        'assembly_level_dict',
        ['level'],
        ['level'],
    )
    op.create_index(
        op.f('ix_assembly_is_reference'), 'assembly', ['is_reference'], unique=False
    )

    # Add project.symlink_template
    op.add_column('project', sa.Column('symlink_template', sa.String(), nullable=True))


def downgrade() -> None:
    pass
