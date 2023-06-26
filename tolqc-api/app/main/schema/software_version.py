# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.model import SoftwareVersion

from tol.api_base.schema import BaseSchema, Str, setup_schema


@setup_schema
class SoftwareVersionSchema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = SoftwareVersion

    id = Str(attribute='software_version_id', dump_only=True)  # noqa: A003
