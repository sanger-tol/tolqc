# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import UserService
from main.swagger import UserSwagger

from tol.api_base.resource import AutoResourceGroup, setup_resource_group


api_user = UserSwagger.api


@setup_resource_group
class UserResourceGroup(AutoResourceGroup):
    class Meta:
        service = UserService
        swagger = UserSwagger
