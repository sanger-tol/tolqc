# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import SexService
from main.swagger import SexSwagger

from .base import AutoResourceGroup, setup_resource_group


api_sex = SexSwagger.api


@setup_resource_group
class SexResourceGroup(AutoResourceGroup):
    class Meta:
        service = SexService
        swagger = SexSwagger
