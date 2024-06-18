# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

import re
from functools import cached_property

from sqlalchemy import (
    BigInteger,
    Boolean,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
    UniqueConstraint,
)
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import mapped_column, relationship

from tolqc.assembly_models import DatasetElement  # noqa: F401
from tolqc.folder_models import HasFolder
from tolqc.model import Base, LogBase


def models_list():
    return [
        Accession,
        AccessionTypeDict,
        Allocation,
        BarcodeMetrics,
        Centre,
        Data,
        File,
        Library,
        LibraryType,
        MappingMetrics,
        Offspring,
        PacbioRunMetrics,
        Platform,
        Project,
        QCDict,
        Run,
        Sample,
        Sex,
        Species,
        Specimen,
        SpecimenStatus,
        SpecimenStatusType,
        VisibilityDict,
    ]


class Accession(LogBase):
    __tablename__ = 'accession'

    @classmethod
    def get_id_column_name(cls):
        return 'accession_id'

    accession_id = mapped_column(String, primary_key=True)
    accession_type_id = mapped_column(
        String,
        ForeignKey('accession_type_dict.accession_type_id'),
    )
    secondary = mapped_column(String)
    submission = mapped_column(String)
    date_submitted = mapped_column(DateTime(timezone=True))
    title = mapped_column(String)
    description = mapped_column(String)

    accession_type = relationship(
        'AccessionTypeDict',
        back_populates='accessions',
    )
    projects = relationship('Project', back_populates='accession')
    specimens = relationship('Specimen', back_populates='accession')
    samples = relationship('Sample', back_populates='accession')
    data = relationship('Data', back_populates='accession')

    bioproject_assemblies = relationship(
        'Assembly',
        primaryjoin='Accession.accession_id == Assembly.bioproject_accession_id',
        back_populates='bioproject_accession',
    )
    genome_assemblies = relationship(
        'Assembly',
        primaryjoin='Accession.accession_id == Assembly.genome_accession_id',
        back_populates='genome_accession',
    )

    data_species = relationship(
        'Species',
        primaryjoin='Accession.accession_id == Species.data_accession_id',
        back_populates='data_accession',
    )
    umbrella_species = relationship(
        'Species',
        primaryjoin='Accession.accession_id == Species.umbrella_accession_id',
        back_populates='umbrella_accession',
    )


class AccessionTypeDict(Base):
    __tablename__ = 'accession_type_dict'

    @classmethod
    def get_id_column_name(cls):
        return 'accession_type_id'

    accession_type_id = mapped_column(String, primary_key=True)
    regexp = mapped_column(String)
    url = mapped_column(String)

    accessions = relationship('Accession', back_populates='accession_type')

    @cached_property
    def compiled_regexp(self):
        return re.compile(self.regexp)

    def valid_accession(self, accn):
        return bool(self.compiled_regexp.search(accn))


class Allocation(Base):
    __tablename__ = 'allocation'

    id = mapped_column(Integer, primary_key=True)  # noqa: A003
    project_id = mapped_column(Integer, ForeignKey('project.project_id'))
    data_id = mapped_column(Integer, ForeignKey('data.data_id'))
    is_primary = mapped_column(Boolean)

    UniqueConstraint('project_id', 'data_id')

    project = relationship('Project', back_populates='data_assn')
    data = relationship('Data', back_populates='project_assn')


class BarcodeMetrics(Base):
    __tablename__ = 'barcode_metrics'

    id = mapped_column(Integer, primary_key=True)  # noqa: A003
    data_id = mapped_column(Integer, ForeignKey('data.data_id'))
    qc_id = mapped_column(Integer)  # QCDict pass|fail ?

    # Is this a foreign key to the species table?
    species_match_top = mapped_column(String)

    species_match_identity = mapped_column(Float)
    species_match_barcode = mapped_column(String)

    data = relationship('Data', back_populates='barcode_metrics')


class Centre(Base):
    __tablename__ = 'centre'

    id = mapped_column(Integer, primary_key=True)  # noqa: A003
    name = mapped_column(String)
    hierarchy_name = mapped_column(String)

    run = relationship('Run', back_populates='centre')


