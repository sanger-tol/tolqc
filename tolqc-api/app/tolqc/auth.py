# SPDX-FileCopyrightText: 2024 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from typing import Callable

from tol.api_base2.auth import require_auth
from tol.api_base2.misc.auth_context import CtxGetter, default_ctx_getter
from tol.sql.session import SessionFactory

from tolqc.system_models import User


require_registered = require_auth(role='registered')


def create_auth_ctx_setter(
    session_factory: SessionFactory,

    ctx_getter: CtxGetter = default_ctx_getter,
) -> Callable[[str], None]:
    """
    Given a `SessionFactory`, returns a callable that takes a token
    and sets the relevant `User` details on the auth context.
    """

    def set_auth_context(token: str) -> None:

        with session_factory() as sess:
            user = User.get_by_token(token, sess)

            if user is None:
                return

            auth_ctx = ctx_getter()
            auth_ctx.user_id = user.id
            auth_ctx.roles = user.roles

    return set_auth_context
