# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.schema import AssemblyComponentSchema

from tol.api_base.swagger import BaseSwagger, setup_swagger


@setup_swagger
class AssemblyComponentSwagger(BaseSwagger):
    class Meta:
        schema = AssemblyComponentSchema
