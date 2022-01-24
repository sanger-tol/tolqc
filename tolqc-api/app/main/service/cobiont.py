# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model import TolqcCobiont
from main.schema import CobiontSchema

from .base import BaseService


class CobiontService(BaseService):
    class Meta:
        model = TolqcCobiont
        schema = CobiontSchema