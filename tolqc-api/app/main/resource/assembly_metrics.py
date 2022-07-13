# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import AssemblyMetricsService
from main.swagger import AssemblyMetricsSwagger

from .base import AutoResourceGroup, setup_resource


api_assembly_metrics = AssemblyMetricsSwagger.api


@setup_resource
class AssemblyMetricsResource(AutoResourceGroup):
    class Meta:
        service = AssemblyMetricsService
        swagger = AssemblyMetricsSwagger
