# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.model import QCDict

from tol.api_base.schema import BaseSchema, Str, setup_schema


@setup_schema
class QCDictSchema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = QCDict

    id = Str(attribute='qc_state', dump_only=True)  # noqa: A003
