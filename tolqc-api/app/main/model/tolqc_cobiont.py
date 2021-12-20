# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .sub_base import SubBase, db


class TolqcCobiont(SubBase):
    __tablename__ = "cobiont"
    id = db.Column(db.Integer(), primary_key=True)
    cobiont_id = db.Column(db.Integer(), nullable=False)
    name = db.Column(db.String())
    alias = db.Column(db.String())
    specimen_instance_id = db.Column(db.Integer(), db.ForeignKey("specimen.id"),
                                     nullable=False)
    changed = db.Column(db.DateTime())
    current = db.Column(db.String())
    specimen = db.relationship("TolqcSpecimen", back_populates="cobiont",
                               foreign_keys=[specimen_instance_id])