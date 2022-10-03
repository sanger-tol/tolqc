# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT
from main.model import TolqcGenomescopeMetrics

from .base import BaseSchema, setup_schema


@setup_schema
class GenomescopeMetricsSchema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = TolqcGenomescopeMetrics
