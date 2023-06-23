# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.model import MarkerscanMetrics
from tol.api_base.schema import BaseSchema, setup_schema


@setup_schema
class MarkerscanMetricsSchema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = MarkerscanMetrics
