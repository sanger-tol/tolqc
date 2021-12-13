# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from sqlalchemy.orm import defaultload
from .base import Base, db
from sqlalchemy.ext.declarative import declared_attr
from .tolqc_user import auth_user_id


class SubBase(Base):
    __abstract__ = True

    @declared_attr
    def created_by(cls):
        return db.Column(db.Integer, db.ForeignKey('user.id'),
                         nullable=False, default=auth_user_id)
