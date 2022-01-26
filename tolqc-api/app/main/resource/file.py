# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import FileService
from main.swagger import FileSwagger

from .base import BaseResource, setup_resource


api_file = FileSwagger.api


@setup_resource
class FileResource(BaseResource):
    class Meta:
        service = FileService
        swagger = FileSwagger
