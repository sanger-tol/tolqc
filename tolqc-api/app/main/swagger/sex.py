# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.schema import SexSchema

from .base import BaseSwagger, setup_swagger


@setup_swagger
class SexSwagger(BaseSwagger):
    class Meta:
        schema = SexSchema
