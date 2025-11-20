"""add_dashboarding_tables_to_database

Revision ID: 403ee1086294
Revises: c8babd30b9f1
Create Date: 2025-10-13 13:08:39.428033

"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB


# revision identifiers, used by Alembic.
revision = '403ee1086294'
down_revision = 'c8babd30b9f1'
branch_labels = None
depends_on = None


def upgrade():
    # Create `data_source_config` table (needed for the `data_source_instance` table)
    op.create_table(
        'data_source_config',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('description', sa.String(), nullable=False),
    )

    # Create `data_source_config_attribute` table (needed for the `data_source_instance` table)
    op.create_table(
        'data_source_config_attribute',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('data_source_config_id', sa.Integer(), sa.ForeignKey('data_source_config.id'), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('object_type', sa.String(), nullable=False),
        sa.Column('display_name', sa.String(), nullable=True),
        sa.Column('description', sa.String(), nullable=True),
        sa.Column('available_on_relationships', sa.Boolean(), nullable=False, server_default=sa.text('true')),
        sa.Column('is_authoritative', sa.Boolean(), nullable=False, server_default=sa.text('false')),
        sa.Column('source', sa.String(), nullable=True),
        sa.Column('runtime_definition', JSONB(astext_type=sa.Text()), nullable=True),
    )

    # Create `data_source_config_relationship` table (needed for the `data_source_instance` table)
    op.create_table(
        'data_source_config_relationship',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('object_type', sa.String(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('foreign_object_type', sa.String(), nullable=False),
        sa.Column('foreign_name', sa.String(), nullable=False),
        sa.Column('data_source_config_id', sa.Integer(), sa.ForeignKey('data_source_config.id'), nullable=False),
    )

    # Create `data_source_instance` table
    op.create_table(
        'data_source_instance',
        sa.Column('id', sa.String(), primary_key=True),
        sa.Column('builtin_name', sa.String(), nullable=False),
        sa.Column('kwargs', JSONB(astext_type=sa.Text()), nullable=True),
        sa.Column('publish', sa.Boolean(), nullable=False, server_default=sa.text('false')),
        sa.Column('data_source_config_id', sa.Integer(), sa.ForeignKey('data_source_config.id'), nullable=True),
        sa.Column('ui_api_details', JSONB, nullable=True)
    )

    op.execute(
        sa.text("""
        INSERT INTO data_source_instance (id, builtin_name, kwargs, publish, data_source_config_id, ui_api_details)
        VALUES ('tolqc', 'tolqc', '{}', 'true', NULL, '{"url": "https://qc.tol.sanger.ac.uk", "apiPath": "/api/v1", "apiDataPath": "", "dataspace": ""}')
        """)
    )


    # Create table `component`
    op.create_table(
        'component',
        sa.Column('id', sa.String, primary_key=True),
        sa.Column('title', sa.String, nullable=False),
        sa.Column('object_type', sa.String, nullable=False),
        sa.Column('data_source_instance_id', sa.String(), sa.ForeignKey('data_source_instance.id'), nullable=False),
        sa.Column('component_type', sa.String, nullable=False),
        sa.Column('widget_type', sa.String, nullable=False),
        sa.Column('config', JSONB, nullable=False),
        sa.Column('filter', JSONB, nullable=False, default={}, server_default='{}'),
        sa.Column('filter_pass_through', sa.Boolean(), nullable=False),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('user.id'), nullable=False)
    )

    # Create table `zone`
    op.create_table(
        'zone',
        sa.Column('id', sa.String, primary_key=True),
        sa.Column('title', sa.String, nullable=False),
        sa.Column('object_type', sa.String, nullable=False),
        sa.Column('data_source_instance_id', sa.String(), sa.ForeignKey('data_source_instance.id'), nullable=False),
        sa.Column('filter', JSONB, nullable=False, default={}, server_default='{}'),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('user.id'), nullable=False),
    )

    # Create table `view`
    op.create_table(
        'view',
        sa.Column('id', sa.String, primary_key=True),
        sa.Column('title', sa.String, nullable=False),
        sa.Column('filter', JSONB, nullable=False, default={}, server_default='{}'),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('user.id'), nullable=False),
    )

    # Create table `board`
    op.create_table(
        'board',
        sa.Column('id', sa.String, primary_key=True),
        sa.Column('title', sa.String, nullable=False),
        sa.Column('filter', JSONB, nullable=False, default={}, server_default='{}'),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('user.id'), nullable=False),
    )

    # Create table `component_zone`
    op.create_table(
        'component_zone',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('order', sa.Integer, nullable=False),
        sa.Column('component_id', sa.String, sa.ForeignKey('component.id'), nullable=False),
        sa.Column('zone_id', sa.String, sa.ForeignKey('zone.id'), nullable=False),
    )

    # Create table `zone_view`
    op.create_table(
        'zone_view',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('order', sa.Integer, nullable=False),
        sa.Column('zone_id', sa.String, sa.ForeignKey('zone.id'), nullable=False),
        sa.Column('view_id', sa.String, sa.ForeignKey('view.id'), nullable=False),
    )

    # Create table `view_board`
    op.create_table(
        'view_board',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('order', sa.Integer, nullable=False),
        sa.Column('view_id', sa.String, sa.ForeignKey('view.id'), nullable=False),
        sa.Column('board_id', sa.String, sa.ForeignKey('board.id'), nullable=False),
    )

    # add order uniqueness constraints
    op.create_unique_constraint(
        None,
        'component_zone',
        ['zone_id', 'order'],
    )
    op.create_unique_constraint(
        None,
        'zone_view',
        ['view_id', 'order'],
    )
    op.create_unique_constraint(
        None,
        'view_board',
        ['board_id', 'order'],
    )


def downgrade():
    # Drop tables in reverse order of creation
    op.drop_table('board')
    op.drop_table('view_board')
    op.drop_table('view')
    op.drop_table('zone_view')
    op.drop_table('zone')
    op.drop_table('component_zone')
    op.drop_table('component')
