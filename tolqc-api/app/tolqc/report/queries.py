# SPDX-FileCopyrightText: 2025 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from sqlalchemy import Float, distinct, func, literal, select
from sqlalchemy.orm import aliased

from tolqc.report.bundles import (
    LastPathElementBundle,
    StarPathBundle,
)
from tolqc.report.request_args import NoArg, RequestArgs
from tolqc.schema import User
from tolqc.schema.metagenome_models import (
    Metagenome,
    MetagenomeBin,
    MetagenomeBinStatus,
    MetagenomeStatus,
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
    SpecimenStatus,
)
from tolqc.schema.system_models import Metadata


def seq_data_header_cols():
    return (
        Data.data_id,
        Species.tolid_prefix,
        Species.species_id.label('species'),
        Specimen.specimen_id.label('specimen'),
        Sample.sample_id.label('sample'),
        Library.library_id.label('library'),
        Library.library_type_id.label('pipeline'),
        Platform.name.label('platform'),
        Platform.model,
        Run.instrument_name.label('instrument'),
        iso_date_col('date', func.coalesce(Run.complete, Run.start)),
        Data.lims_qc,
        Run.lims_id.label('run'),
        Specimen.accession_id.label('biospecimen_accession'),
        Sample.accession_id.label('biosample_accession'),
        Data.accession_id.label('run_accession'),
    )


def basic_seq_stat_cols():
    return (
        Data.reads,
        Data.bases,
        Data.bases_a,
        Data.bases_c,
        Data.bases_g,
        Data.bases_t,
        Data.read_length_mean,
    )


def pipeline_data_report_query(req_args: RequestArgs):
    loc_root = req_args.pop_arg('root')
    if loc_root is NoArg:
        location_path = Location.path
        root_path = []
    elif loc_root is True:
        location_path = func.concat_ws('/', Metadata.string_value, Location.path)
        root_path = [Metadata.string_value]
    else:
        loc_path = literal(loc_root.rstrip('/'))
        location_path = func.concat_ws('/', loc_path, Location.path)
        root_path = [Metadata.string_value]
        root_path = [loc_path]

    hierarchy = [
        *root_path,
        Location.path,
        Data.category,
        Specimen.specimen_id,
        LibraryType.hierarchy_name,
    ]

    query = (
        select(
            *seq_data_header_cols(),
            File.remote_path,
            LastPathElementBundle('species_dir', Location.path),
            Species.taxon_id,
            location_path.label('location_root'),
            Data.category,
            LibraryType.hierarchy_name.label('lib_type_dir'),
            File.name.label('file_name'),
            File.file_type,
            File.has_kinetics,
            File.has_methylation,
            StarPathBundle(
                'location',
                *hierarchy,
            ),
            StarPathBundle(
                'file_location',
                *hierarchy,
                File.name,
            ),
            StarPathBundle(
                'location_branch',
                Data.category,
                Specimen.specimen_id,
                LibraryType.hierarchy_name,
            ),
            Data.pcr_adapter_id.label('pcr_adapter_id'),
            Species.data_accession_id.label('data_bioproject'),
            Species.umbrella_accession_id.label('umbrella_bioproject'),
            Data.study_id,
            Data.visibility,
            Data.qc,
            Data.processed,
        )
        .select_from(Data)
        .outerjoin(Sample)
        .outerjoin(Specimen)
        # Important to join to Location from Specimen not Species!
        .outerjoin(Specimen.location)
        .outerjoin(Specimen.species)
        .join(File)
        .outerjoin(Library)
        .outerjoin(LibraryType)
        .outerjoin(Run)
        .outerjoin(Platform)
        .order_by(Data.data_id.desc())
    )

    if loc_root is True:
        query = query.join(Metadata, Metadata.name == 'location.root')

    return query


