# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from flask_restx import Resource, Namespace

from marshmallow import ValidationError


def check_allowed(function):
    def wrapper(obj, *args, **kwargs):
        method = function.__name__
        resource = obj.name
        if method not in obj.allowed_methods:
            return {
                "error": f"Method '{method}' is not allowed" \
                         f" on resource '{resource}'."
            }, 405
        return function(obj, *args, **kwargs)
    return wrapper


class BaseResource(Resource):
    allowed_methods = []

    @classmethod
    def hide_disallowed_methods(cls):
        ALL_METHODS = ['get', 'post', 'patch', 'put', 'delete']
        disallowed_methods = [
            m for m in ALL_METHODS if m not in cls.allowed_methods
        ]
        for method in disallowed_methods:
            method_function = getattr(cls, method, None)
            if method_function is not None:
                cls.namespace.hide(method_function)


class BaseDetailResource(BaseResource):
    @check_allowed
    def get(self, id):
        _obj = self.schema.Meta.model.find_by_id(id)
        if _obj is None:
            return {
                "error": f"{self.name} with id '{id}' not found"
            }, 404
        return self.schema.dump(_obj), 200
    
    @check_allowed
    def patch(self, id, data):
        pass


class BaseListResource(BaseResource):
    @check_allowed
    def get(self):
        pass

    @check_allowed
    def post(self, data):
        try:
            _obj = self.schema.load(data)
            return self.schema.dump(_obj), 200
        except ValidationError as validation_error:
            return {
                "errorMessages": validation_error.messages
            }, 400


class BaseNamespace(Namespace):
    def add_resource(self, resource, *urls, **kwargs):
        resource.hide_disallowed_methods()
        super().add_resource(resource, *urls, **kwargs)
