# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model import TolqcSample
from main.schema import SampleSchema

from tol.api_base.service import BaseService, setup_service


@setup_service
class SampleService(BaseService):
    class Meta:
        model = TolqcSample
        schema = SampleSchema
