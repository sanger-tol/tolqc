# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT
from main.model import TolqcAsmStats

from .base import BaseSchema, setup_schema


@setup_schema
class AsmStatsSchema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = TolqcAsmStats
