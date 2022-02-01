# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .base import Base, db, setup_model


@setup_model
class TolqcAccessionTypeDict(Base):
    __tablename__ = "accession_type_dict"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    accession = db.relationship("TolqcAccession", back_populates="accession_type_dict")
