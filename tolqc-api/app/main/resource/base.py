# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from flask_restx import Resource

from main.auth import auth

def _compose_decorators(function, *decorators):
    decorators = reversed(decorators)
    func = function.__func__
    for d in decorators:
        func = d(func)
    return func
            

def _document_list_resource(cls):
    swagger = cls.Meta.swagger
    api = swagger.api

    #cls.post = api.expect(swagger.post_request_model)(cls.post.__func__)
    decorators = (
        api.expect(swagger.post_request_model),
        api.response(201, description="Created"),
        auth(api)
    )
    cls.post = _compose_decorators(cls.post, *decorators)

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
