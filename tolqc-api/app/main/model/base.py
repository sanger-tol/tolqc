# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

import dateutil.parser

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
    pass


class StemInstanceDoesNotExistException(Exception):
    """Used on 'related' endpoints"""
    pass


class ExtColumn(db.Column):
    def __init__(self, **kwargs):
        super().__init__(
            db.JSON,
            nullable=False,
            default={},
            **kwargs
        )


def setup_model(cls):
    cls.populate_target_table_dict()
    return cls


class Base(db.Model):
    """The base model class:
    - Its primary key must be called id.
    - Do not call anything other than an ExtColumn 'ext'.
    - The declared tablename will be the HTTP endpoint stem
        - It should be plural, e.g. centres
    """
    __abstract__ = True

    def to_dict(self, exclude_column_names=[]):
        return {
            column_name: getattr(self, column_name)
            for column_name
            in self.get_column_names()
            if column_name not in exclude_column_names
        }

    @classmethod
    def _get_excluded_columns_in_history(cls):
        meta_class = getattr(cls, 'Meta', None)
        if meta_class is None:
            return []
        return list(getattr(cls.Meta, 'exclude_columns_in_history', []))

    def _to_history_dict(self):
        return self.to_dict(self._get_excluded_columns_in_history())

    def add(self):
        db.session.add(self)

    def _update_ext(self, ext_data_changes):
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

    def update(self, data, ext=None):
        for key, item in data.items():
            setattr(self, key, item)
        if ext is not None:
            self._update_ext(ext)

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
    def _get_sort_by_column(cls, sort_by_column_name, ascending):
        sort_by_column = getattr(cls, sort_by_column_name, None)
        if sort_by_column is None:
            raise BadParameterException(
                f'The field "{sort_by_column_name}" does not exist.'
            )
        return sort_by_column if ascending else sort_by_column.desc()

    @classmethod
    def _sort_by_query(cls, query, sort_by):
        if sort_by is None:
            return query.order_by(cls.id)
        (sort_by_column_name, ascending) = sort_by
        sort_by_column = cls._get_sort_by_column(
            sort_by_column_name,
            ascending
        )
        return query.order_by(sort_by_column)

    @classmethod
    def _filter_query(cls, query, eq_filters):
        eq_filter_terms = cls._get_eq_filter_terms(eq_filters)
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
    def _paginate_query(cls, query, page):
        page = cls._preprocess_page(page)
        if page is not None:
            query = query.offset((page - 1) * PAGE_SIZE)
        return query.limit(PAGE_SIZE)

    @classmethod
    def _postprocess_bulk_find(cls, query, page=None, eq_filters=None, sort_by=None):
        query = cls._filter_query(query, eq_filters)
        query = cls._sort_by_query(query, sort_by)
        return cls._paginate_query(query, page)

    @classmethod
    def bulk_find(cls, **kwargs):
        query = db.session.query(cls)
        return cls._postprocess_bulk_find(query, **kwargs).all()

    @classmethod
    def bulk_find_on_relation_id(cls, relation_model, relation_id, **kwargs):
        cls._check_related_model_by_id_exists(relation_model, relation_id)
        foreign_key = cls._get_foreign_key_from_relation_model(relation_model)
        query = db.session.query(cls).filter(foreign_key == relation_id)
        return cls._postprocess_bulk_find(query, **kwargs).all()

    @classmethod
    def _check_related_model_by_id_exists(cls, relation_model, relation_id):
        related_instance = db.session.query(relation_model) \
                                     .filter_by(id=relation_id) \
                                     .one_or_none()
        if related_instance is None:
            raise StemInstanceDoesNotExistException()

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
            raise InstanceDoesNotExistException()
        return instance

    @classmethod
    def _get_target_table_from_column(cls, column):
        return list(column.foreign_keys)[0].target_fullname.split('.')[0]

    @classmethod
    def _get_all_table_names_many_to_one(cls):
        columns = cls._get_columns()
        return [
            cls._get_target_table_from_column(column)
            for column in columns
            if len(list(column.foreign_keys)) != 0
        ]

    @classmethod
    def populate_target_table_dict(cls):
        columns = list(cls.__table__.columns)
        # this doesn't support compound/composite keys
        foreign_keys_columns = [
            c for c in columns
            if len(c.foreign_keys) == 1
        ]
        cls.target_table_dict = {
            cls._get_target_table_from_column(column): column
            for column
            in foreign_keys_columns
        }

    @classmethod
    def _get_foreign_key_from_relation_model(cls, relation_model):
        return cls.target_table_dict[relation_model.__tablename__]

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
    def get_one_to_many_relationship_names(cls):
        relationships = inspect(cls).relationships.items()
        relationship_names = [r[0] for r in relationships]
        # exclude relationships for which this model is the many end
        return [
            r for r in relationship_names
            if r not in cls._get_all_table_names_many_to_one()
        ]

    @classmethod
    def get_target_table_column_from_foreign_key(cls, column_name):
        """Returns a pair:
        - The target table's name
        - The name of the target column on the target table
        """
        # TODO make this support composite/compound keys
        foreign_key = list(cls.__table__.columns[column_name].foreign_keys)[0]
        target_table, target_column = foreign_key.target_fullname.split('.')
        return target_table, target_column

    @classmethod
    def _filter_value_is_float(cls, filter_value):
        try:
            float(filter_value)
            return True
        except ValueError:
            return False

    @classmethod
    def _filter_value_is_datetime(cls, filter_value):
        try:
            dateutil.parser.parse(filter_value)
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
                "This API cannot filter against 'extra' columns."
            )
        return {
            filter_key: cls._preprocess_filter_value(filter_key, filter_value)
            for (filter_key, filter_value)
            in eq_filters.items()
        }
