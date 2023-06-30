# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.schema import AssemblyStatusTypeSchema

from tol.api_base.swagger import BaseSwagger, setup_swagger


@setup_swagger
class AssemblyStatusTypeSwagger(BaseSwagger):
    class Meta:
        schema = AssemblyStatusTypeSchema
