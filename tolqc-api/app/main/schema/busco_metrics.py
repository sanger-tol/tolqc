# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT
from main.model import TolqcBuscoMetrics

from .base import BaseSchema, setup_schema


@setup_schema
class BuscoMetricsSchema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = TolqcBuscoMetrics
