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
    def last_modified_at(cls):
        return db.Column(db.DateTime, nullable=False, default=db.func.now())

    @declared_attr
    def last_modified_by(cls):
        return db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    @declared_attr
    def history(cls):
        return db.Column(db.JSON, nullable=False, default={})


class CreationLogBase(Base, CreationLogMixin):
    __abstract__ = True

    @classmethod
    def has_creation_details(cls):
        return True

    @classmethod
    def _get_excluded_columns_in_history(cls):
        meta_class = getattr(cls, 'Meta', None)
        if meta_class is None:
            return []
        return list(getattr(cls.Meta, 'exclude_columns_in_history', []))
