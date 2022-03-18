# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from datetime import datetime
from sqlalchemy.ext.declarative import declared_attr

from .base import db


class LogMixin(object):
    """Logs all three of:
    - creation details
    - last modification details
    - all previous modifcation detail snapshots (in history)"""

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

    @classmethod
    def setup(cls):
        cls._set_excluded_columns_in_history()
        super(LogMixin, cls).setup()

    @classmethod
    def has_log_details(cls):
        return True

    @classmethod
    def _set_excluded_columns_in_history(cls):
        base_excludes = ['id', 'history', 'created_at', 'created_by']
        if not hasattr(cls, 'Meta'):
            cls._excluded_columns_in_history = base_excludes
        else:
            cls._excluded_columns_in_history = base_excludes + list(
                getattr(cls.Meta, 'exclude_columns_in_history', [])
            )

    def save_update(self, user_id=None):
        self.last_modified_by = user_id
        self.last_modified_at = datetime.now()
        super(LogMixin, self).save_update()

    def save_create(self, user_id=None):
        self.created_by = user_id
        self.last_modified_by = user_id
        super(LogMixin, self).save_create()

    @classmethod
    def _map_history_entry_key(cls, entry_key):
        mapping = {
            'last_modified_by': 'entered_by',
            'last_modified_at': 'entered_at'
        }
        return mapping.get(entry_key, entry_key)

    @classmethod
    def _map_history_entry_value(cls, entry_key, entry_value):
        if entry_key in cls.get_foreign_key_column_names():
            return str(entry_value)
        return entry_value

    def _get_history_entry(self):
        state_snapshot = self.to_dict(
            exclude_column_names=self._excluded_columns_in_history,
            convert_enums=False
        )
        return {
            self._map_history_entry_key(entry_key): self._map_history_entry_value(
                entry_key,
                entry_value
            )
            for (entry_key, entry_value)
            in state_snapshot.items()
        }

    def _update_history(self):
        old_history = [*self.history]
        self.history = old_history + [self._get_history_entry()]

    def update(self, *args, **kwargs):
        self._update_history()
        super(LogMixin, self).update(*args, **kwargs)
