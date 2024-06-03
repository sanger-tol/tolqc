"""Tables and columns for Folders

Revision ID: 0ec89827f532
Revises: bbcd2bbe983a
Create Date: 2024-05-30 17:10:03.880103

"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '0ec89827f532'
down_revision = 'bbcd2bbe983a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'folder_location',
        sa.Column(
            'folder_location_id',
            sa.String(),
            nullable=False,
        ),
        sa.Column(
            'uri_prefix',
            sa.String(),
            nullable=True,
        ),
        sa.PrimaryKeyConstraint('folder_location_id'),
    )

    op.create_table(
        'folder',
        sa.Column(
            'folder_ulid',
            sa.String(),
            nullable=False,
        ),
        sa.Column(
            'folder_location_id',
            sa.String(),
            nullable=False,
        ),
        sa.Column(
            'image_file_list',
            postgresql.JSONB(astext_type=sa.Text()),
            nullable=True,
        ),
        sa.Column(
            'other_file_list',
            postgresql.JSONB(astext_type=sa.Text()),
            nullable=True,
        ),
        sa.Column(
            'files_total_bytes',
            sa.BigInteger(),
            nullable=True,
        ),
        sa.ForeignKeyConstraint(
            ['folder_location_id'],
            ['folder_location.folder_location_id'],
        ),
        sa.PrimaryKeyConstraint('folder_ulid'),
    )

    for table in (
        'busco_metrics',
        'contigviz_metrics',
        'genomescope_metrics',
        'merqury_metrics',
        'ploidyplot_metrics',
    ):
        op.add_column(
            table,
            sa.Column(
                'folder_ulid',
                sa.String(),
                nullable=True,
            ),
        )
        op.create_foreign_key(
            None,
            table,
            'folder',
            ['folder_ulid'],
            ['folder_ulid'],
        )


def downgrade() -> None:
    pass
