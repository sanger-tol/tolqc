# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import CobiontService
from main.swagger import CobiontSwagger

from .base import BaseListResource, BaseDetailResource, setup_resource


api_Cobiont = CobiontSwagger.api


class CobiontResourceMeta:
    service = CobiontService
    swagger = CobiontSwagger


@setup_resource
class CobiontDetailResource(BaseDetailResource):
    Meta = CobiontResourceMeta


@setup_resource
class CobiontListResource(BaseListResource):
    Meta = CobiontResourceMeta
