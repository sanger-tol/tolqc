# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from marshmallow_jsonapi import Schema, SchemaOpts
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema , \
                                   SQLAlchemyAutoSchemaOpts


class CombinedOpts(SQLAlchemyAutoSchemaOpts, SchemaOpts):
    pass


class BaseSchema(SQLAlchemyAutoSchema, Schema):
    OPTIONS_CLASS = CombinedOpts
