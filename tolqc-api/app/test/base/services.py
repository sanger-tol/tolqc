# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service.base import BaseService

from test.base.models import ModelRelationshipB, \
                             ModelWithNullableColumnC, \
                             ModelWithNonNullableColumnD, \
                             ModelWithExtFieldF
from test.base.schemas import B_Schema, C_Schema, \
                              D_Schema, F_Schema


class B_Service(BaseService):
    class Meta:
        model = ModelRelationshipB
        schema = B_Schema


class C_Service(BaseService):
    class Meta:
        model = ModelWithNullableColumnC
        schema = C_Schema


class D_Service(BaseService):
    class Meta:
        model = ModelWithNonNullableColumnD
        schema = D_Schema


class F_Service(BaseService):
    class Meta:
        model = ModelWithExtFieldF
        schema = F_Schema
