# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.service import SoftwareVersionService
from main.swagger import SoftwareVersionSwagger
from tol.api_base.resource import AutoResourceGroup, setup_resource_group


api_software_version = SoftwareVersionSwagger.api


@setup_resource_group
class SoftwareVersionResourceGroup(AutoResourceGroup):
    class Meta:
        service = SoftwareVersionService
        swagger = SoftwareVersionSwagger
