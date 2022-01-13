# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import LibraryTypeService
from main.swagger import LibraryTypeSwagger

from .base import BaseListResource, BaseDetailResource, setup_resource


api_library_type = LibraryTypeSwagger.api


class LibraryTypeResourceMeta:
    service = LibraryTypeService
    swagger = LibraryTypeSwagger


@setup_resource
class LibraryTypeDetailResource(BaseDetailResource):
    Meta = LibraryTypeResourceMeta


@setup_resource
class LibraryTypeListResource(BaseListResource):
    Meta = LibraryTypeResourceMeta
