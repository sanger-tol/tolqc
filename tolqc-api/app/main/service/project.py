# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.model import Project
from main.schema import ProjectSchema

from tol.api_base.service import BaseService, setup_service


@setup_service
class ProjectService(BaseService):
    class Meta:
        model = Project
        schema = ProjectSchema
