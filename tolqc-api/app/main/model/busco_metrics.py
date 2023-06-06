# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from tol.api_base.model import LogBase, db, setup_model


@setup_model
class BuscoMetrics(LogBase):
    __tablename__ = 'busco_metrics'

    class Meta:
        type_ = 'busco_metrics'

    id = db.Column(db.Integer(), primary_key=True)  # noqa A003
    assembly_id = db.Column(db.Integer(), db.ForeignKey('assembly.id'))
    assembly_component_id = db.Column(
        db.Integer(), db.ForeignKey('assembly_component.id')
    )
    complete = db.Column(db.Integer())
    single = db.Column(db.Integer())
    duplicated = db.Column(db.Integer())
    fragmented = db.Column(db.Integer())
    missing = db.Column(db.Integer())
    count = db.Column(db.Integer())
    busco_lineage_id = db.Column(db.Integer(), db.ForeignKey('busco_lineage.id'))
    summary = db.Column(db.String())
    software_version_id = db.Column(db.Integer(), db.ForeignKey('software_version.id'))
    assembly = db.relationship(
        'Assembly', back_populates='busco_metrics', foreign_keys=[assembly_id]
    )
    assembly_component = db.relationship(
        'AssemblyComponent',
        back_populates='busco_metrics',
        foreign_keys=[assembly_component_id],
    )
    busco_lineage = db.relationship(
        'BuscoLineage', back_populates='busco_metrics', foreign_keys=[busco_lineage_id]
    )
    software_version = db.relationship(
        'SoftwareVersion',
        back_populates='busco_metrics',
        foreign_keys=[software_version_id],
    )
