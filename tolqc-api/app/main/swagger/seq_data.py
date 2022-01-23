# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.schema import SeqDataSchema

from .base import BaseSwagger, setup_swagger


@setup_swagger
class SeqDataSwagger(BaseSwagger):
    class Meta:
        schema = SeqDataSchema
