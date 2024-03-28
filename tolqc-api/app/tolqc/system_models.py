# SPDX-FileCopyrightText: 2024 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from __future__ import annotations

from typing import Any, Optional

from sqlalchemy.orm import Mapped, Session, mapped_column

from tolqc.model import Base


def models_list() -> list[Any]:
    return [
        User
    ]


class User(Base):

    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(  # noqa
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

    token: Mapped[str] = mapped_column(
        nullable=True,
        unique=True
    )

    registered: Mapped[bool] = mapped_column(
        nullable=False,
        default=False
    )

    @property
    def roles(self) -> list[str]:
        return [] if self.registered is False else ['registered']

    @classmethod
    def get_by_token(
        cls,
        token: str,
        session: Session
    ) -> Optional[User]:

        return session.query(cls).filter_by(token=token).one_or_none()
