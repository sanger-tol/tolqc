# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .base import Base, db


class TolqcStatusDict(Base):
    __tablename__ = "status_dict"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    description = db.Column(db.String())
    status = db.relationship("TolqcStatus", back_populates="status_dict")
