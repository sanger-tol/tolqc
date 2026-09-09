"""set_relationship_action

Revision ID: 0aa08285a0ab
Revises: 1a082d130527
Create Date: 2026-09-09 11:04:16.455377

"""
from alembic import op


# revision identifiers, used by Alembic.
revision = '0aa08285a0ab'
down_revision = '1a082d130527'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute(
        """
        INSERT INTO action (name, object_type, class_name, params)
        VALUES ('SetRelationshipAction', 'data', 'SetRelationshipAction', '{}')
        """
    )

    op.execute(
        """
        INSERT INTO role_action (action_id, role_id)
        VALUES (7, 1)
        """
    )


def downgrade() -> None:
    pass
