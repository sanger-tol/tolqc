# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from tol.api_base.model import Base, db, setup_model


@setup_model
class BuscoMetrics(Base):
    __tablename__ = 'busco_metrics'

    class Meta:
        type_ = 'busco_metrics'

    id = db.Column(db.Integer(), primary_key=True)  # noqa: A003
    assembly_id = db.Column(db.Integer(), db.ForeignKey('assembly.assembly_id'))
    complete = db.Column(db.Integer())
    single = db.Column(db.Integer())
    duplicated = db.Column(db.Integer())
    fragmented = db.Column(db.Integer())
    missing = db.Column(db.Integer())
    count = db.Column(db.Integer())
    busco_lineage_id = db.Column(db.Integer(), db.ForeignKey('busco_lineage.id'))
    summary = db.Column(db.String())
    software_version_id = db.Column(
        db.Integer(), db.ForeignKey('software_version.software_version_id')
    )

    assembly = db.relationship('Assembly', back_populates='busco_metrics')
    busco_lineage = db.relationship('BuscoLineage', back_populates='busco_metrics')
    software_version = db.relationship(
        'SoftwareVersion', back_populates='busco_metrics'
    )
