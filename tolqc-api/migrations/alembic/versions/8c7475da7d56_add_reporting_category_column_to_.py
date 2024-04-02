"""add reporting_category column to library_type

Revision ID: 8c7475da7d56
Revises: b2e9cff5f865
Create Date: 2024-04-02 12:09:25.644960

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8c7475da7d56'
down_revision = 'b2e9cff5f865'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('library_type',
        sa.Column('reporting_category', sa.String(), nullable=True)
    )
    op.execute("UPDATE library_type SET reporting_category = 'rnaseq' "
               "WHERE library_type_id IN ("
               "'RNA PolyA',"
               "'RNA-seq dUTP eukaryotic',"
               "'RNA-seq dUTP prokaryotic',"
               "'Small RNA (miRNA)'"
               ")")
    op.execute("UPDATE library_type SET reporting_category = 'pacbio' "
               "WHERE library_type_id IN ("
               "'PacBio - HiFi',"
               "'PacBio - HiFi (Microbial)',"
               "'PacBio - HiFi (ULI)'"
               ")")
    op.execute("UPDATE library_type SET reporting_category = 'hic' "
               "WHERE library_type_id IN ("
               "'Hi-C',"
               "'Hi-C - Arima v1',"
               "'Hi-C - Arima v2',"
               "'Hi-C - Dovetail',"
               "'Hi-C - OmniC',"
               "'Hi-C - Qiagen'"
               ")")
    op.execute("UPDATE library_type SET reporting_category = 'hic' "
               "WHERE library_type_id IN ("
               "'Hi-C',"
               "'Hi-C - Arima v1',"
               "'Hi-C - Arima v2',"
               "'Hi-C - Dovetail',"
               "'Hi-C - OmniC',"
               "'Hi-C - Qiagen'"
               ")")


def downgrade() -> None:
    op.drop_column('library_type', 'reporting_category')
