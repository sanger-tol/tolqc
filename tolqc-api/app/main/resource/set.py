# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import SetService
from main.swagger import SetSwagger

from .base import AutoResourceGroup, setup_resource_group


api_set = SetSwagger.api


@setup_resource_group
class SetResourceGroup(AutoResourceGroup):
    class Meta:
        service = SetService
        swagger = SetSwagger
