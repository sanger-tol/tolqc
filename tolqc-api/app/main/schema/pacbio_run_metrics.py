# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT
from main.model import TolqcPacbioRunMetrics

from .base import BaseSchema, setup_schema


@setup_schema
class PacbioRunMetricsSchema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = TolqcPacbioRunMetrics
