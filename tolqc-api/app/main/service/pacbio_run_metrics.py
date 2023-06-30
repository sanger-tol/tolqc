# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.model import PacbioRunMetrics
from main.schema import PacbioRunMetricsSchema

from tol.api_base.service import BaseService, setup_service


@setup_service
class PacbioRunMetricsService(BaseService):
    class Meta:
        model = PacbioRunMetrics
        schema = PacbioRunMetricsSchema
