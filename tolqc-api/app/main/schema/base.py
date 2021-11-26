# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from datetime import datetime
from flask_restx import fields
from marshmallow_jsonapi import Schema, SchemaOpts
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, \
                                   SQLAlchemyAutoSchemaOpts


class IdExcludedOnJsonapiDictException(Exception):
    def __init__(self, schema):
        print("The field 'id' cannot be excluded"
              f", on schema {schema.Meta.type_}, "
              "for a JSON:API resource model dict.")


class CombinedOpts(SQLAlchemyAutoSchemaOpts, SchemaOpts):
    pass


class BaseSchema(SQLAlchemyAutoSchema, Schema):
    OPTIONS_CLASS = CombinedOpts

    @classmethod
    def _get_fields(cls, exclude_fields=None):
        columns = cls.Meta.model.get_columns()
        all_fields = [
            c.name for c in columns
        ]
        if exclude_fields is None:
            return all_fields
        return [
            f for f
            in all_fields
            if f not in exclude_fields
        ]

    @classmethod
    def _get_field_model_type(cls, field):
        model = cls.Meta.model
        python_type = model.get_column_python_type(
            field
        )

        if python_type == int:
            return fields.Integer
        if python_type == str:
            return fields.String
        if python_type == bool:
            return fields.Boolean
        if python_type == datetime:
            return fields.DateTime
        if python_type == float:
            return fields.Float

        raise NotImplementedError(
            f"Type '{python_type}' has not been implemented yet."
        )

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
    def to_model_dict(cls, exclude_fields=None):
        """Returns a dict for a Model, excluding
           the specified fields"""
        fields = cls._get_fields(
            exclude_fields=exclude_fields
        )
        return {
            f: cls._get_field_model_type(f)
            for f in fields
        }

    @classmethod
    def to_model_dict_exclude_id(cls):
        """Returns a dict for a Model excluding the ID"""
        return cls.to_model_dict(
            exclude_fields=['id']
        )

    @classmethod
    def to_jsonapi_schema_model_dict(cls, exclude_fields=None):
        """Returns a dict for a SchemaModel in JSON:API format"""
        dict_schema = {
            f: cls._get_field_schema_model_type(f)
            for f in cls._get_fields(
                exclude_fields=exclude_fields
            )
        }

        id_field = dict_schema.pop('id', None)
        if id_field is None:
            raise IdExcludedOnJsonapiDictException(cls)

        model_dict = {
            'required': ['data'],
            'properties': {
                "data": {
                    'required': ['type', 'attributes', 'id'],
                    'properties': {
                        "type": {
                            'type': 'string',
                            'default': cls.Meta.type_,
                        },
                        "attributes": {
                            'required': list(dict_schema.keys()),
                            'properties': dict_schema,
                            'type': 'object',
                        },
                        "id": id_field,
                    },
                    'type': 'object',
                },
            },
            'type': 'object',
        }
        return model_dict

    @classmethod
    def get_by_id(cls, id):
        model = cls.Meta.model
        return model.find_by_id(id)
