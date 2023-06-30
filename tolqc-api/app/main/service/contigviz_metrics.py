# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.model import ContigvizMetrics
from main.schema import ContigvizMetricsSchema

from tol.api_base.service import BaseService, setup_service


@setup_service
class ContigvizMetricsService(BaseService):
    class Meta:
        model = ContigvizMetrics
        schema = ContigvizMetricsSchema
