# SPDX-FileCopyrightText: 2024 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from datetime import timedelta

from sqlalchemy.orm import configure_mappers

from tol.sql.action import create_action_models
from tol.sql.auth.models import create_models

import tolqc.schema.accession_models
import tolqc.schema.assembly_models
import tolqc.schema.folder_models
import tolqc.schema.metagenome_models
import tolqc.schema.sample_data_models  # noqa: F401
from tolqc.schema.base import Base
from tolqc.schema.system_models import UserMixin


action_models = create_action_models(Base)

auth_models = create_models(
    model_base=Base,
    user_table_name='user',
    oidc_id_column_name='email',
    user_mixin_class=type('ToLQCUserMixin', (UserMixin, action_models._user_mixin), {}),
    token_mixin_class=object,
    token_is_pk=False,
    role_mixin_class=object,
    token_expiry_delta=timedelta(days=7),
    prefix_with_name=False,
)
Role = auth_models.role_class
RoleBinding = auth_models.role_binding_class
Token = auth_models.token_class
User = auth_models.user_class


def models_list():
    """
    The call to `configure_mappers()` is triggered lazily by SQLAlchemy when
    the first instance of a model is created.  Since we dynamically create an
    `EditBase` class for each `LogBase` subclass, we need to call
    `configure_mappers()` here to trigger creation of the `EditBase`
    subclasses and generate the full list of models.
    """

    excluded_models = {x for x in auth_models if x != User}
    configure_mappers()
    return tuple(x for m in Base.registry.mappers if (x := m.class_) not in excluded_models)
