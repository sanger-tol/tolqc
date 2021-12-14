# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.schema.base import BaseListSchema, \
                             BaseDetailSchema, \
                             BaseMeta

from test.core.models import ModelRelationshipB, \
                             ModelWithNullableColumn, \
                             ModelWithNonNullableColumn, \
                             ModelWithExtField


class BMeta(BaseMeta):
    pass


BMeta.add_model(ModelRelationshipB)


class B_DetailSchema(BaseDetailSchema):
    Meta = BMeta


class B_ListSchema(BaseListSchema):
    Meta = BMeta


class CMeta(BaseMeta):
    pass


CMeta.add_model(ModelWithNullableColumn)


class C_DetailSchema(BaseDetailSchema):
    Meta = CMeta


class C_ListSchema(BaseListSchema):
    Meta = CMeta


class DMeta(BaseMeta):
    pass


DMeta.add_model(ModelWithNonNullableColumn)


class D_DetailSchema(BaseDetailSchema):
    Meta = DMeta


class D_ListSchema(BaseListSchema):
    Meta = DMeta


class FMeta(BaseMeta):
    pass


FMeta.add_model(ModelWithExtField)


class F_DetailSchema(BaseDetailSchema):
    Meta = FMeta


class F_ListSchema(BaseListSchema):
    Meta = FMeta
