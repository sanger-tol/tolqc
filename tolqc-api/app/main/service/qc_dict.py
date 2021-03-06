# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model import TolqcQcDict
from main.schema import QcDictSchema

from .base import BaseService, setup_service


@setup_service
class QcDictService(BaseService):
    class Meta:
        model = TolqcQcDict
        schema = QcDictSchema
