# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


class BaseSwagger:
    @classmethod
    def populate_default_models(cls):
        """Defines each of a:
        - detail response model
        - list response model
        - post request model
        - put request model
        """
        type_ = cls.detail_schema.Meta.type_.title()

        cls.detail_response_model = cls.api.schema_model(
            f'{type_} Individual Response',
            cls.detail_schema.to_response_schema_model_dict()
        )

        cls.post_request_model = cls.api.schema_model(
            f'{type_} POST Request',
            cls.list_schema.to_post_request_schema_model_dict()
        )

        cls.put_request_model = cls.api.model(
            f'{type_} PUT Request',
            cls.detail_schema.to_put_request_model_dict()
        )

        cls.list_response_model = cls.api.schema_model(
            f'{type_} Bulk Response',
            cls.list_schema.to_response_schema_model_dict()
        )
