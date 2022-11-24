# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model import TolqcAccessionTypeDict
from main.schema import AccessionTypeDictSchema

from tol.api_base.service import BaseService, setup_service


@setup_service
class AccessionTypeDictService(BaseService):
    class Meta:
        model = TolqcAccessionTypeDict
        schema = AccessionTypeDictSchema
