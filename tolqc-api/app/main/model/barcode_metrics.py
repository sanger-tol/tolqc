# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from tol.api_base.model import Base, db, setup_model


@setup_model
class BarcodeMetrics(Base):
    __tablename__ = 'barcode_metrics'

    class Meta:
        type_ = 'barcode_metrics'

    id = db.Column(db.Integer(), primary_key=True)  # noqa: A003
    data_id = db.Column(db.Integer(), db.ForeignKey('data.data_id'))
    qc_id = db.Column(db.Integer())  # QCDict pass|fail ?
    species_match_top = db.Column(
        db.String()
    )  # Is this a foreign key to the species table?
    species_match_identity = db.Column(db.Float())
    species_match_barcode = db.Column(db.String())

    data = db.relationship('Data', back_populates='barcode_metrics')
