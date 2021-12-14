# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .base import Base, db
from sqlalchemy.ext.declarative import declared_attr
from .tolqc_user import get_user_id


class SubBase(Base):
    __abstract__ = True
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.now())

    @declared_attr
    def created_by(cls):
        return db.Column(db.Integer, db.ForeignKey('user.id'),
                         nullable=False, default=get_user_id)
