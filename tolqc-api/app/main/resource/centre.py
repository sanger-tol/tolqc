# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from flask_restx import Resource

from main.auth import auth
from main.service import CentreService
from main.swagger import CentreSwagger


api_centre = CentreSwagger.api


@api_centre.route('/<int:id>')
class CentreDetailResource(Resource):
    @api_centre.response(
        200,
        description='Success'
    )
    @api_centre.response(
        404,
        description='Not Found'
    )
    def get(self, id, user_id=None):
        return CentreService.read_by_id(id, user_id=user_id)

    @api_centre.response(
        204,
        description='Success'
    )
    @api_centre.response(
        404,
        description='Not Found'
    )
    @auth(api_centre)
    def delete(self, id, user_id=None):
        return CentreService.delete_by_id(id, user_id=user_id)

    @api_centre.expect(CentreSwagger.patch_request_model)
    @api_centre.response(
        200,
        description='Success'
    )
    @api_centre.response(
        404,
        description='Not Found'
    )
    @auth(api_centre)
    def patch(self, id, user_id=None):
        return CentreService.update_by_id(id, user_id=user_id)


@api_centre.route('')
class BaseListResource(Resource):
    @api_centre.expect(CentreSwagger.post_request_model)
    @api_centre.response(
        201,
        description='Created'
    )
    @auth(api_centre)
    def post(self, user_id=None):
        return CentreService.create(user_id=user_id)
