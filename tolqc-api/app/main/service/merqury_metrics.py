# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model import TolqcMerquryMetrics
from main.schema import MerquryMetricsSchema

from .base import BaseService, setup_service


@setup_service
class MerquryMetricsService(BaseService):
    class Meta:
        model = TolqcMerquryMetrics
        schema = MerquryMetricsSchema
