# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .base import Base, db


class TolqcAllocation(Base):
    __tablename__ = "allocation"
    id = db.Column(db.Integer(), db.ForeignKey("project.id"), primary_key=True)
    specimen_row_id = db.Column(db.Integer(), db.ForeignKey("specimen.id"), primary_key=True)
    is_primary = db.Column(db.Boolean())
    project = db.relationship("TolqcProject", back_populates="allocation",
                              foreign_keys=[id])
    specimen = db.relationship("TolqcSpecimen", back_populates="allocation",
                               foreign_keys=[specimen_row_id])
