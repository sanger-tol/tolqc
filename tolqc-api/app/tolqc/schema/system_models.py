# SPDX-FileCopyrightText: 2024 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from __future__ import annotations

from sqlalchemy import (
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
)

from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, Session, mapped_column, relationship, declared_attr


from .base import Base, LogBase


class Metadata(LogBase):
    __tablename__ = 'metadata'

    @classmethod
    def get_id_column_name(cls):
        return 'name'

    name = mapped_column(String, primary_key=True)
    description = mapped_column(String)
    string_value = mapped_column(String)
    timestamp_value = mapped_column(DateTime(timezone=True))
    integer_value = mapped_column(Integer)
    float_value = mapped_column(Float)
    json_value = mapped_column(JSONB)

class UserMixin:

    @declared_attr
    def name(self) -> Mapped[str]:
        return mapped_column()

    @declared_attr
    def organisation(self) -> Mapped[str]:
        return mapped_column()

    @declared_attr
    def assigned_specimens(self) -> Mapped[list['Specimen']]:  # noqa F821
        return relationship(
            primaryjoin='User.id == Specimen.assigned_user_id',
            back_populates='assignee'
        )
    
    @declared_attr
    def assigned_assemblies(self) -> Mapped[list['Assembly']]:  # noqa F821
        return relationship(
            primaryjoin='User.id == Assembly.assigned_user_id',
            back_populates='assignee'
        )

    def get_userinfo_ext(self) -> dict[str, str]:
        """
        Augments the data on `/api/v2/auth/profile`
        """

        return {
            'name': self.name
        }
    

# class User(Base):
#     __tablename__ = 'user'

#     id: Mapped[int] = mapped_column(  # noqa: A003
#         primary_key=True, autoincrement=True
#     )
#     email: Mapped[str] = mapped_column(nullable=False)
#     name: Mapped[str] = mapped_column(nullable=False)
#     organisation: Mapped[str] = mapped_column(nullable=True)
#     registered: Mapped[bool] = mapped_column(nullable=False, default=False)

#     _tokens: Mapped[list[Token]] = relationship(back_populates='user')

#     @property
#     def roles(self) -> list[str]:
#         return [] if self.registered is False else ['registered']

#     assigned_specimens = relationship(
#         'Specimen',
#         primaryjoin='User.id == Specimen.assigned_user_id',
#         back_populates='assignee',
#     )
#     assigned_assemblies = relationship(
#         'Assembly',
#         primaryjoin='User.id == Assembly.assigned_user_id',
#         back_populates='assignee',
#     )


# class Token(Base):
#     __tablename__ = 'token'

#     id: Mapped[int] = mapped_column(  # noqa: A003
#         primary_key=True, autoincrement=True
#     )
#     token: Mapped[str] = mapped_column(nullable=False, unique=True)
#     user_id: Mapped[int] = mapped_column(ForeignKey(User.id))

#     user = relationship('User', back_populates='_tokens', foreign_keys=[user_id])

#     @classmethod
#     def get(cls, sess: Session, token: str) -> Token | None:
#         return sess.query(cls).filter_by(token=token).one_or_none()
