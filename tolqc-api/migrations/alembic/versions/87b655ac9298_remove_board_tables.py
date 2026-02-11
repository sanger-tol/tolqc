"""Remove board tables

Revision ID: 87b655ac9298
Revises: abec0497990c
Create Date: 2026-02-09 22:57:11.438483

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '87b655ac9298'
down_revision = 'abec0497990c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.drop_table('component_zone')
    op.drop_table('component')
    op.drop_table('zone_view')
    op.drop_table('zone')
    op.drop_table('view_board')
    op.drop_table('view')
    op.drop_table('board')
    op.drop_table('data_source_config_attribute')
    op.drop_table('data_source_config_relationship')
    op.drop_table('loader_instance')
    op.drop_table('loader')
    op.drop_table('data_source_config_summary')
    op.drop_table('data_source_instance')
    op.drop_table('data_source_config')


def downgrade() -> None:
    pass
