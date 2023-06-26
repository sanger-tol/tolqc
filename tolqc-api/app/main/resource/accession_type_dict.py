# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.service import AccessionTypeDictService
from main.swagger import AccessionTypeDictSwagger

from tol.api_base.resource import AutoResourceGroup, setup_resource_group


api_accession_type_dict = AccessionTypeDictSwagger.api


@setup_resource_group
class AccessionTypeDictResourceGroup(AutoResourceGroup):
    class Meta:
        service = AccessionTypeDictService
        swagger = AccessionTypeDictSwagger
