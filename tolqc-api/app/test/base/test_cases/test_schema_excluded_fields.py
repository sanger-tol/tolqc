# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

import pytest

from main.schema.base import RequiredFieldExcludedException

from test.core import BaseTestCase
from test.core.schemas import C_DetailSchema, C_ListSchema, \
                              D_DetailSchema, D_ListSchema


class TestSchemaExlucdedFieldsToModelDict(BaseTestCase):
    def test_nullable_column_excluded_C(self):
        """Confirms that non-nullable column exclusion raises
        an exception in the right situations"""
        exclude_fields = ['nullable_column']
        # shouldn't raise exception on any dict conversion for C
        C_ListSchema.to_post_request_schema_model_dict(
            exclude_fields=exclude_fields
        )
        C_DetailSchema.to_response_schema_model_dict(
            exclude_fields=exclude_fields
        )
        C_DetailSchema.to_put_request_model_dict(
            exclude_fields=exclude_fields
        )

    def test_non_nullable_column_excluded_D(self):
        """Confirms that non-nullable column exclusion raises
        an exception in the right situations"""
        exclude_fields = ['non_nullable_column']
        with pytest.raises(RequiredFieldExcludedException):
            D_ListSchema.to_post_request_schema_model_dict(
                exclude_fields=exclude_fields
            )
        with pytest.raises(RequiredFieldExcludedException):
            D_DetailSchema.to_response_schema_model_dict(
                exclude_fields=exclude_fields
            )
        # should not raise exception on PUT dict
        D_DetailSchema.to_put_request_model_dict(
            exclude_fields=exclude_fields
        )
