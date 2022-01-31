# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import AssemblyMetricsService
from main.swagger import AssemblyMetricsSwagger

from .base import BaseResource, setup_resource


api_assembly_metrics = AssemblyMetricsSwagger.api


@setup_resource
class AssemblyMetricsResource(BaseResource):
    class Meta:
        service = AssemblyMetricsService
        swagger = AssemblyMetricsSwagger
