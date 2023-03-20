# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model import Set
from main.schema import SetSchema

from tol.api_base.service import BaseService, setup_service


@setup_service
class SetService(BaseService):
    class Meta:
        model = Set
        schema = SetSchema
