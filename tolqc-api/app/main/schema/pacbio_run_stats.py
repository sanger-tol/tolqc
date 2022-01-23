# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT
from main.model import TolqcPacbioRunStats

from .base import BaseSchema, setup_schema


@setup_schema
class PacbioRunStatsSchema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = TolqcPacbioRunStats
