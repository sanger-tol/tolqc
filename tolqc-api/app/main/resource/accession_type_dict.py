# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import AccessionTypeDictService
from main.swagger import AccessionTypeDictSwagger

from .base import AutoResourceGroup, setup_resource


api_accession_type_dict = AccessionTypeDictSwagger.api


@setup_resource
class AccessionTypeDictResource(AutoResourceGroup):
    class Meta:
        service = AccessionTypeDictService
        swagger = AccessionTypeDictSwagger
