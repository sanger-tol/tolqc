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


def setup_schema(OldCls):
    """Dynamically adds fields to a Schema Class inheriting
    from BaseSchema"""
    OldCls.setup()
    NewCls = type(
        f'_{OldCls.get_type().title()}Schema',
        (OldCls,),
        OldCls.get_dynamically_added_fields()
    )
    return NewCls


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
            cls.self_view = cls.type_
            cls.self_view_kwargs = {cls.type_: "<id>"}
            cls.self_view_many = cls.type_

    OPTIONS_CLASS = CombinedOpts

    id = Str(dump_only=True)

    def __init__(self, **kwargs):
        exclude = self.get_excluded_columns()
        return super().__init__(exclude=exclude, **kwargs)

    @classmethod
    def setup(cls):
        cls.Meta.setup_meta()
        cls._public_attribute_names = cls._get_public_attribute_names()

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
        dump_only_special_names = ['creator'] + list(
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
            "foreign_key_name": foreign_key_name,
            'is_enum': model.relation_is_enum(target_table)
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
        foreign_key_names = cls.Meta.model.get_foreign_key_column_names()
        # maps the relationship name to its target table
        pairs = [
            cls._create_many_to_one_relationship_field_by_name(foreign_key_name)
            for foreign_key_name in foreign_key_names
        ]
        return {
            field_name: field for (field_name, field) in pairs
        }

    @classmethod
    def _create_one_to_many_relationship_field_by_name(cls, name):
        return Relationship(
            f'/{cls.get_type()}/{{id}}/{name}',
            related_url_kwargs={'id': '<id>'},
            many=True,
            type_=name,
            dump_default=lambda: []
        )

    @classmethod
    def _create_one_to_many_relationship_fields(cls):
        # don't populate this on enum schemas
        if cls.is_enum_schema():
            cls.one_to_many_relationship_names = []
            return {}
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
    def _get_dynamically_added_non_relationship_fields(cls):
        return {
            **cls._get_possibly_empty_resource_meta_field(),
            **cls._get_possibly_empty_creation_log_fields()
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

    def _validate_relationship_entry(self, entry):
        specified_id = entry.get('id', None)
        specified_name = entry.get('name', None)
        if specified_id is None and specified_name is None:
            raise BadEnumNameException(
                'On an enum relationship, an id or name must be specified.'
            )
        if specified_id is not None and specified_name is not None:
            raise BadEnumNameException(
                'On an enum relationship, only one of an id or name may be specified'
            )

    def _id_is_on_enum_relationship_entry(self, entry):
        specified_id = entry.get('id', None)
        return specified_id is not None

    def _update_data_name_to_id_on_enum_entry(self, data, relationship_name, target_model_name):
        target_model = self.Meta.model.get_model_by_type(target_model_name)
        name = data[relationship_name]['data'].pop('name')
        id = target_model.get_id_from_name(name)
        if id is None:
            raise BadEnumNameException(
                f'No {relationship_name} exists with name "{name}".'
            )
        data[relationship_name]['data']['id'] = str(id)
        return data

    def _preprocess_name_to_id_individual(self, data, special_name, target_table):
        entry = data.get(special_name, {}).get('data', None)
        if entry is None:
            return data
        self._validate_relationship_entry(entry)
        if self._id_is_on_enum_relationship_entry(entry):
            return data
        return self._update_data_name_to_id_on_enum_entry(
            data,
            special_name,
            target_table
        )

    def _preprocess_names_to_id_if_enum(self, data):
        """Looksup id from name, for all enum relationships"""
        if not self.many_to_one_relationship_info:
            return data
        for special_name, target_info in self.many_to_one_relationship_info.items():
            if target_info['is_enum']:
                data = self._preprocess_name_to_id_individual(
                    data,
                    special_name,
                    target_info['target_table']
                )
        return data

    @pre_load
    def preprocess_instance(self, data, **kwargs):
        self._remove_resource_metadata(data)
        data = self._preprocess_names_to_id_if_enum(data)
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

    @post_dump(pass_many=True)
    def re_insert_ext_data(self, data, many, **kwargs):
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
