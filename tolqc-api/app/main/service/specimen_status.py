# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.model import SpecimenStatus
from main.schema import SpecimenStatusSchema

from tol.api_base.service import BaseService, setup_service


@setup_service
class SpecimenStatusService(BaseService):
    class Meta:
        model = SpecimenStatus
        schema = SpecimenStatusSchema
