# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.util import CustomException
from main import model


class Auth():
    @classmethod
    def check_token_valid(cls, token):
        user_id = model.TolqcUser.get_user_infos_by_token(token)
        if not user_id:
            raise CustomException(401, "User does not exist")
        return user_id
