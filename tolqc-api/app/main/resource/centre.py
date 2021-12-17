# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from flask_restx import Resource

from main.auth import auth
from main.service import CentreService
from main.swagger import CentreSwagger

from .base import BaseListResource, BaseDetailResource, document_resource


api_centre = CentreSwagger.api


class CentreResourceMeta:
    service = CentreService
    swagger = CentreSwagger


@document_resource
class CentreDetailResource(BaseDetailResource):
    Meta = CentreResourceMeta

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


@document_resource
class CentreListResource(BaseListResource):
    Meta = CentreResourceMeta
