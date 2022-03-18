# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .base import db, EnumBase, setup_model


@setup_model
class TolqcStatusDict(EnumBase):
    __tablename__ = "status_dict"

    class Meta:
        type_ = 'status_types'

    status = db.relationship("TolqcStatus", back_populates="status_dict")
