# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import PlatformService
from main.swagger import PlatformSwagger

from .base import BaseResource, setup_resource


api_platform = PlatformSwagger.api


@setup_resource
class PlatformResource(BaseResource):
    class Meta:
        service = PlatformService
        swagger = PlatformSwagger
