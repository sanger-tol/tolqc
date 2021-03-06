# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .log_base import LogBase, db
from .base import setup_model


@setup_model
class TolqcAllocation(LogBase):
    __tablename__ = "allocation"

    class Meta:
        type_ = 'allocations'

    id = db.Column(db.Integer(), primary_key=True)
    project_id = db.Column(db.Integer(), db.ForeignKey("project.id"))
    specimen_id = db.Column(db.Integer(), db.ForeignKey("specimen.id"))
    is_primary = db.Column(db.Boolean())
    project = db.relationship("TolqcProject", back_populates="allocation",
                              foreign_keys=[project_id])
    specimen = db.relationship("TolqcSpecimen", back_populates="allocation",
                               foreign_keys=[specimen_id])
