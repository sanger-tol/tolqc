# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import AllocationService
from main.swagger import AllocationSwagger

from .base import AutoResourceGroup, setup_resource


api_allocation = AllocationSwagger.api


@setup_resource
class AllocationResource(AutoResourceGroup):
    class Meta:
        service = AllocationService
        swagger = AllocationSwagger
