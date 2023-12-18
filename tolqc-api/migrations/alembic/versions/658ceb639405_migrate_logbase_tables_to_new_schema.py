"""Migrate LogBase tables to new schema

Revision ID: 658ceb639405
Revises: 6f373edef955
Create Date: 2023-12-13 17:03:45.937960

"""
from alembic import op

import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '658ceb639405'
down_revision = '6f373edef955'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'visibility_dict',
        sa.Column('visibility', sa.String(), nullable=False),
        sa.Column('description', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('visibility'),
    )

    op.drop_column('data', 'withdrawn')
    op.drop_column('data', 'manually_withdrawn')
    data_rel_tables = (
        'allocation',
        'barcode_metrics',
        'dataset_element',
        'file',
    )
    for tbl in data_rel_tables:
        op.drop_constraint(f'{tbl}_data_id_fkey', tbl)

    with op.batch_alter_table('data', recreate='always') as batch_op:
        batch_op.add_column(
            sa.Column(
                'visibility',
                sa.String(),
                nullable=True,
            ),
            insert_after='qc',
        )
        batch_op.create_foreign_key(
            'data_visibility_fkey',
            'visibility_dict',
            ['visibility'],
            ['visibility'],
        )
        batch_op.create_index(
            op.f('ix_data_visibility'), ['visibility'], unique=False
        )

    for tbl in data_rel_tables:
        op.create_foreign_key(
            f'{tbl}_data_id_fkey', tbl, 'data', ['data_id'], ['data_id']
        )

    for tbl in (
        'assembly',
        'assembly_status',
        'data',
        'dataset',
        'dataset_status',
        'genomescope_metrics',
        'sample',
        'species',
        'specimen',
        'specimen_status',
    ):
        op.drop_constraint(
            f'{tbl}_last_modified_by_fkey', tbl, type_='foreignkey'
        )
        op.drop_constraint(f'{tbl}_created_by_fkey', tbl, type_='foreignkey')
        op.drop_column(tbl, 'created_at')
        op.drop_column(tbl, 'created_by')
        op.drop_column(tbl, 'last_modified_at')
        op.drop_column(tbl, 'last_modified_by')
        op.drop_column(tbl, 'history')
        op.add_column(
            tbl,
            sa.Column(
                'modified_at',
                sa.DateTime(timezone=True),
                nullable=True,
            ),
        )
        op.add_column(
            tbl,
            sa.Column(
                'modified_by',
                sa.String,
                nullable=True,
            ),
        )


def downgrade() -> None:
    pass
