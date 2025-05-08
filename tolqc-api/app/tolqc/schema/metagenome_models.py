# SPDX-FileCopyrightText: 2025 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from sqlalchemy import (
    BigInteger,
    Boolean,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import mapped_column, relationship

from tolqc.schema.base import Base, LogBase


class BinTypeDict(Base):
    __tablename__ = 'bin_type_dict'

    @classmethod
    def get_id_column_name(cls):
        return 'bin_type'

    bin_type = mapped_column(String, primary_key=True)
    description = mapped_column(String)


class Metagenome(LogBase):
    __tablename__ = 'metagenome'

    @classmethod
    def get_id_column_name(cls):
        return 'metagenome_id'

    metagenome_id = mapped_column(String, primary_key=True)
    species_id = mapped_column(
        String,
        ForeignKey('species.species_id'),
    )
    metagenome_status_id = mapped_column(
        Integer, ForeignKey('metagenome_status.metagenome_status_id')
    )
    dataset_id = mapped_column(
        String,
        ForeignKey('dataset.dataset_id'),
    )
    host_specimen_id = mapped_column(
        String,
        ForeignKey('metagenome.metagenome_id'),
    )
    biosample_accession_id = mapped_column(
        String,
        ForeignKey('accession.accession_id'),
    )
    bioproject_accession_id = mapped_column(
        String, ForeignKey('accession.accession_id')
    )
    assembly_accession_id = mapped_column(
        String,
        ForeignKey('accession.accession_id'),
    )
    coverage = mapped_column(Integer)
    version = mapped_column(Integer)
    software_version_id = mapped_column(
        Integer,
        ForeignKey('software_version.software_version_id'),
    )

    biosample_accession = relationship(
        'Accession',
        primaryjoin='Metagenome.biosample_accession_id == Accession.accession_id',
        back_populates='biosample_metagenomes',
    )
    bioproject_accession = relationship(
        'Accession',
        primaryjoin='Metagenome.bioproject_accession_id == Accession.accession_id',
        back_populates='bioproject_metagenomes',
    )
    assembly_accession = relationship(
        'Accession',
        primaryjoin='Metagenome.assembly_accession_id == Accession.accession_id',
        back_populates='assembly_metagenomes',
    )

    species = relationship('Species', back_populates='metagenomes')

    status = relationship('MetagenomeStatus', foreign_keys=[metagenome_status_id])
    status_history = relationship(
        'MetagenomeStatus',
        primaryjoin='Metagenome.metagenome_id == MetagenomeStatus.metagenome_id',
        back_populates='metagenome',
    )

    dataset = relationship('Dataset', back_populates='metagenomes')

    software_version = relationship(
        'SoftwareVersion',
        back_populates='metagenomes',
    )



class MetagenomeBin(LogBase):
    __tablename__ = 'metagenome_bin'

    @classmethod
    def get_id_column_name(cls):
        return 'metagenome_bin_id'

    metagenome_bin_id = mapped_column(String, primary_key=True)
    metagenome_id = mapped_column(String, ForeignKey('metagenome.metagenome_id'))
    species_id = mapped_column(
        String,
        ForeignKey('species.species_id'),
    )
    metagenome_bin_status_id = mapped_column(
        Integer, ForeignKey('metagenome_bin_status.metagenome_bin_status_id')
    )
    biosample_accession_id = mapped_column(
        String,
        ForeignKey('accession.accession_id'),
    )
    assembly_accession_id = mapped_column(
        String,
        ForeignKey('accession.accession_id'),
    )
    gtdb_taxonomy = mapped_column(String)
    bin_type = mapped_column(String, ForeignKey('bin_type_dict.bin_type'))
    length = mapped_column(BigInteger)
    contigs = mapped_column(Integer)
    circular_contigs = mapped_column(Integer)
    completeness = mapped_column(Float)
    contamination = mapped_column(Float)
    mean_coverage = mapped_column(Float)
    ssu_count = mapped_column(Integer)
    trna_total = mapped_column(Integer)
    trna_unique = mapped_column(Integer)
    has_23s = mapped_column(Boolean)
    has_16s = mapped_column(Boolean)
    has_5s = mapped_column(Boolean)
    software_version_id = mapped_column(
        Integer,
        ForeignKey('software_version.software_version_id'),
    )

    biosample_accession = relationship(
        'Accession',
        primaryjoin='MetagenomeBin.biosample_accession_id == Accession.accession_id',
        back_populates='biosample_metagenome_bins',
    )
    assembly_accession = relationship(
        'Accession',
        primaryjoin='MetagenomeBin.assembly_accession_id == Accession.accession_id',
        back_populates='assembly_metagenome_bins',
    )

    species = relationship('Species', back_populates='metagenome_bins')

    status = relationship(
        'MetagenomeBinStatus', foreign_keys=[metagenome_bin_status_id]
    )
    status_history = relationship(
        'MetagenomeBinStatus',
        primaryjoin='MetagenomeBin.metagenome_bin_id == MetagenomeBinStatus.metagenome_bin_id',
        back_populates='metagenome_bin',
    )

    software_version = relationship(
        'SoftwareVersion',
        back_populates='metagenome_bins',
    )



