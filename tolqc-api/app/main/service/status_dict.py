# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model import TolqcStatusDict
from main.schema import StatusDictSchema

from .base import BaseService, setup_service


@setup_service
class StatusDictService(BaseService):
    class Meta:
        model = TolqcStatusDict
        schema = StatusDictSchema
