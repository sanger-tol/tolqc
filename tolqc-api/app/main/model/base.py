# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from datetime import datetime
from sqlalchemy import and_
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from sqlalchemy.inspection import inspect


PAGE_SIZE = 20


db = SQLAlchemy()


class BadParameterException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


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
            getattr(cls, filter_key) == filter_value
            for (filter_key, filter_value)
            in cls._preprocess_filters(eq_filters).items()
        ]

    @classmethod
    def _get_find_bulk_query(cls, eq_filters):
        eq_filter_terms = cls._get_eq_filter_terms(eq_filters)
        query = db.session.query(cls)
        if eq_filter_terms is not None:
            query = query.filter(and_(*eq_filter_terms))
        return query

    @classmethod
    def _preprocess_page(cls, page):
        if not page:
            return None
        try:
            page = int(page)
        except ValueError:
            raise BadParameterException(
                "The page number must be an integer."
            )
        if page < 1:
            raise BadParameterException(
                "The page number must be 1 or greater."
            )
        return page

    @classmethod
    def _get_results_page(cls, query, page):
        #TODO test for off by one errors. E.g. insert 47 results and look on page 3 for just 7
        page = cls._preprocess_page(page)
        if page is not None:
            query = query.offset((page - 1) * PAGE_SIZE)
        return query.limit(PAGE_SIZE).all()

    @classmethod
    def find_bulk(cls, page, eq_filters):
        query = cls._get_find_bulk_query(eq_filters)
        return cls._get_results_page(query, page)

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

    @classmethod
    def _filter_value_is_float(cls, filter_value):
        try:
            float(filter_value)
            return True
        except ValueError:
            return False

    #TODO test all of these filter value types
    @classmethod
    def _filter_value_is_datetime(cls, filter_value):
        try:
            datetime.strptime(filter_value)
            return True
        except ValueError:
            return False

    @classmethod
    def _filter_value_is_delimited_by(cls, filter_value, delimiter):
        return (
            filter_value.startswith(delimiter) and
            filter_value.endswith(delimiter)
        )

    @classmethod
    def _filter_value_is_delimited_string(cls, filter_value):
        return (
            cls._filter_value_is_delimited_by(filter_value, '"') or
            cls._filter_value_is_delimited_by(filter_value, "'")
        )

    @classmethod
    def _filter_value_is_bool(cls, filter_value):
        return filter_value.lower() in ['true', 'false']

    @classmethod
    def _preprocess_filter_value(cls, filter_key, filter_value):
        if getattr(cls, filter_key, None) is None:
            raise BadParameterException(
                f"The filter key '{filter_key}' is invalid."
            )
        python_type = cls.get_column_python_type(filter_key)
        if python_type == str:
            if not cls._filter_value_is_delimited_string(filter_value):
                raise BadParameterException(
                    f"The string filter value '{filter_value}' must be surrounded "
                    "by quotation marks (either ' or \")"
                )
            # strip surrounding quotes
            return filter_value[1:-1]
        if python_type == int and not filter_value.isdigit():
            raise BadParameterException(
                f"The filter value '{filter_value}' must be an integer."
            )
        if python_type == float and not cls._filter_value_is_float(filter_value):
            raise BadParameterException(
                f"The filter value '{filter_value}' must be a float (number)."
            )
        if python_type == datetime and not cls._filter_value_is_datetime(filter_value):
            raise BadParameterException(
                f"The filter value '{filter_value}' must be a valid datetime."
            )
        if python_type == bool:
            if not cls._filter_value_is_bool(filter_value):
                raise BadParameterException(
                    f"The filter value '{filter_value}' must be a boolean"
                )
            # convert to boolean
            return filter_value.lower() == 'true'
        # nothing needs to change, return unmodified filter value
        return filter_value

    @classmethod
    def _preprocess_filters(cls, eq_filters):
        if not eq_filters:
            return None
        if cls.has_ext_column() and 'ext' in eq_filters.keys():
            raise BadParameterException(
                f"This API cannot filter against 'extra' columns."
            )
        return {
            filter_key: cls._preprocess_filter_value(filter_key, filter_value)
            for (filter_key, filter_value)
            in eq_filters.items()
        }
