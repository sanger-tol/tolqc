# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import ProjectService
from main.swagger import ProjectSwagger

from .base import AutoResourceGroup, setup_resource_group


api_project = ProjectSwagger.api


@setup_resource_group
class ProjectResourceGroup(AutoResourceGroup):
    class Meta:
        service = ProjectService
        swagger = ProjectSwagger
