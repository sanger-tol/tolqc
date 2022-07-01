# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from datetime import datetime
from sqlalchemy.ext.declarative import declared_attr

from .base import Base, db


class LogMixin(object):
    @declared_attr
    def created_at(cls):
        return db.Column(db.DateTime, nullable=False, default=db.func.now())

    @declared_attr
    def created_by(cls):
        return db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    @declared_attr
    def last_modified_at(cls):
        return db.Column(db.DateTime, nullable=False, default=db.func.now())

    @declared_attr
    def last_modified_by(cls):
        return db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    @declared_attr
    def history(cls):
        return db.Column(db.JSON, nullable=False, default=[])


class LogBase(Base, LogMixin):
    """Logs all three of:
    - creation details
    - last modification details
    - all previous modifcation detail snapshots (in history)"""

    __abstract__ = True

    @classmethod
    def setup(cls):
        cls._set_excluded_columns_in_history()
        super().setup()

    @classmethod
    def has_log_details(cls):
        return True

    @classmethod
    def _set_excluded_columns_in_history(cls):
        base_excludes = ['history', 'created_at', 'creator']
        if not hasattr(cls, 'Meta'):
            cls._excluded_columns_in_history = base_excludes
        else:
            cls._excluded_columns_in_history = base_excludes + list(
                getattr(cls.Meta, 'exclude_columns_in_history', [])
            )

    def save_update(self, user_id=None):
        self.last_modified_by = user_id
        self.last_modified_at = datetime.now()
        super().save_update()

    def save_create(self, user_id=None):
        self.created_by = user_id
        self.last_modified_by = user_id
        super().save_create()

    def _get_column_excluding_schema(self, schema_instance):
        schema_class = schema_instance.__class__
        return schema_class(
            exclude=self._excluded_columns_in_history
        )

    def _get_history_entry(self, schema):
        column_excluding_schema = self._get_column_excluding_schema(
            schema
        )
        return column_excluding_schema.dump(self)

    def _update_history(self, schema):
        old_history = [*self.history]
        self.history = old_history + [self._get_history_entry(schema)]

    def update(self, *args, schema=None, **kwargs):
        self._update_history(schema)
        super().update(*args, **kwargs)
