# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from tol.api_base.model import LogBase, db, setup_model


@setup_model
class Data(LogBase):
    __tablename__ = 'data'

    class Meta:
        type_ = 'data'

    id = db.Column(db.Integer(), primary_key=True)  # noqa A003
    name = db.Column(db.String())
    hierarchy_name = db.Column(db.String())
    sample_id = db.Column(db.Integer(), db.ForeignKey('sample.id'))
    library_id = db.Column(db.Integer(), db.ForeignKey('library.id'))
    accession_id = db.Column(db.Integer(), db.ForeignKey('accession.id'))
    run_id = db.Column(db.Integer(), db.ForeignKey('run.id'))
    processed = db.Column(db.Integer())
    tag_index = db.Column(db.String())
    tag1_id = db.Column(db.String())
    tag2_id = db.Column(db.String())
    lims_qc = db.Column(db.Integer())
    auto_qc = db.Column(db.Integer())
    qc = db.Column(db.Integer())
    withdrawn = db.Column(db.Boolean())
    manually_withdrawn = db.Column(db.Boolean())
    checksum_from_mlwh = db.Column(db.String())
    sample = db.relationship('Sample', back_populates='data', foreign_keys=[sample_id])
    library = db.relationship(
        'Library', back_populates='data', foreign_keys=[library_id]
    )
    run = db.relationship('Run', back_populates='data', foreign_keys=[run_id])
    accession = db.relationship(
        'Accession', back_populates='data', foreign_keys=[accession_id]
    )
    set = db.relationship('Set', back_populates='data')  # noqa A003
    file = db.relationship('File', back_populates='data')
