# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.service import SexService
from main.swagger import SexSwagger
from tol.api_base.resource import AutoResourceGroup, setup_resource_group


api_sex = SexSwagger.api


@setup_resource_group
class SexResourceGroup(AutoResourceGroup):
    class Meta:
        service = SexService
        swagger = SexSwagger
