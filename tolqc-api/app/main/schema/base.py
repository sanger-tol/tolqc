# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from marshmallow.decorators import post_dump, pre_dump, post_load, pre_load
from marshmallow.exceptions import ValidationError
from marshmallow_jsonapi import Schema as JsonapiSchema, \
                                SchemaOpts as JsonapiSchemaOpts
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, \
                                   SQLAlchemyAutoSchemaOpts
from marshmallow_jsonapi.fields import ResourceMeta, Relationship, Str, \
                                       DateTime, List, Dict

from main.model import db


def setup_schema(cls):
    return cls.setup()


class CombinedOpts(JsonapiSchemaOpts, SQLAlchemyAutoSchemaOpts):
    pass


class BadEnumNameException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


class BaseSchema(SQLAlchemyAutoSchema, JsonapiSchema):
    class BaseMeta(SQLAlchemyAutoSchema.Meta):
        strict = True
        include_resource_linkage = True
        ordered = True
        sqla_session = db.session
        load_instance = True
        include_fk = True

        @classmethod
        def setup_meta(cls):
            cls.type_ = cls.model.get_type()

    OPTIONS_CLASS = CombinedOpts

    id = Str(dump_only=True)

    def __init__(self, **kwargs):
        exclude = kwargs.pop('exclude', []) + self.get_excluded_columns()
        return super().__init__(exclude=exclude, **kwargs)

    @classmethod
    def setup(old_cls):
        """Dynamically adds fields to a Schema Class inheriting
        from BaseSchema"""
        old_cls.Meta.setup_meta()
        old_cls._populate_public_attribute_and_enum_names()
        new_cls = type(
            f'_{old_cls.get_type().title()}Schema',
            (old_cls,),
            old_cls.get_dynamically_added_fields()
        )
        return new_cls

    @classmethod
    def get_model(cls):
        return cls.Meta.model

    @classmethod
    def _populate_public_attribute_and_enum_names(cls):
        cls._public_attribute_names = cls._get_public_attribute_names()
        cls._public_attribute_and_enum_names = \
            cls._public_attribute_names + cls.Meta.model.get_related_enum_types()

    @classmethod
    def _lookup_special_relationship_name(cls, foreign_key_name, target_table):
        lookup_map = {
            'created_by': 'creator',
            'last_modified_by': 'last_modifier'
        }
        # default to the target table if no special name
        return lookup_map.get(foreign_key_name, target_table)

    @classmethod
    def _create_many_to_one_relationship_field(cls, table, column, foreign_key_name, dump_only):
        return Relationship(
            f'/{table}/{{{column}}}',
            related_url_kwargs={f'{column}': f'<{foreign_key_name}>'},
            include_resource_linkage=True,
            type_=table,
            attribute=foreign_key_name,
            dump_only=dump_only
        )

    @classmethod
    def _many_to_one_relationship_is_dump_only(cls, special_name):
        dump_only_special_names = ['creator', 'last_modifier'] + list(
            getattr(cls.Meta, 'dump_only_relationships', [])
        )
        return special_name in dump_only_special_names

    @classmethod
    def _create_many_to_one_relationship_field_by_name(cls, foreign_key_name):
        model = cls.Meta.model
        target_table, target_column = model.get_target_table_column_from_foreign_key(
            foreign_key_name
        )
        special_name = cls._lookup_special_relationship_name(
            foreign_key_name,
            target_table
        )
        cls.many_to_one_relationship_info[special_name] = {
            "target_table": target_table,
            "foreign_key_name": foreign_key_name
        }
        return special_name, cls._create_many_to_one_relationship_field(
            target_table,
            target_column,
            foreign_key_name,
            cls._many_to_one_relationship_is_dump_only(special_name)
        )

    @classmethod
    def _create_many_to_one_relationship_fields(cls):
        cls.many_to_one_relationship_info = {}
        model = cls.Meta.model
        foreign_key_names = model.get_foreign_key_column_names()
        # do not express enums as a true schema relationship
        enum_foreign_key_names = [
            f_key for (f_key, _) in model.get_enum_relationship_details()
        ]
        # maps the relationship name to its target table
        pairs = [
            cls._create_many_to_one_relationship_field_by_name(foreign_key_name)
            for foreign_key_name in foreign_key_names
            if foreign_key_name not in enum_foreign_key_names
        ]
        return {
            field_name: field for (field_name, field) in pairs
        }

    @classmethod
    def _create_one_to_many_relationship_field_by_name_enum(cls, r_name):
        return Relationship(
            f'/enum/{cls.get_type()}/{{name}}/{r_name}',
            related_url_kwargs={'name': '<name>'},
            many=True,
            type_=r_name,
            dump_default=lambda: []
        )

    @classmethod
    def _create_one_to_many_relationship_field_by_name_non_enum(cls, name):
        return Relationship(
            f'/{cls.get_type()}/{{id}}/{name}',
            related_url_kwargs={'id': '<id>'},
            many=True,
            type_=name,
            dump_default=lambda: []
        )

    @classmethod
    def _create_one_to_many_relationship_field_by_name(cls, name):
        if cls.is_enum_schema():
            return cls._create_one_to_many_relationship_field_by_name_enum(name)
        return cls._create_one_to_many_relationship_field_by_name_non_enum(name)

    @classmethod
    def _create_one_to_many_relationship_fields(cls):
        cls.one_to_many_relationship_names = cls.Meta.model.get_one_to_many_relationship_names()
        return {
            name: cls._create_one_to_many_relationship_field_by_name(name)
            for name in cls.one_to_many_relationship_names
        }

    @classmethod
    def _create_relationship_fields(cls):
        return {
            **cls._create_many_to_one_relationship_fields(),
            **cls._create_one_to_many_relationship_fields()
        }

    @classmethod
    def _get_possibly_empty_resource_meta_field(cls):
        if cls.has_ext_field():
            return {'resource_meta': ResourceMeta(required=False)}
        return {}

    @classmethod
    def _get_possibly_empty_creation_log_fields(cls):
        if not cls.has_log_details():
            return {}
        return {
            'created_by': Str(dump_only=True),
            'created_at': DateTime(dump_only=True),
            'last_modified_by': Str(dump_only=True),
            'last_modified_at': DateTime(dump_only=True),
            'history': List(Dict(), dump_only=True)
        }

    @classmethod
    def _get_possibly_empty_enum_name_fields(cls):
        enum_names = cls.Meta.model.get_related_enum_types()
        return {enum_name: Str() for enum_name in enum_names}

    @classmethod
    def _get_dynamically_added_non_relationship_fields(cls):
        return {
            **cls._get_possibly_empty_resource_meta_field(),
            **cls._get_possibly_empty_creation_log_fields(),
            **cls._get_possibly_empty_enum_name_fields()
        }

    @classmethod
    def get_dynamically_added_fields(cls):
        return {
            **cls._create_relationship_fields(),
            **cls._get_dynamically_added_non_relationship_fields()
        }

    @classmethod
    def get_type(cls):
        return cls.Meta.type_

    @classmethod
    def get_excluded_columns(cls):
        """Gets the excluded columns on both requests and responses"""
        excluded_columns = list(getattr(cls.Meta, 'exclude', []))
        excluded_columns += cls.Meta.model.get_foreign_key_column_names()
        return excluded_columns

    @classmethod
    def has_log_details(cls):
        return cls.Meta.model.has_log_details()

    @classmethod
    def has_ext_field(cls):
        return cls.Meta.model.has_ext_column()

    @classmethod
    def is_enum_schema(cls):
        return cls.Meta.model.is_enum_table()

    @classmethod
    def _get_public_attribute_names(cls):
        return [
            column for column
            in cls.Meta.model.get_column_names()
            if column not in ['id', 'ext'] + cls.get_excluded_columns()
        ]

    @classmethod
    def attribute_is_public(cls, attribute_name):
        return attribute_name in cls._public_attribute_and_enum_names

    @classmethod
    def get_included_attributes(cls):
        return [
            (name, cls.Meta.model.get_column_python_type(name))
            for name in cls._get_public_attribute_names()
        ]

    @classmethod
    def get_many_to_one_relationships(cls):
        return cls.many_to_one_relationship_info

    @classmethod
    def get_excluded_many_to_one_relationships_on_request(cls):
        if cls.has_log_details():
            return ['creator', 'last_modifier']
        return []

    @classmethod
    def get_one_to_many_relationship_names(cls):
        return cls.one_to_many_relationship_names

    def _make_instance_without_ext(self, data, **kwargs):
        instance = self.instance
        if instance is None:
            return self.Meta.model(**data)
        instance.update(data)
        return instance

    def _preprocess_ext_on_create(self, ext):
        if ext is None:
            return {}
        # remove null entries with null values
        return {
            key: value for key, value
            in ext.items()
            if value is not None
        }

    def _make_instance_including_ext(self, data, **kwargs):
        instance = self.instance
        ext = self._resource_meta.pop('ext', None)
        if instance is None:
            return self.Meta.model(
                **data,
                ext=self._preprocess_ext_on_create(ext)
            )
        instance.update(data, ext=ext)
        return instance

    def _remove_resource_metadata(self, data):
        self._resource_meta = data.pop('_resource_meta', {})
        if not self.has_ext_field() and 'ext' in self._resource_meta:
            raise ValidationError(
                f'Extra fields are not permitted on {self.get_type()}.'
            )

    @pre_load
    def preprocess_instance(self, data, **kwargs):
        self._remove_resource_metadata(data)
        return data

    @post_load
    def make_instance(self, data, **kwargs):
        # make_instance overrides part of a private API
        if self.has_ext_field():
            return self._make_instance_including_ext(data, **kwargs)
        return self._make_instance_without_ext(data, **kwargs)

    def _store_ext_data(self, data, many):
        if many:
            self._ext_data = [m.ext for m in data]
        else:
            self._ext_data = data.ext

    @pre_dump(pass_many=True)
    def pre_process_dump_data(self, data, many, **kwargs):
        if self.has_ext_field():
            self._store_ext_data(data, many)

        if many:
            return [
                self._model_instance_to_datum(m)
                for m in data
            ]

        return self._model_instance_to_datum(data)

    def _model_instance_to_datum(self, model_instance):
        return model_instance.to_dict(exclude_column_names=['ext'])

    def _re_insert_ext_datum(self, datum, ext_data):
        datum['meta'] = {
            'ext': ext_data
        }
        return datum

    def _reinsert_ext_data(self, data, many):
        if not self.has_ext_field():
            return data

        if many:
            data['data'] = [
                self._re_insert_ext_datum(datum, ext)
                for datum, ext
                in zip(data['data'], self._ext_data)
            ]
        else:
            data['data'] = self._re_insert_ext_datum(
                data['data'],
                self._ext_data
            )

        return data

    @post_dump(pass_many=True)
    def postprocess_data(self, data, many, **kwargs):
        data = self._reinsert_ext_data(data, many)
        return data
