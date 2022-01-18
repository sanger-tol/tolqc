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
                       BadParameterException


class MalformedFilterStringException(Exception):
    pass


def handle_404(function):
    @wraps(function)
    def wrapper(cls, id, *args, **kwargs):
        try:
            return function(cls, id, *args, **kwargs)
        except InstanceDoesNotExistException:
            return cls.error_404(id)
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
            page, eq_filters = cls.parse_parameters()
            return function(
                cls,
                *args,
                page=page,
                eq_filters=eq_filters,
                **kwargs
            )
        except MalformedFilterStringException:
            return cls.error_400(
                "The filter query parameter in the URL is malformed."
            )
    return wrapper


class BaseService:
    """In meta class, requires a model class, and a schema class,
    neither of which are an instantiated instance"""
    @classmethod
    def _get_type(cls):
        return cls.Meta.schema.get_type()

    @classmethod
    def _split_filter_term(cls, filter_term):
        (filter_key, filter_value) = filter_term.split('==', 1)
        return filter_key, filter_value

    @classmethod
    def _parse_filters(cls, filter_string):
        if not filter_string:
            return None
        if not (
            filter_string.startswith('[') and
            filter_string.endswith(']')
        ):
            raise MalformedFilterStringException()
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
    def parse_parameters(cls):
        page = request.args.get('page')
        filter_string = request.args.get('filter')
        eq_filters = cls._parse_filters(filter_string)
        return page, eq_filters

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
            f"No {cls._get_type()} found with id {id}."
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
        new_model_instance = schema.load(
            data,
            instance=old_model_instance,
            partial=True
        )
        new_model_instance.save()
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
        model_instance.created_by = user_id
        cls.Meta.model.save(model_instance)
        return schema.dump(model_instance), 201

    @classmethod
    @provide_parameters
    @handle_400_bad_parameter
    def read_bulk(cls, page=1, eq_filters={}, user_id=None):
        schema = cls.Meta.schema(many=True)
        model_instances = cls.Meta.model.find_bulk(page, eq_filters)
        return schema.dump(model_instances), 200
