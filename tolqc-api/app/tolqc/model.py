# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

import re
from functools import cached_property

from sqlalchemy import (
    BigInteger,
    Boolean,
    Column,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    JSON,
    String,
    UniqueConstraint,
)
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import relationship
from tol.sql import model_base

Base = model_base()
LogBase = Base  # No LogBase yet in v2 API


class User(Base):
    """
    Temporary class while v2 API authentication is being developed.
    """

    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)  # noqa: A003
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    organisation = Column(String)
    # role = relationship('Role', lazy=False, back_populates='user')
    # auth = relationship('Auth', lazy=False, back_populates='user')


class Accession(Base):
    __tablename__ = 'accession'

    @classmethod
    def get_id_column_name(cls):
        return 'accession_id'

    accession_id = Column(String, primary_key=True)
    accession_type_id = Column(
        String,
        ForeignKey('accession_type_dict.accession_type_id'),
    )
    secondary = Column(String)
    submission = Column(String)
    date_submitted = Column(DateTime(timezone=True))
    title = Column(String)
    description = Column(String)

    accession_type = relationship(
        'AccessionTypeDict',
        back_populates='accessions',
    )
    projects = relationship('Project', back_populates='accession')
    specimens = relationship('Specimen', back_populates='accession')
    samples = relationship('Sample', back_populates='accession')
    data = relationship('Data', back_populates='accession')


class AccessionTypeDict(Base):
    __tablename__ = 'accession_type_dict'

    @classmethod
    def get_id_column_name(cls):
        return 'accession_type_id'

    accession_type_id = Column(String, primary_key=True)
    regexp = Column(String)
    url = Column(String)

    accessions = relationship('Accession', back_populates='accession_type')

    @cached_property
    def compiled_regexp(self):
        return re.compile(self.regexp)

    def valid_accession(self, accn):
        return bool(self.compiled_regexp.search(accn))


class Allocation(Base):
    __tablename__ = 'allocation'

    id = Column(Integer, primary_key=True)  # noqa: A003
    project_id = Column(Integer, ForeignKey('project.project_id'))
    data_id = Column(Integer, ForeignKey('data.data_id'))
    is_primary = Column(Boolean)

    UniqueConstraint('project_id', 'data_id')

    project = relationship('Project', back_populates='data_assn')
    data = relationship('Data', back_populates='project_assn')


