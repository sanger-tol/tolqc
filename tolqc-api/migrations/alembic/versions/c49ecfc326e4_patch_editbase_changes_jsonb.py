"""Patch EditBase.changes JSONB

Revision ID: c49ecfc326e4
Revises: f684315bca6b
Create Date: 2024-09-30 13:33:14.764169

"""

from alembic import op
from sqlalchemy import text

# revision identifiers, used by Alembic.
revision = 'c49ecfc326e4'
down_revision = 'f684315bca6b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    for tbl in (
        'edit_accession',
        'edit_assembly',
        'edit_assembly_status',
        'edit_data',
        'edit_dataset',
        'edit_dataset_status',
        'edit_genomescope_metrics',
        'edit_sample',
        'edit_species',
        'edit_specimen',
        'edit_specimen_status',
    ):
        # Patch JSONB `changes` column wrongly stored as an escaped JSON string
        op.execute(
            text(
                f'UPDATE {tbl}'  # noqa: S608
                " SET changes = (changes #>> '{}')::JSONB"
                " WHERE starts_with(changes::VARCHAR, '\"')"
            )
        )


def downgrade() -> None:
    pass
