"""Recreate data.data_id sequence renamed by previous alembic migration

Revision ID: f2d17797a753
Revises: 658ceb639405
Create Date: 2024-02-13 13:55:05.611279

"""
from alembic import op

from sqlalchemy import text
from sqlalchemy.schema import CreateSequence, DropSequence, Sequence

# revision identifiers, used by Alembic.
revision = 'f2d17797a753'
down_revision = '658ceb639405'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Remove the old sequence
    op.alter_column('data', 'data_id', server_default=None)
    op.execute(DropSequence(Sequence('_alembic_tmp_data_data_id_seq1')))

    # Create the new sequence
    data_id_seq = 'data_data_id_seq'
    op.execute(CreateSequence(Sequence(data_id_seq)))
    op.alter_column(
        'data',
        'data_id',
        server_default=text(f"nextval('{data_id_seq}'::regclass)"),
    )

    # Set sequence to correct current value
    set_sql = text(
        f"SELECT setval('{data_id_seq}', (SELECT MAX(data_id) FROM data))"
    )
    op.execute(set_sql)


def downgrade() -> None:
    pass
