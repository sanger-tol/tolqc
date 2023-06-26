# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from tol.api_base.model import Base, db, setup_model


@setup_model
class ContigvizMetrics(Base):
    __tablename__ = 'contigviz_metrics'

    class Meta:
        type_ = 'contigviz_metrics'

    id = db.Column(db.Integer(), primary_key=True)  # noqa: A003
    assembly_id = db.Column(
        db.Integer(), db.ForeignKey('assembly.assembly_id')
    )
    software_version_id = db.Column(
        db.Integer(), db.ForeignKey('software_version.software_version_id')
    )
    results = db.Column(db.JSON())

    assembly = db.relationship('Assembly', back_populates='contigviz_metrics')
    software_version = db.relationship(
        'SoftwareVersion', back_populates='contigviz_metrics'
    )
