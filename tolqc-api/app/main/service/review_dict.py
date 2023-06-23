# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.model import ReviewDict
from main.schema import ReviewDictSchema
from tol.api_base.service import BaseService, setup_service


@setup_service
class ReviewDictService(BaseService):
    class Meta:
        model = ReviewDict
        schema = ReviewDictSchema
