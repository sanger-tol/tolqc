# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.model import Offspring
from main.schema import OffspringSchema
from tol.api_base.service import BaseService, setup_service


@setup_service
class OffspringService(BaseService):
    class Meta:
        model = Offspring
        schema = OffspringSchema
