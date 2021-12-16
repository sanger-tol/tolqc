# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from flask_restx import Resource

from main.auth import auth


def document_list_resource(cls):
    api = cls.Meta.api
    swagger = cls.Meta.swagger

    decorators = (
        api.expect(swagger.post_request_model),
        api.response(201, description='Created'),
        auth(api),
    )

    post_func = getattr(cls, "post")

    for d in reversed(decorators):
        post_func = d(post_func)
    
    setattr(cls, 'post', post_func)

    return api.route('')(cls)

class BaseListResource(Resource):
    def post(self, user_id=None):
        return self.Meta.service.create(user_id=user_id)
