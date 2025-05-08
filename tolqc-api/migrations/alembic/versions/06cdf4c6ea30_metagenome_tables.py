"""metagenome tables

Revision ID: 06cdf4c6ea30
Revises: 8c944b832c1b
Create Date: 2025-05-08 10:38:23.425979

"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '06cdf4c6ea30'
down_revision = '8c944b832c1b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'bin_type_dict',
        sa.Column('bin_type', sa.String(), nullable=False),
        sa.Column('description', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('bin_type'),
    )
    op.create_table(
        'metagenome_status_type',
        sa.Column('status_type_id', sa.String(), nullable=False),
        sa.Column('description', sa.String(), nullable=True),
        sa.Column('assign_order', sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint('status_type_id'),
    )
    op.create_table(
        'metagenome',
        sa.Column('metagenome_id', sa.String(), nullable=False),
        sa.Column('species_id', sa.String(), nullable=True),
        sa.Column('metagenome_status_id', sa.Integer(), nullable=True),
        sa.Column('dataset_id', sa.String(), nullable=True),
        sa.Column('host_specimen_id', sa.String(), nullable=True),
        sa.Column('biosample_accession_id', sa.String(), nullable=True),
        sa.Column('bioproject_accession_id', sa.String(), nullable=True),
        sa.Column('assembly_accession_id', sa.String(), nullable=True),
        sa.Column('coverage', sa.Integer(), nullable=True),
        sa.Column('version', sa.Integer(), nullable=True),
        sa.Column('software_version_id', sa.Integer(), nullable=True),
        sa.Column('modified_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('modified_by', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ['assembly_accession_id'],
            ['accession.accession_id'],
        ),
        sa.ForeignKeyConstraint(
            ['bioproject_accession_id'],
            ['accession.accession_id'],
        ),
        sa.ForeignKeyConstraint(
            ['biosample_accession_id'],
            ['accession.accession_id'],
        ),
        sa.ForeignKeyConstraint(
            ['dataset_id'],
            ['dataset.dataset_id'],
        ),
        sa.ForeignKeyConstraint(
            ['host_specimen_id'],
            ['metagenome.metagenome_id'],
        ),
        sa.ForeignKeyConstraint(
            ['modified_by'],
            ['user.id'],
        ),
        sa.ForeignKeyConstraint(
            ['software_version_id'],
            ['software_version.software_version_id'],
        ),
        sa.ForeignKeyConstraint(
            ['species_id'],
            ['species.species_id'],
        ),
        sa.PrimaryKeyConstraint('metagenome_id'),
    )
    op.create_table(
        'metagenome_status',
        sa.Column('metagenome_status_id', sa.Integer(), nullable=False),
        sa.Column('metagenome_id', sa.String(), nullable=False),
        sa.Column('status_type_id', sa.String(), nullable=False),
        sa.Column('status_time', sa.DateTime(timezone=True), nullable=False),
        sa.Column('modified_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('modified_by', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ['metagenome_id'],
            ['metagenome.metagenome_id'],
        ),
        sa.ForeignKeyConstraint(
            ['modified_by'],
            ['user.id'],
        ),
        sa.ForeignKeyConstraint(
            ['status_type_id'],
            ['metagenome_status_type.status_type_id'],
        ),
        sa.PrimaryKeyConstraint('metagenome_status_id'),
    )
    op.create_foreign_key(
        'metagenome_metagenome_status_id_fkey',
        'metagenome',
        'metagenome_status',
        ['metagenome_status_id'],
        ['metagenome_status_id'],
    )

    op.create_table(
        'metagenome_bin',
        sa.Column('metagenome_bin_id', sa.String(), nullable=False),
        sa.Column('metagenome_id', sa.String(), nullable=True),
        sa.Column('species_id', sa.String(), nullable=True),
        sa.Column('metagenome_bin_status_id', sa.Integer(), nullable=True),
        sa.Column('biosample_accession_id', sa.String(), nullable=True),
        sa.Column('assembly_accession_id', sa.String(), nullable=True),
        sa.Column('gtdb_taxonomy', sa.String(), nullable=True),
        sa.Column('bin_type', sa.String(), nullable=True),
        sa.Column('length', sa.BigInteger(), nullable=True),
        sa.Column('contigs', sa.Integer(), nullable=True),
        sa.Column('circular_contigs', sa.Integer(), nullable=True),
        sa.Column('completeness', sa.Float(), nullable=True),
        sa.Column('contamination', sa.Float(), nullable=True),
        sa.Column('mean_coverage', sa.Float(), nullable=True),
        sa.Column('ssu_count', sa.Integer(), nullable=True),
        sa.Column('trna_total', sa.Integer(), nullable=True),
        sa.Column('trna_unique', sa.Integer(), nullable=True),
        sa.Column('has_23s', sa.Boolean(), nullable=True),
        sa.Column('has_16s', sa.Boolean(), nullable=True),
        sa.Column('has_5s', sa.Boolean(), nullable=True),
        sa.Column('n_23s', sa.Integer(), nullable=True),
        sa.Column('n_16s', sa.Integer(), nullable=True),
        sa.Column('n_5s', sa.Integer(), nullable=True),
        sa.Column('software_version_id', sa.Integer(), nullable=True),
        sa.Column('modified_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('modified_by', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ['assembly_accession_id'],
            ['accession.accession_id'],
        ),
        sa.ForeignKeyConstraint(
            ['bin_type'],
            ['bin_type_dict.bin_type'],
        ),
        sa.ForeignKeyConstraint(
            ['biosample_accession_id'],
            ['accession.accession_id'],
        ),
        sa.ForeignKeyConstraint(
            ['metagenome_id'],
            ['metagenome.metagenome_id'],
        ),
        sa.ForeignKeyConstraint(
            ['modified_by'],
            ['user.id'],
        ),
        sa.ForeignKeyConstraint(
            ['software_version_id'],
            ['software_version.software_version_id'],
        ),
        sa.ForeignKeyConstraint(
            ['species_id'],
            ['species.species_id'],
        ),
        sa.PrimaryKeyConstraint('metagenome_bin_id'),
    )
    op.create_table(
        'metagenome_bin_status',
        sa.Column('metagenome_bin_status_id', sa.Integer(), nullable=False),
        sa.Column('metagenome_bin_id', sa.String(), nullable=False),
        sa.Column('status_type_id', sa.String(), nullable=False),
        sa.Column('status_time', sa.DateTime(timezone=True), nullable=False),
        sa.Column('modified_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('modified_by', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ['metagenome_bin_id'],
            ['metagenome_bin.metagenome_bin_id'],
        ),
        sa.ForeignKeyConstraint(
            ['modified_by'],
            ['user.id'],
        ),
        sa.ForeignKeyConstraint(
            ['status_type_id'],
            ['metagenome_status_type.status_type_id'],
        ),
        sa.PrimaryKeyConstraint('metagenome_bin_status_id'),
    )
    op.create_foreign_key(
        'metagenome_bin_metagenome_bin_status_id_fkey',
        'metagenome_bin',
        'metagenome_bin_status',
        ['metagenome_bin_status_id'],
        ['metagenome_bin_status_id'],
    )

    op.create_table(
        'taxon_request_status_dict',
        sa.Column('request_status', sa.String(), nullable=False),
        sa.Column('description', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('request_status'),
    )
    op.create_table(
        'edit_metagenome',
        sa.Column('edit_id', sa.Integer(), nullable=False),
        sa.Column('metagenome_id', sa.String(), nullable=False),
        sa.Column('changes', postgresql.JSONB(astext_type=sa.Text()), nullable=False),
        sa.Column('modified_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('modified_by', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ['metagenome_id'],
            ['metagenome.metagenome_id'],
        ),
        sa.ForeignKeyConstraint(
            ['modified_by'],
            ['user.id'],
        ),
        sa.PrimaryKeyConstraint('edit_id'),
        sa.UniqueConstraint('modified_at', 'metagenome_id'),
    )
    op.create_table(
        'edit_metagenome_bin',
        sa.Column('edit_id', sa.Integer(), nullable=False),
        sa.Column('metagenome_bin_id', sa.String(), nullable=False),
        sa.Column('changes', postgresql.JSONB(astext_type=sa.Text()), nullable=False),
        sa.Column('modified_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('modified_by', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ['metagenome_bin_id'],
            ['metagenome_bin.metagenome_bin_id'],
        ),
        sa.ForeignKeyConstraint(
            ['modified_by'],
            ['user.id'],
        ),
        sa.PrimaryKeyConstraint('edit_id'),
        sa.UniqueConstraint('modified_at', 'metagenome_bin_id'),
    )
    op.create_table(
        'edit_metagenome_bin_status',
        sa.Column('edit_id', sa.Integer(), nullable=False),
        sa.Column('metagenome_bin_status_id', sa.Integer(), nullable=False),
        sa.Column('changes', postgresql.JSONB(astext_type=sa.Text()), nullable=False),
        sa.Column('modified_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('modified_by', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ['metagenome_bin_status_id'],
            ['metagenome_bin_status.metagenome_bin_status_id'],
        ),
        sa.ForeignKeyConstraint(
            ['modified_by'],
            ['user.id'],
        ),
        sa.PrimaryKeyConstraint('edit_id'),
        sa.UniqueConstraint('modified_at', 'metagenome_bin_status_id'),
    )
    op.create_table(
        'edit_metagenome_status',
        sa.Column('edit_id', sa.Integer(), nullable=False),
        sa.Column('metagenome_status_id', sa.Integer(), nullable=False),
        sa.Column('changes', postgresql.JSONB(astext_type=sa.Text()), nullable=False),
        sa.Column('modified_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('modified_by', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ['metagenome_status_id'],
            ['metagenome_status.metagenome_status_id'],
        ),
        sa.ForeignKeyConstraint(
            ['modified_by'],
            ['user.id'],
        ),
        sa.PrimaryKeyConstraint('edit_id'),
        sa.UniqueConstraint('modified_at', 'metagenome_status_id'),
    )
    op.create_table(
        'taxon_request',
        sa.Column('species_id', sa.String(), nullable=False),
        sa.Column('request_status', sa.String(), nullable=True),
        sa.Column('taxon_id', sa.Integer(), nullable=True),
        sa.Column('modified_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('modified_by', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ['modified_by'],
            ['user.id'],
        ),
        sa.ForeignKeyConstraint(
            ['request_status'],
            ['taxon_request_status_dict.request_status'],
        ),
        sa.PrimaryKeyConstraint('species_id'),
    )
    op.create_index(
        op.f('ix_taxon_request_taxon_id'), 'taxon_request', ['taxon_id'], unique=False
    )
    op.create_table(
        'edit_taxon_request',
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
            ['taxon_request.species_id'],
        ),
        sa.PrimaryKeyConstraint('edit_id'),
        sa.UniqueConstraint('modified_at', 'species_id'),
    )
    op.create_index(op.f('ix_file_name'), 'file', ['name'], unique=False)


def downgrade() -> None:
    pass
