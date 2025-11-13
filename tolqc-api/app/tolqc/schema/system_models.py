# SPDX-FileCopyrightText: 2024 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from __future__ import annotations

from sqlalchemy import (
    DateTime,
    Float,
    Integer,
    String,
)
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, declared_attr, mapped_column, relationship


from .base import LogBase


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
