# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import ProjectService
from main.swagger import ProjectSwagger

from .base import BaseResource, setup_resource


api_project = ProjectSwagger.api


@setup_resource
class ProjectResource(BaseResource):
    class Meta:
        service = ProjectService
        swagger = ProjectSwagger
