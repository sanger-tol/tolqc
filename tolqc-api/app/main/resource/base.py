# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from flask_restx import Resource
from functools import wraps

from main.auth import auth


def make_auth(func):
    def wrapper(cls, *args, **kwargs):
        import logging
        logging.warning("HELLO THERE")
        if getattr(cls, "Meta", None) is None:
            logging.warning("no meta class on class " + cls.__name__)
            return func(cls, *args, **kwargs)
        logging.warning("api exists on class " + cls.__name__)
        api = cls.Meta.swagger.api
        return auth(api)(func(cls, *args, **kwargs))
    return wrapper

def compose(*functions):
    #TODO see if reversed() works instead
    functions = functions[::-1] 
    def wrapper(val):
        for d in functions:
            val = d(val)
        return val
    return wrapper
            

def _document_list_resource(cls):
    swagger = cls.Meta.swagger
    api = swagger.api

    cls.post = api.expect(swagger.post_request_model)(cls.post.__func__)

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
