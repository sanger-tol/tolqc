# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from flask_restx import Resource
from functools import wraps

from main.auth import auth
from main.swagger import BaseSwagger


PARAMS_DICT = {
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
}


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
            params=PARAMS_DICT,
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


def _document_relation_list_get(cls, relation):
    api, self_swagger = _get_api_swagger(cls)
    relation_swagger = BaseSwagger.get_registered_swagger(relation)
    relation_list_response_model = self_swagger.duplicate_relationship_swagger(
        relation_swagger
    )
    decorators = (
        api.doc(
            params=PARAMS_DICT,
            responses={
                '200': (
                    'Success',
                    relation_list_response_model,
                ),
                '400': 'Bad Request',
                '404': 'Not Found'
            }
        ),
        no_op_decorator
    )
    cls.get = _compose_decorators(cls.get, decorators)


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


def _document_relation_list_resource(cls, relation):
    api, _ = _get_api_swagger(cls)
    _document_relation_list_get(cls, relation)
    return api.route(f'/<int:id>/{relation}')(cls)


class BaseResource:
    @classmethod
    def add_list_resource(cls):
        type_ = cls.Meta.service.get_type()
        cls.list_resource = _document_list_resource(type(
            f'{type_.title()}ListResource',
            (BaseListResource,),
            {'Meta': cls.Meta}
        ))

    @classmethod
    def add_detail_resource(cls):
        type_ = cls.Meta.service.get_type()
        cls.detail_resource = _document_detail_resource(type(
            f'{type_.title()}DetailResource',
            (BaseDetailResource,),
            {'Meta': cls.Meta}
        ))

    @classmethod
    def add_relation_list_resources(cls):
        type_ = cls.Meta.service.get_type()
        relationship_names = cls.Meta.service.get_model() \
                                     .get_one_to_many_relationship_names()
        cls.relation_list_resources = [
            _document_relation_list_resource(type(
                f'{type_.title()}RelationDetailResource_{r_name}',
                (BaseRelationListResource,),
                {'Meta': cls.Meta, 'relation': r_name}
            ), r_name)
            for r_name in relationship_names
        ]


class BaseListResource(Resource):
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


class BaseRelationListResource(Resource):
    @classmethod
    def get(cls, id, user_id=None):
        return cls.Meta.service.read_bulk_by_related_id(
            id,
            cls.relation,
            user_id=user_id
        )

    @classmethod
    def auth_error(cls, message):
        return cls.Meta.service.error_401(message)


def setup_resource(cls):
    """Dynamically adds detail, list, and related list resources
    to a BaseResource inheritor."""
    cls.add_list_resource()
    cls.add_detail_resource()
    cls.add_relation_list_resources()
    return cls
