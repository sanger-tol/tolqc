# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model import AssemblyMetrics
from main.schema import AssemblyMetricsSchema

from tol.api_base.service import BaseService, setup_service


@setup_service
class AssemblyMetricsService(BaseService):
    class Meta:
        model = AssemblyMetrics
        schema = AssemblyMetricsSchema
