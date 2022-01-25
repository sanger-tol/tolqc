# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from datetime import datetime
from flask_restx import Namespace, fields


def setup_swagger(cls):
    cls.populate_default_models()
    cls.register_swagger()
    return cls


class BaseSwagger:
    # store a registry of inherited swagger classes in a dict
    swagger_registry_dict = {}

    @classmethod
    def get_type(cls):
        return cls.Meta.schema.get_type()

    @classmethod
    def register_swagger(cls):
        type_ = cls.get_type()
        cls.swagger_registry_dict[type_] = cls

    @classmethod
    def _get_field_schema_model_type(cls, python_type):
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
            f"Type '{python_type}' has not been implemented yet."
        )

    @classmethod
    def _get_attributes_dict(cls, is_request=True):
        exclude_on_request = ['created_at']
        attributes = {
            field_name: cls._get_field_schema_model_type(python_type)
            for field_name, python_type in cls.attributes
            if not (is_request and field_name in exclude_on_request)
        }
        return {
            'type': 'object',
            'properties': attributes
        }

    @classmethod
    def _get_individual_relationship_dict(cls, target_table):
        return {
            'type': 'object',
            'properties': {
                'data': {
                    'type': 'object',
                    'properties': {
                        'type': {
                            'type': 'string',
                            'default': target_table
                        },
                        'id': {
                            'type': 'string',
                            'default': "1"
                        }
                    }
                }
            }
        }

    @classmethod
    def _get_relationships_dict(cls):
        return {
            'type': 'object',
            'properties': {
                special_name: cls._get_individual_relationship_dict(
                    cls.relationships[special_name]["target_table"]
                )
                for special_name
                in cls.relationships.keys()
            }
        }

    @classmethod
    def _get_resource_object_schema_model(cls, is_request=True):
        schema_model = {
            "type": "object",
            'properties': {
                'type': {
                    'type': 'string',
                    'default': cls.get_type()
                },
                'attributes': cls._get_attributes_dict(
                    is_request=is_request
                ),
                'relationships': cls._get_relationships_dict()
            }
        }
        if cls.Meta.schema.has_ext_field():
            schema_model['properties']['meta'] = {
                'type': 'object',
                'properties': {
                    'ext': {
                        'type': 'object'
                    }
                }
            }
        if not is_request:
            schema_model['properties']['id'] = {
                'type': 'string',
                'default': '1'
            }
        return schema_model

    @classmethod
    def _get_request_schema_model(cls):
        return {
            'type': 'object',
            'properties': {
                "data": cls._get_resource_object_schema_model(
                    is_request=True
                )
            }
        }

    @classmethod
    def _get_individual_response_schema_model(cls):
        return {
            'type': 'object',
            'properties': {
                "data": cls._get_resource_object_schema_model(
                    is_request=False
                )
            }
        }

    @classmethod
    def _get_bulk_response_schema_model(cls):
        return {
            'type': 'object',
            'properties': {
                'data': {
                    'type': 'array',
                    'items': cls._get_resource_object_schema_model(
                        is_request=False
                    )
                }
            }
        }

    @classmethod
    def populate_default_models(cls):
        schema = cls.Meta.schema
        type_ = cls.get_type()
        cls.attributes = schema.get_included_attributes()
        cls.relationships = schema.get_included_relationships()

        cls.api = Namespace(
            type_,
            description=f'Methods relating to {type_}',
            path=f'/{type_}'
        )

        cls.request_model = cls.api.schema_model(
            f'{type_.title()} Request',
            cls._get_request_schema_model()
        )

        response_resource_object = cls.api.schema_model(
            f'{type_.title()} Response Resource Object',
            cls._get_resource_object_schema_model(
                is_request=False
            )
        )

        cls.individual_response_model = cls.api.model(
            f'{type_.title()} Individual Response',
            {
                'data': fields.Nested(response_resource_object)
            }
        )

        cls.bulk_response_model = cls.api.model(
            f'{type_.title()} Bulk Response',
            {
                'data': fields.List(
                    fields.Nested(response_resource_object)
                )
            }
        )
