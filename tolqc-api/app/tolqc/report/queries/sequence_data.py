# SPDX-FileCopyrightText: 2026 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from sqlalchemy import Select, case, func, or_, select
from sqlalchemy.orm import aliased

from tolqc.report.column_funcs import (
    array_distinct_non_null,
    iso_date_col,
    iso_datetime_col,
    percent_col,
    star_if_null_path,
)
from tolqc.report.request_args import NoArg, RequestArgs
from tolqc.schema.sample_data_models import (
    Allocation,
    Data,
    File,
    Library,
    LibraryType,
    Location,
    PacbioRunMetrics,
    Platform,
    Run,
    Sample,
    Species,
    Specimen,
)
from tolqc.schema.system_models import Metadata


def seq_data_header_cols():
    return (
        Data.data_id,
        Species.tolid_prefix,
        Species.species_id.label('species'),
        Species.genome_size,
        Specimen.specimen_id.label('specimen'),
        Sample.sample_id.label('sample'),
        Library.library_id.label('library'),
        Library.library_type_id.label('pipeline'),
        LibraryType.reporting_category.label('data_type'),
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


def pipeline_data_report_query(req_args: RequestArgs) -> Select:
    project = req_args.pop_arg('project')

    loc_root = req_args.pop_arg('root')
    location_path = Location.path
    root_path = []
    if loc_root is True:
        location_path = func.concat_ws('/', Metadata.string_value, Location.path)
        root_path = [Metadata.string_value]
    elif isinstance(loc_root, str):
        loc_path = loc_root.rstrip('/')
        location_path = func.concat(f'{loc_path}/', Location.path)
        root_path = [loc_path]

    hierarchy = [
        *root_path,
        Location.path,
        Data.category,
        Specimen.specimen_id,
        case(
            (
                # Include relative_path if set
                File.relative_path != None,  # noqa: E711
                func.concat_ws(
                    '/',
                    func.coalesce(LibraryType.hierarchy_name, '*'),
                    File.relative_path,
                ),
            ),
            else_=LibraryType.hierarchy_name,
        ),
    ]

    # Need aliases for allocation and project table since we join into them to
    # get both the primary project and the list of all projects which the
    # data is in.
    primary_allocation = aliased(Allocation)

    top_data_columns = [
        *seq_data_header_cols(),
        LibraryType.is_pcr,
        File.insdc_path,
        File.public_path,
        Specimen.sts_specimen,
        primary_allocation.project_id.label('primary_project'),
    ]

    bottom_data_columns = [
        File.remote_path,
        func.split_part(Location.path, '/', -1).label('species_dir'),
        Species.taxon_id,
        location_path.label('location_root'),
        Data.category,
        LibraryType.hierarchy_name.label('lib_type_dir'),
        File.name.label('file_name'),
        File.md5,
        File.file_type,
        File.has_kinetics,
        File.has_methylation,
        star_if_null_path(*hierarchy).label('location'),
        star_if_null_path(*hierarchy, File.name).label('file_location'),
        star_if_null_path(Data.category, Specimen.specimen_id, LibraryType.hierarchy_name).label(
            'location_branch'
        ),
        Data.pcr_adapter_id.label('pcr_adapter_id'),
        Species.data_accession_id.label('data_bioproject'),
        Species.umbrella_accession_id.label('umbrella_bioproject'),
        Data.study_id,
        Data.visibility,
        Data.qc,
        Data.processed,
    ]

    query = (
        select(
            *top_data_columns,
            array_distinct_non_null('projects', Allocation.project_id),
            *bottom_data_columns,
        )
        .select_from(Data)
        .outerjoin(Allocation)
        # Second join into allocation table to get the primary project
        .outerjoin(
            primary_allocation,
            Data.project_assn.and_(primary_allocation.is_primary == True),  # noqa: E712
        )
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
        .group_by(*top_data_columns, *bottom_data_columns)
    )

    if project is not NoArg:
        # Add a new Allocation alias for filtering on project
        filter_allocation = aliased(Allocation)
        query = query.outerjoin(filter_allocation).where(filter_allocation.project_id == project)
    if loc_root is True:
        query = query.join(Metadata, Metadata.name == 'location.root')

    return query


def pacbio_data_report_query(req_args: RequestArgs) -> Select:
    data_columns = (
        *seq_data_header_cols(),
        LibraryType.is_pcr,
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
        .outerjoin(LibraryType)
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


def ont_data_report_query(req_args: RequestArgs) -> Select:
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
        .outerjoin(LibraryType)
        .outerjoin(File)
        .where(Platform.name == 'ONT')
        .group_by(*data_columns)
        .order_by(
            Data.date.desc(),
            Specimen.specimen_id,
        )
    )

    return add_methylation_filter(query, req_args)


def mlwh_data_report_query(*_) -> Select:
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
        .where(
            or_(
                # Ignore file types other than BAM and CRAM, which are
                # (currently) the only ones returned from querying the MLWH.
                File.file_type == None,  # noqa: E711
                File.file_type.in_(['BAM', 'CRAM']),
            )
        )
        .order_by(
            Data.date.desc(),
        )
    )


def mlwh_data_report_query_select(*_) -> Select:
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


def illumina_data_report_query(*_) -> Select:
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
        .outerjoin(LibraryType)
        .where(Platform.name == 'Illumina')
        .order_by(
            Data.date.desc(),
            Specimen.specimen_id,
        )
    )