def pacbio_data_report_query(req_args: RequestArgs):
    data_columns = (
        *seq_data_header_cols(),
        Run.run_id.label('movie_name'),
        Run.element.label('well'),
        Run.plex_count,
        PacbioRunMetrics.movie_minutes.label('movie_length'),
        File.has_kinetics,
        Data.tag1_id.label('tag'),
        *basic_seq_stat_cols(),
        Data.read_length_n50,
        Data.read_length_longest,
        Data.read_length_shortest,
        percent_col('reads_duplicated_pct', Data.reads_duplicated, Data.reads),
        percent_col('reads_discarded_pct', Data.reads_discarded, Data.reads),
        percent_col('reads_trimmed_pct', Data.reads_trimmed, Data.reads),
        percent_col('bases_removed_pct', Data.bases_removed, Data.bases),
        PacbioRunMetrics.loading_conc.label('loading_concentration'),
        PacbioRunMetrics.binding_kit,
        PacbioRunMetrics.sequencing_kit,
        PacbioRunMetrics.productive_zmws_num,
        PacbioRunMetrics.p0_num,
        PacbioRunMetrics.p1_num,
        PacbioRunMetrics.p2_num,
        Data.pcr_adapter_id,
        Run.chemistry,
    )

    query = (
        select(
            *data_columns,
            func.bool_or(File.has_methylation).label('has_methylation'),
        )
        .select_from(Data)
        .outerjoin(Sample)
        .outerjoin(Specimen)
        .outerjoin(Species)
        .join(Run)
        .join(Platform)
        .outerjoin(Library)
        .outerjoin(PacbioRunMetrics)
        .outerjoin(File)
        .where(Platform.name == 'PacBio')
        .group_by(*data_columns)
        .order_by(
            Data.date.desc(),
            Specimen.specimen_id,
        )
    )

    return add_methylation_filter(query, req_args)


def add_methylation_filter(query, req_args: RequestArgs):
    meth_arg = req_args.pop_arg('has_methylation')
    if meth_arg is not NoArg:
        query = query.having(func.bool_or(File.has_methylation) == meth_arg)
    return query


def ont_data_report_query(req_args: RequestArgs):
    data_columns = (
        *seq_data_header_cols(),
        Run.run_id.label('flowcell'),
        Run.element.label('element'),
        Data.tag1_id.label('tag'),
        *basic_seq_stat_cols(),
        Data.read_length_n50,
        Data.read_length_longest,
        Data.read_length_shortest,
        Run.chemistry,
    )

    query = (
        select(
            *data_columns,
            func.bool_or(File.has_methylation).label('has_methylation'),
        )
        .select_from(Data)
        .outerjoin(Sample)
        .outerjoin(Specimen)
        .outerjoin(Species)
        .join(Run)
        .join(Platform)
        .outerjoin(Library)
        .outerjoin(File)
        .where(Platform.name == 'ONT')
        .group_by(*data_columns)
        .order_by(
            Data.date.desc(),
            Specimen.specimen_id,
        )
    )

    return add_methylation_filter(query, req_args)


def mlwh_data_report_query(*_):
    return (
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
        .where(Platform.name.in_(('Illumina', 'PacBio')))
        .order_by(
            Data.date.desc(),
        )
    )


def mlwh_data_report_query_select(*_):
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
        iso_datetime_col('run_start', Run.start),
        iso_datetime_col('run_complete', Run.complete),
        Run.plex_count,
        Data.lims_qc,
        iso_datetime_col('qc_date', Data.date),
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


def illumina_data_report_query(*_):
    return (
        select(
            *seq_data_header_cols(),
            *basic_seq_stat_cols(),
        )
        .select_from(Data)
        .outerjoin(Sample)
        .outerjoin(Specimen)
        .outerjoin(Species)
        .join(Run)
        .join(Platform)
        .outerjoin(Library)
        .where(Platform.name == 'Illumina')
        .order_by(
            Data.date.desc(),
            Specimen.specimen_id,
        )
    )


def metagenome_report_query(*_):
    # Construct CTE that counts bin types
    bin_counts = (
        select(
            MetagenomeBin.metagenome_id,
            func.count().filter(MetagenomeBin.bin_type == 'MAG').label('mag_count'),
            func.count().filter(MetagenomeBin.bin_type == 'BIN').label('bin_count'),
        )
        .group_by(MetagenomeBin.metagenome_id)
        .cte('bin_counts')
    )

    # We join into the species table via both the metagenome and host
    # specimen, so we need an alias for it.
    host_species = aliased(Species)

    return (
        select(
            Metagenome.metagenome_id.label('metagenome'),
            Specimen.specimen_id.label('host_specimen'),
            MetagenomeStatus.status_type_id.label('status'),
            Specimen.accession_id.label('host_biospecimen_accession'),
            host_species.species_id.label('host_species'),
            host_species.taxon_id.label('host_taxon_id'),
            Species.species_id.label('taxon_name'),
            Species.taxon_id,
            Metagenome.biosample_accession_id.label('biosample_accession'),
            Metagenome.bioproject_accession_id.label('bioproject'),
            Metagenome.assembly_accession_id.label('assembly_accession'),
            bin_counts.c.mag_count,
            bin_counts.c.bin_count,
            Metagenome.coverage,
            Metagenome.version,
        )
        .select_from(Metagenome)
        .outerjoin(Metagenome.species)
        .outerjoin(Metagenome.host_specimen)
        .outerjoin(host_species, Specimen.species)
        .outerjoin(Metagenome.status)
        .outerjoin(bin_counts)
        .order_by(Metagenome.metagenome_id)
    )


