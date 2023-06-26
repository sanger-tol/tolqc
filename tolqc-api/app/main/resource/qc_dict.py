# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.service import QCDictService
from main.swagger import QCDictSwagger

from tol.api_base.resource import AutoResourceGroup, setup_resource_group


api_qc_dict = QCDictSwagger.api


@setup_resource_group
class QCDictResourceGroup(AutoResourceGroup):
    class Meta:
        service = QCDictService
        swagger = QCDictSwagger
