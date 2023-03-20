# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model import Platform
from main.schema import PlatformSchema

from tol.api_base.service import BaseService, setup_service


@setup_service
class PlatformService(BaseService):
    class Meta:
        model = Platform
        schema = PlatformSchema
