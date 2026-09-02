"""Add relationships to ENUM type fields for UI

Revision ID: 1a082d130527
Revises: d7a55ba09746
Create Date: 2026-09-02 12:32:13.255106

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1a082d130527'
down_revision = 'd7a55ba09746'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # `platform` table
    op.add_column(
        'platform',
        sa.Column('ena_name', sa.String(), nullable=True),
    )

    # Smudgeplot interpretation
    op.drop_constraint(
        'smudgeplot_metrics_interpretation_fkey',
        'smudgeplot_metrics',
        type_='foreignkey',
    )
    op.alter_column(
        'smudgeplot_interpretation_dict',
        'interpretation',
        new_column_name='interpretation_id',
    )
    op.alter_column(
        'smudgeplot_metrics',
        'interpretation',
        new_column_name='interpretation_id',
    )
    op.create_foreign_key(
        None,
        'smudgeplot_metrics',
        'smudgeplot_interpretation_dict',
        ['interpretation_id'],
        ['interpretation_id'],
    )

    # `assembly` table

    # Drop foreign key constraints
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

    # Add two new columns and relationship to the `centre` table
    with op.batch_alter_table('assembly', recreate='always') as batch_op:
        batch_op.add_column(
            sa.Column('centre_id', sa.Integer(), nullable=True),
            insert_after='specimen_id',
        )
        batch_op.add_column(
            sa.Column('file_path', sa.String(), nullable=True),
            insert_after='category_id',
        )
    op.create_foreign_key(None, 'assembly', 'centre', ['centre_id'], ['id'])

    # Add back foreign key constraints
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
