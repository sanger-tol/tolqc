# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from flask_restx import Namespace, Resource
from sqlalchemy.exc import IntegrityError

from main.schema import InstanceDoesNotExistException, \
                        IdSpecifiedInRequestBodyException


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
    input, and will try to validate each
    resource's class variables - do not use for namespaces
    containing custom resources without these"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, validate=True, **kwargs)

    def add_resource(self, resource, *args, **kwargs):
        validate_resource(resource)
        super().add_resource(resource, *args, **kwargs)


def provide_body_data(function):
    def wrapper(obj, *args, **kwargs):
        data = obj.namespace.payload
        return function(obj, data, *args, **kwargs)
    return wrapper


def handle_404(function):
    def wrapper(obj, id, *args, **kwargs):
        try:
            return function(obj, id, *args, **kwargs)
        except InstanceDoesNotExistException:
            return obj.error_404(id)
    return wrapper


def handle_400_db_integrity_error(function):
    def wrapper(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except IntegrityError:
            return {
                "error": "Integrity error, most likely due to"
                         " bad foreign keys specified, or, for "
                         "DELETE - other instances depend on the"
                         " specified instance."
            }, 400
    return wrapper


def handle_400_id_in_body_error(function):
    def wrapper(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except IdSpecifiedInRequestBodyException:
            return {
                "error": "An id must not be specified in the "
                         "body of a request to this endpoint."
            }, 400
    return wrapper

def handle_400_empty_request_body(function):
    def wrapper(obj, data, *args, **kwargs):
        if not data:
            return {
                "error": "Data must be specified in the request"
                         " body, this cannot be empty."
            }, 404
        return function(obj, data, *args, **kwargs)
    return wrapper


class BaseDetailResource(Resource):
    """Wrapper for flask-restx's Resource - provides default
    implementations of GET, DELETE, PUT methods for a detail
    resource

    Need to declare (as class variables):
    * name
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

    @handle_404
    def _get_by_id(self, id):
        model = self.response_schema.read_by_id(id)
        return model, 200

    # TODO add auth
    # TODO add deletion conflict exception
    @handle_400_db_integrity_error
    @handle_404
    def _delete_by_id(self, id):
        self.response_schema.delete_by_id(id)
        return {}, 204

    @provide_body_data
    @handle_400_db_integrity_error
    @handle_400_id_in_body_error
    @handle_400_empty_request_body
    @handle_404
    def _put_by_id(self, data, id):
        # N.B., the process_body_data decorator provides the data,
        # _do not_ provide it in the call signature, only id, i.e.:
        # use _put_by_id(id) not _put_by_id(data, id)
        model = self.response_schema.update_by_id(
            id,
            data
        )
        return model, 200


class BaseListResource(Resource):
    """Wrapper for flask-restx's Resource - provides default
    implementations of a POST method for a list resource

    Need to declare (as class variables):
    * name
    * namespace
    * request_schema
    * response_schema
    """

    # TODO modify to accept multiple instances in one go
    @provide_body_data
    @handle_400_id_in_body_error
    @handle_400_db_integrity_error
    @handle_400_empty_request_body
    def _post(self, data):
        # N.B., the process_body_decorator provides the data,
        # _do not_ provide it in the call signature, i.e.
        # use _post() not _post(data)
        return self.response_schema.dump(
            self.request_schema.create(data)
        ), 200
