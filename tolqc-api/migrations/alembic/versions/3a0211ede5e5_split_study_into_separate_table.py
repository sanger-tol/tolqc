"""Split study into separate table

Revision ID: 3a0211ede5e5
Revises: a66e18edc0e5
Create Date: 2025-05-28 15:54:17.073999

"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '3a0211ede5e5'
down_revision = 'a66e18edc0e5'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'study',
        sa.Column('study_id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=True),
        sa.Column(
            'auto_sync', sa.Boolean(), server_default=sa.text('true'), nullable=False
        ),
        sa.Column('accession_id', sa.String(), nullable=True),
        sa.Column('modified_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('modified_by', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ['accession_id'],
            ['accession.accession_id'],
        ),
        sa.ForeignKeyConstraint(
            ['modified_by'],
            ['user.id'],
        ),
        sa.PrimaryKeyConstraint('study_id'),
    )
    op.drop_constraint('data_study_id_fkey', 'data', type_='foreignkey')

    # Move data from the project table into study
    for sql in (
        """
        INSERT INTO study(study_id, name)
        SELECT study_id, description
        FROM project
        WHERE study_id IS NOT NULL
        """,
        """
        DELETE FROM allocation AS a
        USING project AS p
        WHERE a.project_id = p.project_id
          AND p.study_id IS NOT NULL
        """,
        """
        DELETE FROM project
        WHERE study_id IS NOT NULL
        """,
    ):
        op.execute(sa.text(sql))
    op.create_foreign_key(None, 'data', 'study', ['study_id'], ['study_id'])

    op.drop_column('project', 'study_id')

    op.create_table(
        'edit_study',
        sa.Column('edit_id', sa.Integer(), nullable=False),
        sa.Column('study_id', sa.Integer(), nullable=False),
        sa.Column('changes', postgresql.JSONB(astext_type=sa.Text()), nullable=False),
        sa.Column('modified_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('modified_by', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ['modified_by'],
            ['user.id'],
        ),
        sa.ForeignKeyConstraint(
            ['study_id'],
            ['study.study_id'],
        ),
        sa.PrimaryKeyConstraint('edit_id'),
        sa.UniqueConstraint('modified_at', 'study_id'),
    )

    op.create_table(
        'edit_project',
        sa.Column('edit_id', sa.Integer(), nullable=False),
        sa.Column('project_id', sa.Integer(), nullable=False),
        sa.Column('changes', postgresql.JSONB(astext_type=sa.Text()), nullable=False),
        sa.Column('modified_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('modified_by', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ['modified_by'],
            ['user.id'],
        ),
        sa.ForeignKeyConstraint(
            ['project_id'],
            ['project.project_id'],
        ),
        sa.PrimaryKeyConstraint('edit_id'),
        sa.UniqueConstraint('modified_at', 'project_id'),
    )
    op.add_column(
        'project', sa.Column('modified_at', sa.DateTime(timezone=True), nullable=True)
    )
    op.add_column('project', sa.Column('modified_by', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'project', 'user', ['modified_by'], ['id'])

    acc_rel_table_cols = [
        ('assembly', 'bioproject_accession_id'),
        ('assembly', 'genome_accession_id'),
        ('data', 'accession_id'),
        ('data_submission', 'analysis_accession_id'),
        ('data_submission', 'experiment_accession_id'),
        ('data_submission', 'run_accession_id'),
        ('data_submission', 'sample_accession_id'),
        ('data_submission', 'study_accession_id'),
        ('edit_accession', 'accession_id'),
        ('metagenome', 'assembly_accession_id'),
        ('metagenome', 'bioproject_accession_id'),
        ('metagenome', 'biosample_accession_id'),
        ('metagenome_bin', 'assembly_accession_id'),
        ('metagenome_bin', 'biosample_accession_id'),
        ('project', 'accession_id'),
        ('sample', 'accession_id'),
        ('species', 'data_accession_id'),
        ('species', 'umbrella_accession_id'),
        ('specimen', 'accession_id'),
        ('study', 'accession_id'),
    ]
    for tbl, col in acc_rel_table_cols:
        op.drop_constraint(f'{tbl}_{col}_fkey', tbl)
    with op.batch_alter_table('accession', recreate='always') as batch_op:
        batch_op.add_column(
            sa.Column('name', sa.String(), nullable=True),
            insert_after='date_submitted',
        )
        batch_op.add_column(
            sa.Column('alias', sa.String(), nullable=True),
            insert_after='description',
        )
        batch_op.add_column(
            sa.Column('submitter_id', sa.String(), nullable=True),
            insert_after='alias',
        )
    for tbl, col in acc_rel_table_cols:
        op.create_foreign_key(None, tbl, 'accession', [col], ['accession_id'])

    op.create_table(
        'link_status_dict',
        sa.Column('link_status', sa.String(), nullable=False),
        sa.Column('description', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('link_status'),
    )
    op.create_table(
        'submitter_dict',
        sa.Column('submitter_id', sa.String(), nullable=False),
        sa.Column('webin_account', sa.String(), nullable=True),
        sa.Column('description', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('submitter_id'),
    )
    op.create_table(
        'bioproject_link',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('parent_accession_id', sa.String(), nullable=True),
        sa.Column('child_accession_id', sa.String(), nullable=True),
        sa.Column('link_status', sa.String(), nullable=True),
        sa.Column('modified_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('modified_by', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ['child_accession_id'],
            ['accession.accession_id'],
        ),
        sa.ForeignKeyConstraint(
            ['link_status'],
            ['link_status_dict.link_status'],
        ),
        sa.ForeignKeyConstraint(
            ['modified_by'],
            ['user.id'],
        ),
        sa.ForeignKeyConstraint(
            ['parent_accession_id'],
            ['accession.accession_id'],
        ),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('parent_accession_id', 'child_accession_id'),
    )
    op.create_table(
        'edit_bioproject_link',
        sa.Column('edit_id', sa.Integer(), nullable=False),
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('changes', postgresql.JSONB(astext_type=sa.Text()), nullable=False),
        sa.Column('modified_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('modified_by', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ['id'],
            ['bioproject_link.id'],
        ),
        sa.ForeignKeyConstraint(
            ['modified_by'],
            ['user.id'],
        ),
        sa.PrimaryKeyConstraint('edit_id'),
        sa.UniqueConstraint('modified_at', 'id'),
    )

    op.drop_index('umbrella_project_id_species_id_key', table_name='umbrella')
    op.drop_table('umbrella')

    op.create_index(
        op.f('ix_accession_secondary'), 'accession', ['secondary'], unique=False
    )
    op.create_foreign_key(
        None, 'accession', 'submitter_dict', ['submitter_id'], ['submitter_id']
    )


def downgrade() -> None:
    pass
