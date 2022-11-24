# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.schema import SpeciesSchema

from tol.api_base.swagger import BaseSwagger, setup_swagger


@setup_swagger
class SpeciesSwagger(BaseSwagger):
    class Meta:
        schema = SpeciesSchema
