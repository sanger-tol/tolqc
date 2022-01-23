# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model import TolqcStatus
from main.schema import StatusSchema

from .base import BaseService


class StatusService(BaseService):
    class Meta:
        model = TolqcStatus
        schema = StatusSchema
