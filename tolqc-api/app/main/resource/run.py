# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import RunService
from main.swagger import RunSwagger

from .tol.api_base.resource import AutoResourceGroup, setup_resource_group


api_run = RunSwagger.api


@setup_resource_group
class RunResourceGroup(AutoResourceGroup):
    class Meta:
        service = RunService
        swagger = RunSwagger
