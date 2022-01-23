# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import SoftwareVersionService
from main.swagger import SoftwareVersionSwagger

from .base import BaseListResource, BaseDetailResource, setup_resource


api_SoftwareVersion = SoftwareVersionSwagger.api


class SoftwareVersionResourceMeta:
    service = SoftwareVersionService
    swagger = SoftwareVersionSwagger


@setup_resource
class SoftwareVersionDetailResource(BaseDetailResource):
    Meta = SoftwareVersionResourceMeta


@setup_resource
class SoftwareVersionListResource(BaseListResource):
    Meta = SoftwareVersionResourceMeta