def metagenome_bin_report_query(*_):
    return (
        select(
            MetagenomeBin.metagenome_bin_id.label('metagenome_bin'),
            Metagenome.metagenome_id.label('metagenome'),
            Specimen.specimen_id.label('host_specimen'),
            MetagenomeBinStatus.status_type_id.label('status'),
            Species.species_id.label('taxon_name'),
            Species.taxon_id,
            MetagenomeBin.biosample_accession_id.label('biosample_accession'),
            MetagenomeBin.assembly_accession_id.label('assembly_accession'),
            MetagenomeBin.gtdb_taxonomy,
            MetagenomeBin.bin_type,
            MetagenomeBin.length,
            MetagenomeBin.contigs,
            MetagenomeBin.circular_contigs,
            MetagenomeBin.completeness,
            MetagenomeBin.contamination,
            MetagenomeBin.mean_coverage,
            MetagenomeBin.trna_total,
            MetagenomeBin.trna_unique,
            MetagenomeBin.has_23s,
            MetagenomeBin.has_16s,
            MetagenomeBin.has_5s,
            MetagenomeBin.n_23s,
            MetagenomeBin.n_16s,
            MetagenomeBin.n_5s,
        )
        .select_from(MetagenomeBin)
        .outerjoin(Species)
        .outerjoin(MetagenomeBin.metagenome)
        .outerjoin(Metagenome.host_specimen)
        .outerjoin(MetagenomeBin.status)
        .order_by(MetagenomeBin.metagenome_bin_id)
    )


