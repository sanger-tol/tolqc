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
    def is_enum_swagger(cls):
        return cls.Meta.schema.is_enum_schema()

    @classmethod
    def get_registered_swagger(cls, type_):
        return cls.swagger_registry_dict[type_]

    @classmethod
    def _get_duplicate_relationship_swagger_name(cls, object_title, relation_type):
        return f"{relation_type} {object_title} ({cls.get_type().title()}'s Copy)"

    @classmethod
    def _duplicate_relationship_swagger(cls, relation_swagger_name):
        # models have to be registered (with duplicates) per flask-restx's rules
        relation_swagger = cls.get_registered_swagger(relation_swagger_name)
        resource_object_copy = cls.api.schema_model(
            cls._get_duplicate_relationship_swagger_name(
                'Response Resource Object',
                relation_swagger_name
            ),
            relation_swagger.get_resource_object_schema_model(is_request=False)
        )
        return cls.api.model(
            cls._get_duplicate_relationship_swagger_name(
                'Bulk Response',
                relation_swagger_name
            ),
            {
                'data': fields.List(
                    fields.Nested(resource_object_copy)
                )
            }
        )

    @classmethod
    def duplicate_relationship_swaggers(cls, relationship_names):
        cls._relation_list_get_swagger_models = {
            r_name: cls._duplicate_relationship_swagger(r_name)
            for r_name in relationship_names
        }

    @classmethod
    def get_relation_list_get_swagger_model(cls, relationship_name):
        return cls._relation_list_get_swagger_models[relationship_name]

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
        if 'name' in attributes and cls.is_enum_swagger():
            attributes['name'] = {
                'type': 'string',
                'default': "name"
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
                            'default': f'{cls._get_api_path()}/name/{relation_name}'
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

        if not all_relationships_dict:
            return None

        return {
            'type': 'object',
            'properties': all_relationships_dict
        }

    @classmethod
    def get_resource_object_schema_model(cls, is_request=True):
        relationships = cls._get_relationships_dict(is_request)
        id_dict = {
            'type': 'string',
            'default': '1'
        }
        meta_ext_dict = {
            'type': 'object',
            'properties': {
                'ext': {
                    'type': 'object'
                }
            }
        }
        return {
            "type": "object",
            'properties': {
                'type': {
                    'type': 'string',
                    'default': cls.get_type()
                },
                # don't insert into dict if condition isn't met
                **({'id': id_dict} if not is_request else {}),
                'attributes': cls._get_attributes_dict(is_request),
                **({
                    'relationships': relationships
                } if relationships is not None else {}),
                **({
                    'meta': meta_ext_dict
                } if cls.Meta.schema.has_ext_field() else {})
            }
        }

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
    def _get_api_path(cls):
        type_ = cls.get_type()
        return f'/enum/{type_}' if cls.is_enum_swagger() else f'/{type_}'

    @classmethod
    def _get_api_description(cls):
        type_ = cls.get_type()
        return f'Methods relating to {type_}'

    @classmethod
    def _create_api(cls):
        cls.api = Namespace(
            cls.get_type(),
            description=cls._get_api_description(),
            path=cls._get_api_path()
        )

    @classmethod
    def setup(cls):
        cls._set_attributes()
        cls._set_relationships()
        cls._create_api()
        cls._create_models()
        cls._register_swagger()
