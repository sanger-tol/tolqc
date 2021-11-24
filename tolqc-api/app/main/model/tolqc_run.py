# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .base import Base, db
from .tolqc_centre import TolqcCentre


class TolqcRun(Base):
    __tablename__ = "run"
    # the row id
    id = db.Column(db.Integer(), primary_key=True)
    run_id = db.Column(db.Integer(), nullable=False)
    name = db.Column(db.String(), nullable=False)
    hierarchy_name = db.Column(db.String(), nullable=False)
    #platform_id = db.Column(db.Integer(), db.ForeignKey("platform.platform_id"),
    #                        nullable=False)
    centre_id = db.Column(db.Integer(), db.ForeignKey(TolqcCentre.id),
                          nullable=False)
    lims_id = db.Column(db.Integer())
    element = db.Column(db.String())
    changed = db.Column(db.DateTime())
    current = db.Column(db.Boolean())
    #seq = db.relationship("TolqcSeq", back_populates="run")
    #platform = db.relationship("TolqcPlatform", back_populates="run")#, foreign_keys="[TolqcPlatform.platform_id]")
    centre = db.relationship(TolqcCentre, back_populates="run", foreign_keys=[centre_id])#, foreign_keys="[TolqcCentre.id]")

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).one_or_none()
