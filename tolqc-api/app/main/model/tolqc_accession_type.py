# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .base import db, setup_model
from .enum_base import EnumBase


@setup_model
class TolqcAccessionType(EnumBase):
    __tablename__ = "accession_type"
    accession = db.relationship("TolqcAccession", back_populates="accession_type")
