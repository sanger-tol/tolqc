# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

import dateutil.parser
import json

from datetime import datetime
from sqlalchemy import and_
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from sqlalchemy.inspection import inspect


PAGE_SIZE = 20


def default_datetime_dump(value):
    if isinstance(value, datetime):
        return value.strftime('%Y-%m-%dT%H:%M:%S.%f')
    raise TypeError()


db = SQLAlchemy(
    engine_options={
        'json_serializer': lambda obj: json.dumps(obj, default=default_datetime_dump)
    }
)


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


class NamedEnumStemInstanceDoesNotExistException(Exception):
    """Used on 'related' endpoints concerning enum tables"""
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
    cls.setup()
    return cls


class Base(db.Model):
    """The base model class:
    - Its primary key must be called id.
    - Do not call anything other than an ExtColumn 'ext'.
    - The declared tablename will be the HTTP endpoint stem
        - It should be plural, e.g. centres
    """
    __abstract__ = True

    # a dict in which all inhertied classes are registered during setup
    model_registry_dict = {}

    def __init__(self, **data):
        converted_data = self._convert_enum_names_to_foreign_key_ids(data)
        return super().__init__(**converted_data)

    @classmethod
    def _convert_enum_names_to_foreign_key_ids(cls, data):
        """Converts enum_table:name pairs into foreign_key:id pairs"""
        enum_relationship_details = cls.get_enum_relationship_details()
        enum_relation_names = [
            r_model_name for (_, r_model_name) in enum_relationship_details
        ]
        foreign_key_names = [
            fkey_name for (fkey_name, _) in enum_relationship_details
        ]
        relation_model_name_pairs = [
            (
                r_model_name,
                data.get(r_model_name, None)
            )
            for r_model_name in enum_relation_names
        ]
        enum_foreign_key_id_dict = {
            f_key_name: cls.get_model_by_type(
                r_model_name
            ).get_id_from_name(enum_name)
            for (r_model_name, enum_name), f_key_name in zip(
                relation_model_name_pairs,
                foreign_key_names
            )
            if enum_name is not None
        }
        data = {**data, **enum_foreign_key_id_dict}
        return {
            key: pair for (key, pair) in data.items()
            if key not in enum_relation_names
        }

    @classmethod
    def _convert_foreign_key_ids_to_enum_names(cls, data):
        """Converts foreign_key:id pairs into enum_table:name pairs"""
        enum_relationship_details = cls.get_enum_relationship_details()
        enum_relation_names = [
            r_model_name for (_, r_model_name) in enum_relationship_details
        ]
        foreign_key_names = [
            fkey_name for (fkey_name, _) in enum_relationship_details
        ]
        foreign_key_ids = [
            data.get(foreign_key_name, None)
            for foreign_key_name in foreign_key_names
        ]
        relation_model_name_dict = {
            r_model_name: cls.get_relation_enum_name_by_id(
                r_model_name,
                id
                ) if id is not None else None
            for r_model_name, id in zip(
                enum_relation_names,
                foreign_key_ids,
            )
        }
        data = {**data, **relation_model_name_dict}
        return {
            key: pair for (key, pair) in data.items()
            if key not in foreign_key_names
        }

    @classmethod
    def setup(cls):
        cls._populate_target_table_dict()
        cls._register_model()

    def to_dict(self, exclude_column_names=[], convert_enums=True):
        dict_data = {
            column_name: getattr(self, column_name)
            for column_name
            in self.get_column_names()
            if column_name not in exclude_column_names
        }
        if not convert_enums:
            return dict_data
        return self._convert_foreign_key_ids_to_enum_names(dict_data)

    @classmethod
    def _register_model(cls):
        type_ = cls.__tablename__
        cls.model_registry_dict[type_] = cls

    @classmethod
    def get_model_by_type(cls, type_):
        return cls.model_registry_dict[type_]

    @classmethod
    def model_is_enum(cls, type_):
        model = cls.get_model_by_type(type_)
        return model.is_enum_table()

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

    def save_update(self, **kwargs):
        self.commit()

    def update(self, data, ext=None):
        converted_data = self._convert_enum_names_to_foreign_key_ids(data)
        for key, item in converted_data.items():
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

    def save_create(self, **kwargs):
        self.save()

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
    def _get_sort_by_non_enum(cls, query, sort_by_attribute, ascending):
        sort_by_column = cls._get_sort_by_column(
            sort_by_attribute,
            ascending
        )
        return query.order_by(sort_by_column)

    @classmethod
    def _get_sort_by_enum(cls, query, enum_name, ascending):
        enum_relation_model = cls.get_model_by_type(enum_name)
        enum_relationship = getattr(cls, enum_name)
        sort_by_column = enum_relation_model.name if ascending \
            else enum_relation_model.name.desc()
        return query.select_from(enum_relation_model) \
                    .join(enum_relationship) \
                    .order_by(sort_by_column)

    @classmethod
    def _sort_by_query(cls, query, sort_by):
        if sort_by is None:
            return query.order_by(cls.id)
        (sort_by_attribute, ascending) = sort_by
        if sort_by_attribute in cls._get_related_enum_table_names():
            return cls._get_sort_by_enum(
                query,
                sort_by_attribute,
                ascending
            )
        return cls._get_sort_by_non_enum(
            query,
            sort_by_attribute,
            ascending
        )

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
    def _bulk_find_on_relation(cls, relation_model, relation_id, **kwargs):
        foreign_key = cls._get_foreign_key_from_relation_model(relation_model)
        query = db.session.query(cls).filter(foreign_key == relation_id)
        return cls._postprocess_bulk_find(query, **kwargs).all()

    @classmethod
    def bulk_find_on_relation_id(cls, relation_model, relation_id, **kwargs):
        cls._check_related_model_by_id_exists(relation_model, relation_id)
        return cls._bulk_find_on_relation(relation_model, relation_id, **kwargs)

    @classmethod
    def bulk_find_on_relation_name(cls, relation_model, relation_name, **kwargs):
        relation_id = cls._get_related_model_id_by_name(relation_model, relation_name)
        return cls._bulk_find_on_relation(relation_model, relation_id, **kwargs)

    @classmethod
    def _check_related_model_by_id_exists(cls, relation_model, relation_id):
        related_instance = db.session.query(relation_model) \
                                     .filter_by(id=relation_id) \
                                     .one_or_none()
        if related_instance is None:
            raise StemInstanceDoesNotExistException()

    @classmethod
    def _get_related_model_id_by_name(cls, relation_model, relation_name):
        related_instance = db.session.query(relation_model) \
                                     .filter_by(name=relation_name) \
                                     .one_or_none()
        if related_instance is None:
            raise NamedEnumStemInstanceDoesNotExistException()
        return related_instance.id

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
    def _populate_target_table_dict(cls):
        columns = list(cls.__table__.columns)
        # this doesn't support compound/composite keys
        foreign_keys_columns = [
            c for c in columns
            if len(c.foreign_keys) == 1
        ]
        cls.target_table_column_dict = {
            cls._get_target_table_from_column(column): column
            for column
            in foreign_keys_columns
        }

    @classmethod
    def relation_is_enum(cls, type_):
        relation_model = cls.get_model_by_type(type_)
        return relation_model.is_enum_table()

    @classmethod
    def _get_foreign_key_from_relation_model(cls, relation_model):
        return cls.target_table_column_dict[relation_model.__tablename__]

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
    def has_log_details(cls):
        return False

    @classmethod
    def is_enum_table(cls):
        return False

    @classmethod
    def get_foreign_key_column_names(cls):
        return [
            c.name for c in cls._get_columns()
            if c.foreign_keys
        ]

    @classmethod
    def _get_foreign_keys_and_target_tables(cls):
        foreign_keys = cls.get_foreign_key_column_names()
        target_tables = [
            cls.get_target_table_column_from_foreign_key(c_name)[0]
            for c_name in foreign_keys
        ]
        return foreign_keys, target_tables

    @classmethod
    def get_enum_relationship_details(cls):
        foreign_keys, target_tables = cls._get_foreign_keys_and_target_tables()
        return [
            (column_name, target_table) for column_name, target_table
            in zip(foreign_keys, target_tables)
            if cls.relation_is_enum(target_table)
        ]

    @classmethod
    def get_relation_id_by_enum_name(cls, relation_type, enum_name):
        relation_model = cls.get_model_by_type(relation_type)
        return relation_model.get_id_from_name(enum_name)

    @classmethod
    def get_relation_enum_name_by_id(cls, relation_type, id):
        relation_model = cls.get_model_by_type(relation_type)
        return relation_model.get_name_from_id(id)

    @classmethod
    def _get_related_enum_table_names(cls):
        _, target_tables = cls._get_foreign_keys_and_target_tables()
        return [
            t_table for t_table in target_tables
            if cls.relation_is_enum(t_table)
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
    def _get_enum_relation_names(cls):
        enum_relationship_details = cls.get_enum_relationship_details()
        return [
            r_name for (_, r_name) in enum_relationship_details
        ]

    @classmethod
    def _preprocess_string_filter_value(cls, filter_value):
        if not cls._filter_value_is_delimited_string(filter_value):
            raise BadParameterException(
                f"The string filter value '{filter_value}' must be surrounded "
                "by quotation marks (either ' or \")"
            )
        # strip surrounding quotes
        return filter_value[1:-1]

    @classmethod
    def _preprocess_non_string_filter_value(cls, filter_value, python_type):
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
    def _preprocess_enum_filter(cls, filter_key, filter_value):
        enum_relation_model = cls.get_model_by_type(filter_key)
        filter_enum_name = cls._preprocess_string_filter_value(
            filter_value
        )
        valid_enum_names = enum_relation_model.get_enum_values()
        if filter_enum_name not in valid_enum_names:
            raise BadParameterException(
                f"The (filter) name '{filter_enum_name}' does not exist on "
                f"the enum {filter_key}."
            )
        return filter_enum_name

    @classmethod
    def _preprocess_filter_value(cls, filter_key, filter_value, enum_names):
        if getattr(cls, filter_key, None) is None:
            raise BadParameterException(
                f"The filter key '{filter_key}' is invalid."
            )

        # pre-remove enum types
        if filter_key in enum_names:
            return cls._preprocess_enum_filter(filter_key, filter_value)

        python_type = cls.get_column_python_type(filter_key)

        if python_type == str:
            return cls._preprocess_string_filter_value(filter_value)

        return cls._preprocess_non_string_filter_value(
            filter_value,
            python_type
        )

    @classmethod
    def _preprocess_filters(cls, eq_filters):
        if not eq_filters:
            return None
        if cls.has_ext_column() and 'ext' in eq_filters.keys():
            raise BadParameterException(
                "This API cannot filter against 'extra' columns."
            )
        enum_names = cls._get_enum_relation_names()
        processed_eq_filters = {
            filter_key: cls._preprocess_filter_value(
                filter_key,
                filter_value,
                enum_names
            )
            for (filter_key, filter_value)
            in eq_filters.items()
        }
        return cls._convert_enum_names_to_foreign_key_ids(
            processed_eq_filters
        )
