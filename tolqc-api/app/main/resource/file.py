# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.service import FileService
from main.swagger import FileSwagger
from tol.api_base.resource import AutoResourceGroup, setup_resource_group


api_file = FileSwagger.api


@setup_resource_group
class FileResourceGroup(AutoResourceGroup):
    class Meta:
        service = FileService
        swagger = FileSwagger
