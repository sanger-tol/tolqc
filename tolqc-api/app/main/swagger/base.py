# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from datetime import datetime
from flask_restx import Namespace, fields


def setup_swagger(cls):
    cls.setup()
    return cls


class BaseSwagger:
    # store a registry of inherited swagger classes in a dict
    swagger_registry_dict = {}

    @classmethod
    def get_registered_swagger(cls, type_):
        return cls.swagger_registry_dict[type_]

    @classmethod
    def _get_duplicate_relationship_swagger_name(cls, object_title, relation_swagger, is_enum):
        relation_type = relation_swagger.get_type().title()
        return (
            f"{relation_type} {object_title} ({cls.get_type().title()}'s "
            "Enum " if is_enum else ""
            "Copy')"
        )

    @classmethod
    def duplicate_relationship_swagger(cls, relation_swagger, is_enum=False):
        # models have to be registered (with duplicates) per flask-restx's rules
        resource_object_copy = cls.api.schema_model(
            cls._get_duplicate_relationship_swagger_name(
                'Response Resource Object',
                relation_swagger,
                is_enum
            ),
            relation_swagger.get_resource_object_schema_model(is_request=False)
        )
        return cls.api.model(
            cls._get_duplicate_relationship_swagger_name(
                'Bulk Response',
                relation_swagger,
                is_enum
            ),
            {
                'data': fields.List(
                    fields.Nested(resource_object_copy)
                )
            }
        )

    @classmethod
    def get_type(cls):
        return cls.Meta.schema.get_type()

    @classmethod
    def _register_swagger(cls):
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
        if python_type == dict:
            return {
                'type': 'object'
            }
        if python_type == list:
            return {
                'type': 'array'
            }

        raise NotImplementedError(
            f"Type '{python_type}' has not been implemented yet."
        )

    @classmethod
    def _get_attributes_dict(cls, is_request=True):
        exclude_on_request = [
            'created_at',
            'last_modified_at',
            'history'
        ]
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
    def _get_individual_many_to_one_relationship_dict(cls, target_table):
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
    def _get_individual_one_to_many_relationship_dict(cls, relation_name):
        return {
            'type': 'object',
            'properties': {
                'links': {
                    'type': 'object',
                    'properties': {
                        'related': {
                            'type': 'string',
                            'default': f'/{cls.get_type()}/1/{relation_name}'
                        }
                    }
                }
            }
        }

    @classmethod
    def _get_many_to_one_relationships_dict(cls, is_request):
        relationships = cls.request_many_to_one_relationships \
                        if is_request \
                        else cls.response_many_to_one_relationships
        return {
            special_name: cls._get_individual_many_to_one_relationship_dict(
                relationships[special_name]["target_table"]
            )
            for special_name
            in relationships.keys()
        }

    @classmethod
    def _get_one_to_many_relationships_dict(cls):
        return {
            name: cls._get_individual_one_to_many_relationship_dict(name)
            for name in cls.one_to_many_relationship_names
        }

    @classmethod
    def _get_relationships_dict(cls, is_request):
        many_to_one_relationships_dict = cls._get_many_to_one_relationships_dict(is_request)

        if is_request:
            # don't include one-to-many relationships on a request swagger model
            all_relationships_dict = many_to_one_relationships_dict
        else:
            one_to_many_relationships_dict = cls._get_one_to_many_relationships_dict()
            all_relationships_dict = {
                **many_to_one_relationships_dict,
                **one_to_many_relationships_dict
            }

        return {
            'type': 'object',
            'properties': all_relationships_dict
        }

    @classmethod
    def get_resource_object_schema_model(cls, is_request=True):
        schema_model = {
            "type": "object",
            'properties': {
                'type': {
                    'type': 'string',
                    'default': cls.get_type()
                },
                'attributes': cls._get_attributes_dict(is_request),
                'relationships': cls._get_relationships_dict(is_request)
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
                "data": cls.get_resource_object_schema_model(
                    is_request=True
                )
            }
        }

    @classmethod
    def _set_relationships(cls):
        schema = cls.Meta.schema
        cls.one_to_many_relationship_names = schema.get_one_to_many_relationship_names()
        cls.response_many_to_one_relationships = schema.get_many_to_one_relationships()
        cls.request_many_to_one_relationships = {
            key: value for (key, value) in cls.response_many_to_one_relationships.items()
            if key not in schema.get_excluded_many_to_one_relationships_on_request()
        }

    @classmethod
    def _create_models(cls):
        type_ = cls.get_type()

        cls.request_model = cls.api.schema_model(
            f'{type_.title()} Request',
            cls._get_request_schema_model()
        )

        cls.response_resource_object = cls.api.schema_model(
            f'{type_.title()} Response Resource Object',
            cls.get_resource_object_schema_model(
                is_request=False
            )
        )

        cls.individual_response_model = cls.api.model(
            f'{type_.title()} Individual Response',
            {
                'data': fields.Nested(cls.response_resource_object)
            }
        )

        cls.bulk_response_model = cls.api.model(
            f'{type_.title()} Bulk Response',
            {
                'data': fields.List(
                    fields.Nested(cls.response_resource_object)
                )
            }
        )

    @classmethod
    def _set_attributes(cls):
        schema = cls.Meta.schema
        cls.attributes = schema.get_included_attributes()

    @classmethod
    def _create_api(cls):
        type_ = cls.get_type()
        cls.api = Namespace(
            type_,
            description=f'Methods relating to {type_}',
            path=f'/{type_}'
        )

    @classmethod
    def setup(cls):
        cls._set_attributes()
        cls._set_relationships()
        cls._create_api()
        cls._create_models()
        cls._register_swagger()
