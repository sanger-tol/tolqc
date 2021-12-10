# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main import model
from functools import wraps
from flask import request, abort
from flask_restx import Namespace


def check_key_valid(api_key):
    user_id = model.TolqcUser.get_user_infos_by_api_key(api_key)
    if not user_id:
        abort(401, "User does not exist")
    return user_id


def auth_dec():
    def warp_decorator(function):
        @wraps(function)
        def decorated(*args, **kwargs):
            api_key = request.headers.get('Authorization')
            if not api_key:
                abort(401, "Api key is missing")
            check_key_valid(api_key)
            return function(*args, **kwargs)
        return decorated
    return warp_decorator


def auth(namespace: Namespace):
    decs = (namespace.doc(security=['ApiKeyAuth']), auth_dec())

    def deco(func):
        for dec in reversed(decs):
            func = dec(func)
        return func
    return deco
