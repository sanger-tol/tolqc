# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.model import Accession
from tol.api_base.schema import BaseSchema, Str, setup_schema


@setup_schema
class AccessionSchema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = Accession

    id = Str(attribute='accession_id', dump_only=True)  # noqa: A003
