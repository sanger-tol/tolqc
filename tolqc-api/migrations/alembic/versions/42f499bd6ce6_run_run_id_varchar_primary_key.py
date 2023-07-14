"""run.run_id VarChar primary key

Revision ID: 42f499bd6ce6
Revises: 3936f8476e07
Create Date: 2023-07-14 16:40:34.698009

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '42f499bd6ce6'
down_revision = '3936f8476e07'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.drop_constraint(
        'data_run_id_fkey',
        'data',
        type_='foreignkey',
    )
    op.drop_constraint(
        'pacbio_run_metrics_run_id_fkey',
        'pacbio_run_metrics',
        type_='foreignkey',
    )
    op.alter_column(
        'run',
        'id',
        existing_type=sa.INTEGER(),
        type_=sa.String(),
        new_column_name='run_id',
    )
    op.alter_column(
        'data',
        'run_id',
        existing_type=sa.INTEGER(),
        type_=sa.String(),
        existing_nullable=True,
    )
    op.alter_column(
        'pacbio_run_metrics',
        'run_id',
        existing_type=sa.INTEGER(),
        type_=sa.String(),
        existing_nullable=True,
    )
    op.create_foreign_key(
        None,
        'data',
        'run',
        ['run_id'],
        ['run_id'],
    )
    op.create_foreign_key(
        None,
        'pacbio_run_metrics',
        'run',
        ['run_id'],
        ['run_id'],
    )
    op.alter_column(
        'file',
        'realtive_path',
        new_column_name='relative_path',
    )


def downgrade() -> None:
    op.drop_constraint(
        'data_run_id_fkey',
        'data',
        type_='foreignkey',
    )
    op.drop_constraint(
        'pacbio_run_metrics_run_id_fkey',
        'pacbio_run_metrics',
        type_='foreignkey',
    )
    op.alter_column(
        'run',
        'run_id',
        existing_type=sa.String(),
        type_=sa.INTEGER(),
        new_column_name='id',
    )
    op.alter_column(
        'data',
        'run_id',
        existing_type=sa.String(),
        type_=sa.INTEGER(),
        existing_nullable=True,
    )
    op.alter_column(
        'pacbio_run_metrics',
        'run_id',
        existing_type=sa.String(),
        type_=sa.INTEGER(),
        existing_nullable=True,
    )
    op.create_foreign_key(
        None,
        'data',
        'run',
        ['run_id'],
        ['id'],
    )
    op.create_foreign_key(
        None,
        'pacbio_run_metrics',
        'run',
        ['run_id'],
        ['id'],
    )
    op.alter_column(
        'file',
        'relative_path',
        new_column_name='realtive_path',
    )
