# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.schema import AssemblySchema

from .base import BaseSwagger, setup_swagger


@setup_swagger
class AssemblySwagger(BaseSwagger):
    class Meta:
        schema = AssemblySchema
