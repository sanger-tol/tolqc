"""update_user_table

Revision ID: 81bf8897c7c6
Revises: c8babd30b9f1
Create Date: 2025-10-13 13:04:28.183333

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '81bf8897c7c6'
down_revision = 'c8babd30b9f1'
branch_labels = None
depends_on = None


def upgrade() -> None:

    # Create oidc_state table
    op.create_table(
        'oidc_state',
        sa.Column('id', sa.String, primary_key=True),
        sa.Column('created_at', sa.DateTime, nullable=False),
    )
    # Create role_binding table
    op.create_table(
        'role_binding',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('user_id', sa.Integer, nullable=False),
        sa.Column('role_id', sa.Integer, nullable=False),
        sa.ForeignKeyConstraint(
            ('user_id',),
            ['user.id'],
        ),
        sa.ForeignKeyConstraint(
            ('role_id',),
            ['role.id'],
        ),
    )

    # Update user table
    op.drop_constraint('user_email_key', 'user')
    op.alter_column('user', 'email', new_column_name='oidc_id')
    op.create_unique_constraint(None, 'user', ['oidc_id'])

    # Update role table
    op.add_column('role', sa.Column('name', sa.String, unique=True, nullable=False))
    op.drop_constraint('role_user_id_fkey', 'role')
    op.drop_column('role', 'user_id')

    # Update token table
    op.add_column('token', sa.Column('created_at', sa.DateTime, nullable=True))
    op.add_column('token', sa.Column('expires_at', sa.DateTime, nullable=True))
    for sql in [
        """
        UPDATE token
        SET created_at = CURRENT_TIMESTAMP
        WHERE created_at IS NULL
        """,
        """
        UPDATE token
        SET expires_at = '2030-01-01 00:00:01'
        WHERE expires_at IS NULL
        """
    ]:
        op.execute(sa.text(sql))
    op.alter_column('token', 'created_at', nullable=False)
    op.alter_column('token', 'expires_at', nullable=False)

def downgrade() -> None:

    # Drop oidc_state table
    op.drop_table('oidc_state')

    # Drop role_binding table
    op.drop_table('role_binding')

    # Revert user table changes
    op.drop_constraint('user_oidc_id_key', table_name='user')
    op.alter_column('user', 'oidc_id', new_column_name='email')
    op.create_unique_constraint(None, 'user', ['email'])

    # Revert role table changes
    op.drop_column('role', 'name')
    op.add_column('role', sa.Column('user_id', sa.Integer, nullable=True))
    op.create_foreign_key('role_user_id_fkey', 'role', 'user', ['user_id'], ['id'])

    # Revert token table changes
    op.drop_column('token', 'created_at')
    op.drop_column('token', 'expires_at')
    
