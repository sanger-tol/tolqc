# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model import TolqcRun
from main.schema import RunSchema

from .base import BaseService, setup_service


@setup_service
class RunService(BaseService):
    class Meta:
        model = TolqcRun
        schema = RunSchema
