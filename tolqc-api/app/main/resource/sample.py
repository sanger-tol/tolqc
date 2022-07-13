# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import SampleService
from main.swagger import SampleSwagger

from .base import AutoResourceGroup, setup_resource


api_sample = SampleSwagger.api


@setup_resource
class SampleResource(AutoResourceGroup):
    class Meta:
        service = SampleService
        swagger = SampleSwagger
