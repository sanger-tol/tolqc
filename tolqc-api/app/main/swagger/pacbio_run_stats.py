# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.schema import PacbioRunStatsSchema

from .base import BaseSwagger, setup_swagger


@setup_swagger
class PacbioRunStatsSwagger(BaseSwagger):
    class Meta:
        schema = PacbioRunStatsSchema
