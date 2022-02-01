# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT
from main.model import TolqcAssemblyMetrics

from .base import BaseSchema, setup_schema


@setup_schema
class AssemblyMetricsSchema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = TolqcAssemblyMetrics
