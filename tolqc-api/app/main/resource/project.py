# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import ProjectService
from main.swagger import ProjectSwagger

from .tol.api_base.resource import AutoResourceGroup, setup_resource_group


api_project = ProjectSwagger.api


@setup_resource_group
class ProjectResourceGroup(AutoResourceGroup):
    class Meta:
        service = ProjectService
        swagger = ProjectSwagger
