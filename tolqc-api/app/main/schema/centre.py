# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.model import Centre
from tol.api_base.schema import BaseSchema, setup_schema


@setup_schema
class CentreSchema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = Centre