class Data(LogBase):
    __tablename__ = 'data'

    @classmethod
    def get_id_column_name(cls):
        return 'data_id'

    data_id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String, unique=True)
    hierarchy_name = mapped_column(String)
    sample_id = mapped_column(String, ForeignKey('sample.sample_id'))
    library_id = mapped_column(String, ForeignKey('library.library_id'))
    accession_id = mapped_column(String, ForeignKey('accession.accession_id'))
    run_id = mapped_column(String, ForeignKey('run.run_id'))
    processed = mapped_column(Integer)
    tag_index = mapped_column(String)
    tag1_id = mapped_column(String)
    tag2_id = mapped_column(String)
    date = mapped_column(DateTime(timezone=True))
    lims_qc = mapped_column(String, ForeignKey('qc_dict.qc_state'))
    auto_qc = mapped_column(String, ForeignKey('qc_dict.qc_state'))
    qc = mapped_column(String, ForeignKey('qc_dict.qc_state'))
    visibility = mapped_column(
        String,
        ForeignKey('visibility_dict.visibility'),
        default='Always',
        index=True,
    )
    reads = mapped_column(BigInteger)
    bases = mapped_column(BigInteger)
    read_length_mean = mapped_column(Float)
    read_length_n50 = mapped_column(BigInteger)

    # From PacBio stats file generated by tolpipe:
    bases_a = mapped_column(BigInteger)
    bases_c = mapped_column(BigInteger)
    bases_g = mapped_column(BigInteger)
    bases_t = mapped_column(BigInteger)
    read_length_longest = mapped_column(Integer)
    read_length_shortest = mapped_column(Integer)

    # From parsing PacBio pbmarkdup log generated by tolpipe:
    reads_duplicated = mapped_column(BigInteger)

    # From parsing hifiadapterfilt log generated by tolpipe:
    reads_filtered = mapped_column(BigInteger)

    sample = relationship('Sample', back_populates='data')
    library = relationship('Library', back_populates='data')
    accession = relationship('Accession', back_populates='data')
    run = relationship('Run', back_populates='data')
    files = relationship('File', back_populates='data')
    barcode_metrics = relationship('BarcodeMetrics', back_populates='data')
    mapping_metrics = relationship('MappingMetrics', back_populates='data')

    project_assn = relationship('Allocation', back_populates='data')
    projects = association_proxy('project_assn', 'project')

    dataset_assn = relationship('DatasetElement', back_populates='data')
    datasets = association_proxy('dataset_assn', 'dataset')


class File(Base):
    __tablename__ = 'file'

    id = mapped_column(Integer, primary_key=True)  # noqa: A003
    data_id = mapped_column(Integer, ForeignKey('data.data_id'))
    name = mapped_column(String)
    relative_path = mapped_column(String)
    remote_path = mapped_column(String)
    size_bytes = mapped_column(BigInteger)
    md5 = mapped_column(String)

    data = relationship('Data', back_populates='files')


class Library(Base):
    __tablename__ = 'library'

    @classmethod
    def get_id_column_name(cls):
        return 'library_id'

    library_id = mapped_column(String, primary_key=True)
    library_type_id = mapped_column(
        String,
        ForeignKey('library_type.library_type_id'),
    )
    lims_id = mapped_column(Integer)

    data = relationship('Data', back_populates='library')
    library_type = relationship('LibraryType', back_populates='library')


class LibraryType(Base):
    __tablename__ = 'library_type'

    @classmethod
    def get_id_column_name(cls):
        return 'library_type_id'

    library_type_id = mapped_column(String, primary_key=True)
    hierarchy_name = mapped_column(String)
    category = mapped_column(String)
    reporting_category = mapped_column(String)
    kit = mapped_column(String)
    enzymes = mapped_column(String)
    cut_sites = mapped_column(String)

    library = relationship('Library', back_populates='library_type')


class MappingMetrics(Base, HasFolder):
    __tablename__ = 'mapping_metrics'

    id = mapped_column(Integer, primary_key=True)  # noqa: A003
    data_id = mapped_column(Integer, ForeignKey('data.data_id'), nullable=False)
    assembly_id = mapped_column(Integer, ForeignKey('assembly.assembly_id'))
    software_version_id = mapped_column(
        Integer,
        ForeignKey('software_version.software_version_id'),
    )

    # From parsing Illumina samtools stats file generated on mapped bam by
    # tolpipe:
    reads_duplicated = mapped_column(BigInteger)

    # From Illumina samtools stats file generated by NPG, but copied and
    # parsed by tolpipe (may be able to get a number for PacBio for this
    # too):
    average_quality = mapped_column(Float)

    # From Illumina samtools stats file generated on mapped bam by tolpipe:
    bases_duplicated = mapped_column(BigInteger)
    bases_mapped = mapped_column(BigInteger)
    bases_mapped_cigar = mapped_column(BigInteger)
    bases_trimmed = mapped_column(BigInteger)
    error_rate = mapped_column(Float)
    insert_size_average = mapped_column(Float)
    insert_size_standard_deviation = mapped_column(Float)
    inward_oriented_pairs = mapped_column(BigInteger)
    mismatches = mapped_column(BigInteger)
    outward_oriented_pairs = mapped_column(BigInteger)
    pairs_on_different_chromosomes = mapped_column(BigInteger)
    pairs_with_other_orientation = mapped_column(BigInteger)
    reads_mapped = mapped_column(BigInteger)
    reads_mapped_and_paired = mapped_column(BigInteger)
    reads_mq0 = mapped_column(BigInteger)
    reads_properly_paired = mapped_column(BigInteger)
    reads_unmapped = mapped_column(BigInteger)

    data = relationship('Data', back_populates='mapping_metrics')
    assembly = relationship('Assembly', back_populates='mapping_metrics')
    software_version = relationship(
        'SoftwareVersion',
        back_populates='mapping_metrics',
    )


