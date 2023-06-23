# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.service import SampleService
from main.swagger import SampleSwagger
from tol.api_base.resource import AutoResourceGroup, setup_resource_group


api_sample = SampleSwagger.api


@setup_resource_group
class SampleResourceGroup(AutoResourceGroup):
    class Meta:
        service = SampleService
        swagger = SampleSwagger
