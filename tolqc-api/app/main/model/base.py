# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from sqlalchemy import and_
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from sqlalchemy.inspection import inspect

db = SQLAlchemy()


class ExtraFieldsNotPermittedException(Exception):
    def __init__(self, ext_fields):
        self._ext_fields = ext_fields

    def get_extra_fields_str(self):
        return ', '.join(self._ext_fields.keys())


class InstanceDoesNotExistException(Exception):
    def __init__(self, id):
        self.id = id


class BadFilterKeyException(Exception):
    def __init__(self, filter_key):
        self.message = f"The filter key '{filter_key}' is invalid."
        super().__init__(self.message)


def raise_bad_filter_key_exception(filter_key):
    raise BadFilterKeyException(filter_key)


class ExtColumn(db.Column):
    def __init__(self, **kwargs):
        super().__init__(
            db.JSON,
            nullable=False,
            default={},
            **kwargs
        )


class Base(db.Model):
    """The base model class:
    - Its primary key must be called id.
    - Do not call anything other than an ExtColumn 'ext'.
    - The declared tablename will be the HTTP endpoint stem
        - It should be plural, e.g. centres
    """
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
        try:
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
            raise(e)

    def save(self):
        self.add()
        self.commit()

    @classmethod
    def _get_eq_filter_terms(cls, eq_filters):
        if not eq_filters:
            return None
        return [
            getattr(
                cls,
                filter_key,
                lambda: raise_bad_filter_key_exception(
                    filter_key
                )) == filter_value
            for (filter_key, filter_value)
            in eq_filters.items()
        ]

    @classmethod
    def _get_find_bulk_query(cls, eq_filters):
        eq_filter_terms = cls._get_eq_filter_terms(eq_filters)
        query = db.session.query(cls)
        if eq_filter_terms is not None:
            query = query.filter(and_(*eq_filter_terms))
        return query

    @classmethod
    def _get_result_page(cls, query, page):
        return query.limit(50).all()

    @classmethod
    def find_bulk(cls, page=1, eq_filters={}):
        query = cls._get_find_bulk_query(eq_filters)
        return cls._get_result_page(query, page)

    @staticmethod
    def rollback():
        db.session.rollback()

    @staticmethod
    def bulk_add(data):
        db.session.add_all(data)
        db.session.commit()

    @classmethod
    def find_by_id(cls, id_):
        instance = cls.query.filter_by(id=id_).one_or_none()
        if instance is None:
            raise InstanceDoesNotExistException(id_)
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

    @classmethod
    def get_foreign_key_column_names(cls):
        return [
            c.name for c in cls._get_columns()
            if c.foreign_keys
        ]

    @classmethod
    def get_relationship_from_foreign_key(cls, column_name):
        """Returns a pair:
        - The target table's name
        - The name of the target column on the target table
        """
        # TODO make this support composite/compound keys
        foreign_key = list(cls.__table__.columns[column_name].foreign_keys)[0]
        target_table, target_column = foreign_key.target_fullname.split('.')
        return target_table, target_column

    @classmethod
    def get_relationships_dict(cls):
        return inspect(cls).relationships.items()
