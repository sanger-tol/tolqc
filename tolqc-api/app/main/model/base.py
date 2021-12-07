# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class ExtraFieldsNotPermittedException(Exception):
    def __init__(self, ext_fields):
        self._ext_fields = ext_fields

    def get_extra_fields_str(self):
        return ', '.join(self._ext_fields.keys())


class Base(db.Model):
    """The base model class. Its primary key must be called
    id"""
    __abstract__ = True

    def to_dict(cls):
        return {"override": "this"}

    def add(self):
        db.session.add(self)
    
    def _get_ext_data(self):
        if self.ext is None:
            return {}
        return {**self.ext}
    
    def _set_ext_data_empty(self):
        if self.column_is_nullable('ext'):
            self.ext = None
        else:
            self.ext = {}
    
    def _set_ext_data(self, ext_data):
        if ext_data == {}:
            self._set_ext_data_empty()
        self.ext = ext_data

    def _update_ext(self, ext_data_changes):
        if not self.has_ext_column():
            raise ExtraFieldsNotPermittedException(
                ext_data_changes
            )
        ext_data = self._get_ext_data()
        for key, item in ext_data_changes.items():
            if item is None and ext_data[key]:
                del ext_data[key]
            else:
                ext_data[key] = item
        self._set_ext_data(ext_data)

    def update(self, data):
        for key, item in data.items():
            if key == 'ext':
                self._update_ext(item)
            else:
                setattr(self, key, item)

    def delete(self):
        db.session.delete(self)

    @classmethod
    def commit(cls):
        db.session.commit()

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def rollback():
        db.session.rollback()

    @staticmethod
    def bulk_update(data):
        db.session.add_all(data)
        db.session.commit()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).one_or_none()

    @classmethod
    def _get_columns(cls):
        return list(cls.__table__.c)

    @classmethod
    def get_nullable_column_names(cls):
        return [
            c.name for c in cls._get_columns()
            if c.nullable
        ]

    @classmethod
    def get_column_names(cls):
        return [c.name for c in cls._get_columns()]

    @classmethod
    def get_column_python_type(cls, column_name):
        column = getattr(cls, column_name)
        return column.type.python_type

    @classmethod
    def column_is_nullable(cls, column_name):
        return cls.__table__.columns[column_name].nullable

    @classmethod
    def has_ext_column(cls):
        return 'ext' in cls.get_column_names()
