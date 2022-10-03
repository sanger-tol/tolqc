# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model import TolqcAssemblyMetrics
from main.schema import AssemblyMetricsSchema

from .base import BaseService, setup_service


@setup_service
class AssemblyMetricsService(BaseService):
    class Meta:
        model = TolqcAssemblyMetrics
        schema = AssemblyMetricsSchema
