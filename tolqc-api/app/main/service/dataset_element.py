# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.model import DatasetElement
from main.schema import DatasetElementSchema
from tol.api_base.service import BaseService, setup_service


@setup_service
class DatasetElementService(BaseService):
    class Meta:
        model = DatasetElement
        schema = DatasetElementSchema
