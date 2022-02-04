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
            cls.type_ = cls.model.__tablename__

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
        old_cls._public_attribute_names = old_cls._get_public_attribute_names()
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
        #TODO test that the enum stem is present and correct, and functional
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
        many_to_one_relationship_fields = cls._create_many_to_one_relationship_fields()
        one_to_many_relationship_fields = cls._create_one_to_many_relationship_fields()
        all_relationship_fields = {
            **many_to_one_relationship_fields,
            **one_to_many_relationship_fields
        }
        return all_relationship_fields

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
        enum_names = [
            t_table for (_, t_table)
            in cls.Meta.model.get_enum_relationship_details()
        ]
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
        relationship_fields = cls._create_relationship_fields()
        other_fields = cls._get_dynamically_added_non_relationship_fields()
        return {
            **relationship_fields,
            **other_fields
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
            column for column in cls.Meta.model.get_column_names()
            if column not in ['id', 'ext'] + cls.get_excluded_columns()
        ]

    @classmethod
    def attribute_is_public(cls, attribute_name):
        return attribute_name in cls._public_attribute_names

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

    def _add_enum_foreign_keys(self, data):
        return {
            **data,
            **self._emum_foreign_key_values
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

    @classmethod
    def _get_id_from_enum_detail(cls, data, target_table):
        enum_name = data.get(target_table, None)
        if enum_name is None:
            return None
        return cls.Meta.model.get_relation_id_by_enum_name(
            target_table,
            enum_name
        )


    def _preprocess_enum_names(self, data):
        enum_details = self.Meta.model.get_enum_relationship_details()
        pairs = [
            (f_key, self._get_id_from_enum_detail(data, t_table))
            for f_key, t_table in enum_details
        ]
        self._emum_foreign_key_values = {
            key: value for key, value in pairs
            if value is not None
        }
        return [target_table for (_, target_table) in enum_details]

    def _remove_enum_keys(self, data, enum_keys):
        for key in enum_keys:
            data.pop(key, None)

    def _remove_enum_names(self, data):
        enum_keys = self._preprocess_enum_names(data)
        return self._remove_enum_keys(data, enum_keys)

    @pre_load
    def preprocess_instance(self, data, **kwargs):
        self._remove_resource_metadata(data)
        self._remove_enum_names(data)
        return data

    @post_load
    def make_instance(self, data, **kwargs):
        # make_instance overrides part of a private API
        data = self._add_enum_foreign_keys(data)
        if self.has_ext_field():
            return self._make_instance_including_ext(data, **kwargs)
        return self._make_instance_without_ext(data, **kwargs)

    def _store_ext_data(self, data, many):
        if many:
            self._ext_data = [m.ext for m in data]
        else:
            self._ext_data = data.ext

    def _get_enum_name_from_id(self, datum, target_table, foreign_key):
        id = getattr(datum, foreign_key)
        if id is None:
            return None
        return self.Meta.model.get_relation_enum_name_by_id(target_table, id)

    def _preprocess_enum_foreign_keys_individual(self, enum_details, datum):
        return {
            t_table: self._get_enum_name_from_id(datum, t_table, f_key)
            for f_key, t_table in enum_details
        }

    def _preprocess_enum_foreign_keys(self, data, many):
        enum_details = self.Meta.model.get_enum_relationship_details()
        if many:
            self._enum_name_data = [
                self._preprocess_enum_foreign_keys_individual(
                    enum_details,
                    datum
                )
                for datum in data
            ]
        else:
            self._enum_name_data = self._preprocess_enum_foreign_keys_individual(
                enum_details,
                data
            )
        return [f_key for (f_key, _) in enum_details]

    @pre_dump(pass_many=True)
    def pre_process_dump_data(self, data, many, **kwargs):
        if self.has_ext_field():
            self._store_ext_data(data, many)

        enum_foreign_key_names = self._preprocess_enum_foreign_keys(
            data,
            many
        )

        if many:
            return [
                self._model_instance_to_datum(m, enum_foreign_key_names)
                for m in data
            ]

        return self._model_instance_to_datum(data, enum_foreign_key_names)

    def _model_instance_to_datum(self, model_instance, exclude):
        return model_instance.to_dict(exclude_column_names=['ext', *exclude])

    def _re_insert_ext_datum(self, datum, ext_data):
        datum['meta'] = {
            'ext': ext_data
        }
        return datum

    def _insert_enum_names_to_datum_attributes(self, datum, enum_datum):
        if not enum_datum:
            return datum
        for target_table, enum_name in enum_datum.items():
            datum[target_table] = enum_name
        return datum

    def _get_datum_with_inserted_enum_names(self, datum, enum_datum):
        attributes = self._insert_enum_names_to_datum_attributes(
            datum.get('attributes', {}),
            enum_datum
        )
        if attributes:
            datum['attributes'] = attributes
        return datum

    def _insert_enum_names(self, data, many):
        if not self.is_enum_schema():
            return data

        if many:
            data['data'] = [
                self._get_datum_with_inserted_enum_names(
                    datum, enum_name_datum
                )
                for datum, enum_name_datum
                in zip(data['data'], self._enum_name_data)
            ]
        else:
            data['data'] = self._get_datum_with_inserted_enum_names(
                data['data'],
                self._enum_name_data
            )

        return data

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
        data = self._insert_enum_names(data, many)
        data = self._reinsert_ext_data(data, many)
        return data
