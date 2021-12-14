# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

import json

from flask import Response
from flask_sqlalchemy import model


class InstanceDoesNotExistException(Exception):
    def __init__(self, id, model_instance):
        super().__init__(
            f"No {model_instance.__tablename__}"
            f" instance exists with id {id}."
        )


class BaseService:
    @classmethod
    def _get_type(cls):
        return cls.Meta.model.__tablename__

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
            "detail": detail if detail else "An unknown error occured"
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
        # TODO move this into an "error schema"
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
    def get_by_id(cls, id):
        model_instance = cls.Meta.model.find_by_id(id)
        if model_instance is None:
            return cls.custom_individual_error(
                "Not Found",
                404,
                f"No {cls._get_type()} found with id {id}."
            )
        return cls.Meta.detail_schema.dump(model_instance)
