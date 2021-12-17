# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

import json

from flask import Response, request

from main.model import InstanceDoesNotExistException


def handle_404(function):
    def wrapper(cls, id, *args, **kwargs):
        try:
            return function(cls, id, *args, **kwargs)
        except InstanceDoesNotExistException:
            return cls.error_404(id)
    return wrapper


def provide_body_data(function):
    def wrapper(*args, **kwargs):
        data = request.get_json()
        return function(*args, data, **kwargs)
    return wrapper


class BaseService:
    """In meta class, requires a model class, and a schema object"""
    @classmethod
    def _get_type(cls):
        return cls.Meta.schema.get_type()

    @classmethod
    def error_404(cls, id):
        return cls.custom_individual_error(
            "Not Found",
            404,
            f"No {cls._get_type()} found with id {id}."
        )

    @classmethod
    def _split_error_components(cls, errors):
        titles = [e.get('title', None) for e in errors]
        codes = [e.get('code', None) for e in errors]
        details = [e.get('detail', None) for e in errors]

        return titles, codes, details

    @classmethod
    def _format_error(cls, title, code, detail):
        return {
            "title": title if title else "Internal Server Error",
            "code": code if code else 500,
            "detail": detail if detail else "An unknown error occurred."
        }

    @classmethod
    def custom_post_partial_error(cls, errors=[]):
        titles, codes, details = cls._split_error_components(errors)

        error_messages = [
            None
            if t is None and c is None and d is None
            else cls._format_error(t, c, d)
            for (t, c, d) in zip(titles, codes, details)
        ]

        return {
            'errors': error_messages
        }

    @classmethod
    def custom_errors(cls, status_code=500, errors=[]):
        """Expects a list of dicts, with keys 'title', 'code', and 'detail"""

        titles, codes, details = cls._split_error_components(errors)
        error_messages = [
            cls._format_error(t, c, d)
            for (t, c, d) in zip(titles, codes, details)
        ]

        response = {
            'errors': error_messages
        }

        return Response(
            mimetype="application/json",
            response=json.dumps(response),
            status=status_code
        )

    @classmethod
    def custom_individual_error(cls, title, code, detail):
        return cls.custom_errors(code, errors=[{
            "title": title,
            "code": code,
            "detail": detail
        }])

    @classmethod
    @handle_404
    def read_by_id(cls, id, user_id=None):
        model_instance = cls.Meta.model.find_by_id(id)
        return cls.Meta.schema.dump(model_instance), 200

    @classmethod
    @provide_body_data
    @handle_404
    def update_by_id(cls, id, data, user_id=None):
        schema = cls.Meta.schema
        old_model_instance = cls.Meta.model.find_by_id(id)
        new_model_instance = schema.load(
            data,
            instance=old_model_instance,
            partial=True
        )
        # TODO add ext column procedure here
        new_model_instance.save()
        return schema.dump(new_model_instance), 200

    @classmethod
    @handle_404
    def delete_by_id(cls, id, user_id=None):
        model_instance = cls.Meta.model.find_by_id(id)
        model_instance.delete()
        return None, 204

    @classmethod
    @provide_body_data
    def create(cls, data, user_id=None):
        schema = cls.Meta.schema
        model_instance = schema.load(data)
        cls.Meta.model.save(model_instance)
        return schema.dump(model_instance), 201
