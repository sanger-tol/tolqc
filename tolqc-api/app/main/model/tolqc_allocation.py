# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .base import Base, db


class TolqcAllocation(Base):
    __tablename__ = "allocation"
    project_id = db.Column(db.Integer(), db.ForeignKey("project.project_id"), primary_key=True)
    specimen_row_id = db.Column(db.Integer(), db.ForeignKey("specimen.row_id"), primary_key=True)
    is_primary = db.Column(db.Boolean())
    project = db.relationship("TolqcProject", back_populates="allocation",
                              foreign_keys=[project_id])
    specimen = db.relationship("TolqcSpecimen", back_populates="allocation",
                               foreign_keys=[specimen_row_id])
