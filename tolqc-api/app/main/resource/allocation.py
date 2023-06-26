# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.service import AllocationService
from main.swagger import AllocationSwagger

from tol.api_base.resource import AutoResourceGroup, setup_resource_group


api_allocation = AllocationSwagger.api


@setup_resource_group
class AllocationResourceGroup(AutoResourceGroup):
    class Meta:
        service = AllocationService
        swagger = AllocationSwagger
