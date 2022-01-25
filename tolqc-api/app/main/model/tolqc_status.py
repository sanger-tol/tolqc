# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .base import Base, db, setup_model
from sqlalchemy import Enum


StatusEnum = Enum("na",
                  "pending",
                  "topup",
                  "complete",
                  "archived",
                  name="status enum", create_type=False)

QCEnum = Enum("no_qc",
              "pending",
              "pass",
              "fail",
              "investigate",
              name="qc enum", create_type=False)

TechEnum = Enum("hifi",
                "hic",
                "10x",
                "htag",
                "bionano",
                "illumina",
                "ont",
                "rna-seq",
                "iso-seq",
                "contig_asm",
                "scaffold_asm",
                "asm2curation",
                name="tech enum", create_type=False)


@setup_model
class TolqcStatus(Base):
    __tablename__ = "statuses"
    id = db.Column(db.Integer(), primary_key=True)
    specimen_id = db.Column(db.Integer(), db.ForeignKey("specimens.id"),
                            nullable=False)
    coverage = db.Column(db.String())
    lims_id = db.Column(db.String())
    note_id = db.Column(db.String())
    changed = db.Column(db.DateTime())
    current = db.Column(db.String())
    status = db.Column(StatusEnum)
    qc = db.Column(QCEnum)
    technology = db.Column(TechEnum)
    specimens = db.relationship("TolqcSpecimen", back_populates="statuses")
