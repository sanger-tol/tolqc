# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from flask_restx import Resource


def check_allowed(function):
    def wrapper(obj, *args, **kwargs):
        method = function.__name__
        resource = obj.name
        if method in obj.disallowed_methods:
            return {
                "error": f"Method '{method}' is not an allowed" \
                         f" method on resource {resource}."
            }, 405
        return function(obj, *args, **kwargs)
    return wrapper


class BaseResource(Resource):
    disallowed_methods = []

    @check_allowed
    def get(self, id):
        _obj = self.schema.Meta.model.find_by_id(id)
        if _obj is None:
            return {
                "error": f"{self.name} with id '{id}' not found"
            }, 404

        return self.schema.dump(_obj), 200
