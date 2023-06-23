# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.model import Accession
from main.schema import AccessionSchema
from tol.api_base.service import BaseService, setup_service


@setup_service
class AccessionService(BaseService):
    class Meta:
        model = Accession
        schema = AccessionSchema
