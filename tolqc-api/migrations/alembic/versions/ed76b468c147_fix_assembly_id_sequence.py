"""Fix assembly_id sequence

Revision ID: ed76b468c147
Revises: 0aa08285a0ab
Create Date: 2026-09-16 10:16:38.131817

"""
from alembic import op
from sqlalchemy.schema import CreateSequence, DropSequence, Sequence
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ed76b468c147'
down_revision = '0aa08285a0ab'
branch_labels = None
depends_on = None


def upgrade() -> None:

    # Drop temp sequence name created by previous alembic batch alter table
    op.alter_column('assembly', 'assembly_id', server_default=None)
    op.execute(DropSequence(Sequence('_alembic_tmp_assembly_assembly_id_seq')))

    # Attach the correct sequence to the column
    sqn_name = 'assembly_assembly_id_seq'
    op.alter_column(
        'assembly',
        'assembly_id',
        server_default=sa.text(f"nextval('{sqn_name}'::regclass)"),
    )

    # Sync the sequence with the assembly_id column
    op.execute(
        sa.text(f"""
          SELECT setval('{sqn_name}',
            (SELECT MAX(assembly_id) FROM assembly))
        """)  # noqa: S608
    )


def downgrade() -> None:
    pass
