# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.service import ReviewDictService
from main.swagger import ReviewDictSwagger

from tol.api_base.resource import AutoResourceGroup, setup_resource_group


api_review_dict = ReviewDictSwagger.api


@setup_resource_group
class ReviewDictResourceGroup(AutoResourceGroup):
    class Meta:
        service = ReviewDictService
        swagger = ReviewDictSwagger
