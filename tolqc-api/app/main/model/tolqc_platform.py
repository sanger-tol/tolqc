# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .base import Base, db, setup_model


@setup_model
class TolqcPlatform(Base):
    __tablename__ = "platform"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    model = db.Column(db.String())
    run = db.relationship("TolqcRun", back_populates="platform")
