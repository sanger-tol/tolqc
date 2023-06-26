# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.model import DatasetStatus
from main.schema import DatasetStatusSchema

from tol.api_base.service import BaseService, setup_service


@setup_service
class DatasetStatusService(BaseService):
    class Meta:
        model = DatasetStatus
        schema = DatasetStatusSchema
