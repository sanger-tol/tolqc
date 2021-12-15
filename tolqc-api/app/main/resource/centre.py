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
        description='Success',
        model=CentreSwagger.detail_response_model,
    )
    @api_centre.response(
        404,
        description='Not Found'
    )
    def get(self, id):
        return CentreService.read_by_id(id)

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

    @api_centre.expect(CentreSwagger.put_request_model)
    @api_centre.response(
        200,
        description='Success',
        model=CentreSwagger.detail_response_model
    )
    @api_centre.response(
        400,
        description='Bad Request'
    )
    @api_centre.response(
        404,
        description='Not Found'
    )
    @auth(api_centre)
    def put(self, id, user_id=None):
        return CentreService.put_by_id(id, user_id=user_id)


@api_centre.route('')
class BaseListResource(Resource):
    @api_centre.expect(CentreSwagger.post_request_model)
    @auth(api_centre)
    def post(self, user_id=None):
        return CentreService.post_bulk(user_id=user_id)
