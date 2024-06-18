# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from sqlalchemy import (
    BigInteger,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
    UniqueConstraint,
)
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import mapped_column, relationship

from tolqc.folder_models import HasFolder
from tolqc.model import Base, LogBase


def models_list():
    return [
        Assembly,
        AssemblyComponentType,
        AssemblyMetrics,
        AssemblySource,
        AssemblyStatus,
        AssemblyStatusType,
        BuscoLineage,
        BuscoMetrics,
        ContigvizMetrics,
        Dataset,
        DatasetElement,
        DatasetStatus,
        DatasetStatusType,
        GenomescopeMetrics,
        MarkerscanMetrics,
        MerquryMetrics,
        PloidyplotMetrics,
        ReviewDict,
        SoftwareVersion,
    ]


class Assembly(LogBase):
    __tablename__ = 'assembly'

    @classmethod
    def get_id_column_name(cls):
        return 'assembly_id'

    assembly_id = mapped_column(Integer, primary_key=True)
    software_version_id = mapped_column(
        Integer,
        ForeignKey('software_version.software_version_id'),
    )
    dataset_id = mapped_column(String, ForeignKey('dataset.dataset_id'))
    component_type_id = mapped_column(
        String,
        ForeignKey('assembly_component_type.component_type_id'),
    )
    assembly_status_id = mapped_column(
        Integer,
        ForeignKey('assembly_status.assembly_status_id'),
    )
    name = mapped_column(String)
    description = mapped_column(String)
    bioproject_accession_id = mapped_column(
        String,
        ForeignKey('accession.accession_id'),
    )
    genome_accession_id = mapped_column(
        String,
        ForeignKey('accession.accession_id'),
    )

    dataset = relationship('Dataset', back_populates='assembly')
    component_type = relationship(
        'AssemblyComponentType',
        back_populates='assemblies',
    )
    software_version = relationship(
        'SoftwareVersion',
        back_populates='assemblies',
    )

    assembly_metrics = relationship(
        'AssemblyMetrics',
        back_populates='assembly',
    )
    busco_metrics = relationship('BuscoMetrics', back_populates='assembly')
    contigviz_metrics = relationship(
        'ContigvizMetrics',
        back_populates='assembly',
    )
    mapping_metrics = relationship(
        'MappingMetrics',
        back_populates='assembly',
    )
    merqury_metrics = relationship('MerquryMetrics', back_populates='assembly')
    markerscan_metrics = relationship(
        'MarkerscanMetrics',
        back_populates='assembly',
    )
    bioproject_accession = relationship(
        'Accession',
        back_populates='bioproject_assemblies',
        foreign_keys=[bioproject_accession_id],
    )
    genome_accession = relationship(
        'Accession',
        back_populates='genome_assemblies',
        foreign_keys=[genome_accession_id],
    )

    status = relationship('AssemblyStatus', foreign_keys=[assembly_status_id])
    status_history = relationship(
        'AssemblyStatus',
        primaryjoin='Assembly.assembly_id == AssemblyStatus.assembly_id',
        back_populates='assembly',
    )

    # Sources are assemblies for which there is a row in assembly_source
    # with this instance's assembly_id
    source_assembly_assn = relationship(
        'AssemblySource',
        primaryjoin='Assembly.assembly_id == AssemblySource.assembly_id',
        back_populates='component',
    )
    sources = association_proxy('source_assembly_assn', 'source')

    # Components are assemblies which have this assembly as their source
    component_assembly_assn = relationship(
        'AssemblySource',
        primaryjoin='Assembly.assembly_id == AssemblySource.source_assembly_id',  # noqa: E501
        back_populates='source',
    )
    components = association_proxy('component_assembly_assn', 'component')


class AssemblyComponentType(Base):
    __tablename__ = 'assembly_component_type'

    @classmethod
    def get_id_column_name(cls):
        return 'component_type_id'

    component_type_id = mapped_column(String, primary_key=True)
    description = mapped_column(String)

    assemblies = relationship('Assembly', back_populates='component_type')


