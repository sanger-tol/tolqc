# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import QcDictService
from main.swagger import QcDictSwagger

from .base import AutoResourceGroup, setup_resource_group


api_qc_dict = QcDictSwagger.api


@setup_resource_group
class QcDictResourceGroup(AutoResourceGroup):
    class Meta:
        service = QcDictService
        swagger = QcDictSwagger
