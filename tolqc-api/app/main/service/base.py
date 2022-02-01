# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

import json

from flask import Response, request
from functools import wraps
from sqlalchemy.exc import IntegrityError
from marshmallow import ValidationError
from marshmallow_jsonapi.exceptions import IncorrectTypeError

from main.model import InstanceDoesNotExistException, \
                       StemInstanceDoesNotExistException, \
                       BadParameterException, \
                       EnumInstanceNotFoundException, \
                       StemEnumInstanceDoesNotExistException


class BadParameterStringException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


class BadTargetServiceException(Exception):
    def __init__(self, target_service):
        self.message = f"No endpoint exists with name '{target_service}'."
        super().__init__(self.message)


def setup_service(cls):
    cls.setup()
    return cls


def handle_404(function):
    @wraps(function)
    def wrapper(cls, identifier, *args, **kwargs):
        try:
            return function(cls, identifier, *args, **kwargs)
        except (
            InstanceDoesNotExistException,
            StemInstanceDoesNotExistException
        ):
            return cls.error_404(identifier)
        except (
            EnumInstanceNotFoundException,
            StemEnumInstanceDoesNotExistException
        ):
            return cls.error_404_enum(identifier)
    return wrapper


def handle_400_db_integrity_error(function):
    @wraps(function)
    def wrapper(cls, *args, **kwargs):
        try:
            return function(cls, *args, **kwargs)
        except IntegrityError:
            return cls.error_400(
                "An integrity error occured in the database. "
                "This is most likely due to either a dependency on "
                "this instance, if deleting, or a foreign reference "
                "to an object that does not exist, if creating/updating."
            )
    return wrapper


def handle_400_marshmallow_error(function):
    @wraps(function)
    def wrapper(cls, *args, **kwargs):
        try:
            return function(cls, *args, **kwargs)
        except (ValidationError, IncorrectTypeError) as e:
            return cls.error_400_marshmallow(
                e.messages
            )
    return wrapper


def handle_400_bad_parameter(function):
    @wraps(function)
    def wrapper(cls, *args, **kwargs):
        try:
            return function(cls, *args, **kwargs)
        except BadParameterException as e:
            return cls.error_400(
                e.message
            )
    return wrapper


def handle_400_nonexistent_service(function):
    @wraps(function)
    def wrapper(cls, *args, **kwargs):
        try:
            return function(cls, *args, **kwargs)
        except BadTargetServiceException as e:
            return cls.error_400(
                e.message
            )
    return wrapper


def provide_body_data(function):
    @wraps(function)
    def wrapper(cls, *args, **kwargs):
        data = request.get_json()
        return function(cls, *args, data, **kwargs)
    return wrapper


def provide_parameters(function):
    @wraps(function)
    def wrapper(cls, *args, **kwargs):
        try:
            page, eq_filters, sort_by = cls.parse_parameters()
            return function(
                cls,
                *args,
                page=page,
                eq_filters=eq_filters,
                sort_by=sort_by,
                **kwargs
            )
        except BadParameterStringException as e:
            return cls.error_400(
                e.message
            )
    return wrapper


