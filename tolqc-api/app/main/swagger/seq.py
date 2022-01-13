# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.schema import SeqSchema

from .base import BaseSwagger, setup_swagger


@setup_swagger
class SeqSwagger(BaseSwagger):
    class Meta:
        schema = SeqSchema
