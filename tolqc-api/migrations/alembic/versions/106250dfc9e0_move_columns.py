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
    op.add_column('run', sa.Column('start_date', sa.DateTime(), nullable=True))
    op.add_column('run', sa.Column('qc_date', sa.DateTime(), nullable=True))
    connection = op.get_bind()
    connection.execute(sa.text("""
        UPDATE run set date = data.date FROM data where data.run_id = run.id;
    """))
    op.drop_column('data', 'date')

    connection.execute(sa.text("""
        INSERT INTO "user"(id, name, email, organisation)
        VALUES (1, 'ToL Platforms', 'tol-platforms@sanger.ac.uk', 'Wellcome Sanger Institute');
    """))

    op.rename_table('track_config', 'study')

    op.add_column('study', sa.Column('project_id', sa.Integer, nullable=True))

    connection.execute(sa.text("""
        INSERT INTO project(hierarchy_name, created_at, created_by, last_modified_at, last_modified_by, history)
        SELECT DISTINCT hierarchy_name, CURRENT_TIMESTAMP, 1, CURRENT_TIMESTAMP, 1, '{}'::jsonb
        FROM study
        ORDER BY hierarchy_name
        
    """))

    connection.execute(sa.text("""
       UPDATE study set project_id = project.id from project
        WHERE study.hierarchy_name = project.hierarchy_name;
    """))
    op.alter_column('study', 'project_id', nullable=False)
    op.create_foreign_key(None, 'study', 'project', ['project_id'], ['id'])
    op.drop_column('study', 'hierarchy_name')

    op.drop_table('H')
    op.drop_table('G')
    op.drop_table('F')
    op.drop_table('E')
    op.drop_table('D')
    op.drop_table('C')
    op.drop_table('B')
    op.drop_table('A')

def downgrade() -> None:
    pass
