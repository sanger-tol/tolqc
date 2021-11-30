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
    resource's class variables - do not use for namespaces
    containing custom resources without these"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, validate=True, **kwargs)

    def add_resource(self, resource, *args, **kwargs):
        validate_resource(resource)
        super().add_resource(resource, *args, **kwargs)


def handle_404(function):
    def wrapper(obj, id, *args, **kwargs):
        try:
            return function(obj, id, *args, **kwargs)
        except InstanceDoesNotExistException:
            return obj.error_404(id)
    return wrapper


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

    def error_404(self, id):
        return {
            "error": f"No {self.name} with id {id} found."
        }, 404
    
    def _error_400_empty_put_request(self):
        return {
            "error": "Data must be specified in the body "
                     "of a PUT request"
        }, 400

    @handle_404
    def _get_by_id(self, id):
        model = self.response_schema.read_by_id(id)
        return model, 200

    # TODO add auth
    # TODO add deletion conflict exception
    @handle_404
    def _delete_by_id(self, id):
        self.response_schema.delete_by_id(id)
        return {}, 204

    @handle_404
    def _put_by_id(self, id):
        data = self.namespace.payload
        if not data:
            return self._error_400_empty_put_request()
        model = self.response_schema.update_by_id(
            id,
            data
        )
        return model, 200
