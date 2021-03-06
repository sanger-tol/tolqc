# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import UserService
from main.swagger import UserSwagger

from .base import AutoResourceGroup, setup_resource_group


api_user = UserSwagger.api


@setup_resource_group
class UserResourceGroup(AutoResourceGroup):
    class Meta:
        service = UserService
        swagger = UserSwagger