class AssemblyMetrics(Base):
    __tablename__ = 'assembly_metrics'

    id = mapped_column(Integer, primary_key=True)  # noqa: A003
    assembly_id = mapped_column(Integer, ForeignKey('assembly.assembly_id'))
    bases = mapped_column(BigInteger)
    bases_a = mapped_column(BigInteger)
    bases_c = mapped_column(BigInteger)
    bases_g = mapped_column(BigInteger)
    bases_t = mapped_column(BigInteger)
    bases_n = mapped_column(BigInteger)
    bases_cpg = mapped_column(BigInteger)
    bases_iupac3 = mapped_column(BigInteger)
    bases_iupac2 = mapped_column(BigInteger)
    bases_ts = mapped_column(BigInteger)
    bases_tv = mapped_column(BigInteger)
    bases_cpg_ts = mapped_column(BigInteger)
    contig_n = mapped_column(Integer)
    contig_length = mapped_column(BigInteger)
    contig_n50 = mapped_column(BigInteger)
    contig_aun = mapped_column(Float)
    contig_longest = mapped_column(BigInteger)
    contig_shortest = mapped_column(BigInteger)
    contig_length_mean = mapped_column(Float)
    scaffolds = mapped_column(Integer)
    scaffold_n50 = mapped_column(BigInteger)
    scaffold_aun = mapped_column(Float)
    gaps = mapped_column(Integer)
    gap_n50 = mapped_column(BigInteger)
    assembly = relationship('Assembly', back_populates='assembly_metrics')


class AssemblySource(Base):
    __tablename__ = 'assembly_source'

    id = mapped_column(Integer, primary_key=True)  # noqa: A003
    assembly_id = mapped_column(Integer, ForeignKey('assembly.assembly_id'))
    source_assembly_id = mapped_column(Integer, ForeignKey('assembly.assembly_id'))

    UniqueConstraint('assembly_id', 'source_assembly_id')

    source = relationship(
        'Assembly',
        foreign_keys=[source_assembly_id],
        back_populates='component_assembly_assn',
    )
    component = relationship(
        'Assembly',
        foreign_keys=[assembly_id],
        back_populates='source_assembly_assn',
    )


class AssemblyStatus(LogBase):
    __tablename__ = 'assembly_status'

    @classmethod
    def get_id_column_name(cls):
        return 'assembly_status_id'

    assembly_status_id = mapped_column(Integer, primary_key=True)
    assembly_id = mapped_column(
        Integer,
        ForeignKey('assembly.assembly_id'),
        nullable=False,
    )
    status_type_id = mapped_column(
        String,
        ForeignKey('assembly_status_type.status_type_id'),
        nullable=False,
    )
    status_time = mapped_column(DateTime(timezone=True), nullable=False)

    assembly = relationship(
        'Assembly',
        foreign_keys=[assembly_id],
        back_populates='status_history',
    )
    status_type = relationship('AssemblyStatusType', back_populates='statuses')


class AssemblyStatusType(Base):
    __tablename__ = 'assembly_status_type'

    @classmethod
    def get_id_column_name(cls):
        return 'status_type_id'

    status_type_id = mapped_column(String, primary_key=True)
    description = mapped_column(String)
    assign_order = mapped_column(Integer)

    statuses = relationship('AssemblyStatus', back_populates='status_type')


class BuscoLineage(Base):
    __tablename__ = 'busco_lineage'

    id = mapped_column(Integer, primary_key=True)  # noqa: A003
    name = mapped_column(String)
    date_created = mapped_column(DateTime(timezone=True))
    species_count = mapped_column(Integer)
    gene_count = mapped_column(Integer)
    busco_metrics = relationship(
        'BuscoMetrics',
        back_populates='busco_lineage',
    )


class BuscoMetrics(Base, HasFolder):
    __tablename__ = 'busco_metrics'

    id = mapped_column(Integer, primary_key=True)  # noqa: A003
    assembly_id = mapped_column(Integer, ForeignKey('assembly.assembly_id'))
    complete = mapped_column(Integer)
    single = mapped_column(Integer)
    duplicated = mapped_column(Integer)
    fragmented = mapped_column(Integer)
    missing = mapped_column(Integer)
    count = mapped_column(Integer)
    busco_lineage_id = mapped_column(Integer, ForeignKey('busco_lineage.id'))
    summary = mapped_column(String)
    software_version_id = mapped_column(
        Integer,
        ForeignKey('software_version.software_version_id'),
    )

    assembly = relationship('Assembly', back_populates='busco_metrics')
    busco_lineage = relationship(
        'BuscoLineage',
        back_populates='busco_metrics',
    )
    software_version = relationship(
        'SoftwareVersion',
        back_populates='busco_metrics',
    )


