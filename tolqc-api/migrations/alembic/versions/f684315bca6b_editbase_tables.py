"""EditBase tables

Revision ID: f684315bca6b
Revises: 7d93cd1a5232
Create Date: 2024-08-14 11:11:36.284853

"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'f684315bca6b'
down_revision = '7d93cd1a5232'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Switch modified_by back to integer and make it a ForeignKey to user.id
    for tbl in (
        'accession',
        'assembly',
        'assembly_status',
        'data',
        'dataset',
        'dataset_status',
        'genomescope_metrics',
        'sample',
        'species',
        'specimen',
        'specimen_status',
    ):
        op.alter_column(
            tbl,
            'modified_by',
            existing_type=sa.VARCHAR(),
            type_=sa.Integer(),
            existing_nullable=True,
            postgresql_using='modified_by::integer',
        )
        op.create_foreign_key(None, tbl, 'user', ['modified_by'], ['id'])

    # Create edit_... tables
    op.create_table(
        'edit_assembly',
        sa.Column('edit_id', sa.Integer(), nullable=False),
        sa.Column('assembly_id', sa.Integer(), nullable=False),
        sa.Column('changes', postgresql.JSONB(astext_type=sa.Text()), nullable=False),
        sa.Column('modified_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('modified_by', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ['assembly_id'],
            ['assembly.assembly_id'],
        ),
        sa.ForeignKeyConstraint(
            ['modified_by'],
            ['user.id'],
        ),
        sa.PrimaryKeyConstraint('edit_id'),
        sa.UniqueConstraint('modified_at', 'assembly_id'),
    )
    op.create_table(
        'edit_assembly_status',
        sa.Column('edit_id', sa.Integer(), nullable=False),
        sa.Column('assembly_status_id', sa.Integer(), nullable=False),
        sa.Column('changes', postgresql.JSONB(astext_type=sa.Text()), nullable=False),
        sa.Column('modified_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('modified_by', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ['assembly_status_id'],
            ['assembly_status.assembly_status_id'],
        ),
        sa.ForeignKeyConstraint(
            ['modified_by'],
            ['user.id'],
        ),
        sa.PrimaryKeyConstraint('edit_id'),
        sa.UniqueConstraint('modified_at', 'assembly_status_id'),
    )
    op.create_table(
        'edit_dataset',
        sa.Column('edit_id', sa.Integer(), nullable=False),
        sa.Column('dataset_id', sa.String(), nullable=False),
        sa.Column('changes', postgresql.JSONB(astext_type=sa.Text()), nullable=False),
        sa.Column('modified_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('modified_by', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ['dataset_id'],
            ['dataset.dataset_id'],
        ),
        sa.ForeignKeyConstraint(
            ['modified_by'],
            ['user.id'],
        ),
        sa.PrimaryKeyConstraint('edit_id'),
        sa.UniqueConstraint('modified_at', 'dataset_id'),
    )
    op.create_table(
        'edit_dataset_status',
        sa.Column('edit_id', sa.Integer(), nullable=False),
        sa.Column('dataset_status_id', sa.Integer(), nullable=False),
        sa.Column('changes', postgresql.JSONB(astext_type=sa.Text()), nullable=False),
        sa.Column('modified_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('modified_by', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ['dataset_status_id'],
            ['dataset_status.dataset_status_id'],
        ),
        sa.ForeignKeyConstraint(
            ['modified_by'],
            ['user.id'],
        ),
        sa.PrimaryKeyConstraint('edit_id'),
        sa.UniqueConstraint('modified_at', 'dataset_status_id'),
    )
    op.create_table(
        'edit_specimen',
        sa.Column('edit_id', sa.Integer(), nullable=False),
        sa.Column('specimen_id', sa.String(), nullable=False),
        sa.Column('changes', postgresql.JSONB(astext_type=sa.Text()), nullable=False),
        sa.Column('modified_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('modified_by', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ['modified_by'],
            ['user.id'],
        ),
        sa.ForeignKeyConstraint(
            ['specimen_id'],
            ['specimen.specimen_id'],
        ),
        sa.PrimaryKeyConstraint('edit_id'),
        sa.UniqueConstraint('modified_at', 'specimen_id'),
    )
    op.create_table(
        'edit_specimen_status',
        sa.Column('edit_id', sa.Integer(), nullable=False),
        sa.Column('specimen_status_id', sa.Integer(), nullable=False),
        sa.Column('changes', postgresql.JSONB(astext_type=sa.Text()), nullable=False),
        sa.Column('modified_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('modified_by', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ['modified_by'],
            ['user.id'],
        ),
        sa.ForeignKeyConstraint(
            ['specimen_status_id'],
            ['specimen_status.specimen_status_id'],
        ),
        sa.PrimaryKeyConstraint('edit_id'),
        sa.UniqueConstraint('modified_at', 'specimen_status_id'),
    )
    op.create_table(
        'edit_accession',
        sa.Column('edit_id', sa.Integer(), nullable=False),
        sa.Column('accession_id', sa.String(), nullable=False),
        sa.Column('changes', postgresql.JSONB(astext_type=sa.Text()), nullable=False),
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
        sa.PrimaryKeyConstraint('edit_id'),
        sa.UniqueConstraint('modified_at', 'accession_id'),
    )
    op.create_table(
        'edit_genomescope_metrics',
        sa.Column('edit_id', sa.Integer(), nullable=False),
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('changes', postgresql.JSONB(astext_type=sa.Text()), nullable=False),
        sa.Column('modified_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('modified_by', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ['id'],
            ['genomescope_metrics.id'],
        ),
        sa.ForeignKeyConstraint(
            ['modified_by'],
            ['user.id'],
        ),
        sa.PrimaryKeyConstraint('edit_id'),
        sa.UniqueConstraint('modified_at', 'id'),
    )
    op.create_table(
        'edit_sample',
        sa.Column('edit_id', sa.Integer(), nullable=False),
        sa.Column('sample_id', sa.String(), nullable=False),
        sa.Column('changes', postgresql.JSONB(astext_type=sa.Text()), nullable=False),
        sa.Column('modified_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('modified_by', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ['modified_by'],
            ['user.id'],
        ),
        sa.ForeignKeyConstraint(
            ['sample_id'],
            ['sample.sample_id'],
        ),
        sa.PrimaryKeyConstraint('edit_id'),
        sa.UniqueConstraint('modified_at', 'sample_id'),
    )
    op.create_table(
        'edit_species',
        sa.Column('edit_id', sa.Integer(), nullable=False),
        sa.Column('species_id', sa.String(), nullable=False),
        sa.Column('changes', postgresql.JSONB(astext_type=sa.Text()), nullable=False),
        sa.Column('modified_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('modified_by', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ['modified_by'],
            ['user.id'],
        ),
        sa.ForeignKeyConstraint(
            ['species_id'],
            ['species.species_id'],
        ),
        sa.PrimaryKeyConstraint('edit_id'),
        sa.UniqueConstraint('modified_at', 'species_id'),
    )
    op.create_table(
        'edit_data',
        sa.Column('edit_id', sa.Integer(), nullable=False),
        sa.Column('data_id', sa.String(), nullable=False),
        sa.Column('changes', postgresql.JSONB(astext_type=sa.Text()), nullable=False),
        sa.Column('modified_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('modified_by', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ['data_id'],
            ['data.data_id'],
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
