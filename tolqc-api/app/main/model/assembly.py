# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from tol.api_base.model import LogBase, db, setup_model
from sqlalchemy.ext.associationproxy import association_proxy


@setup_model
class Assembly(LogBase):
    __tablename__ = 'assembly'

    class Meta:
        type_ = 'assemblies'
        id_column = 'assembly_id'

    assembly_id = db.Column(db.Integer(), primary_key=True)  # noqa: A003
    software_version_id = db.Column(
        db.Integer(), db.ForeignKey('software_version.software_version_id')
    )
    dataset_id = db.Column(db.String(), db.ForeignKey('dataset.dataset_id'))
    component_type_id = db.Column(
        db.String(), db.ForeignKey('assembly_component_type.component_type_id')
    )
    assembly_status_id = db.Column(
        db.Integer(), db.ForeignKey('assembly_status.assembly_status_id')
    )
    name = db.Column(db.String())
    description = db.Column(db.String())

    dataset = db.relationship('Dataset', back_populates='assembly')
    component_type = db.relationship(
        'AssemblyComponentType', back_populates='assemblies'
    )
    software_version = db.relationship('SoftwareVersion', back_populates='assemblies')

    assembly_metrics = db.relationship('AssemblyMetrics', back_populates='assembly')
    busco_metrics = db.relationship('BuscoMetrics', back_populates='assembly')
    contigviz_metrics = db.relationship('ContigvizMetrics', back_populates='assembly')
    merqury_metrics = db.relationship('MerquryMetrics', back_populates='assembly')
    markerscan_metrics = db.relationship('MarkerscanMetrics', back_populates='assembly')

    status = db.relationship('AssemblyStatus', foreign_keys=[assembly_status_id])
    status_history = db.relationship(
        'AssemblyStatus',
        primaryjoin='Assembly.assembly_id == AssemblyStatus.assembly_id',
        back_populates='assembly',
    )

    # Sources are assemblies for which there is a row in assembly_source
    # with this instance"s assembly_id
    source_assembly_assn = db.relationship(
        'AssemblySource',
        primaryjoin='Assembly.assembly_id == AssemblySource.assembly_id',
        back_populates='component',
    )
    sources = association_proxy('source_assembly_assn', 'source')

    # Components are assemblies which have this assembly as their source
    component_assembly_assn = db.relationship(
        'AssemblySource',
        primaryjoin='Assembly.assembly_id == AssemblySource.source_assembly_id',
        back_populates='source',
    )
    components = association_proxy('component_assembly_assn', 'component')
