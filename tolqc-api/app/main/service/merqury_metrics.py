# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.model import MerquryMetrics
from main.schema import MerquryMetricsSchema
from tol.api_base.service import BaseService, setup_service


@setup_service
class MerquryMetricsService(BaseService):
    class Meta:
        model = MerquryMetrics
        schema = MerquryMetricsSchema
