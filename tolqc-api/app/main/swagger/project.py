# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.schema import ProjectSchema
from tol.api_base.swagger import BaseSwagger, setup_swagger


@setup_swagger
class ProjectSwagger(BaseSwagger):
    class Meta:
        schema = ProjectSchema
