# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from datetime import datetime

from sqlalchemy import TIMESTAMP
from sqlalchemy.orm import (
    Mapped,
    declared_attr,
    mapped_column,
)

from tol.sql import model_base

Base = model_base()
Base.registry.type_annotation_map[datetime] = TIMESTAMP(timezone=True)


class LogBase(Base.Log):
    __abstract__ = True

    @declared_attr
    def modified_at(self) -> Mapped[datetime]:
        """
        Redeclared here so that timezone is added
        """
        return mapped_column(nullable=True)
