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
        return db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    @declared_attr
    def last_modified_at(cls):
        return db.Column(db.DateTime)

    @declared_attr
    def last_modified_by(cls):
        return db.Column(db.Integer, db.ForeignKey('users.id'))

    @declared_attr
    def history(cls):
        return db.Column(db.JSON, nullable=False, default=[])


class LogBase(Base, LogMixin):
    __abstract__ = True

    @classmethod
    def has_log_details(cls):
        return True

    @classmethod
    def _get_excluded_columns_in_history(cls):
        base_excludes = ['id', 'history', 'created_at', 'created_by']
        if not hasattr(cls, 'Meta'):
            return base_excludes
        return base_excludes + list(
            getattr(cls.Meta, 'exclude_columns_in_history', [])
        )

    def save_update(self, user_id=None):
        #TODO need to consider how to retry this if the SERIALIZABLE transcation fails
        self.last_modified_by = user_id
        self.last_modified_at = datetime.now()
        super().save_update()

    def save_create(self, user_id=None):
        self.created_by = user_id
        self.created_at = datetime.now()
        super().save_create()

    @classmethod
    def _map_history_entry_key(cls, entry_key):
        mapping = {
            'last_modified_by': 'modified_by',
            'last_modified_at': 'modified_at'
        }
        return mapping.get(entry_key, entry_key)

    def _get_history_entry(self):
        state_snapshot = self.to_dict(
            exclude_column_names=self._get_excluded_columns_in_history()
        )
        return {
            self._map_history_entry_key(entry_key): entry_value
            for (entry_key, entry_value)
            in state_snapshot.items()
        }

    def _update_history(self):
        old_history = [*self.history]
        self.history = old_history + [self._get_history_entry()]

    def update(self, *args, **kwargs):
        self._update_history()
        super().update(*args, **kwargs)
