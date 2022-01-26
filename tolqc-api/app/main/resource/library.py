# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import LibraryService
from main.swagger import LibrarySwagger

from .base import BaseResource, setup_resource


api_library = LibrarySwagger.api


@setup_resource
class LibraryResource(BaseResource):
    class Meta:
        service = LibraryService
        swagger = LibrarySwagger