class ContigvizMetrics(Base, HasFolder):
    __tablename__ = 'contigviz_metrics'

    id = mapped_column(Integer, primary_key=True)  # noqa: A003
    assembly_id = mapped_column(Integer, ForeignKey('assembly.assembly_id'))
    software_version_id = mapped_column(
        Integer,
        ForeignKey('software_version.software_version_id'),
    )
    results = mapped_column(JSONB)

    assembly = relationship('Assembly', back_populates='contigviz_metrics')
    software_version = relationship(
        'SoftwareVersion',
        back_populates='contigviz_metrics',
    )


class Dataset(LogBase):
    __tablename__ = 'dataset'

    @classmethod
    def get_id_column_name(cls):
        return 'dataset_id'

    dataset_id = mapped_column(String, primary_key=True)
    dataset_status_id = mapped_column(
        Integer,
        ForeignKey('dataset_status.dataset_status_id'),
    )
    dataset_list_md5 = mapped_column(String)
    reads = mapped_column(BigInteger)
    bases = mapped_column(BigInteger)
    read_length_mean = mapped_column(Float)
    read_length_n50 = mapped_column(BigInteger)

    assembly = relationship('Assembly', back_populates='dataset')
    genomescope_metrics = relationship(
        'GenomescopeMetrics',
        back_populates='dataset',
    )
    merqury_metrics = relationship('MerquryMetrics', back_populates='dataset')
    ploidyplot_metrics = relationship(
        'PloidyplotMetrics',
        back_populates='dataset',
    )

    status = relationship('DatasetStatus', foreign_keys=[dataset_status_id])
    status_history = relationship(
        'DatasetStatus',
        primaryjoin='Dataset.dataset_id == DatasetStatus.dataset_id',
        back_populates='dataset',
    )

    data_assn = relationship('DatasetElement', back_populates='dataset')
    data = association_proxy('data_assn', 'data')


class DatasetElement(Base):
    __tablename__ = 'dataset_element'

    id = mapped_column(Integer, primary_key=True)  # noqa: A003
    data_id = mapped_column(Integer, ForeignKey('data.data_id'))
    dataset_id = mapped_column(String, ForeignKey('dataset.dataset_id'))

    UniqueConstraint('data_id', 'dataset_id')

    data = relationship('Data', back_populates='dataset_assn')
    dataset = relationship('Dataset', back_populates='data_assn')


class DatasetStatus(LogBase):
    __tablename__ = 'dataset_status'

    @classmethod
    def get_id_column_name(cls):
        return 'dataset_status_id'

    dataset_status_id = mapped_column(Integer, primary_key=True)
    dataset_id = mapped_column(
        String,
        ForeignKey('dataset.dataset_id'),
        nullable=False,
    )
    status_type_id = mapped_column(
        String,
        ForeignKey('dataset_status_type.status_type_id'),
        nullable=False,
    )
    status_time = mapped_column(DateTime(timezone=True), nullable=False)

    dataset = relationship(
        'Dataset',
        foreign_keys=[dataset_id],
        back_populates='status_history',
    )
    status_type = relationship('DatasetStatusType', back_populates='statuses')


class DatasetStatusType(Base):
    __tablename__ = 'dataset_status_type'

    @classmethod
    def get_id_column_name(cls):
        return 'status_type_id'

    status_type_id = mapped_column(String, primary_key=True)
    description = mapped_column(String)
    assign_order = mapped_column(Integer)

    statuses = relationship('DatasetStatus', back_populates='status_type')


