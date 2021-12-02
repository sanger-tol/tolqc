# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

import pytest

from main.schema.base import RequiredFieldExcludedException

from test.core import BaseTestCase
from test.core.schemas import C_RequestSchema, C_ResponseSchema, \
                              D_RequestSchema, D_ResponseSchema


class TestSchemaExlucdedFieldsToModelDict(BaseTestCase):
    def test_nullable_column_excluded_C(self):
        """Confirms that non-nullable column exclusion raises
        an exception in the right situations"""
        exclude_fields = ['nullable_column']
        # shouldn't raise exception on any dict conversion for C
        C_RequestSchema.to_post_model_dict(
            exclude_fields=exclude_fields
        )
        C_ResponseSchema.to_schema_model_dict(
            exclude_fields=exclude_fields
        )
        C_RequestSchema.to_put_model_dict(
            exclude_fields=exclude_fields
        )

    def test_non_nullable_column_excluded_D(self):
        """Confirms that non-nullable column exclusion raises
        an exception in the right situations"""
        exclude_fields = ['non_nullable_column']
        with pytest.raises(RequiredFieldExcludedException):
            D_RequestSchema.to_post_model_dict(
                exclude_fields=exclude_fields
            )
        with pytest.raises(RequiredFieldExcludedException):
            D_ResponseSchema.to_schema_model_dict(
                exclude_fields=exclude_fields
            )
        # should not raise exception on PUT dict
        D_RequestSchema.to_put_model_dict(
            exclude_fields=exclude_fields
        )
