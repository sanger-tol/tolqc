# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model import TolqcDataset
from main.schema import DatasetSchema

from .base import BaseService, setup_service


@setup_service
class DatasetService(BaseService):
    class Meta:
        model = TolqcDataset
        schema = DatasetSchema
