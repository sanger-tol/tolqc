# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model import db, TolqcUser
import os
import json
from jwt import (
    JWT,
    jwk_from_dict,
)
from jwt.exceptions import (
    JWTDecodeError,
)
from connexion.exceptions import OAuthProblem


def apikey_auth(token, required_scopes):
    # Direct from api-key (i.e. not Elixir)
    user = db.session.query(TolqcUser) \
        .filter(TolqcUser.api_key == token) \
        .one_or_none()

    if user is None:
        user = db.session.query(TolqcUser) \
            .filter(TolqcUser.token == token) \
            .one_or_none()
        if user is None:
            raise OAuthProblem('Invalid api-key and Elixir token')
        # Is the Elixir token valid and in date
        instance = JWT()
        # This is the Elixir public key as found at https://login.elixir-czech.org/oidc/jwk
        signing_key = jwk_from_dict(json.loads(os.getenv("ELIXIR_JWK")))
        try:
            payload = instance.decode(token, signing_key,
                                      do_verify=True, do_time_check=True,
                                      algorithms=['RS256'])
        except JWTDecodeError as e:
            raise OAuthProblem('Invalid Elixir token: '+e.args[0])
        print(payload)
    return {"user": user.name, "uid": user.user_id}
