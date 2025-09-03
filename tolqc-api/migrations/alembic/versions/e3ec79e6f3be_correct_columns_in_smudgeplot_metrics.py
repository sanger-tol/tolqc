"""Correct columns in smudgeplot_metrics

Revision ID: e3ec79e6f3be
Revises: f5c78f517f05
Create Date: 2025-09-03 17:17:26.183964

"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'e3ec79e6f3be'
down_revision = 'f5c78f517f05'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'smudgeplot_interpretation_dict',
        sa.Column('interpretation', sa.String(), nullable=False),
        sa.Column('description', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('interpretation'),
    )

    for tbl in 'dataset', 'pipeline', 'review':
        op.drop_constraint(f'smudgeplot_metrics_{tbl}_id_fkey', 'smudgeplot_metrics')
    op.drop_table('smudgeplot_metrics')

    op.create_table(
        'smudgeplot_metrics',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('dataset_id', sa.String(), nullable=True),
        sa.Column('pipeline_id', sa.Integer(), nullable=True),
        sa.Column('interpretation', sa.String(), nullable=True),
        sa.Column('haploid_coverage', sa.Float(), nullable=True),
        sa.Column('error_fraction', sa.Float(), nullable=True),
        sa.Column('top_smudges', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.Column('results', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.Column('folder_ulid', sa.String(), nullable=True),
        sa.Column('modified_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('modified_by', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ['interpretation'],
            ['smudgeplot_interpretation_dict.interpretation'],
        ),
        sa.ForeignKeyConstraint(
            ['dataset_id'],
            ['dataset.dataset_id'],
        ),
        sa.ForeignKeyConstraint(
            ['pipeline_id'],
            ['pipeline.pipeline_id'],
        ),
        sa.ForeignKeyConstraint(
            ['folder_ulid'],
            ['folder.folder_ulid'],
        ),
        sa.ForeignKeyConstraint(
            ['modified_by'],
            ['user.id'],
        ),
        sa.PrimaryKeyConstraint('id'),
    )

    op.create_table(
        'edit_smudgeplot_metrics',
        sa.Column('edit_id', sa.Integer(), nullable=False),
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('changes', postgresql.JSONB(astext_type=sa.Text()), nullable=False),
        sa.Column('modified_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('modified_by', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ['id'],
            ['smudgeplot_metrics.id'],
        ),
        sa.ForeignKeyConstraint(
            ['modified_by'],
            ['user.id'],
        ),
        sa.PrimaryKeyConstraint('edit_id'),
        sa.UniqueConstraint('modified_at', 'id'),
    )


def downgrade() -> None:
    pass
