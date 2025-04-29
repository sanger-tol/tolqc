# SPDX-FileCopyrightText: 2025 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from sqlalchemy import select

from tolqc.report.bundles import (
    IsoDateTimeBundle,
    IsoDayBundle,
    LastPathElementBundle,
    ProjectGroupBundle,
    StarPathBundle,
)
from tolqc.schema.sample_data_models import (
    Allocation,
    Data,
    File,
    Library,
    LibraryType,
    Location,
    PacbioRunMetrics,
    Platform,
    Project,
    Run,
    Sample,
    Species,
    Specimen,
)


def pipeline_data_report_query():
    query = (
        select(
            Data.data_id,
            File.remote_path,
            Species.species_id.label('species'),
            LastPathElementBundle('species_dir', Location.path),
            Location.path.label('location_root'),
            Data.category,
            Specimen.specimen_id.label('specimen'),
            LibraryType.hierarchy_name.label('lib_type_dir'),
            StarPathBundle(
                'location',
                Location.path,
                Data.category,
                Specimen.specimen_id,
                LibraryType.hierarchy_name,
            ),
            Library.library_type_id.label('pipeline'),
            Data.tag1_id,
            Data.tag2_id,
            Data.pcr_adapter_id.label('pcr_adapter_id'),
            Data.accession_id.label('run_accession'),
            Sample.accession_id.label('biosample_accession'),
            Specimen.accession_id.label('biospecimen_accession'),
            Species.data_accession_id.label('data_bioproject'),
            Species.umbrella_accession_id.label('umbrella_bioproject'),
            Data.study_id,
            Data.visibility,
            Data.lims_qc,
            Data.processed,
            Sample.sample_id.label('sample'),
            Library.library_id.label('library'),
        )
        .select_from(Data)
        .outerjoin(Sample)
        .outerjoin(Specimen)
        .outerjoin(Location)  # Important to join to Location from Speciemn not Species
        .outerjoin(Species)
        .join(File)
        .join(Library)
        .join(LibraryType)
        .order_by(Data.data_id.desc())
    )

    return query


def pacbio_data_report_query():
    return (
        select(
            ProjectGroupBundle(
                'group',
                Project.hierarchy_name,
                Species.taxon_group,
            ),
            Species.species_id.label('species'),
            Specimen.specimen_id.label('specimen'),
            Sample.sample_id.label('sample'),
            Library.library_type_id.label('pipeline'),
            Platform.name.label('platform'),
            Platform.model,
            IsoDayBundle('date', Run.start),
            Data.lims_qc,
            Run.lims_id.label('run'),
            Run.run_id.label('movie_name'),
            Run.element.label('well'),
            Run.instrument_name.label('instrument'),
            Run.plex_count,
            PacbioRunMetrics.movie_minutes.label('movie_length'),
            Data.tag1_id.label('tag'),
            Sample.accession_id.label('sample_accession'),
            Data.accession_id.label('run_accession'),
            Data.library_id.label('library'),
            Data.reads,
            Data.read_length_mean,
            Data.read_length_n50,
            Data.read_length_longest,
            Data.read_length_shortest,
            Data.reads_duplicated,
            Data.reads_filtered,
            Data.bases.label('bases'),
            Data.bases_a,
            Data.bases_c,
            Data.bases_g,
            Data.bases_t,
            PacbioRunMetrics.loading_conc.label('loading_concentration'),
            PacbioRunMetrics.binding_kit,
            PacbioRunMetrics.sequencing_kit,
            PacbioRunMetrics.productive_zmws_num,
            PacbioRunMetrics.p0_num,
            PacbioRunMetrics.p1_num,
            PacbioRunMetrics.p2_num,
        )
        .select_from(Data)
        .outerjoin(Sample)
        .outerjoin(Specimen)
        .outerjoin(Species)
        .join(Run)
        .join(Platform)
        .outerjoin(Library)
        .outerjoin(PacbioRunMetrics)
        # Cannot do many-to-many join between Data and Project directly.
        # Must explicitly go through Allocation:
        .join(Allocation)
        .join(Project)
        .where(Platform.name == 'PacBio')
        .order_by(
            Data.date.desc(),
            Specimen.specimen_id,
        )
    )


def mlwh_data_report_query():
    query = (
        mlwh_data_report_query_select()
        .select_from(Data)
        .outerjoin(Sample)
        .outerjoin(Specimen)
        .outerjoin(Species)
        .join(Run)
        .join(Platform)
        .outerjoin(File)
        .outerjoin(Library)
        .outerjoin(PacbioRunMetrics)
        .where(Data.study_id != None)  # noqa: E711
        .order_by(
            Data.date.desc(),
        )
    )

    return query


