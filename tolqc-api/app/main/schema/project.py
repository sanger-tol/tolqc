# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.model import Project
from tol.api_base.schema import BaseSchema, Str, setup_schema


@setup_schema
class ProjectSchema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = Project

    id = Str(attribute='project_id', dump_only=True)  # noqa: A003
