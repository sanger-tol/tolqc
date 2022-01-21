# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .sub_base import SubBase, db


class TolqcSoftwareVersion(SubBase):
    __tablename__ = "software_version"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    version = db.Column(db.String())
    cmd = db.Column(db.String())
    busco = db.relationship("TolqcBusco", back_populates="software_version")
    merqury = db.relationship("TolqcMerqury", back_populates="software_version")
