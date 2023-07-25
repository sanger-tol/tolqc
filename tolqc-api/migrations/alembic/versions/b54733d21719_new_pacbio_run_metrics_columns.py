"""New PacBio run metrics columns

Revision ID: b54733d21719
Revises: 42f499bd6ce6
Create Date: 2023-07-24 16:30:33.089427

"""
from alembic import op

import sqlalchemy as sa
from sqlalchemy.schema import DropSequence

# revision identifiers, used by Alembic.
revision = 'b54733d21719'
down_revision = '42f499bd6ce6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Drop foregin key constraints that point to run table so we can batch
    # alter it.
    op.drop_constraint(
        'pacbio_run_metrics_run_id_fkey',
        'pacbio_run_metrics',
    )
    op.drop_constraint(
        'data_run_id_fkey',
        'data',
    )

    # Sequence left behind on run.run_id which was changed to varchar
    op.alter_column('run', 'run_id', server_default=None)
    op.execute(DropSequence(sa.Sequence('run_id_seq')))

    # Batch alter table to keep column order the same as in design
    with op.batch_alter_table('run', recreate='always') as batch_op:
        batch_op.add_column(
            sa.Column('start', sa.DateTime(), nullable=True),
            insert_before='complete',
        )
        batch_op.alter_column(
            'lims_id',
            existing_type=sa.Integer(),
            type_=sa.String(),
            existing_nullable=True,
        )

    # Most columns in pacbio_run_metrics have been changed, but we can drop
    # the table because there is no data in it.
    op.drop_table('pacbio_run_metrics')
    op.create_table(
        'pacbio_run_metrics',
        sa.Column('run_id', sa.String(), primary_key=True),
        sa.Column('movie_minutes', sa.Integer(), nullable=True),
        sa.Column('binding_kit', sa.String(), nullable=True),
        sa.Column('sequencing_kit', sa.String(), nullable=True),
        sa.Column('include_kinetics', sa.String(), nullable=True),
        sa.Column('loading_conc', sa.Float(), nullable=True),
        sa.Column('control_num_reads', sa.Integer(), nullable=True),
        sa.Column('control_read_length_mean', sa.Float(), nullable=True),
        sa.Column('polymerase_read_bases', sa.BigInteger(), nullable=True),
        sa.Column('polymerase_num_reads', sa.Integer(), nullable=True),
        sa.Column('polymerase_read_length_mean', sa.Float(), nullable=True),
        sa.Column('polymerase_read_length_n50', sa.Integer(), nullable=True),
        sa.Column('insert_length_mean', sa.Float(), nullable=True),
        sa.Column('insert_length_n50', sa.Integer(), nullable=True),
        sa.Column('unique_molecular_bases', sa.BigInteger(), nullable=True),
        sa.Column('p0_num', sa.Integer(), nullable=True),
        sa.Column('p1_num', sa.Integer(), nullable=True),
        sa.Column('p2_num', sa.Integer(), nullable=True),
        sa.Column('hifi_read_bases', sa.BigInteger(), nullable=True),
        sa.Column('hifi_num_reads', sa.Integer(), nullable=True),
        sa.Column('hifi_low_quality_num_reads', sa.Integer(), nullable=True),
    )

    # Recreate run table foreign keys
    op.create_foreign_key(
        'pacbio_run_metrics_run_id_fkey',
        'pacbio_run_metrics',
        'run',
        ['run_id'],
        ['run_id'],
    )
    op.create_foreign_key(
        'data_run_id_fkey',
        'data',
        'run',
        ['run_id'],
        ['run_id'],
    )


def downgrade() -> None:
    op.drop_constraint('pacbio_run_metrics_run_id_fkey', 'pacbio_run_metrics')
    op.drop_constraint('data_run_id_fkey', 'data')
    op.drop_column('run', 'start')
    op.alter_column(
        'run',
        'lims_id',
        existing_type=sa.String(),
        type_=sa.Integer(),
        existing_nullable=True,
    )
    op.drop_table('pacbio_run_metrics')
    op.create_table(
        'pacbio_run_metrics',
        sa.Column(
            'id',
            sa.Integer(),
            autoincrement=True,
            nullable=False,
            primary_key=True,
        ),
        sa.Column('run_id', sa.String(), nullable=True),
        sa.Column('movie_time', sa.Integer(), nullable=True),
        sa.Column('pre_extension_time', sa.Integer(), nullable=True),
        sa.Column('total_bases', sa.BigInteger(), nullable=True),
        sa.Column('polymerase_reads', sa.Integer(), nullable=True),
        sa.Column('polymerase_reads_bases', sa.Integer(), nullable=True),
        sa.Column(
            'polymerase_reads_mean',
            sa.Float(precision=53),
            nullable=True,
        ),
        sa.Column('polymerase_reads_n50', sa.Integer(), nullable=True),
        sa.Column('subreads_mean', sa.Float(precision=53), nullable=True),
        sa.Column('subreads_n50', sa.Integer(), nullable=True),
        sa.Column('insert_mean', sa.Float(precision=53), nullable=True),
        sa.Column('insert_n50', sa.Integer(), nullable=True),
        sa.Column('unique_molecular_bases', sa.Integer(), nullable=True),
        sa.Column('p0', sa.Integer(), nullable=True),
        sa.Column('p1', sa.Integer(), nullable=True),
        sa.Column('p2', sa.Integer(), nullable=True),
        sa.Column('ccs_fail', sa.Integer(), nullable=True),
        sa.Column('ccs_pass', sa.Integer(), nullable=True),
        sa.Column('ccs_version_id', sa.String(), nullable=True),
        sa.Column('demux_fail', sa.Integer(), nullable=True),
        sa.Column('demux_pass', sa.Integer(), nullable=True),
        sa.Column('demux_version_id', sa.String(), nullable=True),
    )
    op.create_foreign_key(
        'pacbio_run_metrics_run_id_fkey',
        'pacbio_run_metrics',
        'run',
        ['run_id'],
        ['run_id'],
    )
    op.create_foreign_key(
        'data_run_id_fkey',
        'data',
        'run',
        ['run_id'],
        ['run_id'],
    )
