# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.service import DatasetStatusService
from main.swagger import DatasetStatusSwagger
from tol.api_base.resource import AutoResourceGroup, setup_resource_group


api_dataset_status = DatasetStatusSwagger.api


@setup_resource_group
class DatasetStatusResourceGroup(AutoResourceGroup):
    class Meta:
        service = DatasetStatusService
        swagger = DatasetStatusSwagger
