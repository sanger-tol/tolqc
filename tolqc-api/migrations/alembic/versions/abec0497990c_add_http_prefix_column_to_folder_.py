"""Add http_prefix column to folder_location

Revision ID: abec0497990c
Revises: 9a5f4bb6f974
Create Date: 2026-02-05 16:26:43.134811

"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'abec0497990c'
down_revision = '9a5f4bb6f974'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Add new `http_prefix` column to `folder_location` table
    op.drop_constraint('folder_folder_location_id_fkey', 'folder')
    with op.batch_alter_table('folder_location', recreate='always') as batch_op:
        batch_op.add_column(
            sa.Column('http_prefix', sa.String(), nullable=True),
            insert_after='uri_prefix',
        )
    op.create_foreign_key(
        None,
        'folder',
        'folder_location',
        ['folder_location_id'],
        ['folder_location_id'],
    )

    # Update data source tables to stay in sync with tol-sdk
    op.alter_column(
        'data_source_instance',
        'data_source_config_id',
        existing_type=sa.INTEGER(),
        nullable=False,
    )


def downgrade() -> None:
    pass
