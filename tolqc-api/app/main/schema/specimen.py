# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.model import Specimen
from tol.api_base.schema import BaseSchema, Str, setup_schema


@setup_schema
class SpecimenSchema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = Specimen

    id = Str(attribute='specimen_id', dump_only=True)  # noqa: A003
