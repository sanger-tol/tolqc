# SPDX-FileCopyrightText: 2025 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

import re
from functools import cached_property

from sqlalchemy import (
    Boolean,
    DateTime,
    ForeignKey,
    Integer,
    String,
    UniqueConstraint,
)
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy.sql import expression

from tolqc.schema.base import Base, LogBase


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
    secondary = mapped_column(String, index=True)
    submission = mapped_column(String)
    date_submitted = mapped_column(DateTime(timezone=True))
    name = mapped_column(String)
    title = mapped_column(String)
    description = mapped_column(String)
    alias = mapped_column(String)
    submitter_id = mapped_column(String, ForeignKey('submitter_dict.submitter_id'))
    is_deleted = mapped_column(Boolean, server_default=expression.false(), nullable=False)

    accession_type = relationship(
        'AccessionTypeDict',
        back_populates='accessions',
    )
    projects = relationship('Project', back_populates='accession')
    studies = relationship('Study', back_populates='accession')
    specimens = relationship('Specimen', back_populates='accession')
    samples = relationship('Sample', back_populates='accession')
    data = relationship('Data', back_populates='accession')

    submitter = relationship('SubmitterDict', back_populates='accessions')

    child_assn = relationship(
        'BioprojectLink',
        primaryjoin='Accession.accession_id == BioprojectLink.parent_accession_id',
        back_populates='parent',
    )
    child_accessions = association_proxy('child_assn', 'child')

    parent_assn = relationship(
        'BioprojectLink',
        primaryjoin='Accession.accession_id == BioprojectLink.child_accession_id',
        back_populates='child',
    )
    parent_accessions = association_proxy('parent_assn', 'parent')

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

    study_submissions = relationship(
        'DataSubmission',
        primaryjoin='Accession.accession_id == DataSubmission.study_accession_id',
        back_populates='study_accession',
    )
    sample_submissions = relationship(
        'DataSubmission',
        primaryjoin='Accession.accession_id == DataSubmission.sample_accession_id',
        back_populates='sample_accession',
    )
    experiment_submissions = relationship(
        'DataSubmission',
        primaryjoin='Accession.accession_id == DataSubmission.experiment_accession_id',
        back_populates='experiment_accession',
    )
    run_submissions = relationship(
        'DataSubmission',
        primaryjoin='Accession.accession_id == DataSubmission.run_accession_id',
        back_populates='run_accession',
    )
    analysis_submissions = relationship(
        'DataSubmission',
        primaryjoin='Accession.accession_id == DataSubmission.analysis_accession_id',
        back_populates='analysis_accession',
    )

    biosample_metagenomes = relationship(
        'Metagenome',
        primaryjoin='Accession.accession_id == Metagenome.biosample_accession_id',
        back_populates='biosample_accession',
    )
    bioproject_metagenomes = relationship(
        'Metagenome',
        primaryjoin='Accession.accession_id == Metagenome.bioproject_accession_id',
        back_populates='bioproject_accession',
    )
    assembly_metagenomes = relationship(
        'Metagenome',
        primaryjoin='Accession.accession_id == Metagenome.assembly_accession_id',
        back_populates='assembly_accession',
    )

    biosample_metagenome_bins = relationship(
        'MetagenomeBin',
        primaryjoin='Accession.accession_id == MetagenomeBin.biosample_accession_id',
        back_populates='biosample_accession',
    )
    assembly_metagenome_bins = relationship(
        'MetagenomeBin',
        primaryjoin='Accession.accession_id == MetagenomeBin.assembly_accession_id',
        back_populates='assembly_accession',
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


class BioprojectLink(LogBase):
    __tablename__ = 'bioproject_link'

    id = mapped_column(Integer, primary_key=True)  # noqa: A003
    parent_accession_id = mapped_column(String, ForeignKey('accession.accession_id'))
    child_accession_id = mapped_column(String, ForeignKey('accession.accession_id'))
    link_status = mapped_column(String, ForeignKey('link_status_dict.link_status'))

    UniqueConstraint('parent_accession_id', 'child_accession_id')
    parent = relationship(
        'Accession',
        foreign_keys=[parent_accession_id],
        back_populates='child_assn',
    )
    child = relationship(
        'Accession',
        foreign_keys=[child_accession_id],
        back_populates='parent_assn',
    )


class LinkStatusDict(Base):
    __tablename__ = 'link_status_dict'

    @classmethod
    def get_id_column_name(cls):
        return 'link_status'

    link_status = mapped_column(String, primary_key=True)
    description = mapped_column(String)


class SubmitterDict(Base):
    __tablename__ = 'submitter_dict'

    @classmethod
    def get_id_column_name(cls):
        return 'submitter_id'

    submitter_id = mapped_column(String, primary_key=True)
    webin_account = mapped_column(String)
    description = mapped_column(String)

    accessions = relationship('Accession', back_populates='submitter')
