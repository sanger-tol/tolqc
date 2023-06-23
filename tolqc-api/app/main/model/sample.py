# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from tol.api_base.model import LogBase, db, setup_model


@setup_model
class Sample(LogBase):
    __tablename__ = 'sample'

    class Meta:
        type_ = 'samples'
        id_column = 'sample_id'

    sample_id = db.Column(db.String(), primary_key=True)
    hierarchy_name = db.Column(db.String())
    lims_id = db.Column(db.Integer())
    specimen_id = db.Column(db.String(), db.ForeignKey('specimen.specimen_id'))
    accession_id = db.Column(db.String(), db.ForeignKey('accession.accession_id'))

    specimen = db.relationship('Specimen', back_populates='samples')
    accession = db.relationship('Accession', back_populates='samples')
    data = db.relationship('Data', back_populates='sample')
