# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.model import SpecimenStatusType
from main.schema import SpecimenStatusTypeSchema

from tol.api_base.service import BaseService, setup_service


@setup_service
class SpecimenStatusTypeService(BaseService):
    class Meta:
        model = SpecimenStatusType
        schema = SpecimenStatusTypeSchema
