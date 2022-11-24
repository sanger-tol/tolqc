# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model import TolqcProject
from main.schema import ProjectSchema

from tol.api_base.service import BaseService, setup_service


@setup_service
class ProjectService(BaseService):
    class Meta:
        model = TolqcProject
        schema = ProjectSchema
