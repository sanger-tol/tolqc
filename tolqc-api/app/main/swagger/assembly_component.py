# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.schema import AssemblyComponentSchema

from .base import BaseSwagger, setup_swagger


@setup_swagger
class AssemblyComponentSwagger(BaseSwagger):
    class Meta:
        schema = AssemblyComponentSchema
