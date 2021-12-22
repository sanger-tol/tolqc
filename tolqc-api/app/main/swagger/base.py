# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from flask_restx import Namespace


def setup_swagger(cls):
    cls.populate_default_models()
    return cls


class BaseSwagger:
    @classmethod
    def populate_default_models(cls):
        """Defines each of a:
        - post request model
        - patch request model
        """
        schema = cls.Meta.schema
        type_ = schema.get_type()

        cls.api = Namespace(
            type_,
            description=f'Methods relating to {type_}',
            #validate=True - idk why this changes anythihng :shrug: it sees columns it shouldn't
        )

        cls.post_request_model = cls.api.schema_model(
            f'{type_.title()} POST Request',
            schema.to_post_request_schema_model_dict()
        )

        cls.patch_request_model = cls.api.schema_model(
            f'{type_.title()} PUT Request',
            schema.to_patch_request_schema_model_dict()
        )
