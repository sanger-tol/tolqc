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
        return CentreService.get_by_id(id)

    @api_centre.response(
        204,
        description='Success'
    )
    @api_centre.response(
        404,
        description='Not Found'
    )
    @auth(api_centre)
    def delete(self, id):
        return CentreService.delete_by_id(id)

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
    def put(self, id, data):
        return CentreService.put_by_id(id, data)
