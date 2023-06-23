# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.model import Centre
from main.schema import CentreSchema
from tol.api_base.service import BaseService, setup_service


@setup_service
class CentreService(BaseService):
    class Meta:
        model = Centre
        schema = CentreSchema
