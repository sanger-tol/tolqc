# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from sqlalchemy.ext.associationproxy import association_proxy

from tol.api_base.model import LogBase, db, setup_model


@setup_model
class Data(LogBase):
    __tablename__ = 'data'

    class Meta:
        type_ = 'data'
        id_column = 'data_id'

    data_id = db.Column(db.Integer(), primary_key=True)
    name_root = db.Column(db.String())
    hierarchy_name = db.Column(db.String())
    sample_id = db.Column(db.String(), db.ForeignKey('sample.sample_id'))
    library_id = db.Column(db.String(), db.ForeignKey('library.library_id'))
    accession_id = db.Column(
        db.String(), db.ForeignKey('accession.accession_id')
    )
    run_id = db.Column(db.Integer(), db.ForeignKey('run.id'))
    processed = db.Column(db.Integer())
    tag1_sequence = db.Column(db.String())
    tag2_sequence = db.Column(db.String())
    date = db.Column(db.DateTime())
    lims_qc = db.Column(db.String(), db.ForeignKey('qc_dict.qc_state'))
    auto_qc = db.Column(db.String(), db.ForeignKey('qc_dict.qc_state'))
    qc = db.Column(db.String(), db.ForeignKey('qc_dict.qc_state'))
    withdrawn = db.Column(db.Boolean())
    manually_withdrawn = db.Column(db.Boolean())
    reads = db.Column(db.Integer())
    bases = db.Column(db.Integer())
    read_length_mean = db.Column(db.Float())
    read_length_n50 = db.Column(db.Integer())
    elastic_mlwh_cksum = db.Column(db.String())

    sample = db.relationship('Sample', back_populates='data')
    library = db.relationship('Library', back_populates='data')
    accession = db.relationship('Accession', back_populates='data')
    run = db.relationship('Run', back_populates='data')
    files = db.relationship('File', back_populates='data')
    barcode_metrics = db.relationship('BarcodeMetrics', back_populates='data')

    project_assn = db.relationship('Allocation', back_populates='data')
    projects = association_proxy('project_assn', 'project')

    dataset_assn = db.relationship('DatasetElement', back_populates='data')
    datasets = association_proxy('dataset_assn', 'dataset')
