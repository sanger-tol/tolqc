# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import AccessionService
from main.swagger import AccessionSwagger

from .base import AutoResourceGroup, setup_resource_group


api_accession = AccessionSwagger.api


@setup_resource_group
class AccessionResourceGroup(AutoResourceGroup):
    class Meta:
        service = AccessionService
        swagger = AccessionSwagger
