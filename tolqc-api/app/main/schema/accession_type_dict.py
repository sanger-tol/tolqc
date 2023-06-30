# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.model import AccessionTypeDict

from tol.api_base.schema import BaseSchema, Str, setup_schema


@setup_schema
class AccessionTypeDictSchema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = AccessionTypeDict

    id = Str(attribute='accession_type_id', dump_only=True)  # noqa: A003
