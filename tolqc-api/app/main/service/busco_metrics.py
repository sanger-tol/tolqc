# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model import TolqcBuscoMetrics
from main.schema import BuscoMetricsSchema

from .base import BaseService, setup_service


@setup_service
class BuscoMetricsService(BaseService):
    class Meta:
        model = TolqcBuscoMetrics
        schema = BuscoMetricsSchema
