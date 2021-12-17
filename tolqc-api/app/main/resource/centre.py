# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

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


@document_resource
class CentreListResource(BaseListResource):
    Meta = CentreResourceMeta
