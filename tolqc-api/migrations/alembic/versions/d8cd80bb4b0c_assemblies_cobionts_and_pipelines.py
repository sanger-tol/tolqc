"""Assemblies, cobionts and pipelines

Revision ID: d8cd80bb4b0c
Revises: 3a0211ede5e5
Create Date: 2025-06-23 15:12:14.845913

"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'd8cd80bb4b0c'
down_revision = '3a0211ede5e5'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Drop foreign key constraint for all tables pointing at software_version
    software_version_rel_tables = (
        'assembly',
        'busco_metrics',
        'contigviz_metrics',
        'genomescope_metrics',
        'mapping_metrics',
        'markerscan_metrics',
        'merqury_metrics',
        'metagenome',
        'metagenome_bin',
        'ploidyplot_metrics',
    )
    for tbl in software_version_rel_tables:
        op.drop_constraint(f'{tbl}_software_version_id_fkey', tbl)

    op.drop_table('software_version')

    op.create_table(
        'pipeline',
        sa.Column('pipeline_id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('pipeline_id'),
    )
    op.create_table(
        'pipeline_step',
        sa.Column('pipeline_step_id', sa.Integer(), nullable=False),
        sa.Column('pipeline_id', sa.Integer(), nullable=False),
        sa.Column('software_version_id', sa.Integer(), nullable=True),
        sa.Column('command', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('pipeline_step_id'),
        sa.ForeignKeyConstraint(
            ['pipeline_id'],
            ['pipeline.pipeline_id'],
        ),
    )
    op.create_table(
        'software_version',
        sa.Column('software_version_id', sa.Integer(), nullable=False),
        sa.Column('package_name', sa.String(), nullable=False),
        sa.Column('version', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('software_version_id'),
        sa.UniqueConstraint('package_name', 'version'),
    )
    op.create_foreign_key(
        None,
        'pipeline_step',
        'software_version',
        ['software_version_id'],
        ['software_version_id'],
    )

    for tbl in software_version_rel_tables:
        op.alter_column(tbl, 'software_version_id', new_column_name='pipeline_id')
        op.create_foreign_key(None, tbl, 'pipeline', ['pipeline_id'], ['pipeline_id'])

    # op.create_index(op.f('ix_location_path'), 'location', ['path'], unique=False)

    # Specimen table changes
    op.create_table(
        'specimen_category_dict',
        sa.Column('category', sa.String(), nullable=False),
        sa.Column('description', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('category'),
    )

    # Drop foreign key constraint for all tables pointing at specimen
    specimen_rel_tables = (
        'edit_specimen',
        'offspring',
        'sample',
        'specimen_status',
    )
    for tbl in specimen_rel_tables:
        op.drop_constraint(f'{tbl}_specimen_id_fkey', tbl)
    op.drop_constraint('offspring_offspring_specimen_id_fkey', 'offspring')
    op.drop_constraint('metagenome_host_specimen_id_fkey', 'metagenome')

    # Alter specimen table
    with op.batch_alter_table('specimen', recreate='always') as batch_op:
        batch_op.create_index(None, ['supplied_name'], unique=False)
        batch_op.add_column(
            sa.Column('sts_specimen', sa.String(), nullable=True),
            insert_after='supplied_name',
        )
        batch_op.create_index(None, ['sts_specimen'], unique=False)
        batch_op.add_column(
            sa.Column('category', sa.String(), nullable=True),
            insert_after='sts_specimen',
        )
        batch_op.add_column(
            sa.Column('cobiont_specimen_id', sa.String(), nullable=True),
        )
    op.create_foreign_key(
        None,
        'specimen',
        'specimen_category_dict',
        ['category'],
        ['category'],
    )
    op.create_foreign_key(
        None,
        'specimen',
        'specimen',
        ['cobiont_specimen_id'],
        ['specimen_id'],
    )

    # Recreate specimen table foreign key constraints
    for tbl in specimen_rel_tables:
        op.create_foreign_key(
            None,
            tbl,
            'specimen',
            ['specimen_id'],
            ['specimen_id'],
        )
    op.create_foreign_key(
        None,
        'offspring',
        'specimen',
        ['offspring_specimen_id'],
        ['specimen_id'],
    )
    op.create_foreign_key(
        None,
        'metagenome',
        'specimen',
        ['host_specimen_id'],
        ['specimen_id'],
    )

    # Dataset table
    op.drop_column('assembly', 'dataset_id')
    dastaset_rel_tables = (
        'dataset_element',
        'dataset_status',
        'edit_dataset',
        'genomescope_metrics',
        'merqury_metrics',
        'metagenome',
        'ploidyplot_metrics',
    )
    for tbl in dastaset_rel_tables:
        op.drop_constraint(f'{tbl}_dataset_id_fkey', tbl)
    with op.batch_alter_table('dataset', recreate='always') as batch_op:
        batch_op.add_column(
            sa.Column('name', sa.String(), nullable=True),
            insert_after='dataset_id',
        )
        batch_op.create_index(None, ['name'], unique=False)
    for tbl in dastaset_rel_tables:
        op.create_foreign_key(
            None,
            tbl,
            'dataset',
            ['dataset_id'],
            ['dataset_id'],
        )

    # Assembly table
    assembly_rel_tables = (
        'assembly_metrics',
        'assembly_source',
        'assembly_status',
        'busco_metrics',
        'contigviz_metrics',
        'edit_assembly',
        'mapping_metrics',
        'markerscan_metrics',
        'merqury_metrics',
    )
    for tbl in assembly_rel_tables:
        op.drop_constraint(f'{tbl}_assembly_id_fkey', tbl)
    op.drop_constraint('assembly_source_source_assembly_id_fkey', 'assembly_source')
    with op.batch_alter_table('assembly', recreate='always') as batch_op:
        batch_op.add_column(
            sa.Column('specimen_id', sa.String(), nullable=True),
            insert_after='assembly_status_id',
        )
    op.create_foreign_key(
        None,
        'assembly',
        'specimen',
        ['specimen_id'],
        ['specimen_id'],
    )
    for tbl in assembly_rel_tables:
        op.create_foreign_key(
            None,
            tbl,
            'assembly',
            ['assembly_id'],
            ['assembly_id'],
        )
    op.create_foreign_key(
        None,
        'assembly_source',
        'assembly',
        ['source_assembly_id'],
        ['assembly_id'],
    )

    # AssemblyDataset table
    op.create_table(
        'assembly_dataset',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('assembly_id', sa.Integer()),
        sa.Column('dataset_id', sa.String()),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_foreign_key(
        None, 'assembly_dataset', 'assembly', ['assembly_id'], ['assembly_id']
    )
    op.create_foreign_key(
        None, 'assembly_dataset', 'dataset', ['dataset_id'], ['dataset_id']
    )


def downgrade() -> None:
    pass
