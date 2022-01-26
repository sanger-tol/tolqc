# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .creation_log_base import CreationLogBase, db
from .base import setup_model


@setup_model
class TolqcAsmStats(CreationLogBase):
    __tablename__ = "asm_stats"
    id = db.Column(db.Integer(), primary_key=True)
    bases = db.Column(db.String())
    a = db.Column(db.String())
    c = db.Column(db.String())
    g = db.Column(db.String())
    t = db.Column(db.String())
    n = db.Column(db.String())
    cpg = db.Column(db.String())
    iupac3 = db.Column(db.String())
    iupac2 = db.Column(db.String())
    ts = db.Column(db.String())
    tv = db.Column(db.String())
    cpg_ts = db.Column(db.String())
    contig_n = db.Column(db.Float())
    contig_length = db.Column(db.Float())
    contig_n50 = db.Column(db.Float())
    contig_longest = db.Column(db.Float())
    contig_shortest = db.Column(db.Float())
    contig_mean = db.Column(db.Float())
    scaffold_n = db.Column(db.Float())
    scaffold_n50 = db.Column(db.Float())
    gap_n = db.Column(db.Float())
    gap_n50 = db.Column(db.Float())
    asm = db.relationship("TolqcAsm", back_populates="asm_stats")
    busco = db.relationship("TolqcBusco", back_populates="asm_stats")
    merqury = db.relationship("TolqcMerqury", back_populates="asm_stats")
