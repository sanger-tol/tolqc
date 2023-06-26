# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.service import OffspringService
from main.swagger import OffspringSwagger

from tol.api_base.resource import AutoResourceGroup, setup_resource_group


api_offspring = OffspringSwagger.api


@setup_resource_group
class OffspringResourceGroup(AutoResourceGroup):
    class Meta:
        service = OffspringService
        swagger = OffspringSwagger