class MetagenomeBinStatus(LogBase):
    __tablename__ = 'metagenome_bin_status'

    @classmethod
    def get_id_column_name(cls):
        return 'metagenome_bin_status_id'

    metagenome_bin_status_id = mapped_column(Integer, primary_key=True)
    metagenome_bin_id = mapped_column(
        String,
        ForeignKey('metagenome_bin.metagenome_bin_id'),
        nullable=False,
    )
    status_type_id = mapped_column(
        String,
        ForeignKey('metagenome_status_type.status_type_id'),
        nullable=False,
    )
    status_time = mapped_column(DateTime(timezone=True), nullable=False)

    metagenome_bin = relationship(
        'MetagenomeBin',
        foreign_keys=[metagenome_bin_id],
        back_populates='status_history',
    )
    status_type = relationship('MetagenomeStatusType', back_populates='bin_statuses')


class MetagenomeStatus(LogBase):
    __tablename__ = 'metagenome_status'

    @classmethod
    def get_id_column_name(cls):
        return 'metagenome_status_id'

    metagenome_status_id = mapped_column(Integer, primary_key=True)
    metagenome_id = mapped_column(
        String,
        ForeignKey('metagenome.metagenome_id'),
        nullable=False,
    )
    status_type_id = mapped_column(
        String,
        ForeignKey('metagenome_status_type.status_type_id'),
        nullable=False,
    )
    status_time = mapped_column(DateTime(timezone=True), nullable=False)

    metagenome = relationship(
        'Metagenome',
        foreign_keys=[metagenome_id],
        back_populates='status_history',
    )
    status_type = relationship('MetagenomeStatusType', back_populates='statuses')


class MetagenomeStatusType(Base):
    __tablename__ = 'metagenome_status_type'

    @classmethod
    def get_id_column_name(cls):
        return 'status_type_id'

    status_type_id = mapped_column(String, primary_key=True)
    description = mapped_column(String)
    assign_order = mapped_column(Integer)

    bin_statuses = relationship('MetagenomeBinStatus', back_populates='status_type')
    statuses = relationship('MetagenomeStatus', back_populates='status_type')


class TaxonRequest(LogBase):
    __tablename__ = 'taxon_request'

    @classmethod
    def get_id_column_name(cls):
        return 'species_id'

    species_id = mapped_column(String, primary_key=True)
    request_status = mapped_column(
        String, ForeignKey('taxon_request_status_dict.request_status')
    )
    taxon_id = mapped_column(Integer, index=True)


class TaxonRequestStatusDict(Base):
    __tablename__ = 'taxon_request_status_dict'

    @classmethod
    def get_id_column_name(cls):
        return 'request_status'

    request_status = mapped_column(String, primary_key=True)
    description = mapped_column(String)