class BaseService:
    """In meta class, requires a model class, and a schema class,
    neither of which are an instantiated instance"""

    # store a registry of inherited service classes in a dict
    service_registry_dict = {}

    @classmethod
    def setup(cls):
        cls._register_service()

    @classmethod
    def _register_service(cls):
        type_ = cls.get_type()
        cls.service_registry_dict[type_] = cls

    @classmethod
    def is_enum_service(cls):
        return cls.Meta.schema.is_enum_schema()

    @classmethod
    def get_type(cls):
        return cls.Meta.schema.get_type()

    @classmethod
    def _split_filter_term(cls, filter_term):
        if '==' not in filter_term:
            raise BadParameterStringException(
                "There is no double equals sign in filter "
                f"term: '{filter_term}'."
            )
        (filter_key, filter_value) = filter_term.split('==', 1)
        # don't allow filtering against non public attributes
        if not cls.Meta.schema.attribute_is_public(filter_key):
            raise BadParameterStringException(
                f"The filter key '{filter_key}' is invalid."
            )
        return filter_key, filter_value

    @classmethod
    def _parse_filters(cls):
        filter_string = request.args.get('filter')
        if not filter_string:
            return None
        if not (
            filter_string.startswith('[') and
            filter_string.endswith(']')
        ):
            raise BadParameterStringException(
                'The entire filter query parameter must '
                'be enclosed in square brackets.'
            )
        filter_terms = [
            cls._split_filter_term(filter_term)
            for filter_term
            in filter_string[1:-1].split(',')
        ]
        return {
            filter_key: filter_value
            for (filter_key, filter_value)
            in filter_terms
        }

    @classmethod
    def _parse_sort_by(cls):
        sort_by_string = request.args.get('sort_by')
        if not sort_by_string:
            return None
        # if starts with minus sign, descending and strip the first character
        ascending = not sort_by_string.startswith('-')
        sort_by_string = sort_by_string if ascending else sort_by_string[1:]
        return (sort_by_string, ascending)

    @classmethod
    def parse_parameters(cls):
        page = request.args.get('page')
        eq_filters = cls._parse_filters()
        sort_by = cls._parse_sort_by()
        return page, eq_filters, sort_by

    @classmethod
    def error_400(cls, message):
        return cls._custom_error(
            "Bad Request",
            400,
            message
        )

    @classmethod
    def error_400_marshmallow(cls, messages):
        return messages, 400

    @classmethod
    def error_401(cls, message):
        return cls._custom_error(
            "Unauthorized",
            401,
            message
        )

    @classmethod
    def error_404(cls, id):
        return cls._custom_error(
            "Not Found",
            404,
            f"No {cls.get_type()} found with id {id}."
        )

    @classmethod
    def error_404_enum(cls, name):
        return cls._custom_error(
            "Not Found",
            404,
            f"No name '{name}' exists on enum {cls.get_type()}."
        )

    @classmethod
    def _custom_error(cls, title, code, detail):
        errors = [{
            "title": title,
            "code": code,
            "detail": detail
        }]
        response = {
            'errors': errors
        }
        return Response(
            mimetype="application/json",
            response=json.dumps(response),
            status=code
        )

    @classmethod
    def _get_target_service_by_name(cls, service_name):
        target_service = cls.service_registry_dict.get(service_name, None)
        if target_service is None:
            raise BadTargetServiceException(service_name)
        return target_service

    @classmethod
    def get_bulk_results_for_related_by_id(cls, id, calling_service, **kwargs):
        relation_model = calling_service.get_model()
        return cls.get_model().bulk_find_on_relation_id(relation_model, id, **kwargs)

    @classmethod
    def get_bulk_results_for_related_by_name(cls, name, calling_service, **kwargs):
        relation_model = calling_service.get_model()
        return cls.get_model().bulk_find_on_relation_name(
            relation_model,
            name,
            **kwargs
        )

    @classmethod
    def get_schema(cls, **kwargs):
        return cls.Meta.schema(**kwargs)

    @classmethod
    def get_model(cls):
        schema = cls.Meta.schema
        return schema.get_model()

    @classmethod
    def _update_model_instance(cls, old_model_instance, data, schema, user_id=None):
        new_model_instance = schema.load(
            data,
            instance=old_model_instance,
            partial=True
        )
        new_model_instance.save_update(user_id=user_id)
        return new_model_instance

    @classmethod
    @handle_404
    def read_by_id(cls, id, user_id=None):
        schema = cls.Meta.schema()
        model_instance = cls.Meta.model.find_by_id(id)
        return schema.dump(model_instance), 200

    @classmethod
    @provide_body_data
    @handle_400_db_integrity_error
    @handle_400_marshmallow_error
    @handle_404
    def update_by_id(cls, id, data, user_id=None):
        schema = cls.Meta.schema()
        old_model_instance = cls.Meta.model.find_by_id(id)
        new_model_instance = cls._update_model_instance(
            old_model_instance,
            data,
            schema,
            user_id=user_id
        )
        return schema.dump(new_model_instance), 200

    @classmethod
    @handle_400_db_integrity_error
    @handle_404
    def delete_by_id(cls, id, user_id=None):
        model_instance = cls.Meta.model.find_by_id(id)
        model_instance.delete()
        return None, 204

    @classmethod
    @provide_body_data
    @handle_400_db_integrity_error
    @handle_400_marshmallow_error
    def create(cls, data, user_id=None):
        schema = cls.Meta.schema()
        model_instance = schema.load(data)
        model_instance.save_create(user_id=user_id)
        return schema.dump(model_instance), 201

    @classmethod
    @provide_parameters
    @handle_400_bad_parameter
    def read_bulk(cls, user_id=None, **kwargs):
        schema = cls.Meta.schema(many=True)
        model_instances = cls.Meta.model.bulk_find(**kwargs)
        return schema.dump(model_instances), 200

    @classmethod
    @provide_parameters
    @handle_400_bad_parameter
    @handle_400_nonexistent_service
    @handle_404
    def read_bulk_related_by_id(cls, id, target_service_name, user_id=None, **kwargs):
        """
        Called on the service for the first part of the endpoint
        e.g. A in /A/{id}/B
        """
        target_service = cls._get_target_service_by_name(target_service_name)
        schema = target_service.get_schema(many=True)
        model_instances = target_service.get_bulk_results_for_related_by_id(id, cls, **kwargs)
        return schema.dump(model_instances), 200

    @classmethod
    @provide_parameters
    @handle_400_bad_parameter
    @handle_400_nonexistent_service
    @handle_404
    def read_bulk_related_by_name(cls, name, target_service_name, user_id=None, **kwargs):
        """
        Called on the service for the first part of the endpoint
        e.g. A in /A/{name}/B

        Used only for enum services
        """
        target_service = cls._get_target_service_by_name(target_service_name)
        schema = target_service.get_schema(many=True)
        model_instances = target_service.get_bulk_results_for_related_by_name(name, cls, **kwargs)
        return schema.dump(model_instances), 200

    @classmethod
    @handle_404
    def read_by_name(cls, name, user_id=None):
        """Used only for enum services"""
        schema = cls.Meta.schema()
        model_instance = cls.Meta.model.find_by_name(name)
        return schema.dump(model_instance), 200

    @classmethod
    @provide_body_data
    @handle_400_db_integrity_error
    @handle_400_marshmallow_error
    @handle_404
    def update_by_name(cls, name, data, user_id=None):
        """Used only for enum services"""
        schema = cls.Meta.schema()
        old_model_instance = cls.Meta.model.find_by_name(name)
        new_model_instance = cls._update_model_instance(
            old_model_instance,
            data,
            schema,
            user_id=user_id
        )
        return schema.dump(new_model_instance), 200

    @classmethod
    @handle_400_db_integrity_error
    @handle_404
    def delete_by_name(cls, name, user_id=None):
        """Used only for enum services"""
        model_instance = cls.Meta.model.find_by_name(name)
        model_instance.delete()
        return None, 204
