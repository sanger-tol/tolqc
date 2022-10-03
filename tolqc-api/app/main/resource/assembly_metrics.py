# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import AssemblyMetricsService
from main.swagger import AssemblyMetricsSwagger

from .base import AutoResourceGroup, setup_resource_group


api_assembly_metrics = AssemblyMetricsSwagger.api


@setup_resource_group
class AssemblyMetricsResourceGroup(AutoResourceGroup):
    class Meta:
        service = AssemblyMetricsService
        swagger = AssemblyMetricsSwagger
