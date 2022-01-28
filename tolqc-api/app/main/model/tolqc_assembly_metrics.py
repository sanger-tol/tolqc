# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .creation_log_base import CreationLogBase, db


class TolqcAssemblyMetrics(CreationLogBase):
    __tablename__ = "assembly_metrics"
    id = db.Column(db.Integer(), primary_key=True)
    assembly_id = db.Column(db.Integer, db.ForeignKey("assembly.id"))
    assembly_component_id = db.Column(db.Integer,
                                      db.ForeignKey("assembly_component.id"))
    bases = db.Column(db.Integer())
    a = db.Column(db.Integer())
    c = db.Column(db.Integer())
    g = db.Column(db.Integer())
    t = db.Column(db.Integer())
    n = db.Column(db.Integer())
    cpg = db.Column(db.Integer())
    iupac3 = db.Column(db.Integer())
    iupac2 = db.Column(db.Integer())
    ts = db.Column(db.Integer())
    tv = db.Column(db.Integer())
    cpg_ts = db.Column(db.Integer())
    contig_n = db.Column(db.Integer())
    contig_length = db.Column(db.Integer())
    contig_n50 = db.Column(db.Integer())
    contig_aun = db.Column(db.Float())
    contig_longest = db.Column(db.Integer())
    contig_shortest = db.Column(db.Integer())
    contig_length_mean = db.Column(db.Float())
    scaffold_n = db.Column(db.Integer())
    scaffold_n50 = db.Column(db.Integer())
    scaffold_aun = db.Column(db.Float())
    gap_n = db.Column(db.Integer())
    gap_n50 = db.Column(db.Integer())
    assembly = db.relationship("TolqcAssembly", back_populates="assembly_metrics",
                               foreign_keys=[assembly_id])
    assembly_component = db.relationship("TolqcAssemblyComponent",
                                         back_populates="assembly_metrics",
                                         foreign_keys=[assembly_component_id])
