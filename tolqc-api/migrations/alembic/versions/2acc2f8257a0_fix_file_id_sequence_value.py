"""Fix file.id sequence value

Revision ID: 2acc2f8257a0
Revises: 2d56a365736e
Create Date: 2026-04-09 14:49:48.254577

"""

from alembic import op
from sqlalchemy import text
from sqlalchemy.schema import CreateSequence, DropSequence, Sequence


# revision identifiers, used by Alembic.
revision = '2acc2f8257a0'
down_revision = '2d56a365736e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Remove the old sequence
    op.alter_column('file', 'id', server_default=None)
    seq = 'file_id_seq'
    for x in (seq, '_alembic_tmp_file_id_seq'):
        op.execute(DropSequence(Sequence(x)))

    # Create the new sequence
    op.execute(CreateSequence(Sequence(seq)))
    op.alter_column(
        'file',
        'id',
        server_default=text(f"nextval('{seq}'::regclass)"),
    )

    # Set sequence to correct current value
    set_sql = text(f"""
      SELECT setval('{seq}', ( SELECT MAX(id) FROM file) )
    """)  # noqa: S608
    op.execute(set_sql)


def downgrade() -> None:
    pass
