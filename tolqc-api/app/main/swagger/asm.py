# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.schema import AsmSchema

from .base import BaseSwagger, setup_swagger


@setup_swagger
class AsmSwagger(BaseSwagger):
    class Meta:
        schema = AsmSchema
