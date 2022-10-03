# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model import TolqcCentre
from main.schema import CentreSchema

from tol.api_base.service import BaseService, setup_service


@setup_service
class CentreService(BaseService):
    class Meta:
        model = TolqcCentre
        schema = CentreSchema
