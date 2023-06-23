# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.schema import RunSchema
from tol.api_base.swagger import BaseSwagger, setup_swagger


@setup_swagger
class RunSwagger(BaseSwagger):
    class Meta:
        schema = RunSchema
