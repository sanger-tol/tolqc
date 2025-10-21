# SPDX-FileCopyrightText: 2024 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from sqlalchemy.orm import configure_mappers

from tol.sql.board import create_board_models
from tol.sql.auth.models import create_models

import tolqc.schema.accession_models
import tolqc.schema.assembly_models
import tolqc.schema.folder_models
import tolqc.schema.metagenome_models
import tolqc.schema.sample_data_models  # noqa: F401
from tolqc.schema.base import Base
from tol.sql import Model

from tolqc.schema import system_models

# def __get_board_models(
#     base_model: Model
# ) -> tuple[list[Model], Model]:
#     board_models = create_board_models(base_model)

#     return list(board_models), board_models._user_mixin

def models_list():
    board_models = create_board_models(Base)
    create_models(Base)

    user_mixin = type(
        'User',
        (system_models.UserMixin, board_models._user_mixin),
        {}
    )

    """
    The call to `configure_mappers()` is triggered lazily by SQLAlchemy when
    the first instance of a model is created.  Since we dynamically create an
    `EditBase` class for each `LogBase` subclass, we need to call
    `configure_mappers()` here to trigger creation of the `EditBase`
    subclasses and generate the full list of models.
    """
    configure_mappers()

    excluded_models = []
    return tuple(x for m in Base.registry.mappers if (x := m.class_) not in excluded_models)
