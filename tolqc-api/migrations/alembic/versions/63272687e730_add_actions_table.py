"""add_actions_table

Revision ID: 63272687e730
Revises: c3cc354a7fb6
Create Date: 2026-03-25 13:22:41.532319

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB
from datetime import datetime


# revision identifiers, used by Alembic.
revision = '63272687e730'
down_revision = 'c3cc354a7fb6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'action',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('object_type', sa.String, nullable=False),
        sa.UniqueConstraint('name', 'object_type'),
        sa.Column('flow_name', sa.String, nullable=True),
        sa.Column('class_name', sa.String, nullable=True),
        sa.Column('params', JSONB, nullable=False, default={}),
    )

    op.create_table(
        'user_action',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('created_at', sa.DateTime, nullable=False, default=datetime.now),
        sa.Column('params', JSONB, nullable=False, default={}),
        sa.Column('user_id', sa.Integer, nullable=False),
        sa.ForeignKeyConstraint(
            ('user_id',),
            ['user.id'],
        ),
        sa.Column('action_id', sa.Integer, nullable=False),
        sa.ForeignKeyConstraint(
            ('action_id',),
            ['action.id'],
        ),
    )


def downgrade() -> None:
    pass
