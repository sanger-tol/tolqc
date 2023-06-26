# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.model import Run
from main.schema import RunSchema

from tol.api_base.service import BaseService, setup_service


@setup_service
class RunService(BaseService):
    class Meta:
        model = Run
        schema = RunSchema
