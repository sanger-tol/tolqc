"""New data_submission accession staging table

Revision ID: 593122eb1742
Revises: 3bd633ce4d0d
Create Date: 2025-03-19 15:57:34.994413

"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '593122eb1742'
down_revision = '3bd633ce4d0d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'data_submission',
        sa.Column('data_id', sa.String(), nullable=False),
        sa.Column('study_accession_id', sa.String(), nullable=True),
        sa.Column('sample_accession_id', sa.String(), nullable=True),
        sa.Column('experiment_accession_id', sa.String(), nullable=True),
        sa.Column('run_accession_id', sa.String(), nullable=True),
        sa.Column('analysis_accession_id', sa.String(), nullable=True),
        sa.Column('submission_time', sa.DateTime(timezone=True), nullable=True),
        sa.Column('modified_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('modified_by', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ['analysis_accession_id'],
            ['accession.accession_id'],
        ),
        sa.ForeignKeyConstraint(
            ['data_id'],
            ['data.data_id'],
        ),
        sa.ForeignKeyConstraint(
            ['experiment_accession_id'],
            ['accession.accession_id'],
        ),
        sa.ForeignKeyConstraint(
            ['modified_by'],
            ['user.id'],
        ),
        sa.ForeignKeyConstraint(
            ['run_accession_id'],
            ['accession.accession_id'],
        ),
        sa.ForeignKeyConstraint(
            ['sample_accession_id'],
            ['accession.accession_id'],
        ),
        sa.ForeignKeyConstraint(
            ['study_accession_id'],
            ['accession.accession_id'],
        ),
        sa.PrimaryKeyConstraint('data_id'),
    )
    op.create_index(
        op.f('ix_data_submission_submission_time'),
        'data_submission',
        ['submission_time'],
        unique=False,
    )
    op.create_table(
        'edit_data_submission',
        sa.Column('edit_id', sa.Integer(), nullable=False),
        sa.Column('data_id', sa.String(), nullable=False),
        sa.Column('changes', postgresql.JSONB(astext_type=sa.Text()), nullable=False),
        sa.Column('modified_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('modified_by', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ['data_id'],
            ['data_submission.data_id'],
        ),
        sa.ForeignKeyConstraint(
            ['modified_by'],
            ['user.id'],
        ),
        sa.PrimaryKeyConstraint('edit_id'),
        sa.UniqueConstraint('modified_at', 'data_id'),
    )


def downgrade() -> None:
    pass
