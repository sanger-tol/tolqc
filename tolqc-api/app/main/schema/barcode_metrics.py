# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.model import BarcodeMetrics
from tol.api_base.schema import BaseSchema, setup_schema


@setup_schema
class BarcodeMetricsSchema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = BarcodeMetrics