def mlwh_data_report_query_select():
    return select(
        Data.data_id,
        Data.study_id,
        Sample.sample_id.label('sample_name'),
        Specimen.supplied_name.label('supplier_name'),
        Specimen.specimen_id.label('tol_specimen_id'),
        Sample.accession_id.label('biosample_accession'),
        Specimen.accession_id.label('biospecimen_accession'),
        Species.species_id.label('scientific_name'),
        Species.taxon_id,
        Platform.name.label('platform_type'),
        Platform.model.label('instrument_model'),
        Run.instrument_name,
        Library.library_type_id.label('pipeline_id_lims'),
        Run.run_id,
        Run.lims_id.label('lims_run_id'),
        Run.element,
        IsoDateTimeBundle('run_start', Run.start),
        IsoDateTimeBundle('run_complete', Run.complete),
        Run.plex_count,
        Data.lims_qc,
        IsoDateTimeBundle('qc_date', Data.date),
        Data.tag1_id,
        Data.tag2_id,
        Library.library_id,
        PacbioRunMetrics.movie_minutes,
        PacbioRunMetrics.binding_kit,
        PacbioRunMetrics.sequencing_kit,
        PacbioRunMetrics.sequencing_kit_lot_number,
        PacbioRunMetrics.cell_lot_number,
        PacbioRunMetrics.include_kinetics,
        PacbioRunMetrics.loading_conc,
        PacbioRunMetrics.control_num_reads,
        PacbioRunMetrics.control_read_length_mean,
        PacbioRunMetrics.control_concordance_mean,
        PacbioRunMetrics.control_concordance_mode,
        PacbioRunMetrics.local_base_rate,
        PacbioRunMetrics.polymerase_read_bases,
        PacbioRunMetrics.polymerase_num_reads,
        PacbioRunMetrics.polymerase_read_length_mean,
        PacbioRunMetrics.polymerase_read_length_n50,
        PacbioRunMetrics.insert_length_mean,
        PacbioRunMetrics.insert_length_n50,
        PacbioRunMetrics.unique_molecular_bases,
        PacbioRunMetrics.productive_zmws_num,
        PacbioRunMetrics.p0_num,
        PacbioRunMetrics.p1_num,
        PacbioRunMetrics.p2_num,
        PacbioRunMetrics.adapter_dimer_percent,
        PacbioRunMetrics.short_insert_percent,
        PacbioRunMetrics.hifi_read_bases,
        PacbioRunMetrics.hifi_num_reads,
        PacbioRunMetrics.hifi_read_length_mean,
        PacbioRunMetrics.hifi_read_quality_median,
        PacbioRunMetrics.hifi_number_passes_mean,
        PacbioRunMetrics.hifi_low_quality_read_bases,
        PacbioRunMetrics.hifi_low_quality_num_reads,
        PacbioRunMetrics.hifi_low_quality_read_length_mean,
        PacbioRunMetrics.hifi_low_quality_read_quality_median,
        PacbioRunMetrics.hifi_barcoded_reads,
        PacbioRunMetrics.hifi_bases_in_barcoded_reads,
        File.remote_path,
    )


def illumina_data_report_query():
    query = (
        select(
            ProjectGroupBundle(
                'group',
                Project.hierarchy_name,
                Species.taxon_group,
            ),
            Species.species_id.label('species'),
            Specimen.specimen_id.label('specimen'),
            Platform.name.label('platform'),
            Platform.model,
            Data.data_id.label('data_id'),
            Data.reads.label('reads'),
            Data.bases.label('bases'),
            Data.read_length_mean.label('read_length'),
            Sample.accession_id.label('sample_accession'),
            Data.accession_id.label('run_accession'),
            Sample.sample_id.label('sample'),
            Data.tag1_id.label('tag_id'),
            Data.tag2_id.label('tag2_id'),
            Data.lims_qc.label('lims_qc'),
            IsoDayBundle('date', Run.complete),
            Library.library_type_id.label('pipeline'),
            Data.bases_a,
            Data.bases_c,
            Data.bases_g,
            Data.bases_t,
        )
        .select_from(Data)
        .outerjoin(Sample)
        .outerjoin(Specimen)
        .outerjoin(Species)
        .join(Run)
        .join(Platform)
        .outerjoin(Library)
        # Cannot do many-to-many join between Data and Project directly.
        # Must explicitly go through Allocation:
        .join(Allocation)
        .join(Project)
        # Join accession onto Data
        .outerjoin(Data.accession)
        .where(Platform.name == 'Illumina')
        .order_by(
            Data.date.desc(),
            Specimen.specimen_id,
        )
    )

    return query
