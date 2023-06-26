# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.schema import AssemblySourceSchema

from tol.api_base.swagger import BaseSwagger, setup_swagger


@setup_swagger
class AssemblySourceSwagger(BaseSwagger):
    class Meta:
        schema = AssemblySourceSchema
