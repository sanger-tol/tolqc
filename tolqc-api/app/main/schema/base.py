# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from datetime import datetime
from flask_restx import fields
from marshmallow import Schema as MarshmallowSchema, \
                        SchemaOpts as MarshmallowSchemaOpts
from marshmallow_jsonapi import Schema as JsonapiSchema, \
                                SchemaOpts as JsonapiSchemaOpts
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, \
                                   SQLAlchemyAutoSchemaOpts


class BaseSchema():
    @classmethod
    def _get_fields(cls, exclude_fields=[]):
        columns = cls.Meta.model.get_columns()
        return [
            c.name for c
            in columns
            if c.name not in exclude_fields
        ]
    
    def get_by_id(self, id):
        model = self.Meta.model.find_by_id(id)
        if model is None:
            return None
        return self.dump(model)


class IdExcludedOnResponseException(Exception):
    def __init__(self, schema):
        print("The field 'id' cannot be excluded"
              f", on schema {schema.Meta.type_}, "
              "for a JSON:API resource model dict.")

# requests are in regular dict format, responses in JSON:API


class RequestCombinedOpts(SQLAlchemyAutoSchemaOpts, MarshmallowSchemaOpts):
    pass


class BaseRequestSchema(SQLAlchemyAutoSchema, MarshmallowSchema, BaseSchema):
    """Used for request/input"""

    OPTIONS_CLASS = RequestCombinedOpts

    def save_and_get_model(self, data):
        model = self.Meta.model(**data)
        model.save()
        return model

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
    def to_model_dict(cls, exclude_fields=[]):
        """Returns a dict for a Model, excluding
           the specified fields"""
        fields = cls._get_fields(
            exclude_fields=exclude_fields+['id']
        )
        return {
            f: cls._get_field_model_type(f)
            for f in fields
        }


class ResponseCombinedOpts(SQLAlchemyAutoSchemaOpts, JsonapiSchemaOpts):
    pass


class BaseResponseSchema(SQLAlchemyAutoSchema, JsonapiSchema, BaseSchema):
    """Used for response/output"""

    OPTIONS_CLASS = ResponseCombinedOpts

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
    def to_schema_model_dict(cls, exclude_fields=[]):
        """Returns a dict for a SchemaModel in JSON:API format"""
        dict_schema = {
            f: cls._get_field_schema_model_type(f)
            for f in cls._get_fields(
                exclude_fields=exclude_fields
            )
        }

        id_field = dict_schema.pop('id', None)
        if id_field is None:
            raise IdExcludedOnResponseException(cls)

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
