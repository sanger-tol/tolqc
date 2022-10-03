# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model import TolqcSet
from main.schema import SetSchema

from .base import BaseService, setup_service


@setup_service
class SetService(BaseService):
    class Meta:
        model = TolqcSet
        schema = SetSchema
