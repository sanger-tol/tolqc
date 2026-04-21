"""populating_action_tables

Revision ID: b35d5e13936f
Revises: 02deb6b462fa
Create Date: 2026-04-20 12:40:01.330366

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB


# revision identifiers, used by Alembic.
revision = 'b35d5e13936f'
down_revision = '02deb6b462fa'
branch_labels = None
depends_on = None


def upgrade() -> None:
    action_table = sa.table(
        'action',
        sa.column('name', sa.String),
        sa.column('object_type', sa.String),
        sa.column('class_name', sa.String),
        sa.column('params', JSONB),
    )

    op.bulk_insert(action_table, [
        {
            'name': 'Set Status Pending',
            'object_type': 'dataset',
            'class_name': 'SetStatusAction',
            'params': {'status': 'Pending'},
        },
        {
            'name': 'Set Status Failed',
            'object_type': 'dataset',
            'class_name': 'SetStatusAction',
            'params': {'status': 'Failed'},
        },
        {
            'name': 'Set Status QC Pass',
            'object_type': 'dataset',
            'class_name': 'SetStatusAction',
            'params': {'status': 'QC Pass'},
        },
        {
            'name': 'Set Status GenomeScope Pass',
            'object_type': 'dataset',
            'class_name': 'SetStatusAction',
            'params': {'status': 'GenomeScope Pass'},
        },
        {
            'name': 'Set Status Barcode Check Pass',
            'object_type': 'dataset',
            'class_name': 'SetStatusAction',
            'params': {'status': 'Barcode Check Pass'},
        },
        {
            'name': 'SetStatusAction',
            'object_type': 'dataset',
            'class_name': 'SetStatusAction',
            'params': {},
        },
    ])

    action_table = sa.table(
        'role_action',
        sa.column('action_id', sa.Integer),
        sa.column('role_id', sa.Integer),
    )

    op.bulk_insert(action_table, [
        {'action_id': 1, 'role_id': 1},
        {'action_id': 2, 'role_id': 1},
        {'action_id': 3, 'role_id': 1},
        {'action_id': 4, 'role_id': 1},
        {'action_id': 5, 'role_id': 1},
        {'action_id': 6, 'role_id': 1},
    ])
    
    op.add_column('user', sa.Column('oidc_id', sa.String, nullable=True))
    


def downgrade() -> None:
    pass