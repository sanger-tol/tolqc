# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main import model
from functools import wraps
from flask import request
from main.custom_exception import CustomException

def check_key_valid(api_key):
    user_id = model.TolqcUser.get_user_infos_by_api_key(api_key)
    if not user_id:
        raise CustomException(401, "User does not exist")
    return user_id

def require_auth():
    def warp_decorator(function):
        @wraps(function)
        def decorated(*args, **kwargs):
            api_key = request.headers.get('Authorization')
            if not api_key:
                raise CustomException(401, "Api key is missing")
            user = check_key_valid(api_key)
            request_data = dict(user_id=user.id, **kwargs)
            return function(*args, request_data)

        return decorated
    return warp_decorator
