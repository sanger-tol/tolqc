# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from tol.api_base.model import Base, db, setup_model


@setup_model
class AssemblyMetrics(Base):
    __tablename__ = 'assembly_metrics'

    class Meta:
        type_ = 'assembly_metrics'

    id = db.Column(db.Integer(), primary_key=True)  # noqa: A003
    assembly_id = db.Column(
        db.Integer(), db.ForeignKey('assembly.assembly_id')
    )
    bases = db.Column(db.BigInteger())
    a = db.Column(db.BigInteger())
    c = db.Column(db.BigInteger())
    g = db.Column(db.BigInteger())
    t = db.Column(db.BigInteger())
    n = db.Column(db.BigInteger())
    cpg = db.Column(db.BigInteger())
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
    assembly = db.relationship('Assembly', back_populates='assembly_metrics')
