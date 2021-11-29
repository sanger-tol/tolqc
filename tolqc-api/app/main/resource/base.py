# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from flask_restx import Namespace, Resource

from main.schema import RowDoesNotExistException


class BaseNamespace(Namespace):
    """Wrapper for flask-restx's Namespace - always validates
    input using Marshmallow"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, validate=True, **kwargs)


class BaseDetailResource(Resource):
    """Wrapper for flask-restx's Resource - provides default
    implementations of GET, DELETE, PUT methods for a detail
    resource

    Requires class/static variables request_schema and
    response_schema to be declared in inherited classes, and a
    name to be declared for errors
    """
    name = 'base'

    def _404_error(self, id):
        return {
            "error": f"{self.name} with {id} not found."
        }, 404

    def _get_by_id(self, id):
        try:
            model = self.response_schema.get_by_id(id)
            return model, 200
        except RowDoesNotExistException:
            return self._404_error(id)

    # TODO add auth
    # TODO add deletion conflict exception
    def _delete_by_id(self, id):
        try:
            self.response_schema.delete_by_id(id)
            return {}, 204
        except RowDoesNotExistException:
            return self._404_error(id)
