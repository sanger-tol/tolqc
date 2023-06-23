# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.model import QCDict
from main.schema import QCDictSchema
from tol.api_base.service import BaseService, setup_service


@setup_service
class QCDictService(BaseService):
    class Meta:
        model = QCDict
        schema = QCDictSchema
