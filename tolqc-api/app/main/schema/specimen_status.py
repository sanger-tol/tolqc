# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.model import SpecimenStatus

from tol.api_base.schema import BaseSchema, Str, setup_schema


@setup_schema
class SpecimenStatusSchema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = SpecimenStatus

    id = Str(attribute='specimen_status_id', dump_only=True)  # noqa: A003
