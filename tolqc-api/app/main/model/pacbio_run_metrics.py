# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from tol.api_base.model import Base, db, setup_model


@setup_model
class PacbioRunMetrics(Base):
    __tablename__ = 'pacbio_run_metrics'

    class Meta:
        type_ = 'pacbio_run_metrics'
        id_column = 'run_id'

    run_id = db.Column(
        db.String(), db.ForeignKey('run.run_id'), primary_key=True
    )
    movie_minutes = db.Column(db.Integer())
    binding_kit = db.Column(db.String())
    sequencing_kit = db.Column(db.String())
    include_kinetics = db.Column(db.String())
    loading_conc = db.Column(db.Float())
    control_num_reads = db.Column(db.Integer())
    control_read_length_mean = db.Column(db.Float())
    polymerase_read_bases = db.Column(db.BigInteger())
    polymerase_num_reads = db.Column(db.Integer())
    polymerase_read_length_mean = db.Column(db.Float())
    polymerase_read_length_n50 = db.Column(db.Integer())
    insert_length_mean = db.Column(db.Float())
    insert_length_n50 = db.Column(db.Integer())
    unique_molecular_bases = db.Column(db.BigInteger())
    p0_num = db.Column(db.Integer())
    p1_num = db.Column(db.Integer())
    p2_num = db.Column(db.Integer())
    hifi_read_bases = db.Column(db.BigInteger())
    hifi_num_reads = db.Column(db.Integer())
    hifi_low_quality_num_reads = db.Column(db.Integer())

    run = db.relationship('Run', back_populates='pacbio_run_metrics')
