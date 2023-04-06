# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model import StatusDict
from main.schema import StatusDictSchema

from tol.api_base.service import BaseService, setup_service


@setup_service
class StatusDictService(BaseService):
    class Meta:
        model = StatusDict
        schema = StatusDictSchema
