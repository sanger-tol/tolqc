# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import ProjectService
from main.swagger import ProjectSwagger

from .base import BaseListResource, BaseDetailResource, setup_resource


api_project = ProjectSwagger.api


class ProjectResourceMeta:
    service = ProjectService
    swagger = ProjectSwagger


@setup_resource
class ProjectDetailResource(BaseDetailResource):
    Meta = ProjectResourceMeta


@setup_resource
class ProjectListResource(BaseListResource):
    Meta = ProjectResourceMeta
