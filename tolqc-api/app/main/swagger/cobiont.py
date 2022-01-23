# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.schema import CobiontSchema

from .base import BaseSwagger, setup_swagger


@setup_swagger
class CobiontSwagger(BaseSwagger):
    class Meta:
        schema = CobiontSchema
