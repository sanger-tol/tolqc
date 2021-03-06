# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import LibraryService
from main.swagger import LibrarySwagger

from .base import AutoResourceGroup, setup_resource_group


api_library = LibrarySwagger.api


@setup_resource_group
class LibraryResourceGroup(AutoResourceGroup):
    class Meta:
        service = LibraryService
        swagger = LibrarySwagger
