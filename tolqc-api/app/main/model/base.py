# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

db = SQLAlchemy()


class ExtraFieldsNotPermittedException(Exception):
    def __init__(self, ext_fields):
        self._ext_fields = ext_fields

    def get_extra_fields_str(self):
        return ', '.join(self._ext_fields.keys())


class InstanceDoesNotExistException(Exception):
    def __init__(self, id):
        self.id = id


class ExtColumn(db.Column):
    def __init__(self, **kwargs):
        super().__init__(
            db.JSON,
            nullable=True,
            default={},
            **kwargs
        )


class Base(db.Model):
    """The base model class. Its primary key must be called
    id. Do not call anything other than an ExtColumn 'ext'."""
    __abstract__ = True

    def to_dict(cls):
        return {"override": "this"}

    def add(self):
        db.session.add(self)

    def update_ext(self, ext_data_changes):
        if not self.has_ext_column():
            raise ExtraFieldsNotPermittedException(
                ext_data_changes
            )
        ext_data = {**self.ext}
        for key, item in ext_data_changes.items():
            if item is None:
                if key in ext_data:
                    del ext_data[key]
            else:
                ext_data[key] = item
        self.ext = ext_data

    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)

    def delete(self):
        db.session.delete(self)
        self.commit()

    @classmethod
    def commit(cls):
        db.session.commit()

    def save(self):
        try:
            self.add()
            self.commit()
        except IntegrityError as e:
            self.rollback()
            raise(e)

    @classmethod
    def find_bulk(cls, **kwargs):
        return db.session.query(cls).limit(50).all()

    @staticmethod
    def rollback():
        db.session.rollback()

    @staticmethod
    def bulk_add(data):
        db.session.add_all(data)
        db.session.commit()

    @classmethod
    def find_by_id(cls, _id):
        instance = cls.query.filter_by(id=_id).one_or_none()
        if instance is None:
            raise InstanceDoesNotExistException(_id)
        return instance

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

    @classmethod
    def has_creation_details(cls):
        return False
