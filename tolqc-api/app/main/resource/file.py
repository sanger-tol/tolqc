# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import FileService
from main.swagger import FileSwagger

from .base import BaseListResource, BaseDetailResource, setup_resource


api_File = FileSwagger.api


class FileResourceMeta:
    service = FileService
    swagger = FileSwagger


@setup_resource
class FileDetailResource(BaseDetailResource):
    Meta = FileResourceMeta


@setup_resource
class FileListResource(BaseListResource):
    Meta = FileResourceMeta
