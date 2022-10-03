# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .tol.api_base.model import Base, db
from .tol.api_base.model import setup_model


@setup_model
class TolqcCentre(Base):
    __tablename__ = "centre"

    class Meta:
        type_ = 'centres'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    hierarchy_name = db.Column(db.String())
    run = db.relationship("TolqcRun", back_populates="centre")
