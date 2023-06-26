# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.schema import AssemblyStatusSchema

from tol.api_base.swagger import BaseSwagger, setup_swagger


@setup_swagger
class AssemblyStatusSwagger(BaseSwagger):
    class Meta:
        schema = AssemblyStatusSchema
