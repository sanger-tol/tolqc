# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .creation_log_base import CreationLogBase, db


class TolqcProject(CreationLogBase):
    __tablename__ = "project"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    hierarchy_name = db.Column(db.String(), nullable=False)
    description = db.Column(db.String())
    lims_id = db.Column(db.Integer())
    accession_id = db.Column(db.Integer())
    allocation = db.relationship("TolqcAllocation", back_populates="project")
