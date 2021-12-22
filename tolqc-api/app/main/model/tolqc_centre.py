# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .sub_base import CreationLogBase, db
from .base import ExtColumn #reeemove


class TolqcCentre(CreationLogBase):
    __tablename__ = "centre"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    hierarchy_name = db.Column(db.String(), nullable=False)
    run = db.relationship("TolqcRun", back_populates="centre")
    ext = ExtColumn()
