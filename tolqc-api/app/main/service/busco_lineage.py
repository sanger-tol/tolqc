# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.model import BuscoLineage
from main.schema import BuscoLineageSchema

from tol.api_base.service import BaseService, setup_service


@setup_service
class BuscoLineageService(BaseService):
    class Meta:
        model = BuscoLineage
        schema = BuscoLineageSchema
