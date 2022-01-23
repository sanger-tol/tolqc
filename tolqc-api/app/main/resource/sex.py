# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import SexService
from main.swagger import SexSwagger

from .base import BaseListResource, BaseDetailResource, setup_resource


api_sex = SexSwagger.api


class SexResourceMeta:
    service = SexService
    swagger = SexSwagger


@setup_resource
class SexDetailResource(BaseDetailResource):
    Meta = SexResourceMeta


@setup_resource
class SexListResource(BaseListResource):
    Meta = SexResourceMeta
