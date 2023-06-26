# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.service import LibraryService
from main.swagger import LibrarySwagger

from tol.api_base.resource import AutoResourceGroup, setup_resource_group


api_library = LibrarySwagger.api


@setup_resource_group
class LibraryResourceGroup(AutoResourceGroup):
    class Meta:
        service = LibraryService
        swagger = LibrarySwagger
