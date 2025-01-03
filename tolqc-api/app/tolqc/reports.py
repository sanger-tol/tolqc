# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

import datetime
import json

from flask import Blueprint, request

from sqlalchemy import select
from sqlalchemy.orm import Bundle

from tol.api_base2 import custom_blueprint

from tolqc.schema.sample_data_models import (
    Accession,
    Allocation,
    Data,
    File,
    Library,
    LibraryType,
    MappingMetrics,
    PacbioRunMetrics,
    Platform,
    Project,
    Run,
    Sample,
    Species,
    Specimen,
)

from werkzeug.exceptions import BadRequest


def reports_blueprint(
    session_factory,
    url_prefix: str = '/report',
) -> Blueprint:
    rep = custom_blueprint(name='reports', url_prefix=url_prefix)

    @rep.route('/pacbio-data')
    def pacbio_run_data():
        return tolqc_report(
            session_factory,
            'pacbio_data',
            pacbio_data_report_query,
        )

    @rep.route('/pipeline-data')
    def pipeline_data():
        return tolqc_report(
            session_factory,
            'pipeline_data',
            pipeline_data_report_query,
        )

    @rep.route('/mlwh-data')
    def mlwh_data():
        return tolqc_report(
            session_factory,
            'mlwh_data',
            mlwh_data_report_query,
        )
    
    @rep.route('/illumina-data')
    def illumina_data():
        return tolqc_report(
            session_factory,
            'illumina_data',
            illumina_data_report_query,
        )

    @rep.errorhandler(BadRequest)
    def handle_bad_request(e):
        return {'error': e.description}, 400

    return rep


def tsv_rows(row_itr, query):
    yield '\t'.join(d['name'] for d in query.column_descriptions) + '\n'
    for row in row_itr:
        yield '\t'.join('' if x is None else str(x) for x in row) + '\n'


def ndjson_rows(row_itr, _):
    for row in row_itr:
        yield json.dumps(row._asdict(), separators=(',', ':')) + '\n'


FORMATTERS = {
    'ndjson': (ndjson_rows, 'application/x-ndjson'),
    'tsv': (tsv_rows, 'text/tab-separated-values'),
}


def tolqc_report(session_factory, report_name, build_query):
    # File format if requested; defaults to TSV
    req_fmt = request.args.get('format', 'tsv').lower()
    fmt_mime = FORMATTERS.get(req_fmt)
    if not fmt_mime:
        valid = tuple(FORMATTERS)
        msg = f'format parameter must be one of: {valid}'
        raise BadRequest(msg)
    out_formatter, mime_type = fmt_mime

    # Suggested filename for web browsers
    today = datetime.date.today().isoformat()
    filename = f'{report_name}_{today}.{req_fmt}'
    headers = {
        'Content-Type': mime_type,
        'Content-Disposition': f'attachment; filename="{filename}"',
    }

    # Must either (as here) use session as a context manager or call
    # session.close() to avoid SELECT statements accumulating on server
    # with 'idle in transaction' state.
    with session_factory() as session:
        query = build_query()
        row_itr = session.execute(query)

    # Streams formatted data from the SQL query to the client
    return out_formatter(row_itr, query), 200, headers


