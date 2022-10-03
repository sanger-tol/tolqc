# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model import TolqcAccession
from main.schema import AccessionSchema

from tol.api_base.service import BaseService, setup_service


@setup_service
class AccessionService(BaseService):
    class Meta:
        model = TolqcAccession
        schema = AccessionSchema
