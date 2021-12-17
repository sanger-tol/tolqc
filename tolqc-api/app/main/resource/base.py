# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from flask_restx import Resource

from main.auth import auth


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


def _document_post(cls):
    api, swagger = _get_api_swagger(cls)
    decorators = (
        api.expect(swagger.post_request_model),
        api.response(201, description="Created"),
        auth(api)
    )
    cls.post = _compose_decorators(cls.post, decorators)
            

def _document_list_resource(cls):
    api, _ = _get_api_swagger(cls)    
    _document_post(cls)
    return api.route('')(cls)


def document_resource(cls):
    if cls.is_list_resource():
        return _document_list_resource(cls)
        

class BaseListResource(Resource):        
    @classmethod
    def is_list_resource(cls):
        return True

    @classmethod
    def post(cls, user_id=None):
        return cls.Meta.service.create(user_id=user_id)
