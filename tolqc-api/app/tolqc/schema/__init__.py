# SPDX-FileCopyrightText: 2024 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from sqlalchemy.orm import configure_mappers

import tolqc.schema.assembly_models
import tolqc.schema.folder_models
import tolqc.schema.sample_data_models  # noqa: F401
from tolqc.schema.base import Base
from tolqc.schema.system_models import Token


def models_list():
    """
    The call to `configure_mappers()` is triggered lazily by SQLAlchemy when
    the first instance of a model is created.  Since we dynamically create an
    `EditBase` class for each `LogBase` subclass, we need to call
    `configure_mappers()` here to trigger creation of the `EditBase`
    subclasses and generate the full list of models.
    """
    configure_mappers()

    # Exclude Token class from API
    return tuple(x for m in Base.registry.mappers if (x := m.class_) != Token)
