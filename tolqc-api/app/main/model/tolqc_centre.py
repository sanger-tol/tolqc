# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .base import Base, db


class TolqcCentre(Base):
    __tablename__ = "centre"
    centre_id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    hierarchy_name = db.Column(db.String(), nullable=False)
    run = db.relationship("TolqcRun", back_populates="centre")

    @classmethod
    def find_by_centre_id(cls, _centre_id):
        return cls.query.filter_by(centre_id=_centre_id).one_or_none()
