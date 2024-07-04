"""data.name becomes data.id

Revision ID: 0f9299d6970b
Revises: 2b092ba4a3e9
Create Date: 2024-06-24 14:01:59.747943

"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.schema import DropSequence, Sequence

# revision identifiers, used by Alembic.
revision = '0f9299d6970b'
down_revision = '2b092ba4a3e9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    for tbl in ('barcode_metrics', 'data'):
        op.add_column(tbl, sa.Column('folder_ulid', sa.String(), nullable=True))
        op.create_foreign_key(None, tbl, 'folder', ['folder_ulid'], ['folder_ulid'])

    data_rel_tables = (
        'allocation',
        'barcode_metrics',
        'dataset_element',
        'file',
        'mapping_metrics',
    )

    # For all the tables that point to data.data_id, drop the foreign key
    # constraint and change the `data_id` column from INT to VARCHAR
    for tbl in data_rel_tables:
        op.drop_constraint(f'{tbl}_data_id_fkey', tbl)
        op.alter_column(
            tbl,
            'data_id',
            existing_type=sa.INTEGER(),
            type_=sa.String(),
            existing_nullable=True,
        )

    # Change `data.data_id` column itself from INT to VARCHAR
    op.alter_column(
        'data',
        'data_id',
        existing_type=sa.INTEGER(),
        type_=sa.String(),
        existing_nullable=False,
        server_default=None,
        existing_server_default=sa.text("nextval('data_data_id_seq'::regclass)"),
    )
    op.execute(DropSequence(Sequence('data_data_id_seq')))

    # Set the `data_id` column to `data.name` for each of the related tables
    for tbl in data_rel_tables:
        op.execute(
            sa.text(
                f'UPDATE {tbl} SET data_id = data.name'  # noqa: S608
                f' FROM data WHERE {tbl}.data_id = data.data_id'
            )
        )

    # Copy the `name` column into the `data_id` column then drop `name`
    op.execute(sa.text('UPDATE data SET data_id = name'))
    op.drop_column('data', 'name')

    # Rename `project.lims_id` to `study_id` and add `data.study_id`
    # Shuffle `modified_at` and `modified_by` columns to end of table
    op.drop_index('ix_project_lims_id', table_name='project')
    op.alter_column('project', 'lims_id', new_column_name='study_id')
    op.create_unique_constraint(None, 'project', ['study_id'])
    with op.batch_alter_table('data', recreate='always') as batch_op:
        batch_op.add_column(
            sa.Column('study_id', sa.Integer(), nullable=True),
            insert_after='data_id',
        )
        batch_op.add_column(
            sa.Column('modified_at_tmp', sa.TIMESTAMP(timezone=True), nullable=True),
            insert_before='folder_ulid',
        )
        batch_op.add_column(
            sa.Column('modified_by_tmp', sa.String(), nullable=True),
            insert_before='folder_ulid',
        )
    op.execute(sa.text('UPDATE data SET modified_at_tmp = modified_at'))
    op.execute(sa.text('UPDATE data SET modified_by_tmp = modified_by'))
    op.drop_column('data', 'modified_at')
    op.drop_column('data', 'modified_by')
    op.alter_column('data', 'modified_at_tmp', new_column_name='modified_at')
    op.alter_column('data', 'modified_by_tmp', new_column_name='modified_by')
    op.create_foreign_key(None, 'data', 'project', ['study_id'], ['study_id'])

    # Recreate the foreign key constraints
    for tbl in data_rel_tables:
        op.create_foreign_key(None, tbl, 'data', ['data_id'], ['data_id'])

    # Patch renamed accession types
    for new_type, old_types in (
        ('Analysis', ['ENA Analysis']),
        ('BioProject', ['Bio Project']),
        ('BioSample', ['Bio Sample']),
        ('Experiment', ['ENA Experiment', 'SRA Experiment']),
        ('Run', ['ENA Run', 'SRA Run']),
        ('ToLID', ['ToL Specimen ID']),
    ):
        for old_t in old_types:
            op.execute(
                sa.text(
                    f'UPDATE accession SET accession_type_id'  # noqa: S608
                    f" = '{new_type}' WHERE accession_type_id = '{old_t}'"
                )
            )


def downgrade() -> None:
    pass
