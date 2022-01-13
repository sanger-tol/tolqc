# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model import TolqcRun
from main.schema import RunSchema

from .base import BaseService


class RunService(BaseService):
    class Meta:
        model = TolqcRun
        schema = RunSchema
