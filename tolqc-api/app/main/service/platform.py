# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model import TolqcPlatform
from main.schema import PlatformSchema

from .base import BaseService


class PlatformService(BaseService):
    class Meta:
        model = TolqcPlatform
        schema = PlatformSchema
