# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from marshmallow_jsonapi import fields

from .base_schema import BaseSchema
from main.model import TolqcRun


class TolqcRunSchema(BaseSchema):
    # this should be auto-generated in the future!
    centre = fields.Relationship(
        self_url="/run/{id}/relationships/centre",
        self_url_kwargs={'id':'<id>'},
        related_url='/centre/runs/{id}',
        related_url_kwargs={'id': '<centre_id>'}
    )

    class Meta:
        type_ = 'runs'
        strict = True
        model = TolqcRun
        include_fk = True
