# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from datetime import datetime
from marshmallow.decorators import post_dump, pre_dump, post_load
from marshmallow_jsonapi import Schema as JsonapiSchema, \
                                SchemaOpts as JsonapiSchemaOpts
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, \
                                   SQLAlchemyAutoSchemaOpts
from marshmallow_jsonapi.fields import ResourceMeta

from main.model import db


def setup_schema(cls):
    cls.setup()
    return cls


class BaseMeta:
    strict = True
    include_resource_linkage = True
    sqla_session = db.session
    load_instance = True

    @classmethod
    def add_views(cls):
        cls.self_view = cls.type_
        cls.self_view_kwargs = {cls.type_: "<id>"}
        cls.self_view_many = cls.type_


class CombinedOpts(SQLAlchemyAutoSchemaOpts, JsonapiSchemaOpts):
    pass


class BaseSchema(SQLAlchemyAutoSchema, JsonapiSchema):
    OPTIONS_CLASS = CombinedOpts

    @classmethod
    def setup(cls):
        cls.Meta.add_views()

    @classmethod
    def get_type(cls):
        return cls.Meta.type_

    @classmethod
    def _get_dict_schema(cls, exclude_fields=[]):
        return {
            f: cls._get_field_schema_model_type(f)
            for f in cls.get_fields(
                exclude_fields=exclude_fields + ['ext', 'created_by', 'created_at']
            )
        }

    @classmethod
    def _post_attributes_schema_model_dict(cls, exclude_fields=[]):
        dict_schema = cls._get_dict_schema(exclude_fields=exclude_fields)

        required_fields = cls._get_required_fields(exclude_fields=exclude_fields)

        return {
            'required': required_fields,
            'properties': dict_schema,
            'type': 'object',
        }

    @classmethod
    def _patch_attributes_schema_model_dict(cls, exclude_fields=[]):
        dict_schema = cls._get_dict_schema(exclude_fields=exclude_fields)

        return {
            'properties': dict_schema,
            'type': 'object',
        }

    @classmethod
    def _individual_schema_model_dict(cls):
        id_field = cls._get_dict_schema().pop('id', None)

        return {
            'type': 'object',
            'required': ['type', 'attributes', 'id'],
            'properties': {
                "type": {
                    'type': 'string',
                    'default': cls.get_type(),
                },
                "id": id_field,
                "attributes": cls._individual_attributes_schem_model_dict(
                    exclude_fields=['id', 'created_by', 'created_at']
                )
            }
        }

    @classmethod
    def _get_field_schema_model_type(cls, field):
        model = cls.Meta.model
        python_type = model.get_column_python_type(
            field
        )

        if python_type == int:
            return {
                'type': 'integer'
            }
        if python_type == str:
            return {
                'type': 'string'
            }
        if python_type == bool:
            return {
                'type': 'boolean'
            }
        if python_type == datetime:
            return {
                'type': 'string',
                'format': 'date-time'
            }
        if python_type == float:
            return {
                'type': 'number',
                'format': 'float'
            }

        raise NotImplementedError(
            "Type f'{python_type}' has not been implemented yet."
        )

    @classmethod
    def get_fields(cls, exclude_fields=[]):
        column_names = cls.Meta.model.get_column_names()
        return [
            c for c in column_names
            if c not in exclude_fields
        ]

    @classmethod
    def _get_non_required_fields(cls):
        return cls.Meta.model.get_nullable_column_names()

    @classmethod
    def _get_required_fields(cls, exclude_fields=[]):
        all_fields = cls.get_fields(exclude_fields)
        non_required_fields = cls._get_non_required_fields()
        return [
            f for f in all_fields
            if f not in non_required_fields
            and f not in exclude_fields
        ]

    @classmethod
    def _to_request_schema_model_dict(cls, attributes):
        return {
            'type': 'object',
            'required': ['data'],
            'properties': {
                "data": {
                    "type": "object",
                    'required': ['type', 'attributes'],
                    'properties': {
                        'type': {
                            'type': 'string',
                            'default': cls.get_type()
                        },
                        'attributes': attributes
                    }
                }
            }
        }

    @classmethod
    def to_post_request_schema_model_dict(cls):
        """Returns a dict for a Model for a POST request"""
        attributes = cls._post_attributes_schema_model_dict(
            exclude_fields=['id']
        )
        return cls._to_request_schema_model_dict(attributes)

    @classmethod
    def to_patch_request_schema_model_dict(cls):
        """Returns a dict for a Model for a PATCH request"""
        attributes = cls._patch_attributes_schema_model_dict(
            exclude_fields=['id']
        )
        return cls._to_request_schema_model_dict(attributes)


class BaseExtMeta(BaseMeta):
    """The base Schema (Meta) class for a model containing an
    ext column"""
    exclude = ('ext',)


class BaseExtSchema(BaseSchema):
    """The base Schema class for a model containing an ext column"""
    resource_meta = ResourceMeta(required=False)

    @post_load
    def make_instance(self, data, **kwargs):
        # self.instance is part of a private API
        instance = self.instance
        meta = data.pop('resource_meta', {})
        ext = self._none_coalesce_ext(meta.pop('ext', {}))
        if instance is None:
            return self.Meta.model(**data, ext=ext)
        for field, value in data.items():
            setattr(instance, field, value)
            instance.update_ext(ext)
        return instance

    def _none_coalesce_ext(self, ext):
        return ext if ext is not None else {}

    @pre_dump(pass_many=True)
    def store_ext_data_dump(self, data, many, **kwargs):
        if not many:
            self.ext = self._none_coalesce_ext(data.ext)
        else:
            self.ext = [
                self._none_coalesce_ext(datum.ext)
                for datum in data
            ]
        return data

    def _add_ext_to_datum(self, datum, ext_datum):
        datum['_resource_meta'] = {
            'ext': ext_datum
        }
        return datum

    @post_dump(pass_many=True)
    def add_ext_data(self, data, many, **kwargs):
        if many:
            return [
                self._add_ext_to_datum(datum, ext_datum)
                for datum, ext_datum
                in zip(data, self.ext)
            ]
        return self._add_ext_to_datum(data, self.ext)

    @classmethod
    def _to_request_schema_model_dict(cls, attributes):
        schema_model_dict = super()._to_request_schema_model_dict(attributes)
        # add resource level meta
        schema_model_dict['properties']['data']['properties']['meta'] = {
            'type': 'object',
            'properties': {
                'ext': {
                    'type': 'object'
                }
            }
        }
        return schema_model_dict
