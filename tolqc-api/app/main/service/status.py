# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model import TolqcStatus
from main.schema import StatusSchema

from .base import BaseService, setup_service


@setup_service
class StatusService(BaseService):
    class Meta:
        model = TolqcStatus
        schema = StatusSchema
