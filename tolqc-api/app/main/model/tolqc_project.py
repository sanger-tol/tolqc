# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .log_base import LogBase, db
from .base import setup_model


@setup_model
class TolqcProject(LogBase):
    __tablename__ = "project"

    class Meta:
        type_ = 'projects'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    hierarchy_name = db.Column(db.String())
    description = db.Column(db.String())
    lims_id = db.Column(db.Integer())
    accession_id = db.Column(db.Integer(), db.ForeignKey("accession.id"))
    allocation = db.relationship("TolqcAllocation", back_populates="project")
    accession = db.relationship("TolqcAccession", back_populates="project",
                                foreign_keys=[accession_id])
