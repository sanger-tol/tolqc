# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.model import MarkerscanMetrics
from main.schema import MarkerscanMetricsSchema
from tol.api_base.service import BaseService, setup_service


@setup_service
class MarkerscanMetricsService(BaseService):
    class Meta:
        model = MarkerscanMetrics
        schema = MarkerscanMetricsSchema
