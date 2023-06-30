# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.model import Dataset
from main.schema import DatasetSchema

from tol.api_base.service import BaseService, setup_service


@setup_service
class DatasetService(BaseService):
    class Meta:
        model = Dataset
        schema = DatasetSchema
