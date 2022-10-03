# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT
from main.model import TolqcMerquryMetrics

from .base import BaseSchema, setup_schema


@setup_schema
class MerquryMetricsSchema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = TolqcMerquryMetrics
