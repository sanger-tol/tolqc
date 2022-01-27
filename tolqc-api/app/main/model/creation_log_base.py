# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from datetime import datetime
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
        return db.Column(db.JSON, nullable=False)


class CreationLogBase(Base, CreationLogMixin):
    __abstract__ = True

    @classmethod
    def has_creation_details(cls):
        return True

    @classmethod
    def _get_excluded_columns_in_history(cls):
        #TODO test that this works in a CreationLogBase inherited test model
        base_excludes = ['id', 'history', 'created_at', 'created_by']
        if not hasattr(cls, 'Meta'):
            return base_excludes
        #TODO test that id does not appear in history
        return base_excludes + list(
            getattr(cls.Meta, 'exclude_columns_in_history', [])
        )

    def post_update(self, user_id):
        #TODO check that datetime's don't break dumping of history
        #maybe set a dump method that converts to string??
        self.last_modified_by = user_id
        self.last_modified_at = datetime.now()

    def save_create(self, user_id=None):
        self.created_by = user_id
        self.last_modified_by = user_id
        now = datetime.now()
        self.created_at = now
        self.last_modified_at = now
        self._create_history_array()
        super().save_create()

    def _get_history_entry(self):
        return self.to_dict(
            exclude_column_names=self._get_excluded_columns_in_history()
        )

    def _create_history_array(self):
        self.history = [self._get_history_entry()]

    def _update_history(self):
        self.history.append(self._get_history_entry())

    def update(self, *args, **kwargs):
        self._update_history()
        super().update(*args, **kwargs)
