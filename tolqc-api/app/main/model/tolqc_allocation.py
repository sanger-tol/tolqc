# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .base import Base, db


class TolqcAllocation(Base):
    __tablename__ = "allocation"
    project_id = db.Column(db.String(), db.ForeignKey("project.project_id"), primary_key=True)
    specimen_id = db.Column(db.String(), db.ForeignKey("specimen.specimen_id"), primary_key=True)
    is_primary = db.Column(db.Integer())
    project = db.relationship("TolqcProject", back_populates="allocation",
                              foreign_keys=[project_id])
    specimen = db.relationship("TolqcSpecimen", back_populates="allocation",
                               foreign_keys=[specimen_id])
