# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import PlatformService
from main.swagger import PlatformSwagger

from .base import BaseListResource, BaseDetailResource, setup_resource


api_platform = PlatformSwagger.api


class PlatformResourceMeta:
    service = PlatformService
    swagger = PlatformSwagger


@setup_resource
class PlatformDetailResource(BaseDetailResource):
    Meta = PlatformResourceMeta


@setup_resource
class PlatformListResource(BaseListResource):
    Meta = PlatformResourceMeta
