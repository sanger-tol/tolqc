# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import QcDictService
from main.swagger import QcDictSwagger

from .base import AutoResourceGroup, setup_resource


api_qc_dict = QcDictSwagger.api


@setup_resource
class QcDictResource(AutoResourceGroup):
    class Meta:
        service = QcDictService
        swagger = QcDictSwagger
