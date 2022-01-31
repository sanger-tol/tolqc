# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .base import Base, db, setup_model


@setup_model
class TolqcQcDict(Base):
    __tablename__ = "qc_dict"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    description = db.Column(db.String())
    status = db.relationship("TolqcStatus", back_populates="qc_dict")
    genomescope_metrics = db.relationship("TolqcGenomescopeMetrics",
                                          back_populates="qc_dict")
