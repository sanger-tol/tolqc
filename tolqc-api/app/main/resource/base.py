# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from flask_restx import Namespace


class BaseNamespace(Namespace):
    """Wrapper for flask-restxNamespace, that always validates
    input using Marshmallow"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, validate=True, **kwargs)
