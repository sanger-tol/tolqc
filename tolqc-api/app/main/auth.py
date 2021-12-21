# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model import TolqcUser
from functools import wraps
from flask import request
from flask_restx import Namespace


authorizations = {
    'ApiKeyAuth': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}


def check_key_valid(api_key):
    user_id = TolqcUser.get_user_infos_by_api_key(api_key)
    return user_id


def auth_dec():
    def wrap_decorator(function):
        @wraps(function)
        def decorated(resource, *args, **kwargs):
            api_key = request.headers.get('Authorization')
            if not api_key:
                return resource.auth_error("Api key is missing")
            user_id = check_key_valid(api_key)
            if user_id is None:
                return resource.auth_error("User does not exist")
            return function(resource, *args, user_id=user_id, **kwargs)
        return decorated
    return wrap_decorator


def auth(namespace: Namespace):
    decs = (
        namespace.response(401, description='Unauthorized'),
        namespace.doc(security=['ApiKeyAuth']),
        auth_dec()
    )

    def deco(func):
        for dec in reversed(decs):
            func = dec(func)
        return func
    return deco
