# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.service import CentreService
from main.swagger import CentreSwagger
from tol.api_base.resource import AutoResourceGroup, setup_resource_group


api_centre = CentreSwagger.api


@setup_resource_group
class CentreResourceGroup(AutoResourceGroup):
    class Meta:
        service = CentreService
        swagger = CentreSwagger