class Offspring(Base):
    __tablename__ = 'offspring'

    id = mapped_column(Integer, primary_key=True)  # noqa: A003
    specimen_id = mapped_column(String, ForeignKey('specimen.specimen_id'))
    offspring_specimen_id = mapped_column(String, ForeignKey('specimen.specimen_id'))

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


class PacbioRunMetrics(Base, HasFolder):
    __tablename__ = 'pacbio_run_metrics'

    @classmethod
    def get_id_column_name(cls):
        return 'run_id'

    run_id = mapped_column(String, ForeignKey('run.run_id'), primary_key=True)
    movie_minutes = mapped_column(Integer)
    binding_kit = mapped_column(String)
    sequencing_kit = mapped_column(String)
    sequencing_kit_lot_number = mapped_column(String)
    cell_lot_number = mapped_column(String)
    include_kinetics = mapped_column(String)
    loading_conc = mapped_column(Float)
    control_num_reads = mapped_column(Integer)
    control_read_length_mean = mapped_column(Float)
    control_concordance_mean = mapped_column(Float)
    control_concordance_mode = mapped_column(Float)
    local_base_rate = mapped_column(Float)
    polymerase_read_bases = mapped_column(BigInteger)
    polymerase_num_reads = mapped_column(Integer)
    polymerase_read_length_mean = mapped_column(Float)
    polymerase_read_length_n50 = mapped_column(Integer)
    insert_length_mean = mapped_column(Float)
    insert_length_n50 = mapped_column(Integer)
    unique_molecular_bases = mapped_column(BigInteger)
    productive_zmws_num = mapped_column(Integer)
    p0_num = mapped_column(Integer)
    p1_num = mapped_column(Integer)
    p2_num = mapped_column(Integer)
    adapter_dimer_percent = mapped_column(Float)
    short_insert_percent = mapped_column(Float)
    hifi_read_bases = mapped_column(BigInteger)
    hifi_num_reads = mapped_column(Integer)
    hifi_read_length_mean = mapped_column(Integer)
    hifi_read_quality_median = mapped_column(Integer)
    hifi_number_passes_mean = mapped_column(Float)
    hifi_low_quality_read_bases = mapped_column(BigInteger)
    hifi_low_quality_num_reads = mapped_column(Integer)
    hifi_low_quality_read_length_mean = mapped_column(Integer)
    hifi_low_quality_read_quality_median = mapped_column(Integer)
    hifi_barcoded_reads = mapped_column(Integer)
    hifi_bases_in_barcoded_reads = mapped_column(BigInteger)

    run = relationship('Run', back_populates='pacbio_run_metrics')


class Platform(Base):
    __tablename__ = 'platform'

    id = mapped_column(Integer, primary_key=True)  # noqa: A003
    name = mapped_column(String)
    model = mapped_column(String)

    run = relationship('Run', back_populates='platform')


class Project(Base):
    __tablename__ = 'project'

    @classmethod
    def get_id_column_name(cls):
        return 'project_id'

    project_id = mapped_column(Integer, primary_key=True)
    hierarchy_name = mapped_column(String)
    description = mapped_column(String)
    lims_id = mapped_column(Integer, index=True)
    accession_id = mapped_column(String, ForeignKey('accession.accession_id'))

    accession = relationship('Accession', back_populates='projects')
    data_assn = relationship('Allocation', back_populates='project')
    data = association_proxy('data_assn', 'data')
    species_assn = relationship('Umbrella', back_populates='project')
    species = association_proxy('species_assn', 'species')


class QCDict(Base):
    __tablename__ = 'qc_dict'

    @classmethod
    def get_id_column_name(cls):
        return 'qc_state'

    qc_state = mapped_column(String, primary_key=True)


class Run(Base):
    __tablename__ = 'run'

    @classmethod
    def get_id_column_name(cls):
        return 'run_id'

    run_id = mapped_column(String, primary_key=True)
    name = mapped_column(String)
    hierarchy_name = mapped_column(String)
    platform_id = mapped_column(Integer, ForeignKey('platform.id'))
    centre_id = mapped_column(Integer, ForeignKey('centre.id'))
    lims_id = mapped_column(String)
    element = mapped_column(String)
    instrument_name = mapped_column(String)
    start = mapped_column(DateTime(timezone=True))
    complete = mapped_column(DateTime(timezone=True))
    plex_count = mapped_column(Integer)

    data = relationship('Data', back_populates='run')
    platform = relationship('Platform', back_populates='run')
    centre = relationship('Centre', back_populates='run')
    pacbio_run_metrics = relationship('PacbioRunMetrics', back_populates='run')


