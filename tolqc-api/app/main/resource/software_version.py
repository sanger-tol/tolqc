# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import LibraryService
from main.swagger import LibrarySwagger

from .base import BaseListResource, BaseDetailResource, setup_resource


api_library = LibrarySwagger.api


class LibraryResourceMeta:
    service = LibraryService
    swagger = LibrarySwagger


@setup_resource
class LibraryDetailResource(BaseDetailResource):
    Meta = LibraryResourceMeta


@setup_resource
class LibraryListResource(BaseListResource):
    Meta = LibraryResourceMeta
