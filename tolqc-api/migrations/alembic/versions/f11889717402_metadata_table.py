"""Metadata table

Revision ID: f11889717402
Revises: d8cd80bb4b0c
Create Date: 2025-07-04 13:11:56.639217

"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'f11889717402'
down_revision = 'd8cd80bb4b0c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'metadata',
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('description', sa.String(), nullable=True),
        sa.Column('string_value', sa.String(), nullable=True),
        sa.Column('timestamp_value', sa.DateTime(timezone=True), nullable=True),
        sa.Column('integer_value', sa.Integer(), nullable=True),
        sa.Column('float_value', sa.Float(), nullable=True),
        sa.Column('json_value', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.Column('modified_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('modified_by', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ['modified_by'],
            ['user.id'],
        ),
        sa.PrimaryKeyConstraint('name'),
    )
    op.create_table(
        'edit_metadata',
        sa.Column('edit_id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('changes', postgresql.JSONB(astext_type=sa.Text()), nullable=False),
        sa.Column('modified_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('modified_by', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ['modified_by'],
            ['user.id'],
        ),
        sa.ForeignKeyConstraint(
            ['name'],
            ['metadata.name'],
        ),
        sa.PrimaryKeyConstraint('edit_id'),
        sa.UniqueConstraint('modified_at', 'name'),
    )

    # Missed in previous almebic:
    op.create_index(op.f('ix_assembly_name'), 'assembly', ['name'], unique=False)
    op.alter_column(
        'pipeline_step', 'pipeline_id', existing_type=sa.INTEGER(), nullable=True
    )
    op.alter_column(
        'specimen_category_dict',
        'description',
        existing_type=sa.VARCHAR(),
        nullable=True,
    )

    # Patch out of sync sequence for "platform" table
    op.execute(
        sa.text("SELECT setval('platform_id_seq', (SELECT MAX(id) FROM platform))")
    )


def downgrade() -> None:
    pass
