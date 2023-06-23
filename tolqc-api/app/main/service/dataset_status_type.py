# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.model import DatasetStatusType
from main.schema import DatasetStatusTypeSchema
from tol.api_base.service import BaseService, setup_service


@setup_service
class DatasetStatusTypeService(BaseService):
    class Meta:
        model = DatasetStatusType
        schema = DatasetStatusTypeSchema
