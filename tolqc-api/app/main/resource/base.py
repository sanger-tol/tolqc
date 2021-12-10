# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from flask_restx import Namespace, Resource
from sqlalchemy.exc import IntegrityError

from main.schema import InstanceDoesNotExistException, \
                        ValidationError
from main.model import ExtraFieldsNotPermittedException


class MissingResourceClassVariableException(Exception):
    """Thrown when a required class variable has not been
    declared on a resource"""
    def __init__(self, cls, class_variable):
        message = f"Resource '{cls.__name__}' is missing " \
                  f"required class variable '{class_variable}'"
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

    def add_resource(self, resource, *args, **kwargs):
        validate_resource(resource)
        super().add_resource(resource, *args, **kwargs)


def provide_body_data(function):
    def wrapper(obj, *args, **kwargs):
        data = obj.namespace.payload
        if obj.is_list_resource():
            # no id, return data straight after obj
            return function(obj, data, *args, **kwargs)
        else:
            # id is defined, and needs to go before data
            id = args[0]
            return function(obj, id, data, *args[1:], **kwargs)
    return wrapper


def handle_404(function):
    def wrapper(obj, id, *args, **kwargs):
        try:
            return function(obj, id, *args, **kwargs)
        except InstanceDoesNotExistException:
            return obj.error_404(id)
    return wrapper


def handle_400_extra_fields_not_permitted_error(function):
    def wrapper(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except ExtraFieldsNotPermittedException as e:
            return {
                "error": "Extra fields (" +
                         e.get_extra_fields_str() +
                         ") not permitted."
            }, 400
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


def handle_400_validation_error(function):
    def wrapper(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except ValidationError as e:
            return {
                "error": e.message
            }, 400
    return wrapper


def handle_400_bad_data_error(function):
    def wrapper(obj, *args, **kwargs):
        data = args[0] if obj.is_list_resource() else args[1]
        if not data:
            return {
                "error": "Data must be specified in the request"
                         " body, this cannot be empty."
            }, 400

        if obj.is_list_resource() and type(data) is not list:
            return {
                "error": "A list must be provided to this endpoint."
            }, 400

        if not obj.is_list_resource() and type(data) is not dict:
            return {
                "error": "A non-list object must be provided to this"
                         " endpoint."
            }, 400

        return function(obj, *args, **kwargs)
    return wrapper


class BaseResource(Resource):
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
            'schema',
            'namespace'
        ]
        for class_variable in required_class_variables:
            cls._check_class_variable(class_variable)


class BaseDetailResource(BaseResource):
    """Wrapper for flask-restx's Resource - provides default
    implementations of GET, DELETE, PUT methods for a detail
    resource

    Need to declare (as class variables):
    * name
    * namespace - for PUT requests
    * schema
    """

    @classmethod
    def is_list_resource(cls):
        return False

    def error_404(self, id):
        return {
            "error": f"No {self.name} with id {id} found."
        }, 404

    @handle_404
    def _get_by_id(self, id):
        model = self.schema.read_by_id(id)
        return model, 200

    @handle_400_db_integrity_error
    @handle_404
    def _delete_by_id(self, id):
        self.schema.delete_by_id(id)
        return {}, 204

    @provide_body_data
    @handle_400_db_integrity_error
    @handle_400_validation_error
    @handle_400_bad_data_error
    @handle_400_extra_fields_not_permitted_error
    @handle_404
    def _put_by_id(self, id, data):
        # N.B., the process_body_data decorator provides the data,
        # _do not_ provide it in the call signature, only id, i.e.:
        # use _put_by_id(id) not _put_by_id(id, data)
        model = self.schema.update_by_id(
            id,
            data
        )
        return model, 200


class BaseListResource(BaseResource):
    """Wrapper for flask-restx's Resource - provides default
    implementations of a POST method for a list resource

    Need to declare (as class variables):
    * name
    * namespace
    * schema
    """

    @classmethod
    def is_list_resource(cls):
        return True

    @provide_body_data
    @handle_400_bad_data_error
    def _post(self, data):
        # N.B., the provide_body_decorator adds the data,
        # _do not_ provide it in the call signature, i.e.
        # use _post() not _post(data)
        return self.schema.create_bulk(data), 200

    def _get(self):
        return self.schema.read_bulk(), 200
