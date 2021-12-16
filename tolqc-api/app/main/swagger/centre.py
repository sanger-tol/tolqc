# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.schema import CentreSchema

from .base import BaseSwagger, BaseNamespace


class CentreSwagger(BaseSwagger):
    class Meta:
        schema = CentreSchema

    api = BaseNamespace(
        CentreSchema.get_type(),
        description='Centre related methods'
    )


CentreSwagger.populate_default_models()
