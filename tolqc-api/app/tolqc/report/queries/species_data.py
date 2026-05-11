# SPDX-FileCopyrightText: 2025 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from sqlalchemy import case, func, or_, select
from sqlalchemy.orm import InstrumentedAttribute, aliased

from tolqc.report.column_funcs import array_distinct_non_null
from tolqc.report.request_args import NoArg, RequestArgs
from tolqc.schema import User
from tolqc.schema.accession_models import Accession, BioprojectLink
from tolqc.schema.metagenome_models import (
    Metagenome,
    MetagenomeBin,
    MetagenomeBinStatus,
    MetagenomeStatus,
)
from tolqc.schema.sample_data_models import (
    Allocation,
    Data,
    Library,
    Project,
    Sample,
    Species,
    Specimen,
    SpecimenStatus,
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


class ParentFlag:
    """Join to parent accessions"""


class ChildFlag:
    """Join to child accessions"""


def linked_accessions_json(
    name: str,
    link: type[ParentFlag] | type[ChildFlag],
    include_suppressed: bool | NoArg,
):
    """
    Builds a CTE which returns either child or parent Bioproject link
    accessions as a JSON array.
    """

    linked_acc = aliased(Accession)

    # Join to either parent or child accessions
    (assn_rel, link_rel) = (
        (Accession.parent_assn, BioprojectLink.parent)
        if link is ParentFlag
        else (Accession.child_assn, BioprojectLink.child)
    )

    query = (
        select(
            Accession.accession_id,
            func.jsonb_agg(
                accession_struct(
                    linked_acc,
                    link_status=BioprojectLink.link_status,
                )
            ).label(f'{name}_accessions'),
        )
        .select_from(Accession)
        .join(assn_rel)
        .join(linked_acc, link_rel)
        .group_by(Accession.accession_id)
    )

    if include_suppressed is not True:
        query = query.where(BioprojectLink.link_status != 'Suppressed')

    return query.cte(f'{name}_accs')


def species_bioproject_query(req_args: RequestArgs):
    accession = req_args.pop_arg('accession')
    include_suppressed = req_args.pop_arg('include_suppressed')

    # List of accession structs from BioprojectLink parents
    project_cte = linked_accessions_json('project', ParentFlag, include_suppressed)

    # List of accession structs from BioprojectLink children
    product_cte = linked_accessions_json('product', ChildFlag, include_suppressed)

    umbrella_acc = aliased(Accession)
    data_acc = aliased(Accession)
    group_by = [
        Species.species_id,
        Species.taxon_id,
        Species.tolid_prefix,
        project_cte.c.project_accessions,
        product_cte.c.product_accessions,
    ]
    query = (
        select(
            Species.species_id.label('species'),
            Species.taxon_id,
            Species.tolid_prefix,
            accession_struct(
                umbrella_acc,
                col_list=group_by,
            ).label('umbrella_accession'),
            accession_struct(
                data_acc,
                col_list=group_by,
            ).label('data_accession'),
            project_cte.c.project_accessions,
            product_cte.c.product_accessions,
        )
        .select_from(Species)
        .outerjoin(umbrella_acc, Species.umbrella_accession)
        .outerjoin(data_acc, Species.data_accession)
        .outerjoin(project_cte, Species.umbrella_accession_id == project_cte.c.accession_id)
        .outerjoin(product_cte, Species.umbrella_accession_id == product_cte.c.accession_id)
        .group_by(*group_by)
    )

    if accession is not NoArg:
        project_bpl = aliased(BioprojectLink)
        product_bpl = aliased(BioprojectLink)
        query = (
            query.outerjoin(project_bpl, umbrella_acc.parent_assn)
            .outerjoin(product_bpl, umbrella_acc.child_assn)
            .where(
                or_(
                    Species.umbrella_accession_id == accession,
                    Species.data_accession_id == accession,
                    project_bpl.parent_accession_id == accession,
                    product_bpl.child_accession_id == accession,
                )
            )
        )

    return query


def accession_struct(
    accn,
    link_status: InstrumentedAttribute | None = None,
    col_list: list | None = None,
):
    struct = [
        'accession',
        accn.accession_id,
        'name',
        accn.name,
        'title',
        accn.title,
        'type',
        accn.accession_type_id,
    ]
    if link_status:
        struct.extend(
            [
                'link_status',
                link_status,
            ]
        )
    if col_list:
        col_list.extend([struct[i] for i in range(1, len(struct), 2)])
    return case(
        (accn.accession_id == None, None),  # noqa: E711
        else_=func.jsonb_build_object(*struct),
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
            Specimen.ploidy,
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
        filter_allocation = aliased(Allocation)
        query = query.outerjoin(filter_allocation, Data.project_assn).where(
            filter_allocation.project_id == project
        )
    if assignee is not NoArg:
        query = query.where(User.name == assignee)

    return query
