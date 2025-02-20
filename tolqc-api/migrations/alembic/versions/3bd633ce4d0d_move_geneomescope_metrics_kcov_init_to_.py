"""Move geneomescope_metrics.kcov_init next to other input parameters

Revision ID: 3bd633ce4d0d
Revises: 1a4ae5d77449
Create Date: 2025-01-15 16:49:15.603967

"""

from alembic import op
from sqlalchemy import Column, Integer, text
from sqlalchemy.schema import CreateSequence, DropSequence, Sequence


# revision identifiers, used by Alembic.
revision = '3bd633ce4d0d'
down_revision = '1a4ae5d77449'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # All this is to move the kcov_init column within the genomescope_metrics table!
    tbl_name = 'genomescope_metrics'

    # Drop the sequence and manually recreate it, or alembic.batch_alter_table
    # mangles its name and looses its state.
    sqn_name = 'genomescope_metrics_id_seq'
    op.alter_column(tbl_name, 'id', server_default=None)
    op.drop_constraint('edit_genomescope_metrics_id_fkey', 'edit_genomescope_metrics')
    op.execute(DropSequence(Sequence(sqn_name)))

    op.alter_column(tbl_name, 'kcov_init', new_column_name='tmp')
    with op.batch_alter_table(tbl_name, recreate='always') as batch_op:
        batch_op.add_column(Column('kcov_init', Integer()), insert_after='ploidy')
    op.execute(text(f'UPDATE {tbl_name} SET kcov_init = tmp'))  # noqa: S608
    op.drop_column(tbl_name, 'tmp')
    op.create_foreign_key(
        'edit_genomescope_metrics_id_fkey',
        'edit_genomescope_metrics',
        tbl_name,
        ['id'],
        ['id'],
    )

    # Create the new sequence
    op.execute(CreateSequence(Sequence(sqn_name)))
    op.alter_column(
        tbl_name,
        'id',
        server_default=text(f"nextval('{sqn_name}'::regclass)"),
    )

    # Set sequence to correct current value
    set_sql = text(
        f"SELECT setval('{sqn_name}', (SELECT MAX(id) FROM genomescope_metrics))"  # noqa: S608
    )
    op.execute(set_sql)


def downgrade() -> None:
    pass
