# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from sqlalchemy.ext.declarative import declared_attr

from .base import Base, db


class CreationLogMixin(object):
    @declared_attr
    def created_at(cls):
        return db.Column(db.DateTime, nullable=False, default=db.func.now())

    @declared_attr
    def created_by(cls):
        return db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    @declared_attr
    def history(cls):
        return db.Column(db.String)

    @declared_attr
    def ext(cls):
        return db.Column(db.String)


class CreationLogBase(Base, CreationLogMixin):
    __abstract__ = True

    @classmethod
    def has_creation_details(cls):
        return True
