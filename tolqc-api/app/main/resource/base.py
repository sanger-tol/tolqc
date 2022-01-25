# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from flask_restx import Resource
from functools import wraps

from main.auth import auth


def no_op_decorator(function):
    """Necessary as a substitute for the auth decorator"""
    @wraps(function)
    def wrapper(*args, **kwargs):
        return function(*args, **kwargs)
    return wrapper


def _compose_decorators(function, decorators):
    decorators = reversed(decorators)
    func = function.__func__
    for d in decorators:
        func = d(func)
    return func


def _get_api_swagger(cls):
    swagger = cls.Meta.swagger
    api = swagger.api
    return api, swagger


def _document_detail_get(cls):
    api, swagger = _get_api_swagger(cls)
    decorators = (
        api.response(
            200,
            description='Success',
            model=swagger.individual_response_model
        ),
        api.response(404, description='Not Found'),
        no_op_decorator
    )
    cls.get = _compose_decorators(cls.get, decorators)


def _document_patch(cls):
    api, swagger = _get_api_swagger(cls)
    decorators = (
        api.expect(swagger.request_model),
        api.response(
            200,
            description='Success',
            model=swagger.individual_response_model
        ),
        api.response(400, description='Bad Request'),
        api.response(404, description='Not Found'),
        auth(api)
    )
    cls.patch = _compose_decorators(cls.patch, decorators)


def _document_delete(cls):
    api, _ = _get_api_swagger(cls)
    decorators = (
        api.response(204, description='Success'),
        api.response(400, description='Bad Request'),
        api.response(404, description='Not Found'),
        auth(api)
    )
    cls.delete = _compose_decorators(cls.delete, decorators)


def _document_list_get(cls):
    api, swagger = _get_api_swagger(cls)
    decorators = (
        api.doc(
            params={
                'page': {
                    'in': 'query',
                    'type': 'integer',
                    'description': 'The page of the results'
                },
                'sort_by': {
                    'in': 'query',
                    'description': 'The field by which to order results. '
                                   'Prepend with a minus sign to sort '
                                   'descending, e.g. -name, otherwise sorting '
                                   'will be ascending. (Sorts by id ascending '
                                   'by default).'
                },
                'filter': {
                    'in': 'query',
                    'description': 'Filters by equality. Formatted '
                                   'like [key1==value1,key2==value2]. '
                                   'Delimit strings with " or \', e.g. "string".'
                }
            },
            responses={
                '200': (
                    'Success',
                    swagger.bulk_response_model,
                ),
                '400': 'Bad Request'
            }
        ),
        no_op_decorator
    )
    cls.get = _compose_decorators(cls.get, decorators)


def _document_post(cls):
    api, swagger = _get_api_swagger(cls)
    decorators = (
        api.expect(swagger.request_model),
        api.response(
            201,
            description="Created",
            model=swagger.individual_response_model
        ),
        api.response(400, description='Bad Request'),
        auth(api)
    )
    cls.post = _compose_decorators(cls.post, decorators)


def _document_list_resource(cls):
    api, _ = _get_api_swagger(cls)
    _document_list_get(cls)
    _document_post(cls)
    return api.route('')(cls)


def _document_detail_resource(cls):
    api, _ = _get_api_swagger(cls)
    _document_detail_get(cls)
    _document_patch(cls)
    _document_delete(cls)
    return api.route('/<int:id>')(cls)



class BaseResource(Resource):
    pass


class BaseListResource(Resource):
    @classmethod
    def is_list_resource(cls):
        return True

    @classmethod
    def get(cls, user_id=None):
        return cls.Meta.service.read_bulk(user_id=user_id)

    @classmethod
    def post(cls, user_id=None):
        return cls.Meta.service.create(user_id=user_id)

    @classmethod
    def auth_error(cls, message):
        return cls.Meta.service.error_401(message)


class BaseDetailResource(Resource):
    @classmethod
    def is_list_resource(cls):
        return False

    @classmethod
    def get(cls, id, user_id=None):
        return cls.Meta.service.read_by_id(id, user_id=user_id)

    @classmethod
    def patch(cls, id, user_id=None):
        return cls.Meta.service.update_by_id(id, user_id=user_id)

    @classmethod
    def delete(cls, id, user_id=None):
        return cls.Meta.service.delete_by_id(id, user_id=user_id)

    @classmethod
    def auth_error(cls, message):
        return cls.Meta.service.error_401(message)


def setup_resource(cls):
    """Dynamically adds detail, list, and related list resources
    to a BaseResource inheritor."""
    type_ = cls.Meta.service.get_type()
    cls.list_resource = _document_list_resource(type(
        f'{type_.title()}ListResource',
        (BaseListResource,),
        {}
    ))
    cls.detail_resource = _document_detail_resource(type(
        f'{type_.title()}DetailResource',
        (BaseListResource,),
        {}
    ))
    return cls
