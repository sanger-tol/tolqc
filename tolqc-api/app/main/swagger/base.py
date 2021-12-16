# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from flask_restx import Namespace


class BaseNamespace(Namespace):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, validate=True, **kwargs)


class BaseSwagger:
    @classmethod
    def populate_default_models(cls):
        """Defines each of a:
        - post request model
        - patch request model
        """
        schema = cls.Meta.schema
        type_ = schema.get_type().title()

        cls.post_request_model = cls.api.schema_model(
            f'{type_} POST Request',
            schema.to_post_request_schema_model_dict()
        )

        cls.patch_request_model = cls.api.schema_model(
            f'{type_} PUT Request',
            schema.to_put_request_schema_model_dict()
        )
