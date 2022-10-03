# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import QcDictService
from main.swagger import QcDictSwagger

from .tol.api_base.resource import AutoResourceGroup, setup_resource_group


api_qc_dict = QcDictSwagger.api


@setup_resource_group
class QcDictResourceGroup(AutoResourceGroup):
    class Meta:
        service = QcDictService
        swagger = QcDictSwagger