def pipeline_data_report_query():
    query = (
        select(
            Data.data_id,
            File.remote_path,
            Species.species_id.label('species'),
            Species.hierarchy_name.label('species_hierarchy'),
            Specimen.specimen_id.label('specimen'),
            Library.library_type_id.label('pipeline'),
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
        .outerjoin(Species)
        .join(File)
        .join(Library)
        .order_by(Data.data_id.desc())
    )

    query = add_argument(
        query,
        Data.processed,
        lookup={
            'null': None,
            '0': 0,
            '1': 1,
        },
    )
    query = add_argument(query, Data.visibility)
    query = add_argument(query, Data.lims_qc)
    query = add_argument(query, Library.library_type_id, name='pipeline')
    query = add_argument(query, Data.study_id)

    return query


def add_argument(query, column, name=None, lookup=None):
    if not name:
        name = column.name

    arg = request.args.get(name)
    if not arg:
        return query

    # Guard against being passed excessively long param values
    val = arg[:256]

    if lookup:
        try:
            val = lookup[arg]
        except KeyError:
            valid = tuple(lookup)
            msg = f"'{name}' parameter must be one of: {valid}"
            raise BadRequest(msg) from None

    return query.where(column == val)


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
            Data.tag_index,
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
    query = add_argument(query, Data.study_id)
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
        Data.tag_index,
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
            LibraryType.hierarchy_name.label('source'),
            Specimen.specimen_id.label('specimen'),
            Platform.name.label('platform'),
            Platform.model,
            Data.data_id.label('run'),
            Data.reads.label('read_pairs'),
            Data.bases.label('yield'),
            MappingMetrics.average_quality.label('avg qual'),
            Data.read_length_mean.label('avg length'),
            Sample.accession_id.label('sample_accession'),
            Data.accession_id.label('run_accession'),
            Project.accession_id.label('study_accession'),
            Accession.date_submitted.label('submission_date'),
            Sample.sample_id.label('sanger_id'),
            Data.tag1_id.label('tag_sequence'),
            Data.tag2_id.label('tag2_sequence'),
            Data.lims_qc.label('npg_qc_status'),
            IsoDayBundle('date', Run.start),
            Species.species_id.label('species'),
            Library.library_type_id.label('pipeline_id_lims'),
            Data.read_length_n50,
            Data.read_length_longest,
            Data.read_length_shortest,
            Data.reads_duplicated,
            Data.reads_filtered,
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
        .outerjoin(LibraryType)
        .outerjoin(MappingMetrics)
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
    query = add_argument(query, Data.study_id)
    return query

class ProjectGroupBundle(Bundle):
    """
    Combine the "proj" and "taxon_group" columns if the "proj" column
    contains "{}", else returns the "proj" itself.
    e.g. ("darwin/{}", "birds") becomes "darwin/birds"
    """  # noqa: P102

    def create_row_processor(self, query, getters, _):
        get_proj, get_taxon_group = getters

        def processor(row):
            proj = get_proj(row)
            taxon_group = get_taxon_group(row)
            group = None
            if proj is not None:
                if '{}' in proj and taxon_group is not None:  # noqa: P103
                    group = proj.format(taxon_group)
                else:
                    group = proj
            return group

        return processor


class IsoDayBundle(Bundle):
    """
    Returns just the day portion of a datetime column
    in ISO 8601 format, if it contains a value.
    """

    def create_row_processor(self, query, getters, _):
        (get_datetime,) = getters

        def processor(row):
            dt = get_datetime(row)
            return dt.date().isoformat() if dt else None

        return processor


class IsoDateTimeBundle(Bundle):
    """
    Returns datetime column in ISO 8601 format, if it contains a value.
    """

    def create_row_processor(self, query, getters, _):
        (get_datetime,) = getters

        def processor(row):
            dt = get_datetime(row)
            return dt.isoformat() if dt else None

        return processor






# "group":"jaron/nematodes",
# "type":"hic-arima2",
# "specimen":"nrCaeEleg1",
# "platform":"Illumina",
# "model":"NovaSeqX",
# "run":"49103_3-4#8",
# "reads_paired":1853705600,
# "total_length":279909545600,
# "average_quality":39,
# "average_length":151,
# "accession_number":"SAMEA13831494",
# run_accession
# exp_accession
# study_accession
# submission_date
# "sanger_id":"JaronRG14807346",
# "tag_sequence":"AGACACTA",
# "tag2_sequence":"GTTTCCTA",
# "run_qc_status":"qc complete",
# "npg_qc_status":"1",
# "date":"2024-08-09",
# "species":"Caenorhabditis elegans",
# "species_lims":"Caenorhabditis elegans",
# "pipeline_id_lims":"Hi-C - Arima v2",
# barcode


#     {"reads_MQ0":0,
#     "inward_oriented_pairs":0,
#     "tag_index":"8",
#     "library_id":"SQPP-57330-W:H2",
#     "reads_properly_paired":0,
#     "plot-2_hic":"jaron/nematodes/Caenorhabditis_elegans/genomic_data/nrCaeEleg1/hic-arima2/stats/49103_3-4#8/49103_3-4#8.hic.png",
#     "reads_QC_failed":0,

#     "plot-1_acgt-cycles":"jaron/nematodes/Caenorhabditis_elegans/genomic_data/nrCaeEleg1/hic-arima2/stats/49103_3-4#8/49103_3-4#8_F0xB00-acgt-cycles.png",
#     "plot-1_quals3":"jaron/nematodes/Caenorhabditis_elegans/genomic_data/nrCaeEleg1/hic-arima2/stats/49103_3-4#8/49103_3-4#8_F0xB00-quals3.png",
    

#     "similarty":null,
#     "plot-1_quals":"jaron/nematodes/Caenorhabditis_elegans/genomic_data/nrCaeEleg1/hic-arima2/stats/49103_3-4#8/49103_3-4#8_F0xB00-quals.png",
#     "insert_size_average":0,
#     "maximum_length":151,
#     "reads_duplicated":0,
#     "description":"",

    
#     "run_complete":"2024-07-02",
#     "outward_oriented_pairs":0,
#     "instrument":"NX2",
#     "study_name":"ToL_Jaron_ReferenceGenomes_DNA",
#     "species_name":"Caenorhabditis elegans",
#     "plot-1_quals-hm":"jaron/nematodes/Caenorhabditis_elegans/genomic_data/nrCaeEleg1/hic-arima2/stats/49103_3-4#8/49103_3-4#8_F0xB00-quals-hm.png",
#     "bases_duplicated":0,
#     "bases_mapped_cigar":0,

#     "insert_size_standard_deviation":0,

#     "position":"",




#     "raw_total_sequences":1853705600,

#     "id_run":"49103",

#     "plot-1_gc-content":"jaron/nematodes/Caenorhabditis_elegans/genomic_data/nrCaeEleg1/hic-arima2/stats/49103_3-4#8/49103_3-4#8_F0xB00-gc-content.png",
#     "1st_fragments":926852800,
#     "irods_path":"/seq/illumina/runs/49/49103/lane3-4/plex8",
#     "study_id":"7382",
#     "non_primary_alignments":0,
#     "supplier_name":"SAN20000995",
#     "mismatches":0,

#     "plot-1_quals2":"jaron/nematodes/Caenorhabditis_elegans/genomic_data/nrCaeEleg1/hic-arima2/stats/49103_3-4#8/49103_3-4#8_F0xB00-quals2.png",
#     "plot-2_fragment_separation":"jaron/nematodes/Caenorhabditis_elegans/genomic_data/nrCaeEleg1/hic-arima2/stats/49103_3-4#8/49103_3-4#8.fragment_separation.png",
#     "reads_unmapped":1853705600,
#     "reads_mapped":0,
#     "taxonomicidentification":"Caenorhabditis elegans",
#     "reads_mapped_and_paired":0,
#     "irods_file":"49103_3-4#8.cram",
#     "sequences":1853705600,

#     "biospecimen_accession":"SAMEA13831490",
#     "error_rate":0,
#     "is_sorted":true,

#     "pairs_on_different_chromosomes":0,
#     "bases_mapped":0,

#     "taxon_id":"6239",


#     "filtered_sequences":0,
#     "bases_trimmed":0,
#     "pairs_with_other_orientation":0,

#     "last_fragments":926852800
#     }





#     {"reads_MQ0":0,
#     "inward_oriented_pairs":0,
#     "tag_index":"8",
#     "library_id":"SQPP-57330-W:H2",
#     "reads_properly_paired":0,
#     "plot-2_hic":"jaron/nematodes/Caenorhabditis_elegans/genomic_data/nrCaeEleg1/hic-arima2/stats/49103_3-4#8/49103_3-4#8.hic.png",
#     "reads_QC_failed":0,
#     "reads_paired":1853705600,
#     "plot-1_acgt-cycles":"jaron/nematodes/Caenorhabditis_elegans/genomic_data/nrCaeEleg1/hic-arima2/stats/49103_3-4#8/49103_3-4#8_F0xB00-acgt-cycles.png",
#     "plot-1_quals3":"jaron/nematodes/Caenorhabditis_elegans/genomic_data/nrCaeEleg1/hic-arima2/stats/49103_3-4#8/49103_3-4#8_F0xB00-quals3.png",
#     "total_length":279909545600,
#     "pipeline_id_lims":"Hi-C - Arima v2",
#     "similarty":null,
#     "plot-1_quals":"jaron/nematodes/Caenorhabditis_elegans/genomic_data/nrCaeEleg1/hic-arima2/stats/49103_3-4#8/49103_3-4#8_F0xB00-quals.png",
#     "insert_size_average":0,
#     "maximum_length":151,
#     "reads_duplicated":0,
#     "description":"",
#     "sanger_id":"JaronRG14807346",
#     "npg_qc_status":"1",
#     "run_complete":"2024-07-02",
#     "outward_oriented_pairs":0,
#     "instrument":"NX2",
#     "study_name":"ToL_Jaron_ReferenceGenomes_DNA",
#     "species_name":"Caenorhabditis elegans",
#     "plot-1_quals-hm":"jaron/nematodes/Caenorhabditis_elegans/genomic_data/nrCaeEleg1/hic-arima2/stats/49103_3-4#8/49103_3-4#8_F0xB00-quals-hm.png",
#     "bases_duplicated":0,
#     "bases_mapped_cigar":0,
#     "average_length":151,
#     "insert_size_standard_deviation":0,
#     "run_qc_status":"qc complete",
#     "position":"",
#     "tag2_sequence":"GTTTCCTA",
#     "run":"49103_3-4#8",
#     "tag_sequence":"AGACACTA",
#     "platform":"Illumina",
#     "raw_total_sequences":1853705600,
#     "type":"hic-arima2",
#     "id_run":"49103",
#     "group":"jaron/nematodes",
#     "plot-1_gc-content":"jaron/nematodes/Caenorhabditis_elegans/genomic_data/nrCaeEleg1/hic-arima2/stats/49103_3-4#8/49103_3-4#8_F0xB00-gc-content.png",
#     "1st_fragments":926852800,
#     "irods_path":"/seq/illumina/runs/49/49103/lane3-4/plex8",
#     "study_id":"7382","non_primary_alignments":0,
#     "supplier_name":"SAN20000995","mismatches":0,
#     "average_quality":39,
#     "plot-1_quals2":"jaron/nematodes/Caenorhabditis_elegans/genomic_data/nrCaeEleg1/hic-arima2/stats/49103_3-4#8/49103_3-4#8_F0xB00-quals2.png",
#     "plot-2_fragment_separation":"jaron/nematodes/Caenorhabditis_elegans/genomic_data/nrCaeEleg1/hic-arima2/stats/49103_3-4#8/49103_3-4#8.fragment_separation.png",
#     "reads_unmapped":1853705600,
#     "reads_mapped":0,
#     "taxonomicidentification":"Caenorhabditis elegans",
#     "reads_mapped_and_paired":0,
#     "irods_file":"49103_3-4#8.cram",
#     "sequences":1853705600,
#     "species":"Caenorhabditis elegans",
#     "biospecimen_accession":"SAMEA13831490",
#     "error_rate":0,
#     "is_sorted":true,
#     "species_lims":"Caenorhabditis elegans",
#     "pairs_on_different_chromosomes":0,
#     "bases_mapped":0,
#     "model":"NovaSeqX",
#     "taxon_id":"6239",
#     "accession_number":"SAMEA13831494",
#     "date":"2024-08-09",
#     "filtered_sequences":0,
#     "bases_trimmed":0,
#     "pairs_with_other_orientation":0,
#     "specimen":"nrCaeEleg1",
#     "last_fragments":926852800
#     }



#     {"mean":13600.4705464709,
#     "plot-base_yield":["https://tolqc.cog.sanger.ac.uk/seq/pacbio/r64221e_20230519_150747/2_B01/reports/base_yield_plot.png","Base yield density"],
#     "plot-concordance":["https://tolqc.cog.sanger.ac.uk/seq/pacbio/r64221e_20230519_150747/2_B01/reports/concordance_plot.png","Control concordance"],
#     "pipeline_id_lims":"PacBio - HiFi",
#     "largest":49385,
#     "input":"jaron/nematodes/Caenorhabditis_elegans/genomic_data/nrCaeEleg2/pacbio/stats/m64221e_230520_201452.ccs.bc2003--bc2003.stats",
#     "boldstats":{
#         "taxon":"Caenorhabditis elegans","taxid":27260,
#         "tax_rank":"species",
#         "parentname":"Caenorhabditis",
#         "stats":{
#             "species":1,
#             "barcodespecies":1,
#             "barcodespecimens":21,
#             "publicbins":1,"publicrecords":22,
#             "sequencedspecimens":22,
#             "publicspecies":1,
#             "publicmarkersequences":{"COI-3P":1,"COI-5P":21},
#             "specimenrecords":22
#             },
#             "tax_division":"Animalia",
#             "parentid":27259
#             },
#     "plot-readlength":["https://tolqc.cog.sanger.ac.uk/seq/pacbio/r64221e_20230519_150747/2_B01/reports/readlength_plot.png","Control polymerase read length"],
#     "plot-m5c_detections":["https://tolqc.cog.sanger.ac.uk/seq/pacbio/r64221e_20230519_150747/2_B01/reports/m5c_detections.png","CpG methylation in reads"],
#     "plot-hexbin_length":["https://tolqc.cog.sanger.ac.uk/seq/pacbio/r64221e_20230519_150747/2_B01/reports/hexbin_length_plot.png","Insert read length density"],
#     "tag_index":"2003",
#     "c":17.9,
#     "plot-readLenDist0":["https://tolqc.cog.sanger.ac.uk/seq/pacbio/r64221e_20230519_150747/2_B01/reports/readLenDist0.png","Polymerase read length"],
#     "plot-ccs_hifi_read_length_yield":["https://tolqc.cog.sanger.ac.uk/seq/pacbio/r64221e_20230519_150747/2_B01/reports/ccs_hifi_read_length_yield_plot.png","HiFi yield by read length"],
#     "sum":23025215822,
#     "filtered_reads":7238,
#     "study_name":"959 Nematode Genomes",
#     "species_name":"Caenorhabditis elegans",
#     "barcode":"bc2003--bc2003",
#     "instrument":"m64221e",
#     "plot-ccs_npasses_hist":["https://tolqc.cog.sanger.ac.uk/seq/pacbio/r64221e_20230519_150747/2_B01/reports/ccs_npasses_hist.png","Number of passes"],
#     "sanger_id":"BlaxGeNe13447431",
#     "filtered":0.42753217418835,
#     "g":17.9,
#     "plot-raw_read_length":["https://tolqc.cog.sanger.ac.uk/seq/pacbio/r64221e_20230519_150747/2_B01/reports/raw_read_length_plot.png","Loading evaluation"],
#     "description":""
#     "match":[
#         {"specimen":{
#             "url":"http://www.boldsystems.org/index.php/Public_RecordView?processid=GBNM1564-13",
#             "collectionlocation":{"country":{},"coord":{"lon":{},"lat":{}}}
#             },
#         "taxonomicidentification":"Caenorhabditis elegans",
#         "similarity":"1",
#         "ID":"GBNM1564-13",
#         "sequencedescription":"COI-5P",
#         "database":"BOLD: Public Records","citation":"BOLD Systems, 2024"
#         }],
#     "plot-m5c_detections_hist":["https://tolqc.cog.sanger.ac.uk/seq/pacbio/r64221e_20230519_150747/2_B01/reports/m5c_detections_hist.png","CpG methylation in reads histogram"],
#     "a":32.1,
#     "L100":1692972,
#     "L60":673531,
#     "n":1692972,
#     "dups":0,
#     "supplier_name":"PD1074",
#     "well_label":"B01",
#     "L50":530778,
#     "study_id":"6137",
#     "smallest":100,
#     "movie":"m64221e_230520_201452",
#     "pipeline":"PacBio - HiFi",
#     "group":"jaron/nematodes",
#     "plot-readlength_qv_hist2d.hexbin":["https://tolqc.cog.sanger.ac.uk/seq/pacbio/r64221e_20230519_150747/2_B01/reports/readlength_qv_hist2d.hexbin.png","Accuracy versus read length density"],
#     "N70":13336,
#     "N80":10946,
#     "type":"pacbio",
#     "run":"TRACTION-RUN-598",
#     "L90":1269196,
#     "tag_sequence":"ACGAGTGCTCGAGTAT",
#     "platform":"PacBio",
#     "plot-ccs_accuracy_hist":["https://tolqc.cog.sanger.ac.uk/seq/pacbio/r64221e_20230519_150747/2_B01/reports/ccs_accuracy_hist.png","Read quality distribution"],
#     "plot-ccs_all_readlength_hist":["https://tolqc.cog.sanger.ac.uk/seq/pacbio/r64221e_20230519_150747/2_B01/reports/ccs_all_readlength_hist_plot.png","Read length distribution (all)"],
#     "specimen":"nrCaeEleg2",
#     "N100":100,
#     "N60":15280,
#     "bases_a":7391948405,
#     "accession_number":"SAMEA13831494",
#     "taxon_id":"6239","date":"2023-05-20",
#     "bases_t":7394194740,
#     "bases_g":4116364115,
#     "t":32.1,
#     "N50":16993,
#     "boldcheck":{
#         "to":"6033",
#         "nucleotides":"GGTGGTTTTGGTAACTGATTATTACCACTTATGTTAGGAGCACCTGATATAAGATTTCCACGTTTAAATAATTTAAGATTTTGGTTATTACCTACATCTATATTATTAATTTTAGATGCTTGTTTTGTAGATATAGGTTGTGGGACTAGGTGAACAGTCTACCCACCTTTAAGAACAATGGGGCACCCTGGAAGTAGAGTAGATTTAGCTATTTTTAGTTTACATGCAGCAGGGTTAAGATCTATCTTAGGTGGTATTAATTTTATGTGTACTACTAAAAATTTACGTAGAAGTTCTATTTCATTAGAACATATAACTTTATTTGTTTGAACTGTGTTTGTAACAGTGTTTTTACTGGTTTTATCTCTACCGGTTTTAGCAGGGGCTATTACTATGTTGTTAACTGATCGTAATTTAAATACTTCATTTTTTGATCCAAGAACTGGAGGTAATCCTCTTATTTATCAACATTTGTTTTGATTTTTTGGTCATCCTGAAGTATATATTTTGATTTTACCAGCTTTTGGTATTGTCAGACAATCTACACTTTATTTAACAGGAAAAAAAGAAGTTTTTGGTGCTTTGGGTATAGTTTATGCAATTTTAAGAATTGGTTTAATTGGTTGTGTAGTATGAGCTCACCATATGTATACAGTAGGTATAGATTTGGATTCACGTGCTTATTTT",
#         "from":"5347",
#         "readname":"m64221e_230520_201452/10158278/ccs",
#         "strand":"+"},
#     "model":"Sequel IIe",
#     "bases_c":4122708562,
#     "plot-ccs_readlength_hist":["https://tolqc.cog.sanger.ac.uk/seq/pacbio/r64221e_20230519_150747/2_B01/reports/ccs_readlength_hist_plot.png","HiFi read length distribution"],
#     "species_lims":"Caenorhabditis elegans",
#     "L70":834406,
#     "rundir":"/seq/pacbio/r64221e_20230519_150747/2_B01",
#     "species":"Caenorhabditis elegans",
#     "dup_reads":0,
#     "plot-interAdapterDist0":["https://tolqc.cog.sanger.ac.uk/seq/pacbio/r64221e_20230519_150747/2_B01/reports/interAdapterDist0.png","Adapter distribution"],
#     "biospecimen_accession":"SAMEA13831490",
#     "L80":1023934,
#     "N90":7844,
#     "irods_file":"demultiplex.bc2003--bc2003.bam",
#     "library_load_name":""
#     }