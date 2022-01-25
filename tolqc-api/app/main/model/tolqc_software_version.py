# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .creation_log_base import CreationLogBase, db
from .base import setup_model


@setup_model
class TolqcSoftwareVersion(CreationLogBase):
    __tablename__ = "software_versions"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    version = db.Column(db.String())
    cmd = db.Column(db.String())
    busco = db.relationship("TolqcBusco", back_populates="software_versions")
    merqury = db.relationship("TolqcMerqury", back_populates="software_versions")
