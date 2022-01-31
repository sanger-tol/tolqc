# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .log_base import LogBase, db
from .base import setup_model


@setup_model
class TolqcAllocation(LogBase):
    __tablename__ = "allocations"
    id = db.Column(db.Integer(), primary_key=True)
    project_id = db.Column(db.Integer(), db.ForeignKey("projects.id"))
    specimen_instance_id = db.Column(db.Integer(), db.ForeignKey("specimens.id"))
    is_primary = db.Column(db.Boolean())
    projects = db.relationship("TolqcProject", back_populates="allocations",
                               foreign_keys=[project_id])
    specimens = db.relationship("TolqcSpecimen", back_populates="allocations",
                                foreign_keys=[specimen_instance_id])