class GenomescopeMetrics(LogBase, HasFolder):
    __tablename__ = 'genomescope_metrics'

    id = mapped_column(Integer, primary_key=True)  # noqa: A003
    dataset_id = mapped_column(String, ForeignKey('dataset.dataset_id'))
    software_version_id = mapped_column(
        Integer,
        ForeignKey('software_version.software_version_id'),
    )
    review_id = mapped_column(String, ForeignKey('review_dict.review_id'))
    kmer = mapped_column(Integer)
    ploidy = mapped_column(Integer)
    homozygous = mapped_column(Float)
    heterozygous = mapped_column(Float)
    haploid_length = mapped_column(BigInteger)
    unique_length = mapped_column(BigInteger)
    repeat_length = mapped_column(BigInteger)
    kcov = mapped_column(Float)
    kcov_init = mapped_column(Integer)
    model_fit = mapped_column(Float)
    read_error_rate = mapped_column(Float)
    results = mapped_column(JSONB)

    dataset = relationship('Dataset', back_populates='genomescope_metrics')
    software_version = relationship(
        'SoftwareVersion',
        back_populates='genomescope_metrics',
    )


class MarkerscanMetrics(Base):
    __tablename__ = 'markerscan_metrics'

    id = mapped_column(Integer, primary_key=True)  # noqa: A003
    assembly_id = mapped_column(Integer, ForeignKey('assembly.assembly_id'))
    software_version_id = mapped_column(
        Integer,
        ForeignKey('software_version.software_version_id'),
    )
    results = mapped_column(JSONB)

    assembly = relationship('Assembly', back_populates='markerscan_metrics')
    software_version = relationship(
        'SoftwareVersion',
        back_populates='markerscan_metrics',
    )


class MerquryMetrics(Base, HasFolder):
    __tablename__ = 'merqury_metrics'

    id = mapped_column(Integer, primary_key=True)  # noqa: A003
    assembly_id = mapped_column(Integer, ForeignKey('assembly.assembly_id'))
    dataset_id = mapped_column(String, ForeignKey('dataset.dataset_id'))
    kmer = mapped_column(String)
    complete_primary = mapped_column(Integer)
    complete_alternate = mapped_column(Integer)
    complete_all = mapped_column(Integer)
    qv_primary = mapped_column(Float)
    qv_alternate = mapped_column(Float)
    qv_all = mapped_column(Float)
    software_version_id = mapped_column(
        Integer,
        ForeignKey('software_version.software_version_id'),
    )

    assembly = relationship('Assembly', back_populates='merqury_metrics')
    dataset = relationship('Dataset', back_populates='merqury_metrics')
    software_version = relationship(
        'SoftwareVersion',
        back_populates='merqury_metrics',
    )


class PloidyplotMetrics(Base, HasFolder):
    __tablename__ = 'ploidyplot_metrics'

    id = mapped_column(Integer, primary_key=True)  # noqa: A003
    dataset_id = mapped_column(String, ForeignKey('dataset.dataset_id'))
    kmer = mapped_column(Integer)
    ploidy = mapped_column(Integer)
    n = mapped_column(Float)
    partition = mapped_column(String)
    trim_threshold = mapped_column(Integer)
    software_version_id = mapped_column(
        Integer,
        ForeignKey('software_version.software_version_id'),
    )

    dataset = relationship('Dataset', back_populates='ploidyplot_metrics')
    software_version = relationship(
        'SoftwareVersion',
        back_populates='ploidyplot_metrics',
    )


class ReviewDict(Base):
    __tablename__ = 'review_dict'

    @classmethod
    def get_id_column_name(cls):
        return 'review_id'

    review_id = mapped_column(String, primary_key=True)
    description = mapped_column(String)


class SoftwareVersion(Base):
    __tablename__ = 'software_version'

    @classmethod
    def get_id_column_name(cls):
        return 'software_version_id'

    software_version_id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String)
    version = mapped_column(String)
    cmd = mapped_column(String)

    UniqueConstraint('name', 'version')

    assemblies = relationship('Assembly', back_populates='software_version')
    busco_metrics = relationship(
        'BuscoMetrics',
        back_populates='software_version',
    )
    contigviz_metrics = relationship(
        'ContigvizMetrics',
        back_populates='software_version',
    )
    genomescope_metrics = relationship(
        'GenomescopeMetrics',
        back_populates='software_version',
    )
    markerscan_metrics = relationship(
        'MarkerscanMetrics',
        back_populates='software_version',
    )
    merqury_metrics = relationship(
        'MerquryMetrics',
        back_populates='software_version',
    )
    ploidyplot_metrics = relationship(
        'PloidyplotMetrics',
        back_populates='software_version',
    )
    mapping_metrics = relationship(
        'MappingMetrics',
        back_populates='software_version',
    )
