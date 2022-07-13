# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import LibraryTypeService
from main.swagger import LibraryTypeSwagger

from .base import AutoResourceGroup, setup_resource_group


api_library_type = LibraryTypeSwagger.api


@setup_resource_group
class LibraryTypeResourceGroup(AutoResourceGroup):
    class Meta:
        service = LibraryTypeService
        swagger = LibraryTypeSwagger
