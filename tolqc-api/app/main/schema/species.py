# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.model import Species

from tol.api_base.schema import BaseSchema, Str, setup_schema


@setup_schema
class SpeciesSchema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = Species

    id = Str(attribute='species_id', dump_only=True)  # noqa: A003
