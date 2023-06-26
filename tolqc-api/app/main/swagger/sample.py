# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.schema import SampleSchema

from tol.api_base.swagger import BaseSwagger, setup_swagger


@setup_swagger
class SampleSwagger(BaseSwagger):
    class Meta:
        schema = SampleSchema
