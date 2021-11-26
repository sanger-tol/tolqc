# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from datetime import datetime
from flask_restx import fields
from marshmallow_jsonapi import Schema, SchemaOpts
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema , \
                                   SQLAlchemyAutoSchemaOpts


class DictFieldNotSpecifiedException(Exception):
    def __init__(self):
        print("dict_field was not specified in kwargs")


class DictField(fields.Raw):
    """Provides a field class that marshals to a dict"""
    def __init__(self, *args, dict_field=None, **kwargs):
        if dict_field is None:
            raise DictFieldNotSpecifiedException()
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
    def _get_field_model_type(cls, field):
        model = cls.Meta.model
        python_type = model.get_column_python_type(
            field
        )

        if python_type == int:
            return fields.Integer
        if python_type == str:
            return fields.String(field)
        if python_type == bool:
            return fields.Boolean
        if python_type == datetime:
            return fields.DateTime
        if python_type == float:
            return fields.Float
        
        raise NotImplementedError(
            "Type '%s' has not been implemented yet."
                % python_type
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
    def to_jsonapi_model_dict(cls, exclude_fields=None):
        dict_schema = cls.to_dict(
            exclude_fields=exclude_fields
        )
        id_field = dict_schema.pop('id', None)
        if id_field == None:
            raise IdExcludedOnJsonapiDictException(
                cls
            )
        return {
            "data": DictField(
                dict_field={
                    "type": cls.Meta.type_,
                    "attributes": dict_schema,
                    "id": id_field
                }
            )
        }
    
    @classmethod
    def get_by_id(cls, id):
        model = cls.Meta.model
        return model.find_by_id(id)
