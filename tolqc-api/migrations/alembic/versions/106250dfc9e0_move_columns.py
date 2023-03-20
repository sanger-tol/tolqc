"""Move columns

Revision ID: 106250dfc9e0
Revises: b6b53a522540
Create Date: 2023-03-20 14:08:52.885901

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '106250dfc9e0'
down_revision = 'b6b53a522540'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('run', sa.Column('date', sa.DateTime(), nullable=True))
    connection = op.get_bind()
    connection.execute(sa.text("""
        UPDATE run set date = data.date FROM data where data.run_id = run.id;
    """))
    op.drop_column('data', 'date')


def downgrade() -> None:
    pass
