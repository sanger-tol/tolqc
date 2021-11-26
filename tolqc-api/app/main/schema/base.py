# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from datetime import datetime
from flask_restx import fields
from marshmallow_jsonapi import Schema, SchemaOpts
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema , \
                                   SQLAlchemyAutoSchemaOpts

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
            "Type '%s' has not been implemented yet."
                % python_type
        )


    @classmethod
    def to_api_model_dict(cls, exclude_fields=None):
        fields = cls._get_fields(exclude_fields)
        return {
            f: cls._get_field_model_type(f)
            for f in fields
        }
    
    @classmethod
    def to_api_model_dict_exclude_id(cls):
        return cls.to_api_model_dict(
            exclude_fields=['id']
        )
