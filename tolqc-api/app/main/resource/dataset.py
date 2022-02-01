# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import DatasetService
from main.swagger import DatasetSwagger

from .base import BaseResource, setup_resource


api_dataset = DatasetSwagger.api


@setup_resource
class DatasetResource(BaseResource):
    class Meta:
        service = DatasetService
        swagger = DatasetSwagger
