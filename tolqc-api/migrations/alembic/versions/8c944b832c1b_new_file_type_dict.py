"""New file_type_dict

Revision ID: 8c944b832c1b
Revises: 2871303688df
Create Date: 2025-04-30 15:19:58.147941

"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '8c944b832c1b'
down_revision = '2871303688df'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'file_type_dict',
        sa.Column('file_type', sa.String(), nullable=False),
        sa.Column('description', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('file_type'),
    )
    op.add_column('file', sa.Column('file_type', sa.String(), nullable=True))
    op.create_foreign_key(None, 'file', 'file_type_dict', ['file_type'], ['file_type'])

    for sql in [
        """
        INSERT INTO file_type_dict(file_type, description)
        VALUES ('BAM', 'Binary Alignment Map')
          , ('CRAM', 'Compressed Reference-oriented Alignment Map')
          , ('BNX', 'BioNano BNX')
          , ('CMAP', 'BioNano CMAP')
        """,
        r"""
        UPDATE file
        SET name = (regexp_match(remote_path, '([^/]+)$'))[1]
        WHERE name IS NULL
        """,
        r"""
        UPDATE file
        SET file_type = upper(
          (regexp_match(remote_path, '\.(\w+)(\.gz)?$'))[1]
        )
        WHERE file_type IS NULL
        """,
    ]:
        op.execute(sa.text(sql))


def downgrade() -> None:
    pass
