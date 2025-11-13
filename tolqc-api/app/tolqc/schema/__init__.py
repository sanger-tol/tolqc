# SPDX-FileCopyrightText: 2024 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from sqlalchemy.orm import configure_mappers

from tolqc.schema.base import Base


def models_list(excluded_models: set):

    """
    The call to `configure_mappers()` is triggered lazily by SQLAlchemy when
    the first instance of a model is created.  Since we dynamically create an
    `EditBase` class for each `LogBase` subclass, we need to call
    `configure_mappers()` here to trigger creation of the `EditBase`
    subclasses and generate the full list of models.
    """
    configure_mappers()

    return tuple(x for m in Base.registry.mappers if (x := m.class_) not in excluded_models)
