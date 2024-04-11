# SPDX-FileCopyrightText: 2024 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from __future__ import annotations

from typing import Optional

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, Session, mapped_column, relationship

from tolqc.model import Base


class User(Base):

    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(  # noqa: A003
        primary_key=True,
        autoincrement=True
    )

    email: Mapped[str] = mapped_column(
        nullable=False
    )

    name: Mapped[str] = mapped_column(
        nullable=False
    )

    organisation: Mapped[str] = mapped_column(
        nullable=True
    )

    registered: Mapped[bool] = mapped_column(
        nullable=False,
        default=False
    )

    _tokens: Mapped[list['Token']] = relationship(
        back_populates='user'
    )

    @property
    def roles(self) -> list[str]:
        return [] if self.registered is False else ['registered']


class Token(Base):

    # this has to be prefixed with 'oidc_' for future compatbility
    __tablename__ = 'oidc_token'

    id: Mapped[int] = mapped_column(  # noqa: A003
        primary_key=True,
        autoincrement=True
    )

    token: Mapped[str] = mapped_column(
        nullable=False,
        unique=True
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey(User.id)
    )

    user = relationship(
        'User',
        back_populates='_tokens',
        foreign_keys=[user_id]
    )

    @classmethod
    def get(
        cls,
        sess: Session,
        token: str
    ) -> Optional[Token]:

        return sess.query(
            cls
        ).filter_by(
            token=token
        ).one_or_none()
