# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from datetime import datetime
from typing import Dict
from flask_restx import fields
from marshmallow_jsonapi import Schema, SchemaOpts
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema , \
                                   SQLAlchemyAutoSchemaOpts


class DictField(fields.Raw):
    """Provides a field class that marshals to a dict"""
    def __init__(self, dict_field, *args, **kwargs):
        self._dict_field = dict_field
        super().__init__(*args, **kwargs)
    def output(self, key, obj, *args, **kwargs):
        return self._dict_field


class IdExcludedOnJsonapiDictException(Exception):
    def __init__(self, schema):
        print("The field 'id' cannot be excluded" \
              f", on schema {schema.Meta.type_}, " \
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
    def _python_to_model_type(cls, python_type):
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
            "Type '%s' has not been implemented yet."
                % python_type
        )

    @classmethod
    def _get_field_model_type(cls, field):
        model = cls.Meta.model
        python_type = model.get_column_python_type(
            field
        )

        return cls._python_to_model_type(
            python_type
        )


    @classmethod
    def to_dict(cls, exclude_fields=None):
        fields = cls._get_fields(
            exclude_fields=exclude_fields
        )
        return {
            f: cls._get_field_model_type(f)
            for f in fields
        }
    
    @classmethod
    def to_dict_exclude_id(cls):
        return cls.to_dict(
            exclude_fields=['id']
        )
    
    @classmethod
    def to_jsonapi_schema_model_dict(cls, exclude_fields=None):
        dict_schema = cls.to_dict(
            exclude_fields=exclude_fields
        )
        
        id_field = dict_schema.pop('id', None)
        if id_field == None:
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
