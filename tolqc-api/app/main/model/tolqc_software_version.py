# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .creation_log_base import CreationLogBase, db


class TolqcSoftwareVersion(CreationLogBase):
    __tablename__ = "software_version"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    version = db.Column(db.String())
    cmd = db.Column(db.String())
    busco_metrics = db.relationship("TolqcBuscoMetrics", back_populates="software_version")
    merqury_metrics = db.relationship("TolqcMerquryMetrics", back_populates="software_version")
    genomescope_metrics = db.relationship("TolqcGenomescopeMetrics",
                                          back_populates="software_version")
