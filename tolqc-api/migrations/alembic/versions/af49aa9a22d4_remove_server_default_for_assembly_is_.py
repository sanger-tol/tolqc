"""Remove server default for assembly.is_principal and .is_reference

Revision ID: af49aa9a22d4
Revises: 1203fe3dac4c
Create Date: 2026-10-20 11:27:44.961360

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'af49aa9a22d4'
down_revision = '1203fe3dac4c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('assembly', 'is_principal', server_default=None)
    op.alter_column('assembly', 'is_reference', server_default=None)
    op.execute(
        sa.text("""
      UPDATE assembly
      SET is_principal = NULL
      WHERE is_principal = FALSE
        AND is_reference IS NULL
    """)
    )


def downgrade() -> None:
    pass
