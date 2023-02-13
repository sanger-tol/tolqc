"""drop old histories

Revision ID: a998db198ad4
Revises: 4c93e179786d
Create Date: 2022-07-01 10:54:38.090399

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.engine.reflection import Inspector


# revision identifiers, used by Alembic.
revision = 'a998db198ad4'
down_revision = '4c93e179786d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # get list of tables
    conn = op.get_bind()
    inspector = Inspector.from_engine(conn)
    tables = inspector.get_table_names()

    for table in tables:
        # for all tables with a history column
        column_names = [
            column_dict['name'] for column_dict in inspector.get_columns(table)
        ]
        if 'history' in column_names:
            # remove all history
            conn.execute(sa.text(
                f'''
                UPDATE "{table}"
                SET history='[]'::json;
                '''
            ))

def downgrade() -> None:
    pass
