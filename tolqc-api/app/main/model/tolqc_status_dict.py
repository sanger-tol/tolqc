# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .base import db, setup_model
from .enum_base import EnumBase


@setup_model
class TolqcStatusDict(EnumBase):
    __tablename__ = "status_dict"
    status = db.relationship("TolqcStatus", back_populates="status_dict")