def specimen_status_report_query(req_args: RequestArgs):
    # Filters on the `data` table
    data_vals = req_args.pop_args_dict('processed', 'qc', 'visibility')

    # Filters on project name and assignee
    project = req_args.pop_arg('project')
    assignee = req_args.pop_arg('assignee')

    # Species data summary for all species which are not 'unidentified'.
    species_data_query = (
        select(
            Species.species_id,
            Library.library_type_id.label('pipeline'),
            Specimen.specimen_id,
            func.sum(Data.reads).label('reads'),
            func.sum(Data.bases).label('bases'),
        )
        .join(Specimen)
        .join(Sample)
        .join(Data)
        .join(Library)
        .where(Species.species_id != 'unidentified')
        .group_by(
            Species.species_id,
            Library.library_type_id,
            Specimen.specimen_id,
        )
        .order_by(
            Species.species_id,
            Library.library_type_id,
            Specimen.specimen_id,
        )
    )

    # Specimen summary data for the 'unidentified' species, which includes but
    # is not necessarily limited to the WOSPI project.
    wospi_data_query = (
        select(
            Library.library_type_id.label('pipeline'),
            Specimen.specimen_id,
            func.sum(Data.reads).label('reads'),
            func.sum(Data.bases).label('bases'),
        )
        .select_from(Specimen)
        .join(Sample)
        .join(Data)
        .join(Library)
        .where(Specimen.species_id == 'unidentified')
        .group_by(
            Library.library_type_id,
            Specimen.specimen_id,
        )
        .order_by(
            Library.library_type_id,
            Specimen.specimen_id,
        )
    )

    # Add `data` table filtering
    for colname, val in data_vals.items():
        species_data_query = species_data_query.where(getattr(Data, colname) == val)
        wospi_data_query = wospi_data_query.where(getattr(Data, colname) == val)

    # Add filtering on project name
    if project is not NoArg:
        species_data_query = species_data_query.outerjoin(Allocation).where(
            Allocation.project_id == project
        )
        wospi_data_query = wospi_data_query.outerjoin(Allocation).where(
            Allocation.project_id == project
        )

    # Turn queries into CTEs
    species_data_type = species_data_query.cte('species_data_type')
    wospi_data_type = wospi_data_query.cte('wospi_data_type')

    # CTEs which aggregate species and WOSPI specimen data summaries into JSON
    # lists
    specimen_pipeline = (
        select(
            species_data_type.c.species_id,
            func.jsonb_agg(
                func.jsonb_build_object(
                    'pipeline',
                    species_data_type.c.pipeline,
                    'specimen_id',
                    species_data_type.c.specimen_id,
                    'reads',
                    species_data_type.c.reads,
                    'bases',
                    species_data_type.c.bases,
                )
            ).label('species_data'),
        )
        .select_from(species_data_type)
        .group_by(species_data_type.c.species_id)
        .cte('specimen_pipeline')
    )
    wospi_pipeline = (
        select(
            wospi_data_type.c.specimen_id,
            func.jsonb_agg(
                func.jsonb_build_object(
                    'pipeline',
                    wospi_data_type.c.pipeline,
                    'specimen_id',
                    wospi_data_type.c.specimen_id,
                    'reads',
                    wospi_data_type.c.reads,
                    'bases',
                    wospi_data_type.c.bases,
                )
            ).label('specimen_data'),
        )
        .select_from(wospi_data_type)
        .group_by(wospi_data_type.c.specimen_id)
        .cte('wospi_pipeline')
    )

    query = (
        select(
            Specimen.specimen_id.label('specimen'),
            Specimen.sts_specimen,
            SpecimenStatus.status_type_id.label('specimen_status'),
            array_distinct_non_null('projects', Project.project_id),
            Species.species_id.label('species'),
            Species.common_name,
            Species.taxon_id,
            Species.tolid_prefix,
            Specimen.epithet,
            Specimen.taxon_id.label('specimen_taxon_id'),
            Specimen.sts_priority,
            Specimen.sex_id.label('sex'),
            Species.genome_size,
            Species.family_taxon_id,
            Species.taxon_family,
            Species.taxon_order,
            Species.taxon_phylum,
            Species.taxon_group,
            Specimen.accession_id.label('biospecimen_accession'),
            Species.umbrella_accession_id.label('umbrella_bioproject'),
            Species.data_accession_id.label('data_bioproject'),
            User.name.label('assignee'),
            func.coalesce(
                # Will be able to use any_value() aggregate function and
                # remove these columns from the GROUP BY once the server is
                # PostgreSQL >= 16
                specimen_pipeline.c.species_data,
                wospi_pipeline.c.specimen_data,
            ).label('species_data'),
        )
        .select_from(Specimen)
        .outerjoin(Specimen.species)
        .outerjoin(Specimen.status)
        .outerjoin(Specimen.assignee)
        .outerjoin(Specimen.samples)
        .outerjoin(Specimen.sex)
        .outerjoin(Sample.data)
        .outerjoin(Allocation)
        .outerjoin(Project)
        .outerjoin(specimen_pipeline)
        .outerjoin(
            wospi_pipeline,
            Specimen.specimen_id == wospi_pipeline.c.specimen_id,
        )
        .group_by(
            Specimen.specimen_id,
            Species.species_id,
            SpecimenStatus.status_type_id,
            Species.common_name,
            Species.taxon_id,
            Specimen.epithet,
            Specimen.taxon_id,
            Specimen.sex_id,
            Species.genome_size,
            Species.taxon_family,
            Species.family_taxon_id,
            Species.taxon_order,
            Species.taxon_phylum,
            Species.taxon_group,
            Specimen.sts_priority,
            Specimen.accession_id,
            Species.umbrella_accession_id,
            Species.data_accession_id,
            User.name,
            specimen_pipeline.c.species_data,
            wospi_pipeline.c.specimen_data,
        )
        .order_by(
            Specimen.specimen_id,
        )
    )

    # Add `data` table, project name and assignee filtering to the main query
    for colname, val in data_vals.items():
        query = query.where(getattr(Data, colname) == val)
    if project is not NoArg:
        query = query.where(Allocation.project_id == project)
    if assignee is not NoArg:
        query = query.where(User.name == assignee)

    return query


def array_distinct_non_null(label_txt, column):
    """
    Builds SQL for returning an array aggregate column of non-null distinct
    values
    """
    return func.array_remove(func.array_agg(distinct(column)), None).label(label_txt)


def percent_col(label_txt, nominator, divisor, decimal_places=4):
    """
    Builds SQL for returning a column in %
    """
    return func.round(100 * nominator / divisor, decimal_places).cast(Float).label(label_txt)


def iso_datetime_col(label_txt, column):
    """
    Builds SQL for returning an ISO 8601 datetime string
    """
    return func.to_char(column, 'YYYY-MM-DD"T"HH24:MI:SSTZH:TZM').label(label_txt)


def iso_date_col(label_txt, column):
    """
    Builds SQL for returning an ISO 8601 date string
    """
    return func.to_char(column, 'YYYY-MM-DD').label(label_txt)
