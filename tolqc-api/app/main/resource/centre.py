# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import CentreService
from main.swagger import CentreSwagger

from .base import BaseListResource, BaseDetailResource, setup_resource


api_centre = CentreSwagger.api


class CentreResourceMeta:
    service = CentreService
    swagger = CentreSwagger


@setup_resource
class CentreDetailResource(BaseDetailResource):
    Meta = CentreResourceMeta


@setup_resource
class CentreListResource(BaseListResource):
    Meta = CentreResourceMeta
