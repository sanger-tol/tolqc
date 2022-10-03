# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .base import db, setup_model
from .enum_base import EnumBase


@setup_model
class TolqcStatusDict(EnumBase):
    __tablename__ = "status_dict"

    class Meta:
        type_ = 'status_types'

    status = db.relationship("TolqcStatus", back_populates="status_dict")
