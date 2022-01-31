# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import DataService
from main.swagger import DataSwagger

from .base import BaseResource, setup_resource


api_data = DataSwagger.api


@setup_resource
class DataResource(BaseResource):
    class Meta:
        service = DataService
        swagger = DataSwagger
