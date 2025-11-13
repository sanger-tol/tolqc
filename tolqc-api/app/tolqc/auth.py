# SPDX-FileCopyrightText: 2024 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from tol.api_base.auth import CompositeAuthInspector, require_auth
from tol.api_base.auth.error import ForbiddenError
from tol.api_base.misc.auth_context import (
    CtxGetter,
    default_ctx_getter
)
from tol.core.operator import OperatorMethod

require_editor = require_auth(role='editor')


def create_auth_inspector(
    admin_role: str = 'admin',
    ctx_getter: CtxGetter = default_ctx_getter
) -> CompositeAuthInspector:

    composite = CompositeAuthInspector(
        admin_role=admin_role,
        ctx_getter=ctx_getter
    )

    @composite.noauth
    def __no_write_without_auth(
        __object_type: str,
        op: OperatorMethod,
        **kwargs
    ):

        __WRITE_METHODS = (  # noqa N806
            OperatorMethod.DELETE,
            OperatorMethod.INSERT,
            OperatorMethod.UPDATE,
            OperatorMethod.UPSERT,
        )

        if op in __WRITE_METHODS:
            raise ForbiddenError()

    return composite
