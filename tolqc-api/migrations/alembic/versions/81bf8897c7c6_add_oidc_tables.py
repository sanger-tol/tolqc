"""Tables for new authorisation system

Revision ID: 81bf8897c7c6
Revises: 403ee1086294
Create Date: 2025-11-17 13:35:58.697694

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '81bf8897c7c6'
down_revision = '403ee1086294'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Legacy tables which may exist
    op.drop_table('auth', if_exists=True)
    op.drop_table('role', if_exists=True)
    op.drop_table('state', if_exists=True)

    # Create oidc_state table
    op.create_table(
        'oidc_state',
        sa.Column('id', sa.String(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
    )

    # Create the role table
    op.create_table(
        'role',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('name'),
    )

    # Create role_binding table
    op.create_table(
        'role_binding',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('role_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ['role_id'],
            ['role.id'],
        ),
        sa.ForeignKeyConstraint(
            ['user_id'],
            ['user.id'],
        ),
        sa.PrimaryKeyConstraint('id'),
    )

    # Update user table
    op.add_column('user', sa.Column('full_name', sa.String(), nullable=True))
    op.create_unique_constraint(None, 'user', ['name'])
    for sql in [
        """
        UPDATE "user" SET full_name = name WHERE full_name IS NULL
        """,
        """
        UPDATE "user" SET name = split_part(email, '@sanger.ac.uk', 1)
        """,
        r"""
        UPDATE "user" SET organisation = 'Wellcome Sanger Institute'
        WHERE email ~ '@sanger\.ac\.uk$'
        """,
        """
        INSERT INTO role (name)
        VALUES ('editor')
        """,
        # Populate 'editor' role from users who are 'registered'
        """
        INSERT INTO role_binding (user_id, role_id)
        SELECT u.id, r.id
        FROM "user" AS u
        JOIN role AS r
          ON r.name = 'editor'
        WHERE u.registered = 't'
        """
    ]:
        op.execute(sa.text(sql))

    op.drop_column('user', 'registered')

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
    pass
