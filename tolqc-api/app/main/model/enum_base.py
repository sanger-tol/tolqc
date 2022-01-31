# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .base import Base, db


class EnumBase(Base):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    description = db.Column(db.String(), nullable=True)

    @classmethod
    def is_enum_table(cls):
        return True

    @classmethod
    def get_enum_values(cls):
        query = db.session.query(cls)
        return [m.name for m in query.all()]
