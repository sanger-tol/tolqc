# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from flask_restx import Resource as FlaskRestxResource
from functools import wraps

from main.auth import auth


LIST_GET_PARAMS_DICT = {
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
            params=LIST_GET_PARAMS_DICT,
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


def _document_relation_list_get(cls, relation_name):
    api, swagger = _get_api_swagger(cls)
    decorators = (
        api.doc(
            params=LIST_GET_PARAMS_DICT,
            responses={
                '200': (
                    'Success',
                    swagger.get_relation_list_get_swagger_model(
                        relation_name
                    ),
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


def _document_enum_detail_resource(cls):
    api, _ = _get_api_swagger(cls)
    _document_detail_get(cls)
    _document_patch(cls)
    _document_delete(cls)
    return api.route('/<name>')(cls)


class BaseResource:
    @classmethod
    def is_enum_resource(cls):
        return cls.Meta.service.is_enum_service()

    @classmethod
    def _setup_non_enum_resource(cls):
        cls.add_list_resource()
        cls.add_detail_resource()
        #TODO remove relationships in schema/swagger to and from enums
        cls.populate_relation_list_get_swaggers()
        cls.add_relation_list_resources()

    @classmethod
    def _setup_enum_resource(cls):
        cls.add_list_resource()
        cls.add_enum_detail_resource()

    @classmethod
    def setup(cls):
        if cls.is_enum_resource():
            cls._setup_enum_resource()
        else:
            cls._setup_non_enum_resource()

    @classmethod
    def populate_relation_list_get_swaggers(cls):
        relationship_names = cls.Meta.service.get_model() \
                                     .get_one_to_many_relationship_names()
        cls.Meta.swagger.duplicate_relationship_swaggers(relationship_names)

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
    def _declare_and_decorate_relation_list_resource(cls, relation_name):
        type_ = cls.Meta.service.get_type()
        declared = type(
            f'{type_.title()}RelationListResource_{relation_name}',
            (BaseRelationListResource,),
            {'Meta': cls.Meta, 'relation': relation_name}
        )
        return _document_relation_list_resource(declared, relation_name)

    @classmethod
    def add_relation_list_resources(cls):
        relationship_names = cls.Meta.service.get_model() \
                                     .get_one_to_many_relationship_names()
        cls.relation_list_resources = [
            cls._declare_and_decorate_relation_list_resource(r_name)
            for r_name in relationship_names
        ]

    @classmethod
    def add_enum_detail_resource(cls):
        type_ = cls.Meta.service.get_type()
        cls.detail_resource = _document_enum_detail_resource(type(
            f'{type_.title()}DetailResource',
            (BaseEnumNameDetailResource,),
            {'Meta': cls.Meta}
        ))


class Resource(FlaskRestxResource):
    @classmethod
    def auth_error(cls, message):
        return cls.Meta.service.error_401(message)


class BaseListResource(Resource):
    @classmethod
    def get(cls, user_id=None):
        return cls.Meta.service.read_bulk(user_id=user_id)

    @classmethod
    def post(cls, user_id=None):
        return cls.Meta.service.create(user_id=user_id)


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


class BaseEnumNameDetailResource(Resource):
    @classmethod
    def get(cls, name, user_id=None):
        return cls.Meta.service.read_by_name(name, user_id=user_id)

    @classmethod
    def patch(cls, name, user_id=None):
        return cls.Meta.service.update_by_name(name, user_id=user_id)

    @classmethod
    def delete(cls, name, user_id=None):
        return cls.Meta.service.delete_by_name(name, user_id=user_id)


class BaseRelationListResource(Resource):
    @classmethod
    def get(cls, id, user_id=None):
        return cls.Meta.service.read_bulk_related_by_id(
            id,
            cls.relation,
            user_id=user_id
        )


class BaseEnumNameRelationListResource(Resource):
    @classmethod
    def get(cls, name, user_id=None):
        return cls.Meta.service.read_bulk_related_by_name(
            name,
            cls.relation,
            user_id=user_id
        )


def setup_resource(cls):
    """Dynamically adds detail, list, and related list resources
    to a BaseResource inheritor."""
    cls.setup()
    return cls
