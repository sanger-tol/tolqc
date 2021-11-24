# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .core_base import CoreBase, db
from sqlalchemy.ext.declarative import declared_attr


class Base(CoreBase):
    __abstract__ = True

    @declared_attr
    def created_by(cls):
        return db.Column(db.Integer, db.ForeignKey('user.user_id'),
                         nullable=False)
