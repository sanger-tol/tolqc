# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from tol.api_base.model import Base, db, setup_model


@setup_model
class SoftwareVersion(Base):
    __tablename__ = 'software_version'

    class Meta:
        type_ = 'software_versions'
        id_column = 'software_version_id'

    software_version_id = db.Column(
        db.Integer(), primary_key=True
    )  # noqa: A003
    name = db.Column(db.String())
    version = db.Column(db.String())
    cmd = db.Column(db.String())

    db.UniqueConstraint('name', 'version')

    assemblies = db.relationship('Assembly', back_populates='software_version')
    busco_metrics = db.relationship(
        'BuscoMetrics', back_populates='software_version'
    )
    contigviz_metrics = db.relationship(
        'ContigvizMetrics', back_populates='software_version'
    )
    genomescope_metrics = db.relationship(
        'GenomescopeMetrics', back_populates='software_version'
    )
    markerscan_metrics = db.relationship(
        'MarkerscanMetrics', back_populates='software_version'
    )
    merqury_metrics = db.relationship(
        'MerquryMetrics', back_populates='software_version'
    )
    ploidyplot_metrics = db.relationship(
        'PloidyplotMetrics', back_populates='software_version'
    )
