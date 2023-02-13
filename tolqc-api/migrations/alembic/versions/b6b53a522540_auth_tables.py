"""auth tables

Revision ID: b6b53a522540
Revises: c8b2d6322dbd
Create Date: 2023-01-19 21:14:58.936589

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b6b53a522540'
down_revision = 'c8b2d6322dbd'
branch_labels = None
depends_on = None


def upgrade() -> None:
    connection = op.get_bind()
    connection.execute(sa.text("""
        ALTER TABLE public.user DROP COLUMN token;
        CREATE SEQUENCE public.auth_id_seq
            INCREMENT 1
            START 1
            MINVALUE 1
            MAXVALUE 2147483647
            CACHE 1;
        CREATE TABLE IF NOT EXISTS public.auth
        (
            id integer NOT NULL DEFAULT nextval('auth_id_seq'::regclass),
            user_id integer,
            token character varying COLLATE pg_catalog."default" NOT NULL,
            created_at timestamp without time zone NOT NULL,
            expires_at timestamp without time zone NOT NULL,
            CONSTRAINT auth_pkey PRIMARY KEY (id),
            CONSTRAINT auth_token_key UNIQUE (token),
            CONSTRAINT auth_user_id_fkey FOREIGN KEY (user_id)
                REFERENCES public."user" (id) MATCH SIMPLE
                ON UPDATE NO ACTION
                ON DELETE NO ACTION
        )
        WITH (
            OIDS = FALSE
        )
        TABLESPACE pg_default;
        CREATE TABLE IF NOT EXISTS public.state
        (
            state character varying COLLATE pg_catalog."default" NOT NULL,
            created_at timestamp without time zone NOT NULL,
            CONSTRAINT state_pkey PRIMARY KEY (state)
        )
        WITH (
            OIDS = FALSE
        )
        TABLESPACE pg_default;

        INSERT INTO auth(user_id, token, created_at, expires_at)
        SELECT id, api_key, NOW(), '2025-01-01 00:00:00'
        FROM "user"
        WHERE api_key is not null;

        ALTER TABLE public.user DROP COLUMN api_key;
        """))



def downgrade() -> None:
    pass
