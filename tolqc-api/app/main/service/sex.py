# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model import Sex
from main.schema import SexSchema

from tol.api_base.service import BaseService, setup_service


@setup_service
class SexService(BaseService):
    class Meta:
        model = Sex
        schema = SexSchema
