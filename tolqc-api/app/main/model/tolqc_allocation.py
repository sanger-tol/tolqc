# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .creation_log_base import CreationLogBase, db


class TolqcAllocation(CreationLogBase):
    __tablename__ = "allocations"
    id = db.Column(db.Integer(), primary_key=True)
    project_id = db.Column(db.Integer(), db.ForeignKey("projects.id"))
    specimen_instance_id = db.Column(db.Integer(), db.ForeignKey("specimens.id"))
    is_primary = db.Column(db.Boolean())
    projects = db.relationship("TolqcProject", back_populates="allocations",
                              foreign_keys=[project_id])
    specimens = db.relationship("TolqcSpecimen", back_populates="allocations",
                               foreign_keys=[specimen_instance_id])
