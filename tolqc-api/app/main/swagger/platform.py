# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.schema import PlatformSchema

from tol.api_base.swagger import BaseSwagger, setup_swagger


@setup_swagger
class PlatformSwagger(BaseSwagger):
    class Meta:
        schema = PlatformSchema
