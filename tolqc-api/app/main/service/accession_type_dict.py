# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model import TolqcAccessionTypeDict
from main.schema import AccessionTypeDictSchema

from .base import BaseService, setup_service


@setup_service
class AccessionTypeDictService(BaseService):
    class Meta:
        model = TolqcAccessionTypeDict
        schema = AccessionTypeDictSchema
