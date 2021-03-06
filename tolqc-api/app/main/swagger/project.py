# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.schema import ProjectSchema

from .base import BaseSwagger, setup_swagger


@setup_swagger
class ProjectSwagger(BaseSwagger):
    class Meta:
        schema = ProjectSchema
