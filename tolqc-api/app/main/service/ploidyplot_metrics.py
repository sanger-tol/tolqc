# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.model import PloidyplotMetrics
from main.schema import PloidyplotMetricsSchema

from tol.api_base.service import BaseService, setup_service


@setup_service
class PloidyplotMetricsService(BaseService):
    class Meta:
        model = PloidyplotMetrics
        schema = PloidyplotMetricsSchema
