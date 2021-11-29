# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from flask_restx import Namespace, Resource

from main.schema import InstanceDoesNotExistException


class MissingResourceClassVariableException(Exception):
    """Thrown when a required class variable has not been
    declared on a resource"""
    def __init__(self, cls, class_variable):
        message = f"Resource '{cls.__name__}'' is missing " \
                  f"class variable '{class_variable}'"
        super().__init__(message)


def validate_resource(resource):
    if getattr(
            resource,
            'check_class_variables',
            None
        ) is not None:
            resource.check_class_variables()


class BaseNamespace(Namespace):
    """Wrapper for flask-restx's Namespace - always validates
    input using Marshmallow, and will try to validate each
    resource's class variables"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, validate=True, **kwargs)
    
    def add_resource(self, resource, *args, **kwargs):
        validate_resource(resource)
        super().add_resource(resource, *args, **kwargs)


class BaseDetailResource(Resource):
    """Wrapper for flask-restx's Resource - provides default
    implementations of GET, DELETE, PUT methods for a detail
    resource

    Need to declare (as class variables):
    * name - for custom error messages
    * namespace - for PUT requests
    * request_schema
    * response_schema
    """

    @classmethod
    def _check_class_variable(cls, class_variable):
        if not hasattr(cls, class_variable):
            raise MissingResourceClassVariableException(
                cls,
                class_variable
            )

    @classmethod
    def check_class_variables(cls):
        required_class_variables = [
            'name',
            'request_schema',
            'response_schema',
            'namespace'
        ]
        for class_variable in required_class_variables:
            cls._check_class_variable(class_variable)

    def _404_error(self, id):
        return {
            "error": f"No {self.name} with id {id} found."
        }, 404

    def _get_by_id(self, id):
        try:
            model = self.response_schema.get_by_id(id)
            return model, 200
        except InstanceDoesNotExistException:
            return self._404_error(id)

    # TODO add auth
    # TODO add deletion conflict exception
    def _delete_by_id(self, id):
        try:
            self.response_schema.delete_by_id(id)
            return {}, 204
        except InstanceDoesNotExistException:
            return self._404_error(id)

    def _put_by_id(self, id):
        try:
            model = self.response_schema.put_by_id(
                id,
                self.namespace.payload
            )
            return model, 200
        except InstanceDoesNotExistException:
            return self._404_error(id)