class Assembly(LogBase):
    __tablename__ = 'assembly'

    @classmethod
    def get_id_column_name(cls):
        return 'assembly_id'

    assembly_id = Column(Integer, primary_key=True)
    software_version_id = Column(
        Integer,
        ForeignKey('software_version.software_version_id'),
    )
    dataset_id = Column(String, ForeignKey('dataset.dataset_id'))
    component_type_id = Column(
        String,
        ForeignKey('assembly_component_type.component_type_id'),
    )
    assembly_status_id = Column(
        Integer,
        ForeignKey('assembly_status.assembly_status_id'),
    )
    name = Column(String)
    description = Column(String)

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
    merqury_metrics = relationship('MerquryMetrics', back_populates='assembly')
    markerscan_metrics = relationship(
        'MarkerscanMetrics',
        back_populates='assembly',
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

    component_type_id = Column(String, primary_key=True)
    description = Column(String)

    assemblies = relationship('Assembly', back_populates='component_type')


class AssemblyMetrics(Base):
    __tablename__ = 'assembly_metrics'

    id = Column(Integer, primary_key=True)  # noqa: A003
    assembly_id = Column(Integer, ForeignKey('assembly.assembly_id'))
    bases = Column(BigInteger)
    a = Column(BigInteger)
    c = Column(BigInteger)
    g = Column(BigInteger)
    t = Column(BigInteger)
    n = Column(BigInteger)
    cpg = Column(BigInteger)
    iupac3 = Column(Integer)
    iupac2 = Column(Integer)
    ts = Column(Integer)
    tv = Column(Integer)
    cpg_ts = Column(Integer)
    contig_n = Column(Integer)
    contig_length = Column(Integer)
    contig_n50 = Column(Integer)
    contig_aun = Column(Float)
    contig_longest = Column(Integer)
    contig_shortest = Column(Integer)
    contig_length_mean = Column(Float)
    scaffold_n = Column(Integer)
    scaffold_n50 = Column(Integer)
    scaffold_aun = Column(Float)
    gap_n = Column(Integer)
    gap_n50 = Column(Integer)
    assembly = relationship('Assembly', back_populates='assembly_metrics')


class AssemblySource(Base):
    __tablename__ = 'assembly_source'

    id = Column(Integer, primary_key=True)  # noqa: A003
    assembly_id = Column(Integer, ForeignKey('assembly.assembly_id'))
    source_assembly_id = Column(Integer, ForeignKey('assembly.assembly_id'))

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

    assembly_status_id = Column(Integer, primary_key=True)
    assembly_id = Column(
        Integer,
        ForeignKey('assembly.assembly_id'),
        nullable=False,
    )
    status_type_id = Column(
        String,
        ForeignKey('assembly_status_type.status_type_id'),
        nullable=False,
    )
    status_time = Column(DateTime(timezone=True), nullable=False)

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

    status_type_id = Column(String, primary_key=True)
    description = Column(String)
    assign_order = Column(Integer)

    statuses = relationship('AssemblyStatus', back_populates='status_type')


class BarcodeMetrics(Base):
    __tablename__ = 'barcode_metrics'

    id = Column(Integer, primary_key=True)  # noqa: A003
    data_id = Column(Integer, ForeignKey('data.data_id'))
    qc_id = Column(Integer)  # QCDict pass|fail ?

    # Is this a foreign key to the species table?
    species_match_top = Column(String)

    species_match_identity = Column(Float)
    species_match_barcode = Column(String)

    data = relationship('Data', back_populates='barcode_metrics')


class BuscoLineage(Base):
    __tablename__ = 'busco_lineage'

    id = Column(Integer, primary_key=True)  # noqa: A003
    name = Column(String)
    date_created = Column(DateTime(timezone=True))
    species_count = Column(Integer)
    gene_count = Column(Integer)
    busco_metrics = relationship(
        'BuscoMetrics',
        back_populates='busco_lineage',
    )


class BuscoMetrics(Base):
    __tablename__ = 'busco_metrics'

    id = Column(Integer, primary_key=True)  # noqa: A003
    assembly_id = Column(Integer, ForeignKey('assembly.assembly_id'))
    complete = Column(Integer)
    single = Column(Integer)
    duplicated = Column(Integer)
    fragmented = Column(Integer)
    missing = Column(Integer)
    count = Column(Integer)
    busco_lineage_id = Column(Integer, ForeignKey('busco_lineage.id'))
    summary = Column(String)
    software_version_id = Column(
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


class Centre(Base):
    __tablename__ = 'centre'

    id = Column(Integer, primary_key=True)  # noqa: A003
    name = Column(String)
    hierarchy_name = Column(String)

    run = relationship('Run', back_populates='centre')


class ContigvizMetrics(Base):
    __tablename__ = 'contigviz_metrics'

    id = Column(Integer, primary_key=True)  # noqa: A003
    assembly_id = Column(Integer, ForeignKey('assembly.assembly_id'))
    software_version_id = Column(
        Integer,
        ForeignKey('software_version.software_version_id'),
    )
    results = Column(JSON)

    assembly = relationship('Assembly', back_populates='contigviz_metrics')
    software_version = relationship(
        'SoftwareVersion',
        back_populates='contigviz_metrics',
    )


class Data(LogBase):
    __tablename__ = 'data'

    @classmethod
    def get_id_column_name(cls):
        return 'data_id'

    data_id = Column(Integer, primary_key=True)
    name_root = Column(String, index=True)
    hierarchy_name = Column(String)
    sample_id = Column(String, ForeignKey('sample.sample_id'))
    library_id = Column(String, ForeignKey('library.library_id'))
    accession_id = Column(String, ForeignKey('accession.accession_id'))
    run_id = Column(String, ForeignKey('run.run_id'))
    processed = Column(Integer)
    tag_index = Column(String)
    tag1_id = Column(String)
    tag2_id = Column(String)
    date = Column(DateTime(timezone=True))
    lims_qc = Column(String, ForeignKey('qc_dict.qc_state'))
    auto_qc = Column(String, ForeignKey('qc_dict.qc_state'))
    qc = Column(String, ForeignKey('qc_dict.qc_state'))
    withdrawn = Column(Boolean)
    manually_withdrawn = Column(Boolean)
    reads = Column(Integer)
    bases = Column(BigInteger)
    read_length_mean = Column(Float)
    read_length_n50 = Column(Integer)
    elastic_mlwh_cksum = Column(String)

    sample = relationship('Sample', back_populates='data')
    library = relationship('Library', back_populates='data')
    accession = relationship('Accession', back_populates='data')
    run = relationship('Run', back_populates='data')
    files = relationship('File', back_populates='data')
    barcode_metrics = relationship('BarcodeMetrics', back_populates='data')

    project_assn = relationship('Allocation', back_populates='data')
    projects = association_proxy('project_assn', 'project')

    dataset_assn = relationship('DatasetElement', back_populates='data')
    datasets = association_proxy('dataset_assn', 'dataset')


class Dataset(LogBase):
    __tablename__ = 'dataset'

    @classmethod
    def get_id_column_name(cls):
        return 'dataset_id'

    dataset_id = Column(String, primary_key=True)
    dataset_status_id = Column(
        Integer,
        ForeignKey('dataset_status.dataset_status_id'),
    )
    dataset_list_md5 = Column(String)
    reads = Column(Integer)
    bases = Column(BigInteger)
    read_length_mean = Column(Float)
    read_length_n50 = Column(Integer)

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

    id = Column(Integer, primary_key=True)  # noqa: A003
    data_id = Column(Integer, ForeignKey('data.data_id'))
    dataset_id = Column(String, ForeignKey('dataset.dataset_id'))

    UniqueConstraint('data_id', 'dataset_id')

    data = relationship('Data', back_populates='dataset_assn')
    dataset = relationship('Dataset', back_populates='data_assn')


class DatasetStatus(LogBase):
    __tablename__ = 'dataset_status'

    @classmethod
    def get_id_column_name(cls):
        return 'dataset_status_id'

    dataset_status_id = Column(Integer, primary_key=True)
    dataset_id = Column(
        String,
        ForeignKey('dataset.dataset_id'),
        nullable=False,
    )
    status_type_id = Column(
        String,
        ForeignKey('dataset_status_type.status_type_id'),
        nullable=False,
    )
    status_time = Column(DateTime(timezone=True), nullable=False)

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

    status_type_id = Column(String, primary_key=True)
    description = Column(String)
    assign_order = Column(Integer)

    statuses = relationship('DatasetStatus', back_populates='status_type')


class File(Base):
    __tablename__ = 'file'

    id = Column(Integer, primary_key=True)  # noqa: A003
    data_id = Column(Integer, ForeignKey('data.data_id'))
    name = Column(String)
    relative_path = Column(String)
    remote_path = Column(String)
    size_bytes = Column(BigInteger)
    md5 = Column(String)

    data = relationship('Data', back_populates='files')


class GenomescopeMetrics(LogBase):
    __tablename__ = 'genomescope_metrics'

    id = Column(Integer, primary_key=True)  # noqa: A003
    dataset_id = Column(String, ForeignKey('dataset.dataset_id'))
    software_version_id = Column(
        Integer,
        ForeignKey('software_version.software_version_id'),
    )
    review_id = Column(String, ForeignKey('review_dict.review_id'))
    kmer = Column(Integer)
    ploidy = Column(Integer)
    homozygous = Column(Float)
    heterozygous = Column(Float)
    haploid_length = Column(BigInteger)
    unique_length = Column(BigInteger)
    repeat_length = Column(BigInteger)
    kcov = Column(Float)
    kcov_init = Column(Integer)
    model_fit = Column(Float)
    read_error_rate = Column(Float)
    results = Column(JSON)

    dataset = relationship('Dataset', back_populates='genomescope_metrics')
    software_version = relationship(
        'SoftwareVersion',
        back_populates='genomescope_metrics',
    )
    review = relationship('ReviewDict', back_populates='genomescope_metrics')


class Library(Base):
    __tablename__ = 'library'

    @classmethod
    def get_id_column_name(cls):
        return 'library_id'

    library_id = Column(String, primary_key=True)
    library_type_id = Column(
        String,
        ForeignKey('library_type.library_type_id'),
    )
    lims_id = Column(Integer)

    data = relationship('Data', back_populates='library')
    library_type = relationship('LibraryType', back_populates='library')


class LibraryType(Base):
    __tablename__ = 'library_type'

    @classmethod
    def get_id_column_name(cls):
        return 'library_type_id'

    library_type_id = Column(String, primary_key=True)
    hierarchy_name = Column(String)
    category = Column(String)
    kit = Column(String)
    enzymes = Column(String)
    cut_sites = Column(String)

    library = relationship('Library', back_populates='library_type')


class MarkerscanMetrics(Base):
    __tablename__ = 'markerscan_metrics'

    id = Column(Integer, primary_key=True)  # noqa: A003
    assembly_id = Column(Integer, ForeignKey('assembly.assembly_id'))
    software_version_id = Column(
        Integer,
        ForeignKey('software_version.software_version_id'),
    )
    results = Column(JSON)

    assembly = relationship('Assembly', back_populates='markerscan_metrics')
    software_version = relationship(
        'SoftwareVersion',
        back_populates='markerscan_metrics',
    )


class MerquryMetrics(Base):
    __tablename__ = 'merqury_metrics'

    id = Column(Integer, primary_key=True)  # noqa: A003
    assembly_id = Column(Integer, ForeignKey('assembly.assembly_id'))
    dataset_id = Column(String, ForeignKey('dataset.dataset_id'))
    kmer = Column(String)
    complete_primary = Column(Integer)
    complete_alternate = Column(Integer)
    complete_all = Column(Integer)
    qv_primary = Column(Float)
    qv_alternate = Column(Float)
    qv_all = Column(Float)
    software_version_id = Column(
        Integer,
        ForeignKey('software_version.software_version_id'),
    )

    assembly = relationship('Assembly', back_populates='merqury_metrics')
    dataset = relationship('Dataset', back_populates='merqury_metrics')
    software_version = relationship(
        'SoftwareVersion',
        back_populates='merqury_metrics',
    )


class Offspring(Base):
    __tablename__ = 'offspring'

    id = Column(Integer, primary_key=True)  # noqa: A003
    specimen_id = Column(String, ForeignKey('specimen.specimen_id'))
    offspring_specimen_id = Column(String, ForeignKey('specimen.specimen_id'))

    UniqueConstraint('specimen_id', 'offspring_specimen_id')

    parent = relationship(
        'Specimen',
        foreign_keys=[specimen_id],
        back_populates='parent_assn',
    )
    offspring = relationship(
        'Specimen',
        foreign_keys=[offspring_specimen_id],
        back_populates='offspring_assn',
    )


class PacbioRunMetrics(Base):
    __tablename__ = 'pacbio_run_metrics'

    @classmethod
    def get_id_column_name(cls):
        return 'run_id'

    run_id = Column(String, ForeignKey('run.run_id'), primary_key=True)
    movie_minutes = Column(Integer)
    binding_kit = Column(String)
    sequencing_kit = Column(String)
    include_kinetics = Column(String)
    loading_conc = Column(Float)
    control_num_reads = Column(Integer)
    control_read_length_mean = Column(Float)
    polymerase_read_bases = Column(BigInteger)
    polymerase_num_reads = Column(Integer)
    polymerase_read_length_mean = Column(Float)
    polymerase_read_length_n50 = Column(Integer)
    insert_length_mean = Column(Float)
    insert_length_n50 = Column(Integer)
    unique_molecular_bases = Column(BigInteger)
    p0_num = Column(Integer)
    p1_num = Column(Integer)
    p2_num = Column(Integer)
    hifi_read_bases = Column(BigInteger)
    hifi_num_reads = Column(Integer)
    hifi_low_quality_num_reads = Column(Integer)

    run = relationship('Run', back_populates='pacbio_run_metrics')


class Platform(Base):
    __tablename__ = 'platform'

    id = Column(Integer, primary_key=True)  # noqa: A003
    name = Column(String)
    model = Column(String)

    run = relationship('Run', back_populates='platform')


class PloidyplotMetrics(Base):
    __tablename__ = 'ploidyplot_metrics'

    id = Column(Integer, primary_key=True)  # noqa: A003
    dataset_id = Column(String, ForeignKey('dataset.dataset_id'))
    kmer = Column(Integer)
    ploidy = Column(Integer)
    n = Column(Float)
    partition = Column(String)
    trim_threshold = Column(Integer)
    software_version_id = Column(
        Integer,
        ForeignKey('software_version.software_version_id'),
    )

    dataset = relationship('Dataset', back_populates='ploidyplot_metrics')
    software_version = relationship(
        'SoftwareVersion',
        back_populates='ploidyplot_metrics',
    )


class Project(Base):
    __tablename__ = 'project'

    @classmethod
    def get_id_column_name(cls):
        return 'project_id'

    project_id = Column(Integer, primary_key=True)
    hierarchy_name = Column(String)
    description = Column(String)
    lims_id = Column(Integer, index=True)
    accession_id = Column(String, ForeignKey('accession.accession_id'))

    accession = relationship('Accession', back_populates='projects')
    data_assn = relationship('Allocation', back_populates='project')
    data = association_proxy('data_assn', 'data')


class QCDict(Base):
    __tablename__ = 'qc_dict'

    @classmethod
    def get_id_column_name(cls):
        return 'qc_state'

    qc_state = Column(String, primary_key=True)


class ReviewDict(Base):
    __tablename__ = 'review_dict'

    @classmethod
    def get_id_column_name(cls):
        return 'review_id'

    review_id = Column(String, primary_key=True)
    description = Column(String)

    genomescope_metrics = relationship(
        'GenomescopeMetrics',
        back_populates='review',
    )


class Run(Base):
    __tablename__ = 'run'

    @classmethod
    def get_id_column_name(cls):
        return 'run_id'

    run_id = Column(String, primary_key=True)
    name = Column(String)
    hierarchy_name = Column(String)
    platform_id = Column(Integer, ForeignKey('platform.id'))
    centre_id = Column(Integer, ForeignKey('centre.id'))
    lims_id = Column(String)
    element = Column(String)
    instrument_name = Column(String)
    start = Column(DateTime(timezone=True))
    complete = Column(DateTime(timezone=True))

    data = relationship('Data', back_populates='run')
    platform = relationship('Platform', back_populates='run')
    centre = relationship('Centre', back_populates='run')
    pacbio_run_metrics = relationship('PacbioRunMetrics', back_populates='run')


class Sample(LogBase):
    __tablename__ = 'sample'

    @classmethod
    def get_id_column_name(cls):
        return 'sample_id'

    sample_id = Column(String, primary_key=True)
    hierarchy_name = Column(String)
    lims_id = Column(Integer)
    specimen_id = Column(String, ForeignKey('specimen.specimen_id'))
    accession_id = Column(String, ForeignKey('accession.accession_id'))

    specimen = relationship('Specimen', back_populates='samples')
    accession = relationship('Accession', back_populates='samples')
    data = relationship('Data', back_populates='sample')


class Sex(Base):
    __tablename__ = 'sex'

    @classmethod
    def get_id_column_name(cls):
        return 'sex_id'

    sex_id = Column(String, primary_key=True)
    description = Column(String)

    specimens = relationship('Specimen', back_populates='sex')


class SoftwareVersion(Base):
    __tablename__ = 'software_version'

    @classmethod
    def get_id_column_name(cls):
        return 'software_version_id'

    software_version_id = Column(Integer, primary_key=True)
    name = Column(String)
    version = Column(String)
    cmd = Column(String)

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


class Species(LogBase):
    __tablename__ = 'species'

    @classmethod
    def get_id_column_name(cls):
        return 'species_id'

    species_id = Column(String, primary_key=True)
    hierarchy_name = Column(String, nullable=False, index=True)
    strain = Column(String)
    common_name = Column(String)
    taxon_id = Column(Integer, index=True)
    taxon_family = Column(String)
    taxon_order = Column(String)
    taxon_phylum = Column(String)
    taxon_group = Column(String)
    genome_size = Column(BigInteger)
    chromosome_number = Column(Integer)

    specimens = relationship('Specimen', back_populates='species')


class Specimen(LogBase):
    __tablename__ = 'specimen'

    @classmethod
    def get_id_column_name(cls):
        return 'specimen_id'

    specimen_id = Column(String, primary_key=True)
    hierarchy_name = Column(String)
    specimen_status_id = Column(
        Integer,
        ForeignKey('specimen_status.specimen_status_id'),
    )
    species_id = Column(String, ForeignKey('species.species_id'))
    lims_id = Column(Integer)
    supplied_name = Column(String)
    accession_id = Column(String, ForeignKey('accession.accession_id'))
    sex_id = Column(String, ForeignKey('sex.sex_id'))
    ploidy = Column(String)
    karyotype = Column(String)

    species = relationship('Species', back_populates='specimens')
    samples = relationship('Sample', back_populates='specimen')
    sex = relationship('Sex', back_populates='specimens')
    accession = relationship('Accession', back_populates='specimens')

    status = relationship('SpecimenStatus', foreign_keys=[specimen_status_id])
    status_history = relationship(
        'SpecimenStatus',
        primaryjoin='Specimen.specimen_id == SpecimenStatus.specimen_id',
        back_populates='specimen',
    )

    parent_assn = relationship(
        'Offspring',
        primaryjoin='Specimen.specimen_id == Offspring.specimen_id',
        back_populates='parent',
    )
    offspring = association_proxy('parent_assn', 'offspring')

    offspring_assn = relationship(
        'Offspring',
        primaryjoin='Specimen.specimen_id == Offspring.offspring_specimen_id',
        back_populates='offspring',
    )
    parents = association_proxy('offspring_assn', 'parent')


class SpecimenStatus(LogBase):
    __tablename__ = 'specimen_status'

    @classmethod
    def get_id_column_name(cls):
        return 'specimen_status_id'

    specimen_status_id = Column(Integer, primary_key=True)
    specimen_id = Column(
        String,
        ForeignKey('specimen.specimen_id'),
        nullable=False,
    )
    status_type_id = Column(
        String,
        ForeignKey('specimen_status_type.status_type_id'),
        nullable=False,
    )
    status_time = Column(DateTime(timezone=True), nullable=False)

    specimen = relationship(
        'Specimen',
        foreign_keys=[specimen_id],
        back_populates='status_history',
    )
    status_type = relationship('SpecimenStatusType', back_populates='statuses')


class SpecimenStatusType(Base):
    __tablename__ = 'specimen_status_type'

    @classmethod
    def get_id_column_name(cls):
        return 'status_type_id'

    status_type_id = Column(String, primary_key=True)
    description = Column(String)
    assign_order = Column(Integer)

    statuses = relationship('SpecimenStatus', back_populates='status_type')
