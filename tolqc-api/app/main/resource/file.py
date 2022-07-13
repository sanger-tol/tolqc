# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import FileService
from main.swagger import FileSwagger

from .base import AutoResourceGroup, setup_resource


api_file = FileSwagger.api


@setup_resource
class FileResource(AutoResourceGroup):
    class Meta:
        service = FileService
        swagger = FileSwagger
