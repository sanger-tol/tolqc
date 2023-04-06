# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model import BuscoMetrics
from main.schema import BuscoMetricsSchema

from tol.api_base.service import BaseService, setup_service


@setup_service
class BuscoMetricsService(BaseService):
    class Meta:
        model = BuscoMetrics
        schema = BuscoMetricsSchema
