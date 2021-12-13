# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from flask_restx import Namespace

from main.schema import CentreDetailSchema, \
                        CentreListSchema


class CentreSwagger:
    api = Namespace(
        'centres',
        description='Centre related methods',
    )

    detail_response_model = api.schema_model(
        'Centre Individual Response',
        CentreDetailSchema.to_response_schema_model_dict()
    )

    post_request_model = api.schema_model(
        'Centre POST Request',
        CentreListSchema.to_post_request_schema_model_dict()
    )

    put_request_model = api.model(
        'Centre PUT Request',
        CentreDetailSchema.to_put_request_model_dict()
    )

    list_response_model = api.schema_model(
        'Centre Bulk Response',
        CentreListSchema.to_response_schema_model_dict()
    )
