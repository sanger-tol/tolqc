# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.service import BarcodeMetricsService
from main.swagger import BarcodeMetricsSwagger
from tol.api_base.resource import AutoResourceGroup, setup_resource_group


api_barcode_metrics = BarcodeMetricsSwagger.api


@setup_resource_group
class BarcodeMetricsResourceGroup(AutoResourceGroup):
    class Meta:
        service = BarcodeMetricsService
        swagger = BarcodeMetricsSwagger