class Sample(LogBase):
    __tablename__ = 'sample'

    @classmethod
    def get_id_column_name(cls):
        return 'sample_id'

    sample_id = mapped_column(String, primary_key=True)
    hierarchy_name = mapped_column(String)
    lims_id = mapped_column(Integer)
    specimen_id = mapped_column(String, ForeignKey('specimen.specimen_id'))
    accession_id = mapped_column(String, ForeignKey('accession.accession_id'))

    specimen = relationship('Specimen', back_populates='samples')
    accession = relationship('Accession', back_populates='samples')
    data = relationship('Data', back_populates='sample')


class Sex(Base):
    __tablename__ = 'sex'

    @classmethod
    def get_id_column_name(cls):
        return 'sex_id'

    sex_id = mapped_column(String, primary_key=True)
    description = mapped_column(String)

    specimens = relationship('Specimen', back_populates='sex')


class Species(LogBase):
    __tablename__ = 'species'

    @classmethod
    def get_id_column_name(cls):
        return 'species_id'

    species_id = mapped_column(String, primary_key=True)
    hierarchy_name = mapped_column(String, nullable=False, unique=True)
    tolid_prefix = mapped_column(String, unique=True)
    strain = mapped_column(String)
    common_name = mapped_column(String)
    taxon_id = mapped_column(Integer, index=True)
    taxon_family = mapped_column(String)
    taxon_order = mapped_column(String)
    taxon_phylum = mapped_column(String)
    taxon_group = mapped_column(String)
    genome_size = mapped_column(BigInteger)
    chromosome_number = mapped_column(Integer)
    data_accession_id = mapped_column(String, ForeignKey('accession.accession_id'))
    umbrella_accession_id = mapped_column(String, ForeignKey('accession.accession_id'))

    specimens = relationship('Specimen', back_populates='species')
    data_accession = relationship(
        'Accession',
        primaryjoin='Species.data_accession_id == Accession.accession_id',
        back_populates='data_species',
    )
    umbrella_accession = relationship(
        'Accession',
        primaryjoin='Species.umbrella_accession_id == Accession.accession_id',
        back_populates='umbrella_species',
    )

    project_assn = relationship('Umbrella', back_populates='species')
    projects = association_proxy('project_assn', 'project')


class Specimen(LogBase):
    __tablename__ = 'specimen'

    @classmethod
    def get_id_column_name(cls):
        return 'specimen_id'

    specimen_id = mapped_column(String, primary_key=True)
    hierarchy_name = mapped_column(String)
    specimen_status_id = mapped_column(
        Integer,
        ForeignKey('specimen_status.specimen_status_id'),
    )
    species_id = mapped_column(String, ForeignKey('species.species_id'))
    lims_id = mapped_column(Integer)
    supplied_name = mapped_column(String)
    accession_id = mapped_column(String, ForeignKey('accession.accession_id'))
    sex_id = mapped_column(String, ForeignKey('sex.sex_id'))
    ploidy = mapped_column(String)
    karyotype = mapped_column(String)

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

    specimen_status_id = mapped_column(Integer, primary_key=True)
    specimen_id = mapped_column(
        String,
        ForeignKey('specimen.specimen_id'),
        nullable=False,
    )
    status_type_id = mapped_column(
        String,
        ForeignKey('specimen_status_type.status_type_id'),
        nullable=False,
    )
    status_time = mapped_column(DateTime(timezone=True), nullable=False)

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

    status_type_id = mapped_column(String, primary_key=True)
    description = mapped_column(String)
    assign_order = mapped_column(Integer)

    statuses = relationship('SpecimenStatus', back_populates='status_type')


class Umbrella(Base):
    __tablename__ = 'umbrella'

    id = mapped_column(Integer, primary_key=True)  # noqa: A003
    project_id = mapped_column(Integer, ForeignKey('project.project_id'))
    species_id = mapped_column(String, ForeignKey('species.species_id'))

    UniqueConstraint('project_id', 'species_id')

    project = relationship('Project', back_populates='species_assn')
    species = relationship('Species', back_populates='project_assn')


class VisibilityDict(Base):
    __tablename__ = 'visibility_dict'

    @classmethod
    def get_id_column_name(cls):
        return 'visibility'

    visibility = mapped_column(String, primary_key=True)
    description = mapped_column(String)
