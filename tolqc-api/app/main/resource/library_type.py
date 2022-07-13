# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import LibraryTypeService
from main.swagger import LibraryTypeSwagger

from .base import AutoResourceGroup, setup_resource


api_library_type = LibraryTypeSwagger.api


@setup_resource
class LibraryTypeResource(AutoResourceGroup):
    class Meta:
        service = LibraryTypeService
        swagger = LibraryTypeSwagger
