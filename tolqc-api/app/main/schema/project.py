# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT
from main.model import Project

from tol.api_base.schema import BaseSchema, setup_schema


@setup_schema
class ProjectSchema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = Project
