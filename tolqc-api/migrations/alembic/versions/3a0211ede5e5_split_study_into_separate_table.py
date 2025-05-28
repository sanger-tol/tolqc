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


def downgrade() -> None:
    pass
