# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .base import Base, db, populate_once


class TolqcCentre(Base):
    __tablename__ = "centre"

    @populate_once
    @classmethod
    def populate_columns(cls):
        cls.add_column("centre_id", db.Integer(),
                       in_schema=False, primary_key=True)
        cls.add_column("name", db.String())
        cls.add_column("hierarchy_name", db.String())

TolqcCentre.populate_columns()
