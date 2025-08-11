"""Smudgeplot metrics table

Revision ID: a79168bbc430
Revises: f11889717402
Create Date: 2025-08-11 14:39:03.822442

"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'a79168bbc430'
down_revision = 'f11889717402'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.drop_table('allocation')
    op.drop_table('edit_project')
    op.drop_table('project')
    op.create_table(
        'project',
        sa.Column('project_id', sa.String(), nullable=False),
        sa.Column('name', sa.String(), nullable=True),
        sa.Column('description', sa.String(), nullable=True),
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
        sa.PrimaryKeyConstraint('project_id'),
    )
    op.create_table(
        'edit_project',
        sa.Column('edit_id', sa.Integer(), nullable=False),
        sa.Column('project_id', sa.String(), nullable=False),
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
    op.create_table(
        'allocation',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('project_id', sa.String(), nullable=True),
        sa.Column('data_id', sa.String(), nullable=True),
        sa.Column('is_primary', sa.Boolean(), nullable=True),
        sa.ForeignKeyConstraint(
            ['data_id'],
            ['data.data_id'],
        ),
        sa.ForeignKeyConstraint(
            ['project_id'],
            ['project.project_id'],
        ),
        sa.PrimaryKeyConstraint('id'),
    )

    op.drop_table('ploidyplot_metrics')
    op.create_table(
        'smudgeplot_metrics',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('dataset_id', sa.String(), nullable=True),
        sa.Column('review_id', sa.String(), nullable=True),
        sa.Column('kmer', sa.Integer(), nullable=True),
        sa.Column('ploidy', sa.Integer(), nullable=True),
        sa.Column('n', sa.Float(), nullable=True),
        sa.Column('partition', sa.String(), nullable=True),
        sa.Column('trim_threshold', sa.Integer(), nullable=True),
        sa.Column('pipeline_id', sa.Integer(), nullable=True),
        sa.Column('folder_ulid', sa.String(), nullable=True),
        sa.ForeignKeyConstraint(
            ['dataset_id'],
            ['dataset.dataset_id'],
        ),
        sa.ForeignKeyConstraint(
            ['folder_ulid'],
            ['folder.folder_ulid'],
        ),
        sa.ForeignKeyConstraint(
            ['pipeline_id'],
            ['pipeline.pipeline_id'],
        ),
        sa.ForeignKeyConstraint(
            ['review_id'],
            ['review_dict.review_id'],
        ),
        sa.PrimaryKeyConstraint('id'),
    )

    op.add_column(
        'accession',
        sa.Column(
            'is_deleted', sa.Boolean(), server_default=sa.text('false'), nullable=False
        ),
    )

    op.drop_table('merqury_metrics')
    op.create_table(
        'merqury_metrics',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('assembly_id', sa.Integer(), nullable=True),
        sa.Column('dataset_id', sa.String(), nullable=True),
        sa.Column('kmer', sa.String(), nullable=True),
        sa.Column('complete_asm1', sa.Integer(), nullable=True),
        sa.Column('complete_asm2', sa.Integer(), nullable=True),
        sa.Column('complete_all', sa.Integer(), nullable=True),
        sa.Column('qv_asm1', sa.Float(), nullable=True),
        sa.Column('qv_asm2', sa.Float(), nullable=True),
        sa.Column('qv_all', sa.Float(), nullable=True),
        sa.Column('pipeline_id', sa.Integer(), nullable=True),
        sa.Column('folder_ulid', sa.String(), nullable=True),
        sa.ForeignKeyConstraint(
            ['assembly_id'],
            ['assembly.assembly_id'],
        ),
        sa.ForeignKeyConstraint(
            ['dataset_id'],
            ['dataset.dataset_id'],
        ),
        sa.ForeignKeyConstraint(
            ['folder_ulid'],
            ['folder.folder_ulid'],
        ),
        sa.ForeignKeyConstraint(
            ['pipeline_id'],
            ['pipeline.pipeline_id'],
        ),
        sa.PrimaryKeyConstraint('id'),
    )


def downgrade() -> None:
    pass
