# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import FileService
from main.swagger import FileSwagger

from .base import AutoResourceGroup, setup_resource_group


api_file = FileSwagger.api


@setup_resource_group
class FileResourceGroup(AutoResourceGroup):
    class Meta:
        service = FileService
        swagger = FileSwagger
