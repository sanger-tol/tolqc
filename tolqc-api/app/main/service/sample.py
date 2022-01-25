# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model import TolqcSample
from main.schema import SampleSchema

from .base import BaseService, setup_service


@setup_service
class SampleService(BaseService):
    class Meta:
        model = TolqcSample
        schema = SampleSchema
