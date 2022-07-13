# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import SoftwareVersionService
from main.swagger import SoftwareVersionSwagger

from .base import AutoResourceGroup, setup_resource


api_software_version = SoftwareVersionSwagger.api


@setup_resource
class SoftwareVersionResource(AutoResourceGroup):
    class Meta:
        service = SoftwareVersionService
        swagger = SoftwareVersionSwagger
