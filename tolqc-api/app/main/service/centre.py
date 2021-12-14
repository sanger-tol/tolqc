# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model import TolqcCentre
from main.schema import CentreDetailSchema

from .base import BaseService

class CentreService(BaseService):
    class Meta:
        model = TolqcCentre
        detail_schema = CentreDetailSchema

    @classmethod
    def put_by_id(self, id, data):
        CentreDetailSchema().update_by_id(id, data)

    @classmethod
    def delete_by_id(self, id):
        CentreDetailSchema().delete_by_id(id)
