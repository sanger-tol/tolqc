# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import PlatformService
from main.swagger import PlatformSwagger

from .base import AutoResourceGroup, setup_resource


api_platform = PlatformSwagger.api


@setup_resource
class PlatformResource(AutoResourceGroup):
    class Meta:
        service = PlatformService
        swagger = PlatformSwagger
