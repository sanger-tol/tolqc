# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .log_base import LogBase, db
from .base import setup_model


@setup_model
class TolqcSample(LogBase):
    __tablename__ = "samples"
    id = db.Column(db.Integer(), primary_key=True)
    sample_id = db.Column(db.Integer(), nullable=False)
    name = db.Column(db.String(), nullable=False)
    hierarchy_name = db.Column(db.String(), nullable=False)
    lims_id = db.Column(db.Integer())
    specimen_instance_id = db.Column(db.Integer(), db.ForeignKey("specimens.id"),
                                     nullable=False)
    accession_id = db.Column(db.Integer())
    changed = db.Column(db.DateTime())
    current = db.Column(db.Boolean())
    specimens = db.relationship("TolqcSpecimen", back_populates="samples",
                                foreign_keys=[specimen_instance_id])
    seq = db.relationship("TolqcSeq", back_populates="samples")
