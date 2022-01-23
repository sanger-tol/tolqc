# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import DataService
from main.swagger import DataSwagger

from .base import BaseListResource, BaseDetailResource, setup_resource


api_data = DataSwagger.api


class DataResourceMeta:
    service = DataService
    swagger = DataSwagger


@setup_resource
class DataDetailResource(BaseDetailResource):
    Meta = DataResourceMeta


@setup_resource
class DataListResource(BaseListResource):
    Meta = DataResourceMeta
