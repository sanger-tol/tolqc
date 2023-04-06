# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model import Specimen
from main.schema import SpecimenSchema

from tol.api_base.service import BaseService, setup_service


@setup_service
class SpecimenService(BaseService):
    class Meta:
        model = Specimen
        schema = SpecimenSchema
