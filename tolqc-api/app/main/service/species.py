# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model import Species
from main.schema import SpeciesSchema

from tol.api_base.service import BaseService, setup_service


@setup_service
class SpeciesService(BaseService):
    class Meta:
        model = Species
        schema = SpeciesSchema
