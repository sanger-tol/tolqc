# SPDX-FileCopyrightText: 2026 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from tolqc.schema import Role, RoleBinding, Token, User
from tolqc.schema.accession_models import (
    Accession,
    AccessionTypeDict,
    BioprojectLink,
    LinkStatusDict,
    SubmitterDict,
)
from tolqc.schema.assembly_models import (
    Assembly,
    AssemblyDataset,
    AssemblyLevelDict,
    AssemblyStatus,
    AssemblyStatusType,
    Dataset,
    DatasetElement,
    DatasetStatus,
    DatasetStatusType,
)
from tolqc.schema.folder_models import Folder, FolderLocation
from tolqc.schema.sample_data_models import (
    Allocation,
    CategoryDict,
    Centre,
    ChemistryDict,
    Data,
    File,
    FileTypeDict,
    Library,
    LibraryType,
    Location,
    PacbioRunMetrics,
    Platform,
    Project,
    QCDict,
    Run,
    Sample,
    Sex,
    Species,
    Specimen,
    Study,
    VisibilityDict,
)
from tolqc.schema.system_models import Metadata


def test_data(token: str):
    return [
        User(id=100, name='tester', email='tester@sanger.ac.uk'),
        Token(token=token, user_id=100, id=200),
        Role(id=300, name='editor'),
        RoleBinding(user_id=100, role_id=300),
        Metadata(name='location.root', string_value='/test/loc_root'),
        Project(project_id='aegis'),
        Project(project_id='britain-and-ireland'),
        Project(project_id='darwin'),
        Project(project_id='protist-microalgae'),
        Project(project_id='tol'),
        Project(project_id='vgp'),
        AccessionTypeDict(
            accession_type_id='GenBank Genome Assembly',
            regexp='^GCA_\\d+\\.\\d+$',
            url='https://www.ncbi.nlm.nih.gov/datasets/genome/{}/',  # noqa: P103
        ),
        AccessionTypeDict(
            accession_type_id='BioProject',
            regexp='^PRJ[A-Z]{2}\\d+$',
            url='https://www.ebi.ac.uk/ena/browser/view/{}',  # noqa: P103
        ),
        AccessionTypeDict(
            accession_type_id='BioSample',
            regexp='^SAM[A-Z]{2}\\d+$',
            url='https://www.ebi.ac.uk/biosamples/samples/{}',  # noqa: P103
        ),
        AccessionTypeDict(
            accession_type_id='Analysis',
            regexp='^ERZ\\d+$',
            url='https://www.ebi.ac.uk/ena/browser/view/{}',  # noqa: P103
        ),
        AccessionTypeDict(
            accession_type_id='Experiment',
            regexp='^[ES]RX\\d+$',
            url='https://www.ebi.ac.uk/ena/browser/view/{}',  # noqa: P103
        ),
        AccessionTypeDict(
            accession_type_id='Run',
            regexp='^[ES]RR\\d+$',
            url='https://www.ebi.ac.uk/ena/browser/view/{}',  # noqa: P103
        ),
        AccessionTypeDict(
            accession_type_id='RefSeq Genome Assembly',
            regexp='^GCF_\\d+\\.\\d+$',
            url='https://www.ncbi.nlm.nih.gov/datasets/genome/{}/',  # noqa: P103
        ),
        AccessionTypeDict(
            accession_type_id='ToLID',
            regexp='^[a-z]{1,2}[A-Z][a-z]{2}[A-Z][a-z]{2,3}\\d+$',
            url='https://id.tol.sanger.ac.uk/api/v2/tol-ids/{}',  # noqa: P103
        ),
        AccessionTypeDict(accession_type_id='Placeholder', regexp='^(Request|Pending)$'),
        AccessionTypeDict(
            accession_type_id='BioSpecimen',
            regexp='^SAM[A-Z]{2}\\d+$',
            url='https://www.ebi.ac.uk/biosamples/samples/{}',  # noqa: P103
        ),
        AccessionTypeDict(
            accession_type_id='BioProject - Species Data',
            regexp='^PRJ[A-Z]{2}\\d+$',
            url='https://www.ebi.ac.uk/ena/browser/view/{}',  # noqa: P103
        ),
        AccessionTypeDict(
            accession_type_id='BioProject - Species Umbrella',
            regexp='^PRJ[A-Z]{2}\\d+$',
            url='https://www.ebi.ac.uk/ena/browser/view/{}',  # noqa: P103
        ),
        AccessionTypeDict(
            accession_type_id='BioProject - Project Umbrella',
            regexp='^PRJ[A-Z]{2}\\d+$',
            url='https://www.ebi.ac.uk/ena/browser/view/{}',  # noqa: P103
        ),
        AccessionTypeDict(
            accession_type_id='Sample',
            regexp='^[ES]RS\\d+$',
            url='https://www.ebi.ac.uk/ena/browser/view/{}',  # noqa: P103
        ),
        AccessionTypeDict(
            accession_type_id='BioProject - Species Assembly',
            regexp='^PRJ[A-Z]{2}\\d+$',
            url='https://www.ebi.ac.uk/ena/browser/view/{}',  # noqa: P103
        ),
        AccessionTypeDict(
            accession_type_id='BioProject - Species Organelle Assembly',
            regexp='^PRJ[A-Z]{2}\\d+$',
            url='https://www.ebi.ac.uk/ena/browser/view/{}',  # noqa: P103
        ),
        AccessionTypeDict(
            accession_type_id='BioProject - Eukaryotic Cobiont Assembly',
            regexp='^PRJ[A-Z]{2}\\d+$',
            url='https://www.ebi.ac.uk/ena/browser/view/{}',  # noqa: P103
        ),
        AccessionTypeDict(
            accession_type_id='BioProject - Metagenome Assembly',
            regexp='^PRJ[A-Z]{2}\\d+$',
            url='https://www.ebi.ac.uk/ena/browser/view/{}',  # noqa: P103
        ),
        AccessionTypeDict(
            accession_type_id='BioProject - Prokaryotic Cobiont Assembly',
            regexp='^PRJ[A-Z]{2}\\d+$',
            url='https://www.ebi.ac.uk/ena/browser/view/{}',  # noqa: P103
        ),
        AssemblyLevelDict(
            level='contig', description='A list of contiguous nucleotide sequences'
        ),
        AssemblyLevelDict(
            level='scaffold',
            description='Scaffolds of ordered and oriented contigs separated by gaps',
        ),
        AssemblyLevelDict(
            level='chromosome', description='Contains scaffolds representing chromosomes'
        ),
        AssemblyLevelDict(
            level='complete genome',
            description=(
                'A whole prokaryote or plastid genome, or a telomere-to-telomere quality'
                ' chromosomal genome'
            ),
        ),
        AssemblyStatusType(
            status_type_id='Pending',
            description='New entry waiting to be assembled',
            assign_order=10,
        ),
        AssemblyStatusType(
            status_type_id='Hifiasm Complete',
            description='Hifiasm assembly has finished',
            assign_order=20,
        ),
        AssemblyStatusType(
            status_type_id='YaHS Complete',
            description='YaHS assembly scaffolding has finished',
            assign_order=30,
        ),
        AssemblyStatusType(
            status_type_id='Good Metrics',
            description='The metrics of the assembly have passed',
            assign_order=40,
        ),
        AssemblyStatusType(
            status_type_id='BUSCO Pass',
            description='BUSCO genes assembly completeness check has passed',
            assign_order=50,
        ),
        AssemblyStatusType(
            status_type_id='ENA Public',
            description='Assembly is public with a GCA accession at the ENA',
            assign_order=70,
        ),
        AssemblyStatusType(
            status_type_id='Submitted',
            description='Assembly has been passed to the Sanger data release team',
            assign_order=60,
        ),
        CategoryDict(category='transcriptomic_data'),
        CategoryDict(category='genomic_data'),
        CategoryDict(category='resequencing_data'),
        Centre(id=2, name='Wellcome Sanger Institute'),
        Centre(id=3, name='Baylor College of Medicine'),
        Centre(id=4, name='Pacific Biosciences'),
        Centre(id=5, name='Arima Genomics'),
        Centre(id=6, name='University of Cambridge'),
        ChemistryDict(chemistry='R/P1-C1/5.0-25M'),
        ChemistryDict(chemistry='R/P2-C2/5.0-25M'),
        ChemistryDict(chemistry='S/P2-C2/5.0'),
        ChemistryDict(chemistry='S/P3-C1/5.0-8M'),
        ChemistryDict(chemistry='S/P3-C3/5.0'),
        ChemistryDict(chemistry='S/P4.1-C2/5.0-8M'),
        ChemistryDict(chemistry='S/P4-C2/5.0-8M'),
        ChemistryDict(chemistry='S/P5-C2/5.0-8M'),
        DatasetStatusType(
            status_type_id='Pending', description='New dataset awaiting QC', assign_order=10
        ),
        DatasetStatusType(
            status_type_id='GenomeScope Pass',
            description='Has passed GenomeScope QC checks',
            assign_order=20,
        ),
        DatasetStatusType(
            status_type_id='Barcode Check Pass',
            description='Matches species in barcode database',
            assign_order=30,
        ),
        DatasetStatusType(
            status_type_id='QC Pass', description='Cleared for assembly', assign_order=40
        ),
        DatasetStatusType(
            status_type_id='Failed', description='Not suitable for assembly', assign_order=50
        ),
        FileTypeDict(file_type='BAM', description='Binary Alignment Map'),
        FileTypeDict(file_type='CRAM', description='Compressed Reference-oriented Alignment Map'),
        FileTypeDict(file_type='BNX', description='BioNano BNX'),
        FileTypeDict(file_type='CMAP', description='BioNano CMAP'),
        FileTypeDict(
            file_type='RAW_FAST5_TAR_DIR',
            description=(
                'Early ONT data. A directory of TAR archives containing FAST5 format raw ONT data'
            ),
        ),
        FileTypeDict(
            file_type='RAW_FASTQ_DIR',
            description='Directory of raw ONT data in (gzipped) FASTQ format',
        ),
        FileTypeDict(
            file_type='RAW_BAM_DIR', description='Directory of raw ONT data in BAM format'
        ),
        FileTypeDict(
            file_type='RECALL_FASTQ_DIR',
            description='Directory of re-basecalled ONT data in (gzipped) FASTQ format',
        ),
        FileTypeDict(
            file_type='RAW_FAST5_DIR', description='Directory of raw ONT data in FAST5 format'
        ),
        FileTypeDict(
            file_type='RAW_POD5_DIR', description='Directory of raw ONT data in POD5 format'
        ),
        FileTypeDict(
            file_type='PACBIO_TRIMMED_FASTA',
            description='PacBio data in (gzipped) FASTA format processed for input into assembly',
        ),
        FileTypeDict(file_type='RECALL_BAM', description='BAM file of re-basecalled ONT data'),
        FolderLocation(
            folder_location_id='smudgeplot_s3',
            uri_prefix='s3://tolqc-dev/smudgeplot',
            http_prefix='https://tolqc-dev.cog.sanger.ac.uk/smudgeplot',
            files_template={
                'image_file_patterns': [
                    {
                        'index': 0,
                        'caption': 'Smudgeplot plot',
                        'pattern': '.*_smudgeplot_smudgeplot\\.png',
                    },
                    {
                        'index': 1,
                        'caption': 'Smudgeplot log plot',
                        'pattern': '.*_smudgeplot_smudgeplot_log10\\.png',
                    },
                    {
                        'index': 2,
                        'caption': 'Smudgeplot centralities',
                        'pattern': '.*_smudgeplot_centralities\\.png',
                    },
                ]
            },
        ),
        FolderLocation(
            folder_location_id='genomescope_s3',
            uri_prefix='s3://tolqc-dev/genomescope',
            http_prefix='https://tolqc-dev.cog.sanger.ac.uk/genomescope',
            files_template={
                'image_file_patterns': [
                    {
                        'index': 2,
                        'caption': 'Genomescope 2.0 transformed linear plot',
                        'pattern': '.*_genomescope_transformed_linear_plot\\.png',
                    },
                    {
                        'index': 0,
                        'caption': 'Genomescope 2.0 linear plot',
                        'pattern': '.*_genomescope_linear_plot\\.png',
                    },
                    {
                        'index': 3,
                        'caption': 'Genomescope 2.0 transformed log plot',
                        'pattern': '.*_genomescope_transformed_log_plot\\.png',
                    },
                    {
                        'index': 1,
                        'caption': 'Genomescope 2.0 log plot',
                        'pattern': '.*_genomescope_log_plot\\.png',
                    },
                ],
                'other_file_patterns': [
                    {'caption': 'Kmer counts histogram data', 'pattern': '.*\\.hist\\.txt'}
                ],
            },
        ),
        FolderLocation(
            folder_location_id='illumina_data_s3',
            uri_prefix='s3://tolqc-dev/illumina_data',
            http_prefix='https://tolqc-dev.cog.sanger.ac.uk/illumina_data',
            files_template={
                'image_file_patterns': [
                    {
                        'caption': '{library_type} G|C Content',
                        'pattern': '.+_F0xB00-gc-content\\.png',
                    },
                    {
                        'caption': '{library_type} A|C|G|T Content Per Cycle',
                        'pattern': '.+_F0xB00-acgt-cycles\\.png',
                    },
                    {
                        'caption': '{library_type} Quality Per Cycle (Overlaid)',
                        'pattern': '.+_F0xB00-quals\\.png',
                    },
                    {
                        'caption': '{library_type} Quality Per Cycle (Split)',
                        'pattern': '.+_F0xB00-quals2\\.png',
                    },
                    {
                        'caption': '{library_type} Quality Frequencies, Per Cycle Heat Map',
                        'pattern': '.+_F0xB00-quals-hm\\.png',
                    },
                    {
                        'caption': '{library_type} Quality Frequencies, Separate Curve Per Cycle',
                        'pattern': '.+_F0xB00-quals3\\.png',
                    },
                ]
            },
        ),
        FolderLocation(
            folder_location_id='pacbio_run_s3',
            uri_prefix='s3://tolqc-dev/pacbio_run',
            http_prefix='https://tolqc-dev.cog.sanger.ac.uk/pacbio_run',
            files_template={
                'image_file_patterns': [
                    {'caption': 'Base yield density', 'pattern': 'base_yield_plot\\.png'},
                    {'caption': 'Barcode quality distribution', 'pattern': 'bq_histogram\\.png'},
                    {
                        'caption': 'Read quality distribution',
                        'pattern': 'ccs_accuracy_hist\\.png',
                    },
                    {
                        'caption': 'Read length distribution (all)',
                        'pattern': 'ccs_all_readlength_hist_plot\\.png',
                    },
                    {
                        'caption': 'HiFi yield by read length',
                        'pattern': 'ccs_hifi_read_length_yield_plot\\.png',
                    },
                    {'caption': 'Number of passes', 'pattern': 'ccs_npasses_hist\\.png'},
                    {
                        'caption': 'HiFi read length distribution',
                        'pattern': 'ccs_readlength_hist_plot\\.png',
                    },
                    {'caption': 'Control concordance', 'pattern': 'concordance_plot\\.png'},
                    {
                        'caption': 'Insert read length density',
                        'pattern': 'hexbin_length_plot\\.png',
                    },
                    {'caption': 'CpG methylation in reads', 'pattern': 'm5c_detections\\.png'},
                    {
                        'caption': 'CpG methylation in reads histogram',
                        'pattern': 'm5c_detections_hist\\.png',
                    },
                    {'caption': 'Number of reads per barcode', 'pattern': 'nreads\\.png'},
                    {
                        'caption': 'Number of reads per barcode histogram',
                        'pattern': 'nreads_histogram\\.png',
                    },
                    {'caption': 'Loading evaluation', 'pattern': 'raw_read_length_plot\\.png'},
                    {'caption': 'Polymerase read length', 'pattern': 'readLenDist0\\.png'},
                    {
                        'caption': 'Control polymerase read length',
                        'pattern': 'readlength_plot\\.png',
                    },
                    {
                        'caption': 'Mean readlength histogram',
                        'pattern': 'readlength_histogram\\.png',
                    },
                    {
                        'caption': 'Accuracy versus read length density',
                        'pattern': 'readlength_qv_hist2d\\.hexbin\\.png',
                    },
                ]
            },
        ),
        LibraryType(
            library_type_id='Chromium genome',
            hierarchy_name='10x',
            default_category='genomic_data',
            is_pcr=False,
        ),
        LibraryType(
            library_type_id='Haplotagging',
            hierarchy_name='htag',
            default_category='genomic_data',
            is_pcr=False,
        ),
        LibraryType(
            library_type_id='HiSeqX PCR free',
            hierarchy_name='illumina',
            default_category='genomic_data',
            is_pcr=False,
        ),
        LibraryType(
            library_type_id='PacBio - IsoSeq',
            hierarchy_name='pacbio',
            default_category='transcriptomic_data',
            is_pcr=False,
        ),
        LibraryType(
            library_type_id='Standard',
            hierarchy_name='illumina',
            default_category='genomic_data',
            is_pcr=False,
        ),
        LibraryType(library_type_id='Custom', is_pcr=False),
        LibraryType(library_type_id='qPCR only', is_pcr=False),
        LibraryType(library_type_id='Pre-quality controlled', is_pcr=False),
        LibraryType(library_type_id='Manual Standard WGS (Plate)', is_pcr=False),
        LibraryType(library_type_id='Nextera dual index pre quality controlled', is_pcr=False),
        LibraryType(
            library_type_id='RNA PolyA',
            hierarchy_name='rna-seq',
            default_category='transcriptomic_data',
            reporting_category='rnaseq',
            is_pcr=False,
        ),
        LibraryType(
            library_type_id='RNA-seq dUTP eukaryotic',
            hierarchy_name='rna-seq',
            default_category='transcriptomic_data',
            reporting_category='rnaseq',
            is_pcr=False,
        ),
        LibraryType(
            library_type_id='RNA-seq dUTP prokaryotic',
            hierarchy_name='rna-seq',
            default_category='transcriptomic_data',
            reporting_category='rnaseq',
            is_pcr=False,
        ),
        LibraryType(
            library_type_id='Small RNA (miRNA)',
            hierarchy_name='rna-seq',
            default_category='transcriptomic_data',
            reporting_category='rnaseq',
            is_pcr=False,
        ),
        LibraryType(
            library_type_id='PacBio - HiFi',
            hierarchy_name='pacbio',
            default_category='genomic_data',
            reporting_category='pacbio',
            is_pcr=False,
        ),
        LibraryType(
            library_type_id='PacBio - HiFi (Microbial)',
            hierarchy_name='pacbio',
            default_category='genomic_data',
            reporting_category='pacbio',
            is_pcr=False,
        ),
        LibraryType(
            library_type_id='Hi-C',
            hierarchy_name='hic',
            default_category='genomic_data',
            reporting_category='hic',
            is_pcr=False,
        ),
        LibraryType(
            library_type_id='ATAC-seq',
            hierarchy_name='atac-seq',
            default_category='genomic_data',
            is_pcr=False,
        ),
        LibraryType(
            library_type_id='Hi-C - Arima v1',
            hierarchy_name='hic-arima',
            default_category='genomic_data',
            reporting_category='hic',
            kit='Arima v1',
            enzymes='HinfI,DpnII',
            cut_sites='^GATC,G^ANTC',
            is_pcr=False,
        ),
        LibraryType(
            library_type_id='Hi-C - Arima v2',
            hierarchy_name='hic-arima2',
            default_category='genomic_data',
            reporting_category='hic',
            kit='Arima v2',
            enzymes='HinfI,DpnII,DdeI,MseI',
            cut_sites='^GATC,G^ANTC,C^TNAG,T^TAA',
            is_pcr=False,
        ),
        LibraryType(
            library_type_id='Hi-C - Dovetail',
            hierarchy_name='hic-dovetail',
            default_category='genomic_data',
            reporting_category='hic',
            kit='Dovetail - Hi-C',
            enzymes='DpnII',
            cut_sites='^GATC',
            is_pcr=False,
        ),
        LibraryType(
            library_type_id='Hi-C - Qiagen',
            hierarchy_name='hic-qiagen',
            default_category='genomic_data',
            reporting_category='hic',
            kit='Qiagen',
            enzymes='DpnII',
            cut_sites='^GATC',
            is_pcr=False,
        ),
        LibraryType(
            library_type_id='Hi-C - DNAzoo (Csp6I,MseI)',
            hierarchy_name='hic-dnazoo',
            default_category='genomic_data',
            reporting_category='hic',
            kit='DNAzoo',
            enzymes='Csp6I,MseI',
            cut_sites='G^TAC,T^TAA',
            is_pcr=False,
        ),
        LibraryType(
            library_type_id='Hi-C - DNAzoo (MboI,MseI)',
            hierarchy_name='hic-dnazoo',
            default_category='genomic_data',
            reporting_category='hic',
            kit='DNAzoo',
            enzymes='MboI,MseI',
            cut_sites='^GATC,T^TAA',
            is_pcr=False,
        ),
        LibraryType(
            library_type_id='BioNano - DLE1',
            hierarchy_name='bionano',
            default_category='genomic_data',
            reporting_category='bionano',
            enzymes='DLE1',
            is_pcr=False,
        ),
        LibraryType(
            library_type_id='BioNano - BssSI',
            hierarchy_name='bionano',
            default_category='genomic_data',
            reporting_category='bionano',
            enzymes='BssSI',
            is_pcr=False,
        ),
        LibraryType(
            library_type_id='BioNano - BspQI',
            hierarchy_name='bionano',
            default_category='genomic_data',
            reporting_category='bionano',
            enzymes='BspQI',
            is_pcr=False,
        ),
        LibraryType(
            library_type_id='Hi-C - Phase',
            hierarchy_name='hic-phase',
            default_category='genomic_data',
            reporting_category='hic',
            kit='Phase',
            is_pcr=False,
        ),
        LibraryType(
            library_type_id='Hi-C - Homebrew',
            hierarchy_name='hic-homebrew',
            default_category='genomic_data',
            reporting_category='hic',
            is_pcr=False,
        ),
        LibraryType(
            library_type_id='No PCR (Plate)',
            hierarchy_name='illumina',
            default_category='genomic_data',
            is_pcr=False,
        ),
        LibraryType(
            library_type_id='Long range',
            hierarchy_name='illumina',
            default_category='genomic_data',
            is_pcr=False,
        ),
        LibraryType(library_type_id='RNA Ribo', hierarchy_name='rna-seq', is_pcr=False),
        LibraryType(library_type_id='PacBio - CLR', hierarchy_name='pacbio', is_pcr=False),
        LibraryType(
            library_type_id='Hi-C - OmniC',
            hierarchy_name='hic-omnic',
            default_category='genomic_data',
            reporting_category='hic',
            kit='Dovetail - Omni-C',
            is_pcr=False,
        ),
        LibraryType(
            library_type_id='Haplotagging (202103)',
            hierarchy_name='htag-202103',
            default_category='genomic_data',
            is_pcr=False,
        ),
        LibraryType(
            library_type_id='Haplotagging (202106)',
            hierarchy_name='htag-202106',
            default_category='genomic_data',
            is_pcr=False,
        ),
        LibraryType(
            library_type_id='Haplotagging (202110)',
            hierarchy_name='htag-202110',
            default_category='genomic_data',
            is_pcr=False,
        ),
        LibraryType(
            library_type_id='Haplotagging (202203)',
            hierarchy_name='htag-202203',
            default_category='genomic_data',
            is_pcr=False,
        ),
        LibraryType(
            library_type_id='Haplotagging (Sanger libraries)',
            hierarchy_name='htag-sanger',
            default_category='genomic_data',
            is_pcr=False,
        ),
        LibraryType(library_type_id='Rapid', is_pcr=False),
        LibraryType(
            library_type_id='Haplotagging (Marek libraries)',
            hierarchy_name='htag-marek',
            default_category='genomic_data',
            is_pcr=False,
        ),
        LibraryType(
            library_type_id='Chicago - Dovetail',
            hierarchy_name='chicago-dovetail',
            default_category='genomic_data',
            kit='Dovetail',
            is_pcr=False,
        ),
        LibraryType(
            library_type_id='Haplotagging (202108)',
            hierarchy_name='htag-202108',
            default_category='genomic_data',
            is_pcr=False,
        ),
        LibraryType(
            library_type_id='PacBio - IsoSeq (Kinnex)',
            hierarchy_name='pacbio',
            default_category='transcriptomic_data',
            is_pcr=False,
        ),
        LibraryType(library_type_id='Ligation', is_pcr=False),
        LibraryType(
            library_type_id='ONT_GridIon',
            hierarchy_name='ont',
            default_category='genomic_data',
            reporting_category='ont',
            is_pcr=False,
        ),
        LibraryType(
            library_type_id='ONT_PromethIon',
            hierarchy_name='ont',
            default_category='genomic_data',
            reporting_category='ont',
            is_pcr=False,
        ),
        LibraryType(
            library_type_id='ONT_PromethIon_mplx',
            hierarchy_name='ont',
            default_category='genomic_data',
            reporting_category='ont',
            is_pcr=False,
        ),
        LibraryType(
            library_type_id='ONT_Ultralong',
            hierarchy_name='ont',
            default_category='genomic_data',
            reporting_category='ont',
            is_pcr=False,
        ),
        LibraryType(
            library_type_id='PacBio - HiFi (Amplicon)',
            hierarchy_name='pacbio',
            default_category='genomic_data',
            reporting_category='pacbio',
            is_pcr=False,
        ),
        LibraryType(library_type_id='LCMB', is_pcr=False),
        LibraryType(
            library_type_id='PacBio - HiFi (ULI)',
            hierarchy_name='pacbio',
            default_category='genomic_data',
            reporting_category='pacbio',
            is_pcr=True,
        ),
        LibraryType(
            library_type_id='PacBio - HiFi (PiMmS)',
            hierarchy_name='pacbio',
            default_category='genomic_data',
            reporting_category='pacbio',
            is_pcr=True,
        ),
        LibraryType(
            library_type_id='PacBio - HiFi (Ampli-Fi)',
            hierarchy_name='pacbio',
            default_category='genomic_data',
            reporting_category='pacbio',
            is_pcr=True,
        ),
        LinkStatusDict(link_status='New', description='BioProject link newly created'),
        LinkStatusDict(
            link_status='Verified', description='BioProject link verified to exist at ENA'
        ),
        LinkStatusDict(link_status='Suppressed', description='BioProject link suppressed at ENA'),
        LinkStatusDict(
            link_status='Suppression Requested',
            description='BioProject link has been requested to be suppressed',
        ),
        Platform(id=1, name='Illumina', model='HiSeq'),
        Platform(id=2, name='Illumina', model='HiSeqX'),
        Platform(id=4, name='Illumina', model='HiSeq 4000'),
        Platform(id=5, name='Illumina', model='NovaSeq'),
        Platform(id=6, name='PacBio', model='Revio'),
        Platform(id=7, name='Illumina', model='MiSeq'),
        Platform(id=3, name='PacBio', model='Sequel IIe'),
        Platform(id=8, name='Illumina', model='NovaSeqX'),
        Platform(id=12, name='PacBio', model='Sequel'),
        Platform(id=13, name='PacBio', model='RSII'),
        Platform(id=14, name='PacBio', model='Sequel II'),
        Platform(id=15, name='Illumina'),
        Platform(id=16, name='Illumina', model='HiSeq 2500'),
        Platform(id=17, name='Illumina', model='NovaSeq 6000'),
        Platform(id=18, name='Illumina', model='HiSeq 2000'),
        Platform(id=19, name='Illumina', model='NextSeq 500'),
        Platform(id=20, name='BioNano', model='Saphyr'),
        Platform(id=21, name='BioNano', model='Irys'),
        Platform(id=22, name='ONT', model='gridion'),
        Platform(id=23, name='ONT', model='promethion'),
        QCDict(qc_state='pass'),
        QCDict(qc_state='fail'),
        Sex(sex_id='Male'),
        Sex(sex_id='Female'),
        Sex(sex_id='Male (uncertain)'),
        Sex(sex_id='Female (uncertain)'),
        Sex(sex_id='Hermaphrodite'),
        Sex(sex_id='Hermaphrodite, monoecious'),
        Sex(sex_id='Not applicable'),
        Sex(sex_id='Unknown'),
        Sex(sex_id='Asexual morph'),
        Sex(sex_id='Sexual morph'),
        Sex(sex_id='Not collected'),
        Sex(sex_id='Not provided'),
        SubmitterDict(
            submitter_id='Wellcome Sanger Institute',
            webin_account='Webin-2',
            description='Sanger Data Release Team account',
        ),
        SubmitterDict(
            submitter_id='WELLCOME SANGER INSTITUTE',
            webin_account='Webin-57671',
            description='ToL-Datahose account used for submitting data, assemblies and projects',
        ),
        SubmitterDict(
            submitter_id='Tree of Life Programme',
            webin_account='Webin-58409',
            description='ToL Platforms account for registering Biosamples',
        ),
        SubmitterDict(submitter_id='Bat1K', description='Bat1K Project'),
        SubmitterDict(
            submitter_id='Baylor College of Medicine', description='Baylor College of Medicine'
        ),
        SubmitterDict(submitter_id='Earlham Institute', description='Earlham Institute'),
        SubmitterDict(submitter_id='EBP', description='Earth Biogenome Project'),
        SubmitterDict(
            submitter_id='european reference genome atlas',
            description='European Reference Genome Atlas',
        ),
        SubmitterDict(submitter_id='Genome 10K', description='Genome 10K Project'),
        SubmitterDict(
            submitter_id='NOAA Southwest Fisheries Science Center',
            description='NOAA Southwest Fisheries Science Center',
        ),
        SubmitterDict(submitter_id='SC', description='Sanger Centre'),
        SubmitterDict(submitter_id='University of Bari', description='University of Bari'),
        SubmitterDict(
            submitter_id='University of Florence', description='University of Florence'
        ),
        SubmitterDict(
            submitter_id='Wellcome Trust Sanger Institute',
            description='Wellcome Trust Sanger Institute',
        ),
        SubmitterDict(
            submitter_id='University of Cambridge, UK', description='University of Cambridge, UK'
        ),
        SubmitterDict(submitter_id='B10K', description='Bird 10K Project'),
        VisibilityDict(visibility='Always', description='Shown in standard reporting'),
        VisibilityDict(visibility='Testing', description='Sequencing development data'),
        VisibilityDict(visibility='Withdrawn', description='Data has been deleted'),
        VisibilityDict(visibility='MetadataIssue', description='Metadata has issues'),
        VisibilityDict(
            visibility='SampleSwap', description='Data involved in a possible sample swap'
        ),
        VisibilityDict(visibility='Fail', description='Failed - do not import'),
        VisibilityDict(visibility='Legacy', description='Legacy data - do not display'),
        VisibilityDict(
            visibility='Reseq', description='Re-sequencing or Population-genetics data'
        ),
        VisibilityDict(
            visibility='Kinnex',
            description='Pooled Kinnex data that will be deplexed to other records',
        ),
        Study(study_id=5822, name='DTOL_Darwin R&D', auto_sync=True),
        Study(study_id=5901, name='DTOL_Darwin Tree of Life', auto_sync=True),
        Study(study_id=6327, name='DTOL_Darwin Tree of Life RNA', auto_sync=True),
        Species(
            species_id='Brachiomonas submarina',
            location_id=3113,
            tolid_prefix='ucBraSubm',
            taxon_id=327064,
            family_taxon_id=3051,
            taxon_family='Chlamydomonadaceae',
            taxon_order='Chlamydomonadales',
            taxon_phylum='Chlorophyta',
            taxon_group='algae',
            genome_size=293400000,
            chromosome_number=16,
            specimens=[
                Specimen(
                    specimen_id='ucBraSubm2',
                    location_id=3113,
                    species_id='Brachiomonas submarina',
                    epithet='var. pulsifera',
                    taxon_id=327065,
                    supplied_name='SAN0000889',
                    sts_specimen='SAN0000889',
                    accession_id='SAMEA7532740',
                    sex_id='Not collected',
                    ploidy='2',
                    samples=[
                        Sample(
                            sample_id='DTOL9310949',
                            specimen_id='ucBraSubm2',
                            data=[
                                Data(
                                    data_id='35344_1#1',
                                    study_id=5901,
                                    category='genomic_data',
                                    sample_id='DTOL9310949',
                                    library_id='DN683544F:A5',
                                    run_id='35344_1',
                                    processed=1,
                                    tag1_id='129',
                                    date='2020-11-13T11:13:32+00:00',
                                    lims_qc='pass',
                                    visibility='Always',
                                    reads=117883578,
                                    bases=17800420278,
                                    read_length_mean=151.0,
                                    bases_a=3535469853,
                                    bases_c=5344296934,
                                    bases_g=5363949726,
                                    bases_t=3554034645,
                                    folder_ulid='01J8GNT7RDJNSEPWTKHG8QSHSB',
                                    library=Library(
                                        library_id='DN683544F:A5',
                                        library_type_id='Chromium genome',
                                    ),
                                    run=Run(
                                        run_id='35344_1',
                                        platform_id=2,
                                        centre_id=2,
                                        element='1',
                                        instrument_name='HX8',
                                        complete='2020-11-06T10:04:30+00:00',
                                    ),
                                    files=[
                                        File(
                                            id=114488,
                                            data_id='35344_1#1',
                                            name='35344_1#1.cram',
                                            remote_path='irods:/seq/35344/35344_1#1.cram',
                                            size_bytes=8253265734,
                                            md5='a8ebee530fc5edf3cb3644e2af276498',
                                            file_type='CRAM',
                                            has_methylation=False,
                                            sam_tags=['BC:Z', 'QT:Z', 'RG:Z'],
                                        )
                                    ],
                                    project_assn=[
                                        Allocation(
                                            id=6963,
                                            project_id='britain-and-ireland',
                                            data_id='35344_1#1',
                                        ),
                                        Allocation(
                                            id=6964, project_id='darwin', data_id='35344_1#1'
                                        ),
                                        Allocation(
                                            id=6965,
                                            project_id='protist-microalgae',
                                            data_id='35344_1#1',
                                        ),
                                        Allocation(
                                            id=6966, project_id='tol', data_id='35344_1#1'
                                        ),
                                    ],
                                    dataset_assn=[
                                        DatasetElement(
                                            id=21916,
                                            data_id='35344_1#1',
                                            dataset_id='01K6BJYB201CTC53DYQ1M674KK',
                                            dataset=Dataset(
                                                dataset_id='01K6BJYB201CTC53DYQ1M674KK',
                                                name='10x',
                                                status_history=[
                                                    DatasetStatus(
                                                        dataset_status_id=15592,
                                                        dataset_id='01K6BJYB201CTC53DYQ1M674KK',
                                                        status_type_id='Pending',
                                                        status_time=(
                                                            '2025-09-29T21:34:35.257948+01:00'
                                                        ),
                                                    )
                                                ],
                                            ),
                                        )
                                    ],
                                    folder=Folder(
                                        folder_ulid='01J8GNT7RDJNSEPWTKHG8QSHSB',
                                        folder_location_id='illumina_data_s3',
                                        image_file_list=[
                                            {
                                                'file': '35344_1#1_F0xB00-acgt-cycles.png',
                                                'caption': 'Chromium genome A|C|G|T Content Per Cycle',  # noqa: E501
                                            },
                                            {
                                                'file': '35344_1#1_F0xB00-quals3.png',
                                                'caption': 'Chromium genome Quality Frequencies, Separate Curve Per Cycle',  # noqa: E501
                                            },
                                            {
                                                'file': '35344_1#1_F0xB00-quals2.png',
                                                'caption': 'Chromium genome Quality Per Cycle (Split)',  # noqa: E501
                                            },
                                            {
                                                'file': '35344_1#1_F0xB00-gc-content.png',
                                                'caption': 'Chromium genome G|C Content',
                                            },
                                            {
                                                'file': '35344_1#1_F0xB00-quals-hm.png',
                                                'caption': 'Chromium genome Quality Frequencies, Per Cycle Heat Map',  # noqa: E501
                                            },
                                            {
                                                'file': '35344_1#1_F0xB00-quals.png',
                                                'caption': 'Chromium genome Quality Per Cycle (Overlaid)',  # noqa: E501
                                            },
                                        ],
                                        files_total_bytes=193479,
                                    ),
                                ),
                                Data(
                                    data_id='35344_1#2',
                                    study_id=5901,
                                    category='genomic_data',
                                    sample_id='DTOL9310949',
                                    library_id='DN683544F:A5',
                                    run_id='35344_1',
                                    tag1_id='130',
                                    date='2020-11-13T11:13:32+00:00',
                                    lims_qc='pass',
                                    qc='pass',
                                    visibility='Always',
                                    reads=3205550,
                                    bases=484038050,
                                    read_length_mean=151.0,
                                    bases_a=96323000,
                                    bases_c=145218591,
                                    bases_g=145800670,
                                    bases_t=96626120,
                                    folder_ulid='01J8GNT901PKS6AZBX0QPJEP95',
                                    library=Library(
                                        library_id='DN683544F:A5',
                                        library_type_id='Chromium genome',
                                    ),
                                    run=Run(
                                        run_id='35344_1',
                                        platform_id=2,
                                        centre_id=2,
                                        element='1',
                                        instrument_name='HX8',
                                        complete='2020-11-06T10:04:30+00:00',
                                    ),
                                    files=[
                                        File(
                                            id=114489,
                                            data_id='35344_1#2',
                                            name='35344_1#2.cram',
                                            remote_path='irods:/seq/35344/35344_1#2.cram',
                                            size_bytes=226437448,
                                            md5='794433fd4dbcf8e81f4b7e87073ebe33',
                                            file_type='CRAM',
                                            has_methylation=False,
                                            sam_tags=[
                                                'BC:Z',
                                                'QT:Z',
                                                'RG:Z',
                                                'a3:i',
                                                'aa:Z',
                                                'af:f',
                                                'ah:i',
                                                'ar:f',
                                                'as:i',
                                            ],
                                        )
                                    ],
                                    project_assn=[
                                        Allocation(
                                            id=6967,
                                            project_id='britain-and-ireland',
                                            data_id='35344_1#2',
                                        ),
                                        Allocation(
                                            id=6968, project_id='darwin', data_id='35344_1#2'
                                        ),
                                        Allocation(
                                            id=6969,
                                            project_id='protist-microalgae',
                                            data_id='35344_1#2',
                                        ),
                                        Allocation(
                                            id=6970, project_id='tol', data_id='35344_1#2'
                                        ),
                                    ],
                                    dataset_assn=[
                                        DatasetElement(
                                            id=21917,
                                            data_id='35344_1#2',
                                            dataset_id='01K6BJYB201CTC53DYQ1M674KK',
                                            dataset=Dataset(
                                                dataset_id='01K6BJYB201CTC53DYQ1M674KK',
                                                name='10x',
                                                status_history=[
                                                    DatasetStatus(
                                                        dataset_status_id=15592,
                                                        dataset_id='01K6BJYB201CTC53DYQ1M674KK',
                                                        status_type_id='Pending',
                                                        status_time=(
                                                            '2025-09-29T21:34:35.257948+01:00'
                                                        ),
                                                    )
                                                ],
                                            ),
                                        )
                                    ],
                                    folder=Folder(
                                        folder_ulid='01J8GNT901PKS6AZBX0QPJEP95',
                                        folder_location_id='illumina_data_s3',
                                        image_file_list=[
                                            {
                                                'file': '35344_1#2_F0xB00-quals2.png',
                                                'caption': 'Chromium genome Quality Per Cycle (Split)',  # noqa: E501
                                            },
                                            {
                                                'file': '35344_1#2_F0xB00-quals.png',
                                                'caption': 'Chromium genome Quality Per Cycle (Overlaid)',  # noqa: E501
                                            },
                                            {
                                                'file': '35344_1#2_F0xB00-gc-content.png',
                                                'caption': 'Chromium genome G|C Content',
                                            },
                                            {
                                                'file': '35344_1#2_F0xB00-quals-hm.png',
                                                'caption': 'Chromium genome Quality Frequencies, Per Cycle Heat Map',  # noqa: E501
                                            },
                                            {
                                                'file': '35344_1#2_F0xB00-quals3.png',
                                                'caption': 'Chromium genome Quality Frequencies, Separate Curve Per Cycle',  # noqa: E501
                                            },
                                            {
                                                'file': '35344_1#2_F0xB00-acgt-cycles.png',
                                                'caption': 'Chromium genome A|C|G|T Content Per Cycle',  # noqa: E501
                                            },
                                        ],
                                        files_total_bytes=191188,
                                    ),
                                ),
                                Data(
                                    data_id='35344_1#3',
                                    study_id=5901,
                                    category='genomic_data',
                                    sample_id='DTOL9310949',
                                    library_id='DN683544F:A5',
                                    run_id='35344_1',
                                    processed=0,
                                    tag1_id='131',
                                    date='2020-11-13T11:13:32+00:00',
                                    lims_qc='pass',
                                    qc='pass',
                                    visibility='Always',
                                    reads=118915580,
                                    bases=17956252580,
                                    read_length_mean=151.0,
                                    bases_a=3574864149,
                                    bases_c=5387034008,
                                    bases_g=5399306197,
                                    bases_t=3592329137,
                                    folder_ulid='01J8GNTAE04KEY675Z4WX8KDK4',
                                    library=Library(
                                        library_id='DN683544F:A5',
                                        library_type_id='Chromium genome',
                                    ),
                                    run=Run(
                                        run_id='35344_1',
                                        platform_id=2,
                                        centre_id=2,
                                        element='1',
                                        instrument_name='HX8',
                                        complete='2020-11-06T10:04:30+00:00',
                                    ),
                                    files=[
                                        File(
                                            id=114490,
                                            data_id='35344_1#3',
                                            name='35344_1#3.cram',
                                            remote_path='irods:/seq/35344/35344_1#3.cram',
                                            size_bytes=8269429324,
                                            md5='d62df44f9dcb5982497720667ba017a3',
                                            file_type='CRAM',
                                            has_methylation=False,
                                            sam_tags=['BC:Z', 'QT:Z', 'RG:Z', 'a3:i', 'ah:i'],
                                        )
                                    ],
                                    project_assn=[
                                        Allocation(
                                            id=6971,
                                            project_id='britain-and-ireland',
                                            data_id='35344_1#3',
                                        ),
                                        Allocation(
                                            id=6972, project_id='darwin', data_id='35344_1#3'
                                        ),
                                        Allocation(
                                            id=6973,
                                            project_id='protist-microalgae',
                                            data_id='35344_1#3',
                                        ),
                                        Allocation(
                                            id=6974, project_id='tol', data_id='35344_1#3'
                                        ),
                                    ],
                                    dataset_assn=[
                                        DatasetElement(
                                            id=21918,
                                            data_id='35344_1#3',
                                            dataset_id='01K6BJYB201CTC53DYQ1M674KK',
                                            dataset=Dataset(
                                                dataset_id='01K6BJYB201CTC53DYQ1M674KK',
                                                name='10x',
                                                status_history=[
                                                    DatasetStatus(
                                                        dataset_status_id=15592,
                                                        dataset_id='01K6BJYB201CTC53DYQ1M674KK',
                                                        status_type_id='Pending',
                                                        status_time=(
                                                            '2025-09-29T21:34:35.257948+01:00'
                                                        ),
                                                    )
                                                ],
                                            ),
                                        )
                                    ],
                                    folder=Folder(
                                        folder_ulid='01J8GNTAE04KEY675Z4WX8KDK4',
                                        folder_location_id='illumina_data_s3',
                                        image_file_list=[
                                            {
                                                'file': '35344_1#3_F0xB00-quals-hm.png',
                                                'caption': 'Chromium genome Quality Frequencies, Per Cycle Heat Map',  # noqa: E501
                                            },
                                            {
                                                'file': '35344_1#3_F0xB00-quals3.png',
                                                'caption': 'Chromium genome Quality Frequencies, Separate Curve Per Cycle',  # noqa: E501
                                            },
                                            {
                                                'file': '35344_1#3_F0xB00-quals.png',
                                                'caption': 'Chromium genome Quality Per Cycle (Overlaid)',  # noqa: E501
                                            },
                                            {
                                                'file': '35344_1#3_F0xB00-acgt-cycles.png',
                                                'caption': 'Chromium genome A|C|G|T Content Per Cycle',  # noqa: E501
                                            },
                                            {
                                                'file': '35344_1#3_F0xB00-quals2.png',
                                                'caption': 'Chromium genome Quality Per Cycle (Split)',  # noqa: E501
                                            },
                                            {
                                                'file': '35344_1#3_F0xB00-gc-content.png',
                                                'caption': 'Chromium genome G|C Content',
                                            },
                                        ],
                                        files_total_bytes=193887,
                                    ),
                                ),
                                Data(
                                    data_id='35344_1#4',
                                    study_id=5901,
                                    category='genomic_data',
                                    sample_id='DTOL9310949',
                                    library_id='DN683544F:A5',
                                    run_id='35344_1',
                                    processed=0,
                                    tag1_id='132',
                                    date='2020-11-13T11:13:32+00:00',
                                    lims_qc='pass',
                                    qc='pass',
                                    visibility='Testing',
                                    reads=120600430,
                                    bases=18210664930,
                                    read_length_mean=151.0,
                                    bases_a=3612935737,
                                    bases_c=5477449982,
                                    bases_g=5489970795,
                                    bases_t=3627594029,
                                    folder_ulid='01J8GNTBMMYVA2RJZKYZCHZAAM',
                                    library=Library(
                                        library_id='DN683544F:A5',
                                        library_type_id='Chromium genome',
                                    ),
                                    run=Run(
                                        run_id='35344_1',
                                        platform_id=2,
                                        centre_id=2,
                                        element='1',
                                        instrument_name='HX8',
                                        complete='2020-11-06T10:04:30+00:00',
                                    ),
                                    files=[
                                        File(
                                            id=114491,
                                            data_id='35344_1#4',
                                            name='35344_1#4.cram',
                                            remote_path='irods:/seq/35344/35344_1#4.cram',
                                            size_bytes=8421281844,
                                            md5='901f0a009eee03f14c2ddb3b614e217e',
                                            file_type='CRAM',
                                            has_methylation=False,
                                            sam_tags=[
                                                'BC:Z',
                                                'QT:Z',
                                                'RG:Z',
                                                'aa:Z',
                                                'af:f',
                                                'ar:f',
                                                'as:i',
                                            ],
                                        )
                                    ],
                                    project_assn=[
                                        Allocation(
                                            id=6975,
                                            project_id='britain-and-ireland',
                                            data_id='35344_1#4',
                                        ),
                                        Allocation(
                                            id=6976, project_id='darwin', data_id='35344_1#4'
                                        ),
                                        Allocation(
                                            id=6977,
                                            project_id='protist-microalgae',
                                            data_id='35344_1#4',
                                        ),
                                        Allocation(
                                            id=6978, project_id='tol', data_id='35344_1#4'
                                        ),
                                    ],
                                    dataset_assn=[
                                        DatasetElement(
                                            id=21919,
                                            data_id='35344_1#4',
                                            dataset_id='01K6BJYB201CTC53DYQ1M674KK',
                                            dataset=Dataset(
                                                dataset_id='01K6BJYB201CTC53DYQ1M674KK',
                                                name='10x',
                                                status_history=[
                                                    DatasetStatus(
                                                        dataset_status_id=15592,
                                                        dataset_id='01K6BJYB201CTC53DYQ1M674KK',
                                                        status_type_id='Pending',
                                                        status_time=(
                                                            '2025-09-29T21:34:35.257948+01:00'
                                                        ),
                                                    )
                                                ],
                                            ),
                                        )
                                    ],
                                    folder=Folder(
                                        folder_ulid='01J8GNTBMMYVA2RJZKYZCHZAAM',
                                        folder_location_id='illumina_data_s3',
                                        image_file_list=[
                                            {
                                                'file': '35344_1#4_F0xB00-quals-hm.png',
                                                'caption': 'Chromium genome Quality Frequencies, Per Cycle Heat Map',  # noqa: E501
                                            },
                                            {
                                                'file': '35344_1#4_F0xB00-quals2.png',
                                                'caption': 'Chromium genome Quality Per Cycle (Split)',  # noqa: E501
                                            },
                                            {
                                                'file': '35344_1#4_F0xB00-quals3.png',
                                                'caption': 'Chromium genome Quality Frequencies, Separate Curve Per Cycle',  # noqa: E501
                                            },
                                            {
                                                'file': '35344_1#4_F0xB00-acgt-cycles.png',
                                                'caption': 'Chromium genome A|C|G|T Content Per Cycle',  # noqa: E501
                                            },
                                            {
                                                'file': '35344_1#4_F0xB00-quals.png',
                                                'caption': 'Chromium genome Quality Per Cycle (Overlaid)',  # noqa: E501
                                            },
                                            {
                                                'file': '35344_1#4_F0xB00-gc-content.png',
                                                'caption': 'Chromium genome G|C Content',
                                            },
                                        ],
                                        files_total_bytes=194264,
                                    ),
                                ),
                            ],
                        ),
                        Sample(
                            sample_id='DTOL9384820',
                            specimen_id='ucBraSubm2',
                            accession_id='SAMEA7532766',
                            accession=Accession(
                                accession_id='SAMEA7532766',
                                accession_type_id='BioSample',
                                is_deleted=False,
                            ),
                            data=[
                                Data(
                                    data_id='35528_4#8',
                                    study_id=5901,
                                    category='genomic_data',
                                    sample_id='DTOL9384820',
                                    library_id='DN703060C:H1',
                                    run_id='35528_4',
                                    processed=1,
                                    tag1_id='72',
                                    tag2_id='72',
                                    date='2020-11-24T19:23:18+00:00',
                                    lims_qc='pass',
                                    visibility='Always',
                                    reads=748759474,
                                    bases=113062680574,
                                    read_length_mean=151.0,
                                    bases_a=25282939585,
                                    bases_c=30291651451,
                                    bases_g=33032570272,
                                    bases_t=24454648885,
                                    folder_ulid='01J8GP34MFJNAHCBM0X20TA8VF',
                                    library=Library(
                                        library_id='DN703060C:H1',
                                        library_type_id='Hi-C - Arima v2',
                                    ),
                                    run=Run(
                                        run_id='35528_4',
                                        platform_id=5,
                                        centre_id=2,
                                        element='4',
                                        instrument_name='NV16',
                                        complete='2020-11-19T08:24:02+00:00',
                                    ),
                                    files=[
                                        File(
                                            id=114697,
                                            data_id='35528_4#8',
                                            name='35528_4#8.cram',
                                            remote_path=(
                                                'irods:/seq/illumina/runs/35/35528/lane4/plex8'
                                                '/35528_4#8.cram'
                                            ),
                                            size_bytes=38152933620,
                                            md5='6fdc802b815d8109cca0e05b64390c3f',
                                            file_type='CRAM',
                                            has_methylation=False,
                                            sam_tags=['BC:Z', 'QT:Z', 'RG:Z'],
                                        )
                                    ],
                                    project_assn=[
                                        Allocation(
                                            id=7551,
                                            project_id='britain-and-ireland',
                                            data_id='35528_4#8',
                                        ),
                                        Allocation(
                                            id=7552, project_id='darwin', data_id='35528_4#8'
                                        ),
                                        Allocation(
                                            id=7553,
                                            project_id='protist-microalgae',
                                            data_id='35528_4#8',
                                        ),
                                        Allocation(
                                            id=7554, project_id='tol', data_id='35528_4#8'
                                        ),
                                    ],
                                    dataset_assn=[
                                        DatasetElement(
                                            id=15385,
                                            data_id='35528_4#8',
                                            dataset_id='01K6B5R10VC8F9XTXCVGXM50Q2',
                                            dataset=Dataset(
                                                dataset_id='01K6B5R10VC8F9XTXCVGXM50Q2',
                                                name='hic-arima2',
                                                status_history=[
                                                    DatasetStatus(
                                                        dataset_status_id=10911,
                                                        dataset_id='01K6B5R10VC8F9XTXCVGXM50Q2',
                                                        status_type_id='Pending',
                                                        status_time=(
                                                            '2025-09-29T17:43:56.894702+01:00'
                                                        ),
                                                    )
                                                ],
                                            ),
                                        )
                                    ],
                                    folder=Folder(
                                        folder_ulid='01J8GP34MFJNAHCBM0X20TA8VF',
                                        folder_location_id='illumina_data_s3',
                                        image_file_list=[
                                            {
                                                'file': '35528_4#8_F0xB00-quals3.png',
                                                'caption': 'Hi-C - Arima v2 Quality Frequencies, Separate Curve Per Cycle',  # noqa: E501
                                            },
                                            {
                                                'file': '35528_4#8_F0xB00-quals-hm.png',
                                                'caption': 'Hi-C - Arima v2 Quality Frequencies, Per Cycle Heat Map',  # noqa: E501
                                            },
                                            {
                                                'file': '35528_4#8_F0xB00-acgt-cycles.png',
                                                'caption': 'Hi-C - Arima v2 A|C|G|T Content Per Cycle',  # noqa: E501
                                            },
                                            {
                                                'file': '35528_4#8_F0xB00-quals.png',
                                                'caption': 'Hi-C - Arima v2 Quality Per Cycle (Overlaid)',  # noqa: E501
                                            },
                                            {
                                                'file': '35528_4#8_F0xB00-gc-content.png',
                                                'caption': 'Hi-C - Arima v2 G|C Content',
                                            },
                                            {
                                                'file': '35528_4#8_F0xB00-quals2.png',
                                                'caption': 'Hi-C - Arima v2 Quality Per Cycle (Split)',  # noqa: E501
                                            },
                                        ],
                                        files_total_bytes=157201,
                                    ),
                                )
                            ],
                        ),
                        Sample(
                            sample_id='DTOL9397431',
                            specimen_id='ucBraSubm2',
                            data=[
                                Data(
                                    data_id='m64016_201115_112225#1022',
                                    study_id=5901,
                                    category='genomic_data',
                                    sample_id='DTOL9397431',
                                    library_id='DN703483V',
                                    run_id='m64016_201115_112225',
                                    processed=1,
                                    tag1_id='bc1022_BAK8B_OA',
                                    visibility='Always',
                                    reads=881269,
                                    bases=9026879627,
                                    read_length_mean=10243.0468188487,
                                    read_length_n50=11689,
                                    bases_a=1653086454,
                                    bases_c=2863188209,
                                    bases_g=2856726634,
                                    bases_t=1653878330,
                                    read_length_longest=39513,
                                    read_length_shortest=53,
                                    reads_duplicated=0,
                                    reads_discarded=200,
                                    reads_trimmed=1652,
                                    bases_removed=1850523,
                                    library=Library(
                                        library_id='DN703483V', library_type_id='PacBio - HiFi'
                                    ),
                                    run=Run(
                                        run_id='m64016_201115_112225',
                                        platform_id=14,
                                        centre_id=2,
                                        lims_id='78299',
                                        element='D1',
                                        instrument_name='m64016',
                                        complete='2020-11-15T00:00:00+00:00',
                                        chemistry='S/P4-C2/5.0-8M',
                                        pacbio_run_metrics=[
                                            PacbioRunMetrics(
                                                run_id='m64016_201115_112225',
                                                folder_ulid='EMPTY_PACBIO_RUN_S3',
                                                folder=Folder(
                                                    folder_ulid='EMPTY_PACBIO_RUN_S3',
                                                    folder_location_id='pacbio_run_s3',
                                                    files_total_bytes=0,
                                                ),
                                            )
                                        ],
                                    ),
                                    files=[
                                        File(
                                            id=143249,
                                            data_id='m64016_201115_112225#1022',
                                            name=(
                                                'm64016_201115_112225.ccs.bc1022_BAK8B_OA'
                                                '--bc1022_BAK8B_OA.bam'
                                            ),
                                            remote_path=(
                                                'irods:/seq/pacbio/r64016_20201112_100113/4_D01'
                                                '/demultiplex.bc1022_BAK8B_OA'
                                                '--bc1022_BAK8B_OA.bam'
                                            ),
                                            size_bytes=7877130682,
                                            md5='391fc5db79b693a27bb95cc5291888be',
                                            file_type='BAM',
                                            has_methylation=True,
                                            sam_tags=[
                                                'HZ:f',
                                                'RG:Z',
                                                'bc:B',
                                                'bl:Z',
                                                'bq:i',
                                                'bt:Z',
                                                'bx:B',
                                                'cx:i',
                                                'ec:f',
                                                'np:i',
                                                'qe:i',
                                                'ql:Z',
                                                'qs:i',
                                                'qt:Z',
                                                'rq:f',
                                                'sn:B',
                                                'we:i',
                                                'ws:i',
                                                'zm:i',
                                            ],
                                        )
                                    ],
                                    project_assn=[
                                        Allocation(
                                            id=46274,
                                            project_id='britain-and-ireland',
                                            data_id='m64016_201115_112225#1022',
                                        ),
                                        Allocation(
                                            id=46275,
                                            project_id='darwin',
                                            data_id='m64016_201115_112225#1022',
                                        ),
                                        Allocation(
                                            id=46276,
                                            project_id='protist-microalgae',
                                            data_id='m64016_201115_112225#1022',
                                        ),
                                        Allocation(
                                            id=46277,
                                            project_id='tol',
                                            data_id='m64016_201115_112225#1022',
                                        ),
                                    ],
                                    dataset_assn=[
                                        DatasetElement(
                                            id=4666,
                                            data_id='m64016_201115_112225#1022',
                                            dataset_id='01K6AW4EBE124C2EEA91HFCA1E',
                                            dataset=Dataset(
                                                dataset_id='01K6AW4EBE124C2EEA91HFCA1E',
                                                name='pacbio.ccs',
                                                status_history=[
                                                    DatasetStatus(
                                                        dataset_status_id=3069,
                                                        dataset_id='01K6AW4EBE124C2EEA91HFCA1E',
                                                        status_type_id='Pending',
                                                        status_time=(
                                                            '2025-09-29T14:55:57.986068+01:00'
                                                        ),
                                                    )
                                                ],
                                            ),
                                        )
                                    ],
                                ),
                                Data(
                                    data_id='m64089e_210601_133425#1022',
                                    study_id=5901,
                                    category='genomic_data',
                                    sample_id='DTOL9397431',
                                    library_id='DN695911V-H1',
                                    run_id='m64089e_210601_133425',
                                    tag1_id='1022',
                                    date='2021-06-02T23:04:37+01:00',
                                    lims_qc='fail',
                                    qc='pass',
                                    visibility='Always',
                                    reads=120626,
                                    bases=1290572095,
                                    read_length_mean=10698.9545786149,
                                    read_length_n50=11906,
                                    bases_a=241970518,
                                    bases_c=403273112,
                                    bases_g=403221295,
                                    bases_t=242107170,
                                    read_length_longest=42852,
                                    read_length_shortest=56,
                                    reads_duplicated=0,
                                    reads_discarded=60,
                                    reads_trimmed=114,
                                    bases_removed=427249,
                                    library=Library(
                                        library_id='DN695911V-H1', library_type_id='PacBio - HiFi'
                                    ),
                                    run=Run(
                                        run_id='m64089e_210601_133425',
                                        platform_id=3,
                                        centre_id=2,
                                        lims_id='82803',
                                        element='D1',
                                        instrument_name='m64089e',
                                        start='2021-05-28T10:26:51+01:00',
                                        complete='2021-06-02T23:04:37+01:00',
                                        plex_count=1,
                                        chemistry='S/P5-C2/5.0-8M',
                                        pacbio_run_metrics=[
                                            PacbioRunMetrics(
                                                run_id='m64089e_210601_133425',
                                                movie_minutes=1800,
                                                binding_kit='Sequel II Binding Kit 2.2',
                                                sequencing_kit=(
                                                    'Sequel II Sequencing Plate 2.0 (4 rxn)'
                                                ),
                                                sequencing_kit_lot_number='019994',
                                                cell_lot_number='416626',
                                                include_kinetics='true',
                                                loading_conc=70.0,
                                                control_num_reads=8197,
                                                control_read_length_mean=27617.0,
                                                control_concordance_mean=0.86696,
                                                control_concordance_mode=0.89,
                                                local_base_rate=2.32624,
                                                polymerase_read_bases=28215924595,
                                                polymerase_num_reads=622368,
                                                polymerase_read_length_mean=45336.0,
                                                polymerase_read_length_n50=160250,
                                                insert_length_mean=12667.0,
                                                insert_length_n50=14750,
                                                unique_molecular_bases=7474866688,
                                                productive_zmws_num=8006474,
                                                p0_num=7376744,
                                                p1_num=630565,
                                                p2_num=7362,
                                                adapter_dimer_percent=0.0,
                                                short_insert_percent=0.0,
                                                hifi_read_bases=1295136871,
                                                hifi_num_reads=120696,
                                                hifi_read_length_mean=10730,
                                                hifi_read_quality_median=35,
                                                hifi_number_passes_mean=13.0,
                                                hifi_low_quality_read_bases=187949502,
                                                hifi_low_quality_num_reads=16141,
                                                hifi_low_quality_read_length_mean=11644,
                                                hifi_low_quality_read_quality_median=16,
                                                folder_ulid='01J8G8XQ7SPGXVJX1QYHNZ1PSV',
                                                folder=Folder(
                                                    folder_ulid='01J8G8XQ7SPGXVJX1QYHNZ1PSV',
                                                    folder_location_id='pacbio_run_s3',
                                                    image_file_list=[
                                                        {
                                                            'file': 'readlength_qv_hist2d.hexbin.png',  # noqa: E501
                                                            'caption': 'Accuracy versus read length density',  # noqa: E501
                                                        },
                                                        {
                                                            'file': 'ccs_npasses_hist.png',
                                                            'caption': 'Number of passes',
                                                        },
                                                        {
                                                            'file': 'ccs_accuracy_hist.png',
                                                            'caption': 'Read quality distribution',  # noqa: E501
                                                        },
                                                        {
                                                            'file': 'readlength_plot.png',
                                                            'caption': 'Control polymerase read length',  # noqa: E501
                                                        },
                                                        {
                                                            'file': 'raw_read_length_plot.png',
                                                            'caption': 'Loading evaluation',
                                                        },
                                                        {
                                                            'file': 'concordance_plot.png',
                                                            'caption': 'Control concordance',
                                                        },
                                                        {
                                                            'file': 'readLenDist0.png',
                                                            'caption': 'Polymerase read length',
                                                        },
                                                        {
                                                            'file': 'base_yield_plot.png',
                                                            'caption': 'Base yield density',
                                                        },
                                                        {
                                                            'file': 'hexbin_length_plot.png',
                                                            'caption': 'Insert read length density',  # noqa: E501
                                                        },
                                                    ],
                                                    files_total_bytes=3299923,
                                                ),
                                            )
                                        ],
                                    ),
                                    files=[
                                        File(
                                            id=120785,
                                            data_id='m64089e_210601_133425#1022',
                                            name=(
                                                'm64089e_210601_133425.ccs.bc1022_BAK8B_OA'
                                                '--bc1022_BAK8B_OA.bam'
                                            ),
                                            remote_path=(
                                                'irods:/seq/pacbio/r64089e_20210528_093647/4_D01'
                                                '/demultiplex.bc1022_BAK8B_OA'
                                                '--bc1022_BAK8B_OA.bam'
                                            ),
                                            size_bytes=4943416701,
                                            md5='cfb6b3e0cb54eb97ee1fec78964b6944',
                                            file_type='BAM',
                                            has_methylation=False,
                                            has_kinetics=True,
                                            sam_tags=[
                                                'RG:Z',
                                                'bc:B',
                                                'bl:Z',
                                                'bq:i',
                                                'bt:Z',
                                                'bx:B',
                                                'cx:i',
                                                'ec:f',
                                                'fi:B',
                                                'fn:i',
                                                'fp:B',
                                                'np:i',
                                                'qe:i',
                                                'ql:Z',
                                                'qs:i',
                                                'qt:Z',
                                                'ri:B',
                                                'rn:i',
                                                'rp:B',
                                                'rq:f',
                                                'sn:B',
                                                'we:i',
                                                'ws:i',
                                                'zm:i',
                                            ],
                                        )
                                    ],
                                    project_assn=[
                                        Allocation(
                                            id=47766,
                                            project_id='britain-and-ireland',
                                            data_id='m64089e_210601_133425#1022',
                                        ),
                                        Allocation(
                                            id=47767,
                                            project_id='darwin',
                                            data_id='m64089e_210601_133425#1022',
                                        ),
                                        Allocation(
                                            id=47768,
                                            project_id='protist-microalgae',
                                            data_id='m64089e_210601_133425#1022',
                                        ),
                                        Allocation(
                                            id=47769,
                                            project_id='tol',
                                            data_id='m64089e_210601_133425#1022',
                                        ),
                                    ],
                                    dataset_assn=[
                                        DatasetElement(
                                            id=4667,
                                            data_id='m64089e_210601_133425#1022',
                                            dataset_id='01K6AW4EBE124C2EEA91HFCA1E',
                                            dataset=Dataset(
                                                dataset_id='01K6AW4EBE124C2EEA91HFCA1E',
                                                name='pacbio.ccs',
                                                status_history=[
                                                    DatasetStatus(
                                                        dataset_status_id=3069,
                                                        dataset_id='01K6AW4EBE124C2EEA91HFCA1E',
                                                        status_type_id='Pending',
                                                        status_time=(
                                                            '2025-09-29T14:55:57.986068+01:00'
                                                        ),
                                                    )
                                                ],
                                            ),
                                        )
                                    ],
                                ),
                            ],
                        ),
                        Sample(
                            sample_id='DTOLRNA9465095',
                            specimen_id='ucBraSubm2',
                            accession_id='SAMEA7532770',
                            accession=Accession(
                                accession_id='SAMEA7532770',
                                accession_type_id='BioSample',
                                is_deleted=False,
                            ),
                            data=[
                                Data(
                                    data_id='36703_5#4',
                                    study_id=6327,
                                    category='transcriptomic_data',
                                    sample_id='DTOLRNA9465095',
                                    library_id='DN611904M:F3',
                                    run_id='36703_5',
                                    processed=1,
                                    tag1_id='22',
                                    tag2_id='22',
                                    date='2021-03-19T10:56:23+00:00',
                                    lims_qc='pass',
                                    visibility='Always',
                                    reads=41616914,
                                    bases=6284154014,
                                    read_length_mean=151.0,
                                    bases_a=1485594035,
                                    bases_c=1669256406,
                                    bases_g=1684013113,
                                    bases_t=1444777110,
                                    folder_ulid='01J8GQ6KCY1QQ32TSMP7KRRT3Z',
                                    library=Library(
                                        library_id='DN611904M:F3', library_type_id='RNA PolyA'
                                    ),
                                    run=Run(
                                        run_id='36703_5',
                                        platform_id=4,
                                        centre_id=2,
                                        element='5',
                                        instrument_name='HF1',
                                        complete='2021-03-08T10:31:06+00:00',
                                    ),
                                    files=[
                                        File(
                                            id=123947,
                                            data_id='36703_5#4',
                                            name='36703_5#4.cram',
                                            remote_path='irods:/seq/36703/36703_5#4.cram',
                                            size_bytes=2596511348,
                                            md5='a4f243cf29cabaa05fbeeb126495e7f8',
                                            file_type='CRAM',
                                            has_methylation=False,
                                            sam_tags=['BC:Z', 'QT:Z', 'RG:Z', 'a3:i', 'ah:i'],
                                        )
                                    ],
                                    project_assn=[
                                        Allocation(
                                            id=9435,
                                            project_id='britain-and-ireland',
                                            data_id='36703_5#4',
                                        ),
                                        Allocation(
                                            id=9436, project_id='darwin', data_id='36703_5#4'
                                        ),
                                        Allocation(
                                            id=9437,
                                            project_id='protist-microalgae',
                                            data_id='36703_5#4',
                                        ),
                                        Allocation(
                                            id=9438, project_id='tol', data_id='36703_5#4'
                                        ),
                                    ],
                                    dataset_assn=[
                                        DatasetElement(
                                            id=29976,
                                            data_id='36703_5#4',
                                            dataset_id='01K6BPZJ9ENAJP5C2VRA9KFY2A',
                                            dataset=Dataset(
                                                dataset_id='01K6BPZJ9ENAJP5C2VRA9KFY2A',
                                                name='rna-seq',
                                                status_history=[
                                                    DatasetStatus(
                                                        dataset_status_id=19599,
                                                        dataset_id='01K6BPZJ9ENAJP5C2VRA9KFY2A',
                                                        status_type_id='Pending',
                                                        status_time=(
                                                            '2025-09-29T22:45:09.729719+01:00'
                                                        ),
                                                    )
                                                ],
                                            ),
                                        )
                                    ],
                                    folder=Folder(
                                        folder_ulid='01J8GQ6KCY1QQ32TSMP7KRRT3Z',
                                        folder_location_id='illumina_data_s3',
                                        image_file_list=[
                                            {
                                                'file': '36703_5#4_F0xB00-quals-hm.png',
                                                'caption': 'RNA PolyA Quality Frequencies, Per Cycle Heat Map',  # noqa: E501
                                            },
                                            {
                                                'file': '36703_5#4_F0xB00-quals.png',
                                                'caption': 'RNA PolyA Quality Per Cycle (Overlaid)',  # noqa: E501
                                            },
                                            {
                                                'file': '36703_5#4_F0xB00-quals3.png',
                                                'caption': 'RNA PolyA Quality Frequencies, Separate Curve Per Cycle',  # noqa: E501
                                            },
                                            {
                                                'file': '36703_5#4_F0xB00-quals2.png',
                                                'caption': 'RNA PolyA Quality Per Cycle (Split)',
                                            },
                                            {
                                                'file': '36703_5#4_F0xB00-acgt-cycles.png',
                                                'caption': 'RNA PolyA A|C|G|T Content Per Cycle',
                                            },
                                            {
                                                'file': '36703_5#4_F0xB00-gc-content.png',
                                                'caption': 'RNA PolyA G|C Content',
                                            },
                                        ],
                                        files_total_bytes=193250,
                                    ),
                                )
                            ],
                        ),
                        Sample(
                            sample_id='DTOL_RD10244236',
                            specimen_id='ucBraSubm2',
                            data=[
                                Data(
                                    data_id='37939_1#2',
                                    study_id=5822,
                                    category='genomic_data',
                                    sample_id='DTOL_RD10244236',
                                    library_id='DN805609I:B3',
                                    run_id='37939_1',
                                    processed=0,
                                    tag1_id='18',
                                    tag2_id='18',
                                    date='2021-05-21T10:35:42+01:00',
                                    lims_qc='pass',
                                    qc='fail',
                                    visibility='Always',
                                    reads=81186152,
                                    bases=12056143572,
                                    read_length_mean=148.0,
                                    bases_a=2574611227,
                                    bases_c=3421507646,
                                    bases_g=3531935839,
                                    bases_t=2527342736,
                                    folder_ulid='01J8GSEF3JDHWEVBP5EWYD9QC8',
                                    library=Library(
                                        library_id='DN805609I:B3',
                                        library_type_id='Haplotagging (202106)',
                                    ),
                                    run=Run(
                                        run_id='37939_1',
                                        platform_id=5,
                                        centre_id=2,
                                        element='1',
                                        instrument_name='NV22',
                                        complete='2021-05-14T11:44:28+01:00',
                                    ),
                                    files=[
                                        File(
                                            id=112380,
                                            data_id='37939_1#2',
                                            name='37939_1#2.cram',
                                            remote_path=(
                                                'irods:/seq/illumina/runs/37/37939/lane1/plex2'
                                                '/37939_1#2.cram'
                                            ),
                                            size_bytes=4232398866,
                                            md5='c0ac0c8f911a62997ad2afc28642a56a',
                                            file_type='CRAM',
                                            has_methylation=False,
                                            sam_tags=['BC:Z', 'QT:Z', 'RG:Z'],
                                        )
                                    ],
                                    project_assn=[
                                        Allocation(
                                            id=12848,
                                            project_id='britain-and-ireland',
                                            data_id='37939_1#2',
                                        ),
                                        Allocation(
                                            id=12849, project_id='darwin', data_id='37939_1#2'
                                        ),
                                        Allocation(
                                            id=12850,
                                            project_id='protist-microalgae',
                                            data_id='37939_1#2',
                                        ),
                                        Allocation(
                                            id=12851, project_id='tol', data_id='37939_1#2'
                                        ),
                                    ],
                                    dataset_assn=[
                                        DatasetElement(
                                            id=25832,
                                            data_id='37939_1#2',
                                            dataset_id='01K6BKWEJ26GQ6CTC5WW7A2HDG',
                                            dataset=Dataset(
                                                dataset_id='01K6BKWEJ26GQ6CTC5WW7A2HDG',
                                                name='htag-202106',
                                                status_history=[
                                                    DatasetStatus(
                                                        dataset_status_id=16531,
                                                        dataset_id='01K6BKWEJ26GQ6CTC5WW7A2HDG',
                                                        status_type_id='Pending',
                                                        status_time=(
                                                            '2025-09-29T21:51:01.879041+01:00'
                                                        ),
                                                    )
                                                ],
                                            ),
                                        )
                                    ],
                                    folder=Folder(
                                        folder_ulid='01J8GSEF3JDHWEVBP5EWYD9QC8',
                                        folder_location_id='illumina_data_s3',
                                        image_file_list=[
                                            {
                                                'file': '37939_1#2_F0xB00-quals3.png',
                                                'caption': 'Haplotagging Quality Frequencies, Separate Curve Per Cycle',  # noqa: E501
                                            },
                                            {
                                                'file': '37939_1#2_F0xB00-quals-hm.png',
                                                'caption': 'Haplotagging Quality Frequencies, Per Cycle Heat Map',  # noqa: E501
                                            },
                                            {
                                                'file': '37939_1#2_F0xB00-quals.png',
                                                'caption': 'Haplotagging Quality Per Cycle (Overlaid)',  # noqa: E501
                                            },
                                            {
                                                'file': '37939_1#2_F0xB00-acgt-cycles.png',
                                                'caption': 'Haplotagging A|C|G|T Content Per Cycle',  # noqa: E501
                                            },
                                            {
                                                'file': '37939_1#2_F0xB00-quals2.png',
                                                'caption': 'Haplotagging Quality Per Cycle (Split)',  # noqa: E501
                                            },
                                            {
                                                'file': '37939_1#2_F0xB00-gc-content.png',
                                                'caption': 'Haplotagging G|C Content',
                                            },
                                        ],
                                        files_total_bytes=155892,
                                    ),
                                )
                            ],
                        ),
                        Sample(
                            sample_id='DTOL_RD9912264',
                            specimen_id='ucBraSubm2',
                            data=[
                                Data(
                                    data_id='36857#13',
                                    study_id=5822,
                                    category='genomic_data',
                                    sample_id='DTOL_RD9912264',
                                    library_id='NT1659733A',
                                    run_id='36857',
                                    processed=1,
                                    tag1_id='4332',
                                    tag2_id='4356',
                                    date='2021-03-22T09:42:03+00:00',
                                    lims_qc='pass',
                                    visibility='Always',
                                    reads=27966966,
                                    bases=4153094451,
                                    read_length_mean=148.0,
                                    bases_a=797145425,
                                    bases_c=1275996438,
                                    bases_g=1284970808,
                                    bases_t=794904415,
                                    folder_ulid='01J8GQ93RN80BXDY4WTYJZYB24',
                                    library=Library(
                                        library_id='NT1659733A',
                                        library_type_id='Haplotagging (202103)',
                                    ),
                                    run=Run(
                                        run_id='36857',
                                        platform_id=5,
                                        centre_id=2,
                                        element='1',
                                        instrument_name='NV20',
                                        complete='2021-03-14T15:59:21+00:00',
                                    ),
                                    files=[
                                        File(
                                            id=112358,
                                            data_id='36857#13',
                                            name='36857#13.cram',
                                            remote_path=(
                                                'irods:/seq/illumina/runs/36/36857/plex13'
                                                '/36857#13.cram'
                                            ),
                                            size_bytes=1417578072,
                                            md5='6001d9101395ae26e07a3c619d6f5985',
                                            file_type='CRAM',
                                            has_methylation=False,
                                            sam_tags=['BC:Z', 'QT:Z', 'RG:Z'],
                                        )
                                    ],
                                    project_assn=[
                                        Allocation(
                                            id=9466,
                                            project_id='britain-and-ireland',
                                            data_id='36857#13',
                                        ),
                                        Allocation(
                                            id=9467, project_id='darwin', data_id='36857#13'
                                        ),
                                        Allocation(
                                            id=9468,
                                            project_id='protist-microalgae',
                                            data_id='36857#13',
                                        ),
                                        Allocation(id=9469, project_id='tol', data_id='36857#13'),
                                    ],
                                    dataset_assn=[
                                        DatasetElement(
                                            id=25825,
                                            data_id='36857#13',
                                            dataset_id='01K6BKW5G6FD6N8R67M976W9V9',
                                            dataset=Dataset(
                                                dataset_id='01K6BKW5G6FD6N8R67M976W9V9',
                                                name='htag-202103',
                                                status_history=[
                                                    DatasetStatus(
                                                        dataset_status_id=16524,
                                                        dataset_id='01K6BKW5G6FD6N8R67M976W9V9',
                                                        status_type_id='Pending',
                                                        status_time=(
                                                            '2025-09-29T21:50:52.649160+01:00'
                                                        ),
                                                    )
                                                ],
                                            ),
                                        )
                                    ],
                                    folder=Folder(
                                        folder_ulid='01J8GQ93RN80BXDY4WTYJZYB24',
                                        folder_location_id='illumina_data_s3',
                                        image_file_list=[
                                            {
                                                'file': '36857#13_F0xB00-quals3.png',
                                                'caption': 'Pre-quality controlled Quality Frequencies, Separate Curve Per Cycle',  # noqa: E501
                                            },
                                            {
                                                'file': '36857#13_F0xB00-quals.png',
                                                'caption': 'Pre-quality controlled Quality Per Cycle (Overlaid)',  # noqa: E501
                                            },
                                            {
                                                'file': '36857#13_F0xB00-quals-hm.png',
                                                'caption': 'Pre-quality controlled Quality Frequencies, Per Cycle Heat Map',  # noqa: E501
                                            },
                                            {
                                                'file': '36857#13_F0xB00-acgt-cycles.png',
                                                'caption': 'Pre-quality controlled A|C|G|T Content Per Cycle',  # noqa: E501
                                            },
                                            {
                                                'file': '36857#13_F0xB00-quals2.png',
                                                'caption': 'Pre-quality controlled Quality Per Cycle (Split)',  # noqa: E501
                                            },
                                            {
                                                'file': '36857#13_F0xB00-gc-content.png',
                                                'caption': 'Pre-quality controlled G|C Content',
                                            },
                                        ],
                                        files_total_bytes=154047,
                                    ),
                                )
                            ],
                        ),
                    ],
                    accession=Accession(
                        accession_id='SAMEA7532740',
                        accession_type_id='BioSample',
                        is_deleted=False,
                    ),
                    location=Location(
                        location_id=3113, path='6/c/c/f/1/b/Brachiomonas_submarina'
                    ),
                ),
                Specimen(
                    specimen_id='ucBraSubm3',
                    location_id=3113,
                    species_id='Brachiomonas submarina',
                    supplied_name='SubSam_7066',
                    sts_specimen='Ox800027',
                    accession_id='SAMEA12753558',
                    sex_id='Not applicable',
                    ploidy='2',
                    samples=[
                        Sample(
                            sample_id='DTOL14909592',
                            specimen_id='ucBraSubm3',
                            accession_id='SAMEA12753689',
                            accession=Accession(
                                accession_id='SAMEA12753689',
                                accession_type_id='BioSample',
                                is_deleted=False,
                            ),
                            data=[
                                Data(
                                    data_id='m84309_250205_121831_s4#2076',
                                    study_id=5901,
                                    category='genomic_data',
                                    sample_id='DTOL14909592',
                                    library_id='DTOL14909592',
                                    run_id='m84309_250205_121831_s4',
                                    processed=1,
                                    tag1_id='bc2076',
                                    date='2025-02-07T12:04:12+00:00',
                                    lims_qc='pass',
                                    qc='pass',
                                    visibility='Always',
                                    reads=6782153,
                                    bases=58162339677,
                                    read_length_mean=8575.79291959353,
                                    read_length_n50=8557,
                                    bases_a=15495489894,
                                    bases_c=13309833484,
                                    bases_g=13834851558,
                                    bases_t=15522164741,
                                    read_length_longest=30129,
                                    read_length_shortest=62,
                                    reads_duplicated=494675,
                                    reads_discarded=14187,
                                    reads_trimmed=767,
                                    bases_removed=128899080,
                                    library=Library(
                                        library_id='DTOL14909592',
                                        library_type_id='PacBio - HiFi (ULI)',
                                    ),
                                    run=Run(
                                        run_id='m84309_250205_121831_s4',
                                        platform_id=6,
                                        centre_id=2,
                                        lims_id='TRACTION-RUN-1755',
                                        element='D1.1',
                                        instrument_name='m84309',
                                        start='2025-02-05T10:35:22+00:00',
                                        complete='2025-02-06T17:14:49+00:00',
                                        plex_count=1,
                                        chemistry='R/P1-C1/5.0-25M',
                                        pacbio_run_metrics=[
                                            PacbioRunMetrics(
                                                run_id='m84309_250205_121831_s4',
                                                movie_minutes=1440,
                                                binding_kit='Revio polymerase kit',
                                                sequencing_kit='Revio sequencing plate',
                                                sequencing_kit_lot_number='037237',
                                                cell_lot_number='1000004187',
                                                include_kinetics='false',
                                                loading_conc=109.0,
                                                control_num_reads=6191,
                                                control_read_length_mean=61753.0,
                                                control_concordance_mean=0.909936,
                                                control_concordance_mode=0.93,
                                                local_base_rate=2.0455,
                                                polymerase_read_bases=1012134761938,
                                                polymerase_num_reads=16628028,
                                                polymerase_read_length_mean=60869.0,
                                                polymerase_read_length_n50=127750,
                                                insert_length_mean=11646.0,
                                                insert_length_n50=12250,
                                                unique_molecular_bases=171822858240,
                                                productive_zmws_num=25165824,
                                                p0_num=8471527,
                                                p1_num=16634219,
                                                p2_num=60078,
                                                hifi_read_bases=62957031005,
                                                hifi_num_reads=7302257,
                                                hifi_read_length_mean=8621,
                                                hifi_read_quality_median=39,
                                                hifi_number_passes_mean=12.0,
                                                hifi_barcoded_reads=7284734,
                                                hifi_bases_in_barcoded_reads=62808083286,
                                                folder_ulid='01K0YHWEAA7R6X17WPRJZNTVMP',
                                                folder=Folder(
                                                    folder_ulid='01K0YHWEAA7R6X17WPRJZNTVMP',
                                                    folder_location_id='pacbio_run_s3',
                                                    image_file_list=[
                                                        {
                                                            'file': 'readlength_histogram.png',
                                                            'caption': 'Mean readlength histogram',  # noqa: E501
                                                        },
                                                        {
                                                            'file': 'hexbin_length_plot.png',
                                                            'caption': 'Insert read length density',  # noqa: E501
                                                        },
                                                        {
                                                            'file': 'base_yield_plot.png',
                                                            'caption': 'Base yield density',
                                                        },
                                                        {
                                                            'file': 'nreads_histogram.png',
                                                            'caption': 'Number of reads per barcode histogram',  # noqa: E501
                                                        },
                                                        {
                                                            'file': 'readLenDist0.png',
                                                            'caption': 'Polymerase read length',
                                                        },
                                                        {
                                                            'file': 'readlength_qv_hist2d.hexbin.png',  # noqa: E501
                                                            'caption': 'Accuracy versus read length density',  # noqa: E501
                                                        },
                                                        {
                                                            'file': 'ccs_npasses_hist.png',
                                                            'caption': 'Number of passes',
                                                        },
                                                        {
                                                            'file': 'bq_histogram.png',
                                                            'caption': 'Barcode quality distribution',  # noqa: E501
                                                        },
                                                        {
                                                            'file': 'readlength_plot.png',
                                                            'caption': 'Control polymerase read length',  # noqa: E501
                                                        },
                                                        {
                                                            'file': 'concordance_plot.png',
                                                            'caption': 'Control concordance',
                                                        },
                                                        {
                                                            'file': 'ccs_all_readlength_hist_plot.png',  # noqa: E501
                                                            'caption': 'Read length distribution (all)',  # noqa: E501
                                                        },
                                                        {
                                                            'file': 'ccs_hifi_read_length_yield_plot.png',  # noqa: E501
                                                            'caption': 'HiFi yield by read length',  # noqa: E501
                                                        },
                                                        {
                                                            'file': 'ccs_accuracy_hist.png',
                                                            'caption': 'Read quality distribution',  # noqa: E501
                                                        },
                                                        {
                                                            'file': 'nreads.png',
                                                            'caption': 'Number of reads per barcode',  # noqa: E501
                                                        },
                                                    ],
                                                    files_total_bytes=1127307,
                                                ),
                                            )
                                        ],
                                    ),
                                    files=[
                                        File(
                                            id=148709,
                                            data_id='m84309_250205_121831_s4#2076',
                                            name='m84309_250205_121831_s4.hifi_reads.bc2076.bam',
                                            remote_path=(
                                                'irods:/seq/pacbio/r84309_20250205_103258/1_D01'
                                                '/m84309_250205_121831_s4.hifi_reads.bc2076.bam'
                                            ),
                                            size_bytes=23451855096,
                                            md5='f48387aeea2595cbfd4397ab97336485',
                                            file_type='BAM',
                                            has_methylation=True,
                                            sam_tags=[
                                                'ML:B',
                                                'MM:Z',
                                                'RG:Z',
                                                'ac:B',
                                                'bc:B',
                                                'bl:Z',
                                                'bq:i',
                                                'bt:Z',
                                                'bx:B',
                                                'cx:i',
                                                'ec:f',
                                                'ls:B',
                                                'ma:i',
                                                'np:i',
                                                'qe:i',
                                                'ql:Z',
                                                'qs:i',
                                                'qt:Z',
                                                'rq:f',
                                                'sn:B',
                                                'we:i',
                                                'ws:i',
                                                'zm:i',
                                            ],
                                        )
                                    ],
                                    project_assn=[
                                        Allocation(
                                            id=80860,
                                            project_id='britain-and-ireland',
                                            data_id='m84309_250205_121831_s4#2076',
                                        ),
                                        Allocation(
                                            id=80861,
                                            project_id='darwin',
                                            data_id='m84309_250205_121831_s4#2076',
                                        ),
                                        Allocation(
                                            id=80862,
                                            project_id='tol',
                                            data_id='m84309_250205_121831_s4#2076',
                                        ),
                                    ],
                                    dataset_assn=[
                                        DatasetElement(
                                            id=4668,
                                            data_id='m84309_250205_121831_s4#2076',
                                            dataset_id='01K6AW4FD9B0PHTZ6BGWV31K7M',
                                            dataset=Dataset(
                                                dataset_id='01K6AW4FD9B0PHTZ6BGWV31K7M',
                                                name='pacbio.ccs',
                                                status_history=[
                                                    DatasetStatus(
                                                        dataset_status_id=3070,
                                                        dataset_id='01K6AW4FD9B0PHTZ6BGWV31K7M',
                                                        status_type_id='Pending',
                                                        status_time=(
                                                            '2025-09-29T14:55:59.067208+01:00'
                                                        ),
                                                    )
                                                ],
                                            ),
                                        )
                                    ],
                                )
                            ],
                        )
                    ],
                    accession=Accession(
                        accession_id='SAMEA12753558',
                        accession_type_id='BioSample',
                        is_deleted=False,
                    ),
                    location=Location(
                        location_id=3113, path='6/c/c/f/1/b/Brachiomonas_submarina'
                    ),
                ),
            ],
            location=Location(location_id=3113, path='6/c/c/f/1/b/Brachiomonas_submarina'),
        ),
        Species(
            species_id='Juncus effusus',
            location_id=299,
            tolid_prefix='lpJunEffu',
            common_name='common rush',
            taxon_id=13579,
            family_taxon_id=14101,
            taxon_family='Juncaceae',
            taxon_order='Poales',
            taxon_phylum='Streptophyta',
            taxon_group='monocots',
            genome_size=293400000,
            chromosome_number=46,
            data_accession_id='PRJEB50167',
            umbrella_accession_id='PRJEB50168',
            specimens=[
                Specimen(
                    specimen_id='lpJunEffu1',
                    location_id=299,
                    species_id='Juncus effusus',
                    supplied_name='KDTOL10021',
                    sts_specimen='KDTOL10021',
                    accession_id='SAMEA7521930',
                    sex_id='Hermaphrodite, monoecious',
                    ploidy='2',
                    assigned_user_id=100,
                    samples=[
                        Sample(
                            sample_id='DTOL10341656',
                            specimen_id='lpJunEffu1',
                            accession_id='SAMEA7521954',
                            accession=Accession(
                                accession_id='SAMEA7521954',
                                accession_type_id='BioSample',
                                is_deleted=False,
                            ),
                            data=[
                                Data(
                                    data_id='40666_2#2',
                                    study_id=5901,
                                    category='genomic_data',
                                    sample_id='DTOL10341656',
                                    library_id='DN826505P:B3',
                                    accession_id='ERR8097174',
                                    run_id='40666_2',
                                    processed=1,
                                    tag1_id='90',
                                    tag2_id='90',
                                    date='2021-09-11T11:11:14+01:00',
                                    lims_qc='pass',
                                    visibility='Always',
                                    reads=3345851480,
                                    bases=505223573480,
                                    read_length_mean=151.0,
                                    bases_a=165046940660,
                                    bases_c=88665580861,
                                    bases_g=88955239448,
                                    bases_t=162546734482,
                                    folder_ulid='01J8GVRDZR9KA1EXWZM48W09MZ',
                                    library=Library(
                                        library_id='DN826505P:B3',
                                        library_type_id='Hi-C - Arima v2',
                                    ),
                                    accession=Accession(
                                        accession_id='ERR8097174',
                                        accession_type_id='Run',
                                        secondary='ERX7663266',
                                        date_submitted='2022-01-24T00:00:00+00:00',
                                        is_deleted=False,
                                    ),
                                    run=Run(
                                        run_id='40666_2',
                                        platform_id=5,
                                        centre_id=2,
                                        element='2',
                                        instrument_name='NV11',
                                        complete='2021-09-05T07:44:37+01:00',
                                    ),
                                    files=[
                                        File(
                                            id=117820,
                                            data_id='40666_2#2',
                                            name='40666_2#2.cram',
                                            remote_path=(
                                                'irods:/seq/illumina/runs/40/40666/lane2/plex2'
                                                '/40666_2#2.cram'
                                            ),
                                            insdc_path=(
                                                'https://ftp.sra.ebi.ac.uk/vol1/run/ERR809'
                                                '/ERR8097174/40666_2%232.cram'
                                            ),
                                            size_bytes=158472491403,
                                            md5='da73a821a18429f9fc956e806b7f4a82',
                                            file_type='CRAM',
                                            has_methylation=False,
                                            sam_tags=['BC:Z', 'QT:Z', 'RG:Z'],
                                        )
                                    ],
                                    project_assn=[
                                        Allocation(
                                            id=16987,
                                            project_id='britain-and-ireland',
                                            data_id='40666_2#2',
                                        ),
                                        Allocation(
                                            id=16988, project_id='darwin', data_id='40666_2#2'
                                        ),
                                        Allocation(
                                            id=16989, project_id='tol', data_id='40666_2#2'
                                        ),
                                    ],
                                    dataset_assn=[
                                        DatasetElement(
                                            id=12480,
                                            data_id='40666_2#2',
                                            dataset_id='01K6B331TCWW21W4K60YFKMNRW',
                                            dataset=Dataset(
                                                dataset_id='01K6B331TCWW21W4K60YFKMNRW',
                                                name='hic-arima2',
                                                assembly_assn=[
                                                    AssemblyDataset(
                                                        id=13839,
                                                        assembly_id=7103,
                                                        dataset_id='01K6B331TCWW21W4K60YFKMNRW',
                                                    ),
                                                    AssemblyDataset(
                                                        id=13842,
                                                        assembly_id=7104,
                                                        dataset_id='01K6B331TCWW21W4K60YFKMNRW',
                                                    ),
                                                ],
                                                status_history=[
                                                    DatasetStatus(
                                                        dataset_status_id=8206,
                                                        dataset_id='01K6B331TCWW21W4K60YFKMNRW',
                                                        status_type_id='Pending',
                                                        status_time=(
                                                            '2025-09-29T16:57:32.418140+01:00'
                                                        ),
                                                    )
                                                ],
                                            ),
                                        )
                                    ],
                                    folder=Folder(
                                        folder_ulid='01J8GVRDZR9KA1EXWZM48W09MZ',
                                        folder_location_id='illumina_data_s3',
                                        image_file_list=[
                                            {
                                                'file': '40666_2#2_F0xB00-acgt-cycles.png',
                                                'caption': 'Hi-C - Arima v2 A|C|G|T Content Per Cycle',  # noqa: E501
                                            },
                                            {
                                                'file': '40666_2#2_F0xB00-quals3.png',
                                                'caption': 'Hi-C - Arima v2 Quality Frequencies, Separate Curve Per Cycle',  # noqa: E501
                                            },
                                            {
                                                'file': '40666_2#2_F0xB00-quals-hm.png',
                                                'caption': 'Hi-C - Arima v2 Quality Frequencies, Per Cycle Heat Map',  # noqa: E501
                                            },
                                            {
                                                'file': '40666_2#2_F0xB00-quals2.png',
                                                'caption': 'Hi-C - Arima v2 Quality Per Cycle (Split)',  # noqa: E501
                                            },
                                            {
                                                'file': '40666_2#2_F0xB00-gc-content.png',
                                                'caption': 'Hi-C - Arima v2 G|C Content',
                                            },
                                            {
                                                'file': '40666_2#2_F0xB00-quals.png',
                                                'caption': 'Hi-C - Arima v2 Quality Per Cycle (Overlaid)',  # noqa: E501
                                            },
                                        ],
                                        files_total_bytes=155088,
                                    ),
                                )
                            ],
                        ),
                        Sample(
                            sample_id='DTOL9702654',
                            specimen_id='lpJunEffu1',
                            accession_id='SAMEA7521953',
                            accession=Accession(
                                accession_id='SAMEA7521953',
                                accession_type_id='BioSample',
                                is_deleted=False,
                            ),
                            data=[
                                Data(
                                    data_id='36691_2#5',
                                    study_id=5901,
                                    category='genomic_data',
                                    sample_id='DTOL9702654',
                                    library_id='DN771163M:G8',
                                    accession_id='ERR8097169',
                                    run_id='36691_2',
                                    processed=1,
                                    tag1_id='249',
                                    date='2021-03-18T12:16:43+00:00',
                                    lims_qc='pass',
                                    visibility='Always',
                                    reads=195080402,
                                    bases=29457140702,
                                    read_length_mean=151.0,
                                    bases_a=9258985827,
                                    bases_c=5442014861,
                                    bases_g=5558090183,
                                    bases_t=9197450561,
                                    folder_ulid='01J8GQ31A3VN2XMDY7PP7XMFSV',
                                    library=Library(
                                        library_id='DN771163M:G8',
                                        library_type_id='Chromium genome',
                                    ),
                                    accession=Accession(
                                        accession_id='ERR8097169',
                                        accession_type_id='Run',
                                        secondary='ERX7663261',
                                        date_submitted='2022-01-24T00:00:00+00:00',
                                        is_deleted=False,
                                    ),
                                    run=Run(
                                        run_id='36691_2',
                                        platform_id=5,
                                        centre_id=2,
                                        element='2',
                                        instrument_name='NV20',
                                        complete='2021-03-06T05:07:44+00:00',
                                    ),
                                    files=[
                                        File(
                                            id=115164,
                                            data_id='36691_2#5',
                                            name='36691_2#5.cram',
                                            remote_path=(
                                                'irods:/seq/illumina/runs/36/36691/lane2/plex5'
                                                '/36691_2#5.cram'
                                            ),
                                            insdc_path=(
                                                'https://ftp.sra.ebi.ac.uk/vol1/run/ERR809'
                                                '/ERR8097169/36691_2%235.cram'
                                            ),
                                            size_bytes=9307345471,
                                            md5='d5ddea4e50f28e1438c8042cbfcc31a8',
                                            file_type='CRAM',
                                            has_methylation=False,
                                            sam_tags=['BC:Z', 'QT:Z', 'RG:Z'],
                                        )
                                    ],
                                    project_assn=[
                                        Allocation(
                                            id=9234,
                                            project_id='britain-and-ireland',
                                            data_id='36691_2#5',
                                        ),
                                        Allocation(
                                            id=9235, project_id='darwin', data_id='36691_2#5'
                                        ),
                                        Allocation(
                                            id=9236, project_id='tol', data_id='36691_2#5'
                                        ),
                                    ],
                                    dataset_assn=[
                                        DatasetElement(
                                            id=20160,
                                            data_id='36691_2#5',
                                            dataset_id='01K6BJJ6NW4EXP9XBGYDJZED12',
                                            dataset=Dataset(
                                                dataset_id='01K6BJJ6NW4EXP9XBGYDJZED12',
                                                name='10x',
                                                assembly_assn=[
                                                    AssemblyDataset(
                                                        id=13838,
                                                        assembly_id=7103,
                                                        dataset_id='01K6BJJ6NW4EXP9XBGYDJZED12',
                                                    ),
                                                    AssemblyDataset(
                                                        id=13841,
                                                        assembly_id=7104,
                                                        dataset_id='01K6BJJ6NW4EXP9XBGYDJZED12',
                                                    ),
                                                ],
                                                status_history=[
                                                    DatasetStatus(
                                                        dataset_status_id=15210,
                                                        dataset_id='01K6BJJ6NW4EXP9XBGYDJZED12',
                                                        status_type_id='Pending',
                                                        status_time=(
                                                            '2025-09-29T21:27:57.559761+01:00'
                                                        ),
                                                    )
                                                ],
                                            ),
                                        )
                                    ],
                                    folder=Folder(
                                        folder_ulid='01J8GQ31A3VN2XMDY7PP7XMFSV',
                                        folder_location_id='illumina_data_s3',
                                        image_file_list=[
                                            {
                                                'file': '36691_2#5_F0xB00-quals2.png',
                                                'caption': 'Chromium genome Quality Per Cycle (Split)',  # noqa: E501
                                            },
                                            {
                                                'file': '36691_2#5_F0xB00-quals-hm.png',
                                                'caption': 'Chromium genome Quality Frequencies, Per Cycle Heat Map',  # noqa: E501
                                            },
                                            {
                                                'file': '36691_2#5_F0xB00-gc-content.png',
                                                'caption': 'Chromium genome G|C Content',
                                            },
                                            {
                                                'file': '36691_2#5_F0xB00-quals3.png',
                                                'caption': 'Chromium genome Quality Frequencies, Separate Curve Per Cycle',  # noqa: E501
                                            },
                                            {
                                                'file': '36691_2#5_F0xB00-acgt-cycles.png',
                                                'caption': 'Chromium genome A|C|G|T Content Per Cycle',  # noqa: E501
                                            },
                                            {
                                                'file': '36691_2#5_F0xB00-quals.png',
                                                'caption': 'Chromium genome Quality Per Cycle (Overlaid)',  # noqa: E501
                                            },
                                        ],
                                        files_total_bytes=167913,
                                    ),
                                ),
                                Data(
                                    data_id='36691_2#6',
                                    study_id=5901,
                                    category='genomic_data',
                                    sample_id='DTOL9702654',
                                    library_id='DN771163M:G8',
                                    accession_id='ERR8097170',
                                    run_id='36691_2',
                                    processed=1,
                                    tag1_id='250',
                                    date='2021-03-18T12:16:43+00:00',
                                    lims_qc='pass',
                                    visibility='Always',
                                    reads=206862242,
                                    bases=31236198542,
                                    read_length_mean=151.0,
                                    bases_a=9812272262,
                                    bases_c=5778032407,
                                    bases_g=5899517116,
                                    bases_t=9745758677,
                                    folder_ulid='01J8GQ32MZ3YKMTSPGRS5HWCD1',
                                    library=Library(
                                        library_id='DN771163M:G8',
                                        library_type_id='Chromium genome',
                                    ),
                                    accession=Accession(
                                        accession_id='ERR8097170',
                                        accession_type_id='Run',
                                        secondary='ERX7663262',
                                        date_submitted='2022-01-24T00:00:00+00:00',
                                        is_deleted=False,
                                    ),
                                    run=Run(
                                        run_id='36691_2',
                                        platform_id=5,
                                        centre_id=2,
                                        element='2',
                                        instrument_name='NV20',
                                        complete='2021-03-06T05:07:44+00:00',
                                    ),
                                    files=[
                                        File(
                                            id=115165,
                                            data_id='36691_2#6',
                                            name='36691_2#6.cram',
                                            remote_path=(
                                                'irods:/seq/illumina/runs/36/36691/lane2/plex6'
                                                '/36691_2#6.cram'
                                            ),
                                            insdc_path=(
                                                'https://ftp.sra.ebi.ac.uk/vol1/run/ERR809'
                                                '/ERR8097170/36691_2%236.cram'
                                            ),
                                            size_bytes=9778070700,
                                            md5='09e26bf8255cd03b333744f9432b5393',
                                            file_type='CRAM',
                                            has_methylation=False,
                                            sam_tags=['BC:Z', 'QT:Z', 'RG:Z'],
                                        )
                                    ],
                                    project_assn=[
                                        Allocation(
                                            id=9237,
                                            project_id='britain-and-ireland',
                                            data_id='36691_2#6',
                                        ),
                                        Allocation(
                                            id=9238, project_id='darwin', data_id='36691_2#6'
                                        ),
                                        Allocation(
                                            id=9239, project_id='tol', data_id='36691_2#6'
                                        ),
                                    ],
                                    dataset_assn=[
                                        DatasetElement(
                                            id=20161,
                                            data_id='36691_2#6',
                                            dataset_id='01K6BJJ6NW4EXP9XBGYDJZED12',
                                            dataset=Dataset(
                                                dataset_id='01K6BJJ6NW4EXP9XBGYDJZED12',
                                                name='10x',
                                                assembly_assn=[
                                                    AssemblyDataset(
                                                        id=13838,
                                                        assembly_id=7103,
                                                        dataset_id='01K6BJJ6NW4EXP9XBGYDJZED12',
                                                    ),
                                                    AssemblyDataset(
                                                        id=13841,
                                                        assembly_id=7104,
                                                        dataset_id='01K6BJJ6NW4EXP9XBGYDJZED12',
                                                    ),
                                                ],
                                                status_history=[
                                                    DatasetStatus(
                                                        dataset_status_id=15210,
                                                        dataset_id='01K6BJJ6NW4EXP9XBGYDJZED12',
                                                        status_type_id='Pending',
                                                        status_time=(
                                                            '2025-09-29T21:27:57.559761+01:00'
                                                        ),
                                                    )
                                                ],
                                            ),
                                        )
                                    ],
                                    folder=Folder(
                                        folder_ulid='01J8GQ32MZ3YKMTSPGRS5HWCD1',
                                        folder_location_id='illumina_data_s3',
                                        image_file_list=[
                                            {
                                                'file': '36691_2#6_F0xB00-quals.png',
                                                'caption': 'Chromium genome Quality Per Cycle (Overlaid)',  # noqa: E501
                                            },
                                            {
                                                'file': '36691_2#6_F0xB00-quals2.png',
                                                'caption': 'Chromium genome Quality Per Cycle (Split)',  # noqa: E501
                                            },
                                            {
                                                'file': '36691_2#6_F0xB00-quals3.png',
                                                'caption': 'Chromium genome Quality Frequencies, Separate Curve Per Cycle',  # noqa: E501
                                            },
                                            {
                                                'file': '36691_2#6_F0xB00-gc-content.png',
                                                'caption': 'Chromium genome G|C Content',
                                            },
                                            {
                                                'file': '36691_2#6_F0xB00-acgt-cycles.png',
                                                'caption': 'Chromium genome A|C|G|T Content Per Cycle',  # noqa: E501
                                            },
                                            {
                                                'file': '36691_2#6_F0xB00-quals-hm.png',
                                                'caption': 'Chromium genome Quality Frequencies, Per Cycle Heat Map',  # noqa: E501
                                            },
                                        ],
                                        files_total_bytes=156979,
                                    ),
                                ),
                                Data(
                                    data_id='36691_2#7',
                                    study_id=5901,
                                    category='genomic_data',
                                    sample_id='DTOL9702654',
                                    library_id='DN771163M:G8',
                                    accession_id='ERR8097171',
                                    run_id='36691_2',
                                    processed=1,
                                    tag1_id='251',
                                    date='2021-03-18T12:16:43+00:00',
                                    lims_qc='pass',
                                    visibility='Always',
                                    reads=183614994,
                                    bases=27725864094,
                                    read_length_mean=151.0,
                                    bases_a=8716084313,
                                    bases_c=5126488093,
                                    bases_g=5237913221,
                                    bases_t=8644832190,
                                    folder_ulid='01J8GQ33XK1D5AVJN9XCP7YQ84',
                                    library=Library(
                                        library_id='DN771163M:G8',
                                        library_type_id='Chromium genome',
                                    ),
                                    accession=Accession(
                                        accession_id='ERR8097171',
                                        accession_type_id='Run',
                                        secondary='ERX7663263',
                                        date_submitted='2022-01-24T00:00:00+00:00',
                                        is_deleted=False,
                                    ),
                                    run=Run(
                                        run_id='36691_2',
                                        platform_id=5,
                                        centre_id=2,
                                        element='2',
                                        instrument_name='NV20',
                                        complete='2021-03-06T05:07:44+00:00',
                                    ),
                                    files=[
                                        File(
                                            id=115166,
                                            data_id='36691_2#7',
                                            name='36691_2#7.cram',
                                            remote_path=(
                                                'irods:/seq/illumina/runs/36/36691/lane2/plex7'
                                                '/36691_2#7.cram'
                                            ),
                                            insdc_path=(
                                                'https://ftp.sra.ebi.ac.uk/vol1/run/ERR809'
                                                '/ERR8097171/36691_2%237.cram'
                                            ),
                                            size_bytes=8754454310,
                                            md5='8b87819338c08db3f325a451e864f227',
                                            file_type='CRAM',
                                            has_methylation=False,
                                            sam_tags=['BC:Z', 'QT:Z', 'RG:Z'],
                                        )
                                    ],
                                    project_assn=[
                                        Allocation(
                                            id=9240,
                                            project_id='britain-and-ireland',
                                            data_id='36691_2#7',
                                        ),
                                        Allocation(
                                            id=9241, project_id='darwin', data_id='36691_2#7'
                                        ),
                                        Allocation(
                                            id=9242, project_id='tol', data_id='36691_2#7'
                                        ),
                                    ],
                                    dataset_assn=[
                                        DatasetElement(
                                            id=20162,
                                            data_id='36691_2#7',
                                            dataset_id='01K6BJJ6NW4EXP9XBGYDJZED12',
                                            dataset=Dataset(
                                                dataset_id='01K6BJJ6NW4EXP9XBGYDJZED12',
                                                name='10x',
                                                assembly_assn=[
                                                    AssemblyDataset(
                                                        id=13838,
                                                        assembly_id=7103,
                                                        dataset_id='01K6BJJ6NW4EXP9XBGYDJZED12',
                                                    ),
                                                    AssemblyDataset(
                                                        id=13841,
                                                        assembly_id=7104,
                                                        dataset_id='01K6BJJ6NW4EXP9XBGYDJZED12',
                                                    ),
                                                ],
                                                status_history=[
                                                    DatasetStatus(
                                                        dataset_status_id=15210,
                                                        dataset_id='01K6BJJ6NW4EXP9XBGYDJZED12',
                                                        status_type_id='Pending',
                                                        status_time=(
                                                            '2025-09-29T21:27:57.559761+01:00'
                                                        ),
                                                    )
                                                ],
                                            ),
                                        )
                                    ],
                                    folder=Folder(
                                        folder_ulid='01J8GQ33XK1D5AVJN9XCP7YQ84',
                                        folder_location_id='illumina_data_s3',
                                        image_file_list=[
                                            {
                                                'file': '36691_2#7_F0xB00-acgt-cycles.png',
                                                'caption': 'Chromium genome A|C|G|T Content Per Cycle',  # noqa: E501
                                            },
                                            {
                                                'file': '36691_2#7_F0xB00-gc-content.png',
                                                'caption': 'Chromium genome G|C Content',
                                            },
                                            {
                                                'file': '36691_2#7_F0xB00-quals2.png',
                                                'caption': 'Chromium genome Quality Per Cycle (Split)',  # noqa: E501
                                            },
                                            {
                                                'file': '36691_2#7_F0xB00-quals3.png',
                                                'caption': 'Chromium genome Quality Frequencies, Separate Curve Per Cycle',  # noqa: E501
                                            },
                                            {
                                                'file': '36691_2#7_F0xB00-quals-hm.png',
                                                'caption': 'Chromium genome Quality Frequencies, Per Cycle Heat Map',  # noqa: E501
                                            },
                                            {
                                                'file': '36691_2#7_F0xB00-quals.png',
                                                'caption': 'Chromium genome Quality Per Cycle (Overlaid)',  # noqa: E501
                                            },
                                        ],
                                        files_total_bytes=164863,
                                    ),
                                ),
                                Data(
                                    data_id='36691_2#8',
                                    study_id=5901,
                                    category='genomic_data',
                                    sample_id='DTOL9702654',
                                    library_id='DN771163M:G8',
                                    accession_id='ERR8097172',
                                    run_id='36691_2',
                                    processed=1,
                                    tag1_id='252',
                                    date='2021-03-18T12:16:43+00:00',
                                    lims_qc='pass',
                                    visibility='Always',
                                    reads=210626924,
                                    bases=31804665524,
                                    read_length_mean=151.0,
                                    bases_a=9992182143,
                                    bases_c=5876706784,
                                    bases_g=6004233902,
                                    bases_t=9930898084,
                                    folder_ulid='01J8GQ356P8AEKKAPW0VD2PJKD',
                                    library=Library(
                                        library_id='DN771163M:G8',
                                        library_type_id='Chromium genome',
                                    ),
                                    accession=Accession(
                                        accession_id='ERR8097172',
                                        accession_type_id='Run',
                                        secondary='ERX7663264',
                                        date_submitted='2022-01-24T00:00:00+00:00',
                                        is_deleted=False,
                                    ),
                                    run=Run(
                                        run_id='36691_2',
                                        platform_id=5,
                                        centre_id=2,
                                        element='2',
                                        instrument_name='NV20',
                                        complete='2021-03-06T05:07:44+00:00',
                                    ),
                                    files=[
                                        File(
                                            id=115167,
                                            data_id='36691_2#8',
                                            name='36691_2#8.cram',
                                            remote_path=(
                                                'irods:/seq/illumina/runs/36/36691/lane2/plex8'
                                                '/36691_2#8.cram'
                                            ),
                                            insdc_path=(
                                                'https://ftp.sra.ebi.ac.uk/vol1/run/ERR809'
                                                '/ERR8097172/36691_2%238.cram'
                                            ),
                                            size_bytes=9969777773,
                                            md5='66334c7f81b59b0f1d99b840e6d36550',
                                            file_type='CRAM',
                                            has_methylation=False,
                                            sam_tags=['BC:Z', 'QT:Z', 'RG:Z'],
                                        )
                                    ],
                                    project_assn=[
                                        Allocation(
                                            id=9243,
                                            project_id='britain-and-ireland',
                                            data_id='36691_2#8',
                                        ),
                                        Allocation(
                                            id=9244, project_id='darwin', data_id='36691_2#8'
                                        ),
                                        Allocation(
                                            id=9245, project_id='tol', data_id='36691_2#8'
                                        ),
                                    ],
                                    dataset_assn=[
                                        DatasetElement(
                                            id=20163,
                                            data_id='36691_2#8',
                                            dataset_id='01K6BJJ6NW4EXP9XBGYDJZED12',
                                            dataset=Dataset(
                                                dataset_id='01K6BJJ6NW4EXP9XBGYDJZED12',
                                                name='10x',
                                                assembly_assn=[
                                                    AssemblyDataset(
                                                        id=13838,
                                                        assembly_id=7103,
                                                        dataset_id='01K6BJJ6NW4EXP9XBGYDJZED12',
                                                    ),
                                                    AssemblyDataset(
                                                        id=13841,
                                                        assembly_id=7104,
                                                        dataset_id='01K6BJJ6NW4EXP9XBGYDJZED12',
                                                    ),
                                                ],
                                                status_history=[
                                                    DatasetStatus(
                                                        dataset_status_id=15210,
                                                        dataset_id='01K6BJJ6NW4EXP9XBGYDJZED12',
                                                        status_type_id='Pending',
                                                        status_time=(
                                                            '2025-09-29T21:27:57.559761+01:00'
                                                        ),
                                                    )
                                                ],
                                            ),
                                        )
                                    ],
                                    folder=Folder(
                                        folder_ulid='01J8GQ356P8AEKKAPW0VD2PJKD',
                                        folder_location_id='illumina_data_s3',
                                        image_file_list=[
                                            {
                                                'file': '36691_2#8_F0xB00-quals2.png',
                                                'caption': 'Chromium genome Quality Per Cycle (Split)',  # noqa: E501
                                            },
                                            {
                                                'file': '36691_2#8_F0xB00-acgt-cycles.png',
                                                'caption': 'Chromium genome A|C|G|T Content Per Cycle',  # noqa: E501
                                            },
                                            {
                                                'file': '36691_2#8_F0xB00-quals3.png',
                                                'caption': 'Chromium genome Quality Frequencies, Separate Curve Per Cycle',  # noqa: E501
                                            },
                                            {
                                                'file': '36691_2#8_F0xB00-quals.png',
                                                'caption': 'Chromium genome Quality Per Cycle (Overlaid)',  # noqa: E501
                                            },
                                            {
                                                'file': '36691_2#8_F0xB00-gc-content.png',
                                                'caption': 'Chromium genome G|C Content',
                                            },
                                            {
                                                'file': '36691_2#8_F0xB00-quals-hm.png',
                                                'caption': 'Chromium genome Quality Frequencies, Per Cycle Heat Map',  # noqa: E501
                                            },
                                        ],
                                        files_total_bytes=150719,
                                    ),
                                ),
                            ],
                        ),
                        Sample(
                            sample_id='DTOL9838614',
                            specimen_id='lpJunEffu1',
                            accession_id='SAMEA7521953',
                            accession=Accession(
                                accession_id='SAMEA7521953',
                                accession_type_id='BioSample',
                                is_deleted=False,
                            ),
                            data=[
                                Data(
                                    data_id='m64097e_210221_172213#1019',
                                    study_id=5901,
                                    category='genomic_data',
                                    sample_id='DTOL9838614',
                                    library_id='DN765124Q-B1',
                                    accession_id='ERR8282830',
                                    run_id='m64097e_210221_172213',
                                    processed=1,
                                    tag1_id='1019',
                                    date='2021-02-22T23:07:55+00:00',
                                    lims_qc='pass',
                                    visibility='Always',
                                    reads=1861770,
                                    bases=22552841091,
                                    read_length_mean=12113.655871026,
                                    read_length_n50=13209,
                                    bases_a=7343914800,
                                    bases_c=3936864489,
                                    bases_g=3932481777,
                                    bases_t=7339580025,
                                    read_length_longest=37726,
                                    read_length_shortest=51,
                                    reads_duplicated=0,
                                    reads_discarded=369,
                                    reads_trimmed=12744,
                                    bases_removed=6409521,
                                    library=Library(
                                        library_id='DN765124Q-B1', library_type_id='PacBio - HiFi'
                                    ),
                                    accession=Accession(
                                        accession_id='ERR8282830',
                                        accession_type_id='Run',
                                        secondary='ERX7850261',
                                        date_submitted='2022-02-02T00:00:00+00:00',
                                        is_deleted=False,
                                    ),
                                    run=Run(
                                        run_id='m64097e_210221_172213',
                                        platform_id=3,
                                        centre_id=2,
                                        lims_id='79924',
                                        element='D1',
                                        instrument_name='m64097e',
                                        start='2021-02-18T16:18:11+00:00',
                                        complete='2021-02-22T23:07:55+00:00',
                                        plex_count=1,
                                        chemistry='S/P4-C2/5.0-8M',
                                        pacbio_run_metrics=[
                                            PacbioRunMetrics(
                                                run_id='m64097e_210221_172213',
                                                movie_minutes=1440,
                                                binding_kit='Sequel II Binding Kit 2.0',
                                                sequencing_kit=(
                                                    'Sequel II Sequencing Plate 2.0 (4 rxn)'
                                                ),
                                                sequencing_kit_lot_number='018779',
                                                cell_lot_number='416347',
                                                include_kinetics='true',
                                                loading_conc=45.0,
                                                control_num_reads=3200,
                                                control_read_length_mean=51271.0,
                                                control_concordance_mean=0.85524,
                                                control_concordance_mode=0.89,
                                                local_base_rate=2.03257,
                                                polymerase_read_bases=329209363529,
                                                polymerase_num_reads=4556774,
                                                polymerase_read_length_mean=72246.0,
                                                polymerase_read_length_n50=146877,
                                                insert_length_mean=13239.0,
                                                insert_length_n50=15638,
                                                unique_molecular_bases=57195683840,
                                                productive_zmws_num=8011471,
                                                p0_num=3352198,
                                                p1_num=4559996,
                                                p2_num=102477,
                                                adapter_dimer_percent=0.0,
                                                short_insert_percent=0.01,
                                                hifi_read_bases=22632028638,
                                                hifi_num_reads=1863309,
                                                hifi_read_length_mean=12146,
                                                hifi_read_quality_median=32,
                                                hifi_number_passes_mean=11.0,
                                                hifi_low_quality_read_bases=4628882121,
                                                hifi_low_quality_num_reads=345974,
                                                hifi_low_quality_read_length_mean=13379,
                                                hifi_low_quality_read_quality_median=16,
                                                folder_ulid='EMPTY_PACBIO_RUN_S3',
                                            )
                                        ],
                                    ),
                                    files=[
                                        File(
                                            id=121145,
                                            data_id='m64097e_210221_172213#1019',
                                            name=(
                                                'm64097e_210221_172213.ccs.bc1019_BAK8B_OA'
                                                '--bc1019_BAK8B_OA.bam'
                                            ),
                                            remote_path=(
                                                'irods:/seq/pacbio/r64097e_20210218_161440/4_D01'
                                                '/demultiplex.bc1019_BAK8B_OA'
                                                '--bc1019_BAK8B_OA.bam'
                                            ),
                                            insdc_path=(
                                                'https://ftp.sra.ebi.ac.uk/vol1/run/ERR828'
                                                '/ERR8282830'
                                                '/m64097e_210221_172213.ccs.bc1019_BAK8B_OA'
                                                '--bc1019_BAK8B_OA.bam'
                                            ),
                                            size_bytes=87814836350,
                                            md5='9a6ffb74593409209ab8857b114d799d',
                                            file_type='BAM',
                                            has_methylation=False,
                                            has_kinetics=True,
                                            sam_tags=[
                                                'RG:Z',
                                                'bc:B',
                                                'bl:Z',
                                                'bq:i',
                                                'bt:Z',
                                                'bx:B',
                                                'cx:i',
                                                'ec:f',
                                                'fi:B',
                                                'fn:i',
                                                'fp:B',
                                                'np:i',
                                                'qe:i',
                                                'ql:Z',
                                                'qs:i',
                                                'qt:Z',
                                                'ri:B',
                                                'rn:i',
                                                'rp:B',
                                                'rq:f',
                                                'sn:B',
                                                'we:i',
                                                'ws:i',
                                                'zm:i',
                                            ],
                                        )
                                    ],
                                    project_assn=[
                                        Allocation(
                                            id=50680,
                                            project_id='britain-and-ireland',
                                            data_id='m64097e_210221_172213#1019',
                                        ),
                                        Allocation(
                                            id=50681,
                                            project_id='darwin',
                                            data_id='m64097e_210221_172213#1019',
                                        ),
                                        Allocation(
                                            id=50682,
                                            project_id='tol',
                                            data_id='m64097e_210221_172213#1019',
                                        ),
                                    ],
                                    dataset_assn=[
                                        DatasetElement(
                                            id=310,
                                            data_id='m64097e_210221_172213#1019',
                                            dataset_id='01K6AS7B9XT21VZZ2CWMV40V08',
                                            dataset=Dataset(
                                                dataset_id='01K6AS7B9XT21VZZ2CWMV40V08',
                                                name='pacbio.ccs',
                                                assembly_assn=[
                                                    AssemblyDataset(
                                                        id=13840,
                                                        assembly_id=7103,
                                                        dataset_id='01K6AS7B9XT21VZZ2CWMV40V08',
                                                    ),
                                                    AssemblyDataset(
                                                        id=13843,
                                                        assembly_id=7104,
                                                        dataset_id='01K6AS7B9XT21VZZ2CWMV40V08',
                                                    ),
                                                ],
                                                status_history=[
                                                    DatasetStatus(
                                                        dataset_status_id=204,
                                                        dataset_id='01K6AS7B9XT21VZZ2CWMV40V08',
                                                        status_type_id='Pending',
                                                        status_time=(
                                                            '2025-09-29T14:05:07.440053+01:00'
                                                        ),
                                                    )
                                                ],
                                            ),
                                        )
                                    ],
                                )
                            ],
                        ),
                        Sample(
                            sample_id='DTOLRNA10187174',
                            specimen_id='lpJunEffu1',
                            accession_id='SAMEA7521953',
                            accession=Accession(
                                accession_id='SAMEA7521953',
                                accession_type_id='BioSample',
                                is_deleted=False,
                            ),
                            data=[
                                Data(
                                    data_id='37935_8#13',
                                    study_id=6327,
                                    category='transcriptomic_data',
                                    sample_id='DTOLRNA10187174',
                                    library_id='DN612239G:G9',
                                    accession_id='ERR8097173',
                                    run_id='37935_8',
                                    processed=1,
                                    tag1_id='71',
                                    tag2_id='71',
                                    date='2021-05-25T13:45:59+01:00',
                                    lims_qc='pass',
                                    visibility='Always',
                                    reads=36344960,
                                    bases=5488088960,
                                    read_length_mean=151.0,
                                    bases_a=1518941960,
                                    bases_c=1267752556,
                                    bases_g=1232383463,
                                    bases_t=1468060555,
                                    folder_ulid='01J8GSDTKDZYAX2X2F8K7WD045',
                                    library=Library(
                                        library_id='DN612239G:G9', library_type_id='RNA PolyA'
                                    ),
                                    accession=Accession(
                                        accession_id='ERR8097173',
                                        accession_type_id='Run',
                                        secondary='ERX7663265',
                                        date_submitted='2022-01-24T00:00:00+00:00',
                                        is_deleted=False,
                                    ),
                                    run=Run(
                                        run_id='37935_8',
                                        platform_id=4,
                                        centre_id=2,
                                        element='8',
                                        instrument_name='HF2',
                                        complete='2021-05-16T21:08:02+01:00',
                                    ),
                                    files=[
                                        File(
                                            id=124080,
                                            data_id='37935_8#13',
                                            name='37935_8#13.cram',
                                            remote_path='irods:/seq/37935/37935_8#13.cram',
                                            insdc_path=(
                                                'https://ftp.sra.ebi.ac.uk/vol1/run/ERR809'
                                                '/ERR8097173/37935_8%2313.cram'
                                            ),
                                            size_bytes=2246652402,
                                            md5='40c3393cf594d9e84e6d4cb932328e33',
                                            file_type='CRAM',
                                            has_methylation=False,
                                            sam_tags=['BC:Z', 'QT:Z', 'RG:Z'],
                                        )
                                    ],
                                    project_assn=[
                                        Allocation(
                                            id=12798,
                                            project_id='britain-and-ireland',
                                            data_id='37935_8#13',
                                        ),
                                        Allocation(
                                            id=12799, project_id='darwin', data_id='37935_8#13'
                                        ),
                                        Allocation(
                                            id=12800, project_id='tol', data_id='37935_8#13'
                                        ),
                                    ],
                                    dataset_assn=[
                                        DatasetElement(
                                            id=28564,
                                            data_id='37935_8#13',
                                            dataset_id='01K6BNNXDTQ6G48M1YDB0DQXYM',
                                            dataset=Dataset(
                                                dataset_id='01K6BNNXDTQ6G48M1YDB0DQXYM',
                                                name='rna-seq',
                                                status_history=[
                                                    DatasetStatus(
                                                        dataset_status_id=18321,
                                                        dataset_id='01K6BNNXDTQ6G48M1YDB0DQXYM',
                                                        status_type_id='Pending',
                                                        status_time=(
                                                            '2025-09-29T22:22:24.879947+01:00'
                                                        ),
                                                    )
                                                ],
                                            ),
                                        )
                                    ],
                                    folder=Folder(
                                        folder_ulid='01J8GSDTKDZYAX2X2F8K7WD045',
                                        folder_location_id='illumina_data_s3',
                                        image_file_list=[
                                            {
                                                'file': '37935_8#13_F0xB00-quals3.png',
                                                'caption': 'RNA PolyA Quality Frequencies, Separate Curve Per Cycle',  # noqa: E501
                                            },
                                            {
                                                'file': '37935_8#13_F0xB00-quals2.png',
                                                'caption': 'RNA PolyA Quality Per Cycle (Split)',
                                            },
                                            {
                                                'file': '37935_8#13_F0xB00-acgt-cycles.png',
                                                'caption': 'RNA PolyA A|C|G|T Content Per Cycle',
                                            },
                                            {
                                                'file': '37935_8#13_F0xB00-quals-hm.png',
                                                'caption': 'RNA PolyA Quality Frequencies, Per Cycle Heat Map',  # noqa: E501
                                            },
                                            {
                                                'file': '37935_8#13_F0xB00-gc-content.png',
                                                'caption': 'RNA PolyA G|C Content',
                                            },
                                            {
                                                'file': '37935_8#13_F0xB00-quals.png',
                                                'caption': 'RNA PolyA Quality Per Cycle (Overlaid)',  # noqa: E501
                                            },
                                        ],
                                        files_total_bytes=191605,
                                    ),
                                )
                            ],
                        ),
                        Sample(
                            sample_id='DTOLRNA14460441',
                            specimen_id='lpJunEffu1',
                            accession_id='SAMEA7521957',
                            accession=Accession(
                                accession_id='SAMEA7521957',
                                accession_type_id='BioSample',
                                is_deleted=False,
                            ),
                            data=[
                                Data(
                                    data_id='48593_1#25',
                                    study_id=6327,
                                    category='transcriptomic_data',
                                    sample_id='DTOLRNA14460441',
                                    library_id='SQPP-7739-H:B9',
                                    accession_id='ERR12765103',
                                    run_id='48593_1',
                                    processed=1,
                                    tag1_id='66',
                                    tag2_id='66',
                                    date='2024-03-15T15:52:57+00:00',
                                    lims_qc='pass',
                                    visibility='Always',
                                    reads=52850970,
                                    bases=7980496470,
                                    read_length_mean=151.0,
                                    bases_a=2178367667,
                                    bases_c=1864133032,
                                    bases_g=1828534352,
                                    bases_t=2108890126,
                                    folder_ulid='01J8HAZJY0CG2BHX6Q7TSA54DA',
                                    library=Library(
                                        library_id='SQPP-7739-H:B9', library_type_id='RNA PolyA'
                                    ),
                                    accession=Accession(
                                        accession_id='ERR12765103',
                                        accession_type_id='Run',
                                        secondary='ERX12138201',
                                        date_submitted='2024-03-18T00:00:00+00:00',
                                        is_deleted=False,
                                    ),
                                    run=Run(
                                        run_id='48593_1',
                                        platform_id=8,
                                        centre_id=2,
                                        element='1',
                                        instrument_name='NX1',
                                        complete='2024-03-08T10:04:27+00:00',
                                    ),
                                    files=[
                                        File(
                                            id=139273,
                                            data_id='48593_1#25',
                                            name='48593_1#25.cram',
                                            remote_path=(
                                                'irods:/seq/illumina/runs/48/48593/lane1/plex25'
                                                '/48593_1#25.cram'
                                            ),
                                            insdc_path=(
                                                'https://ftp.sra.ebi.ac.uk/vol1/run/ERR127'
                                                '/ERR12765103/48593_1%2325.cram'
                                            ),
                                            size_bytes=2338594230,
                                            md5='2271d40cf440b7fa532b9d808766b189',
                                            file_type='CRAM',
                                            has_methylation=False,
                                            sam_tags=['BC:Z', 'QT:Z', 'RG:Z'],
                                        )
                                    ],
                                    project_assn=[
                                        Allocation(
                                            id=30343,
                                            project_id='britain-and-ireland',
                                            data_id='48593_1#25',
                                        ),
                                        Allocation(
                                            id=30344, project_id='darwin', data_id='48593_1#25'
                                        ),
                                        Allocation(
                                            id=30345, project_id='tol', data_id='48593_1#25'
                                        ),
                                    ],
                                    dataset_assn=[
                                        DatasetElement(
                                            id=28565,
                                            data_id='48593_1#25',
                                            dataset_id='01K6BNNXDTQ6G48M1YDB0DQXYM',
                                            dataset=Dataset(
                                                dataset_id='01K6BNNXDTQ6G48M1YDB0DQXYM',
                                                name='rna-seq',
                                                status_history=[
                                                    DatasetStatus(
                                                        dataset_status_id=18321,
                                                        dataset_id='01K6BNNXDTQ6G48M1YDB0DQXYM',
                                                        status_type_id='Pending',
                                                        status_time=(
                                                            '2025-09-29T22:22:24.879947+01:00'
                                                        ),
                                                    )
                                                ],
                                            ),
                                        )
                                    ],
                                    folder=Folder(
                                        folder_ulid='01J8HAZJY0CG2BHX6Q7TSA54DA',
                                        folder_location_id='illumina_data_s3',
                                        image_file_list=[
                                            {
                                                'file': '48593_1#25_F0xB00-quals3.png',
                                                'caption': 'RNA PolyA Quality Frequencies, Separate Curve Per Cycle',  # noqa: E501
                                            },
                                            {
                                                'file': '48593_1#25_F0xB00-quals.png',
                                                'caption': 'RNA PolyA Quality Per Cycle (Overlaid)',  # noqa: E501
                                            },
                                            {
                                                'file': '48593_1#25_F0xB00-acgt-cycles.png',
                                                'caption': 'RNA PolyA A|C|G|T Content Per Cycle',
                                            },
                                            {
                                                'file': '48593_1#25_F0xB00-quals-hm.png',
                                                'caption': 'RNA PolyA Quality Frequencies, Per Cycle Heat Map',  # noqa: E501
                                            },
                                            {
                                                'file': '48593_1#25_F0xB00-quals2.png',
                                                'caption': 'RNA PolyA Quality Per Cycle (Split)',
                                            },
                                            {
                                                'file': '48593_1#25_F0xB00-gc-content.png',
                                                'caption': 'RNA PolyA G|C Content',
                                            },
                                        ],
                                        files_total_bytes=148603,
                                    ),
                                )
                            ],
                        ),
                    ],
                    accession=Accession(
                        accession_id='SAMEA7521930',
                        accession_type_id='BioSample',
                        is_deleted=False,
                    ),
                    location=Location(location_id=299, path='e/1/3/d/d/0/Juncus_effusus'),
                    assemblies=[
                        Assembly(
                            assembly_id=7103,
                            specimen_id='lpJunEffu1',
                            name='lpJunEffu1.1',
                            description='lpJunEffu1.1 assembly for Juncus effusus',
                            level='chromosome',
                            is_reference=False,
                            bioproject_accession_id='PRJEB55668',
                            genome_accession_id='GCA_946800655.1',
                            bioproject_accession=Accession(
                                accession_id='PRJEB55668',
                                accession_type_id='BioProject - Species Assembly',
                                secondary='ERP140591',
                                submission='ERA17616049',
                                date_submitted='2022-08-31T00:00:00+01:00',
                                name='lpJunEffu1',
                                title='Juncus effusus genome assembly, lpJunEffu1',
                                description=(
                                    'This project provides the genome assembly of Juncus effusus.'
                                    ' The assembly is provided by the Darwin Tree of Life Project'
                                    ' (https: //www.darwintreeoflife.org/). The data under this'
                                    ' project are made available subject to the Darwin Tree of'
                                    ' Life Open Data Release Policy (https'
                                    ': //www.darwintreeoflife.org/project-resources/).'
                                ),
                                alias='WSI_primary_lpJunEffu1.1',
                                submitter_id='WELLCOME SANGER INSTITUTE',
                                is_deleted=False,
                            ),
                            genome_accession=Accession(
                                accession_id='GCA_946800655.1',
                                accession_type_id='GenBank Genome Assembly',
                                is_deleted=False,
                            ),
                            status_history=[
                                AssemblyStatus(
                                    assembly_status_id=7103,
                                    assembly_id=7103,
                                    status_type_id='ENA Public',
                                    status_time='2022-10-12T00:00:00+01:00',
                                )
                            ],
                        ),
                        Assembly(
                            assembly_id=7104,
                            specimen_id='lpJunEffu1',
                            name='lpJunEffu1.1 alternate haplotype',
                            description=(
                                'lpJunEffu1.1 alternate haplotype assembly for Juncus effusus'
                            ),
                            level='contig',
                            is_reference=False,
                            bioproject_accession_id='PRJEB55669',
                            genome_accession_id='GCA_946800645.1',
                            bioproject_accession=Accession(
                                accession_id='PRJEB55669',
                                accession_type_id='BioProject - Species Assembly',
                                secondary='ERP140592',
                                submission='ERA17616049',
                                date_submitted='2022-08-31T00:00:00+01:00',
                                name='lpJunEffu1 alternate haplotype',
                                title=(
                                    'Juncus effusus genome assembly, lpJunEffu1, alternate'
                                    ' haplotype'
                                ),
                                description=(
                                    'This project provides the genome assembly of Juncus effusus.'
                                    ' The assembly is provided by the Darwin Tree of Life Project'
                                    ' (https: //www.darwintreeoflife.org/). The data under this'
                                    ' project are made available subject to the Darwin Tree of'
                                    ' Life Open Data Release Policy (https'
                                    ': //www.darwintreeoflife.org/project-resources/).'
                                ),
                                alias='WSI_haplotigs_lpJunEffu1.1',
                                submitter_id='WELLCOME SANGER INSTITUTE',
                                is_deleted=False,
                            ),
                            genome_accession=Accession(
                                accession_id='GCA_946800645.1',
                                accession_type_id='GenBank Genome Assembly',
                                is_deleted=False,
                            ),
                            status_history=[
                                AssemblyStatus(
                                    assembly_status_id=7104,
                                    assembly_id=7104,
                                    status_type_id='ENA Public',
                                    status_time='2022-09-25T00:00:00+01:00',
                                )
                            ],
                        ),
                    ],
                )
            ],
            data_accession=Accession(
                accession_id='PRJEB50167',
                accession_type_id='BioProject - Species Data',
                secondary='ERP134724',
                submission='ERA8395505',
                date_submitted='2022-01-17T00:00:00+00:00',
                name='lpJunEffu',
                title='Juncus effusus, genomic and transcriptomic data',
                description=(
                    'This project collects the genomic and transcriptomic data generated for'
                    ' Juncus effusus to facilitate genome assembly and annotation as part of the'
                    ' Darwin Tree of Life Project (https://www.darwintreeoflife.org/). The data'
                    ' under this project are made available subject to the Darwin Tree of Life'
                    ' Open Data Release Policy (https://www.darwintreeoflife.org/project'
                    '-resources/).'
                ),
                alias='ena-tol-lpJunEffu-study-rawdata-20220117',
                submitter_id='WELLCOME SANGER INSTITUTE',
                is_deleted=False,
            ),
            umbrella_accession=Accession(
                accession_id='PRJEB50168',
                accession_type_id='BioProject - Species Umbrella',
                submission='ERA8395506',
                date_submitted='2022-01-17T00:00:00+00:00',
                name='lpJunEffu',
                title='Juncus effusus',
                description=(
                    'This project collects the sequencing data and assemblies generated for'
                    ' Juncus effusus by the Darwin Tree of Life Project (https'
                    '://www.darwintreeoflife.org/). The data under this project are made'
                    ' available subject to the Darwin Tree of Life Open Data Release Policy'
                    ' (https://www.darwintreeoflife.org/project-resources/).'
                ),
                alias='ena-tol-lpJunEffu-study-umbrella-20220117',
                submitter_id='WELLCOME SANGER INSTITUTE',
                is_deleted=False,
                child_assn=[
                    BioprojectLink(
                        id=2168,
                        parent_accession_id='PRJEB50168',
                        child_accession_id='PRJEB55668',
                        link_status='New',
                        child=Accession(
                            accession_id='PRJEB55668',
                            accession_type_id='BioProject - Species Assembly',
                            secondary='ERP140591',
                            submission='ERA17616049',
                            date_submitted='2022-08-31T00:00:00+01:00',
                            name='lpJunEffu1',
                            title='Juncus effusus genome assembly, lpJunEffu1',
                            description=(
                                'This project provides the genome assembly of Juncus effusus. The'
                                ' assembly is provided by the Darwin Tree of Life Project (https'
                                ': //www.darwintreeoflife.org/). The data under this project are'
                                ' made available subject to the Darwin Tree of Life Open Data'
                                ' Release Policy (https: //www.darwintreeoflife.org/project'
                                '-resources/).'
                            ),
                            alias='WSI_primary_lpJunEffu1.1',
                            submitter_id='WELLCOME SANGER INSTITUTE',
                            is_deleted=False,
                        ),
                    ),
                    BioprojectLink(
                        id=2169,
                        parent_accession_id='PRJEB50168',
                        child_accession_id='PRJEB55669',
                        link_status='New',
                        child=Accession(
                            accession_id='PRJEB55669',
                            accession_type_id='BioProject - Species Assembly',
                            secondary='ERP140592',
                            submission='ERA17616049',
                            date_submitted='2022-08-31T00:00:00+01:00',
                            name='lpJunEffu1 alternate haplotype',
                            title=(
                                'Juncus effusus genome assembly, lpJunEffu1, alternate haplotype'
                            ),
                            description=(
                                'This project provides the genome assembly of Juncus effusus. The'
                                ' assembly is provided by the Darwin Tree of Life Project (https'
                                ': //www.darwintreeoflife.org/). The data under this project are'
                                ' made available subject to the Darwin Tree of Life Open Data'
                                ' Release Policy (https: //www.darwintreeoflife.org/project'
                                '-resources/).'
                            ),
                            alias='WSI_haplotigs_lpJunEffu1.1',
                            submitter_id='WELLCOME SANGER INSTITUTE',
                            is_deleted=False,
                        ),
                    ),
                    BioprojectLink(
                        id=2170,
                        parent_accession_id='PRJEB50168',
                        child_accession_id='PRJEB50167',
                        link_status='New',
                        child=Accession(
                            accession_id='PRJEB50167',
                            accession_type_id='BioProject - Species Data',
                            secondary='ERP134724',
                            submission='ERA8395505',
                            date_submitted='2022-01-17T00:00:00+00:00',
                            name='lpJunEffu',
                            title='Juncus effusus, genomic and transcriptomic data',
                            description=(
                                'This project collects the genomic and transcriptomic data'
                                ' generated for Juncus effusus to facilitate genome assembly and'
                                ' annotation as part of the Darwin Tree of Life Project (https'
                                '://www.darwintreeoflife.org/). The data under this project are'
                                ' made available subject to the Darwin Tree of Life Open Data'
                                ' Release Policy (https://www.darwintreeoflife.org/project'
                                '-resources/).'
                            ),
                            alias='ena-tol-lpJunEffu-study-rawdata-20220117',
                            submitter_id='WELLCOME SANGER INSTITUTE',
                            is_deleted=False,
                        ),
                    ),
                ],
                parent_assn=[
                    BioprojectLink(
                        id=2171,
                        parent_accession_id='PRJEB40665',
                        child_accession_id='PRJEB50168',
                        link_status='New',
                        parent=Accession(
                            accession_id='PRJEB40665',
                            accession_type_id='BioProject - Project Umbrella',
                            submission='ERA2939302',
                            date_submitted='2020-10-05T00:00:00+01:00',
                            name='Darwin Tree of Life Project',
                            title='Darwin Tree of Life Project: Genome Data and Assemblies',
                            description=(
                                'The Darwin Tree of Life Project (darwintreeoflife.org) generates'
                                ' high quality genome assemblies for the approximately 60,000'
                                ' species of eukaryotic organisms found in Britain and Ireland to'
                                ' contribute towards providing reference genome sequences for all'
                                ' life. It is a collaboration between biodiversity, genomics and'
                                ' analysis partners that hopes to transform the way we do biology'
                                ', conservation and biotechnology. The project partners are the'
                                ' Natural History Museum London, the Royal Botanic Gardens Kew'
                                ', the Royal Botanic Gardens Edinburgh, the Marine Biological'
                                ' Association, the Earlham Institute, the University of Oxford'
                                ' and its Wytham Woods field station, the University of Edinburgh'
                                ', the University of Cambridge, EMBL-EBI and others, led by the'
                                ' Wellcome Sanger Institute, UK'
                            ),
                            alias='SC_2020-10-05T14:21:44Z',
                            submitter_id='Wellcome Sanger Institute',
                            is_deleted=False,
                        ),
                    ),
                    BioprojectLink(
                        id=2172,
                        parent_accession_id='PRJEB43745',
                        child_accession_id='PRJEB50168',
                        link_status='New',
                        parent=Accession(
                            accession_id='PRJEB43745',
                            accession_type_id='BioProject - Project Umbrella',
                            submission='ERA3682544',
                            date_submitted='2021-03-18T00:00:00+00:00',
                            name='Sanger Institute Tree of Life Programme',
                            title='Sanger Institute Tree of Life Programme: Data and Assemblies',
                            description=(
                                'The Wellcome Sanger Institute Tree of Life programme (https'
                                '://www.sanger.ac.uk/programme/tree-of-life/) generates reference'
                                ' genome assemblies and other genomic and transcriptome data to'
                                ' deliver to an overarching goal of sequencing all of eukaryotic'
                                ' life. The Tree of Life programme is affiliated with the Earth'
                                ' BioGenome Project (EBP: PRJNA533106). The data and analyses are'
                                ' generated in collaboration with a range of external colleagues'
                                ', alongside Tree of Life contributions to the Darwin Tree of'
                                ' Life Project (DToL: PRJEB40665), the Aquatic Symbiosis Genomics'
                                ' project (ASG: PRJEB43743) the Vertebrate Genomes Project (VGP'
                                ': PRJNA489243) and others.'
                            ),
                            alias='ena-tol-ToL-project-umbrella-20210317',
                            submitter_id='WELLCOME SANGER INSTITUTE',
                            is_deleted=False,
                        ),
                    ),
                ],
            ),
            location=Location(location_id=299, path='e/1/3/d/d/0/Juncus_effusus'),
        ),
        Species(
            species_id='Rallus aquaticus',
            location_id=824,
            tolid_prefix='bRalAqu',
            taxon_id=54496,
            family_taxon_id=9119,
            taxon_family='Rallidae',
            taxon_order='Gruiformes',
            taxon_phylum='Chordata',
            taxon_group='birds',
            genome_size=1222500000,
            chromosome_number=78,
            data_accession_id='PRJEB75638',
            umbrella_accession_id='PRJEB75639',
            specimens=[
                Specimen(
                    specimen_id='bRalAqu1',
                    location_id=824,
                    species_id='Rallus aquaticus',
                    supplied_name='NHMUK014551542',
                    sts_specimen='NHMUK014551542',
                    sts_priority=1,
                    accession_id='SAMEA113398957',
                    sex_id='Male',
                    ploidy='2',
                    samples=[
                        Sample(
                            sample_id='DTOL14392235',
                            specimen_id='bRalAqu1',
                            accession_id='SAMEA114299701',
                            accession=Accession(
                                accession_id='SAMEA114299701',
                                accession_type_id='BioSample',
                                is_deleted=False,
                            ),
                            data=[
                                Data(
                                    data_id='48587_5-6#2',
                                    study_id=5901,
                                    category='genomic_data',
                                    sample_id='DTOL14392235',
                                    library_id='SQPP-49303-W:B1',
                                    accession_id='ERR13093686',
                                    run_id='48587_5-6',
                                    processed=1,
                                    tag1_id='2',
                                    tag2_id='2',
                                    date='2024-03-08T14:01:36+00:00',
                                    lims_qc='pass',
                                    visibility='Always',
                                    reads=694971792,
                                    bases=104940740592,
                                    read_length_mean=151.0,
                                    folder_ulid='01J8HAY65YNTH7P0M2F65PMN39',
                                    library=Library(
                                        library_id='SQPP-49303-W:B1',
                                        library_type_id='Hi-C - Arima v2',
                                    ),
                                    accession=Accession(
                                        accession_id='ERR13093686',
                                        accession_type_id='Run',
                                        secondary='ERX12465384',
                                        date_submitted='2024-05-13T00:00:00+01:00',
                                        is_deleted=False,
                                    ),
                                    run=Run(
                                        run_id='48587_5-6',
                                        platform_id=8,
                                        centre_id=2,
                                        element='5-6',
                                        instrument_name='NX1',
                                        complete='2024-03-07T09:39:25+00:00',
                                    ),
                                    files=[
                                        File(
                                            id=134928,
                                            data_id='48587_5-6#2',
                                            name='48587_5-6#2.cram',
                                            remote_path=(
                                                'irods:/seq/illumina/runs/48/48587/lane5-6/plex2'
                                                '/48587_5-6#2.cram'
                                            ),
                                            insdc_path=(
                                                'https://ftp.sra.ebi.ac.uk/vol1/run/ERR130'
                                                '/ERR13093686/48587_5-6%232.cram'
                                            ),
                                            size_bytes=31081394145,
                                            md5='0ac93acd48d2dd15577a8c161764878b',
                                            file_type='CRAM',
                                            has_methylation=False,
                                            sam_tags=['BC:Z', 'QT:Z', 'RG:Z', 'a3:i', 'ah:i'],
                                        )
                                    ],
                                    project_assn=[
                                        Allocation(
                                            id=30287, project_id='aegis', data_id='48587_5-6#2'
                                        ),
                                        Allocation(
                                            id=30288,
                                            project_id='britain-and-ireland',
                                            data_id='48587_5-6#2',
                                        ),
                                        Allocation(
                                            id=30289, project_id='darwin', data_id='48587_5-6#2'
                                        ),
                                        Allocation(
                                            id=30290, project_id='tol', data_id='48587_5-6#2'
                                        ),
                                        Allocation(
                                            id=30291, project_id='vgp', data_id='48587_5-6#2'
                                        ),
                                    ],
                                    dataset_assn=[
                                        DatasetElement(
                                            id=14051,
                                            data_id='48587_5-6#2',
                                            dataset_id='01K6B4HP8K8MDPQYB63C0HWT6G',
                                            dataset=Dataset(
                                                dataset_id='01K6B4HP8K8MDPQYB63C0HWT6G',
                                                name='hic-arima2',
                                                assembly_assn=[
                                                    AssemblyDataset(
                                                        id=245,
                                                        assembly_id=156,
                                                        dataset_id='01K6B4HP8K8MDPQYB63C0HWT6G',
                                                    ),
                                                    AssemblyDataset(
                                                        id=247,
                                                        assembly_id=157,
                                                        dataset_id='01K6B4HP8K8MDPQYB63C0HWT6G',
                                                    ),
                                                ],
                                                status_history=[
                                                    DatasetStatus(
                                                        dataset_status_id=9685,
                                                        dataset_id='01K6B4HP8K8MDPQYB63C0HWT6G',
                                                        status_type_id='Pending',
                                                        status_time=(
                                                            '2025-09-29T17:23:00.676255+01:00'
                                                        ),
                                                    )
                                                ],
                                            ),
                                        )
                                    ],
                                    folder=Folder(
                                        folder_ulid='01J8HAY65YNTH7P0M2F65PMN39',
                                        folder_location_id='illumina_data_s3',
                                        image_file_list=[
                                            {
                                                'file': '48587_5-6#2_F0xB00-acgt-cycles.png',
                                                'caption': 'Hi-C - Arima v2 A|C|G|T Content Per Cycle',  # noqa: E501
                                            },
                                            {
                                                'file': '48587_5-6#2_F0xB00-quals3.png',
                                                'caption': 'Hi-C - Arima v2 Quality Frequencies, Separate Curve Per Cycle',  # noqa: E501
                                            },
                                            {
                                                'file': '48587_5-6#2_F0xB00-gc-content.png',
                                                'caption': 'Hi-C - Arima v2 G|C Content',
                                            },
                                            {
                                                'file': '48587_5-6#2_F0xB00-quals.png',
                                                'caption': 'Hi-C - Arima v2 Quality Per Cycle (Overlaid)',  # noqa: E501
                                            },
                                            {
                                                'file': '48587_5-6#2_F0xB00-quals-hm.png',
                                                'caption': 'Hi-C - Arima v2 Quality Frequencies, Per Cycle Heat Map',  # noqa: E501
                                            },
                                            {
                                                'file': '48587_5-6#2_F0xB00-quals2.png',
                                                'caption': 'Hi-C - Arima v2 Quality Per Cycle (Split)',  # noqa: E501
                                            },
                                        ],
                                        files_total_bytes=151114,
                                    ),
                                )
                            ],
                        ),
                        Sample(
                            sample_id='DTOL14550031',
                            specimen_id='bRalAqu1',
                            accession_id='SAMEA114299701',
                            accession=Accession(
                                accession_id='SAMEA114299701',
                                accession_type_id='BioSample',
                                is_deleted=False,
                            ),
                            data=[
                                Data(
                                    data_id='m84047_240219_121238_s3#2089',
                                    study_id=5901,
                                    category='genomic_data',
                                    sample_id='DTOL14550031',
                                    library_id='DTOL14550031',
                                    accession_id='ERR13112065',
                                    run_id='m84047_240219_121238_s3',
                                    processed=1,
                                    tag1_id='bc2089',
                                    date='2024-02-21T10:56:38+00:00',
                                    lims_qc='pass',
                                    visibility='Always',
                                    reads=5667911,
                                    bases=52090647829,
                                    read_length_mean=9190.44914943089,
                                    read_length_n50=10306,
                                    bases_a=14668588897,
                                    bases_c=11006690502,
                                    bases_g=11411698987,
                                    bases_t=15003669443,
                                    read_length_longest=46331,
                                    read_length_shortest=70,
                                    reads_duplicated=0,
                                    reads_discarded=0,
                                    reads_trimmed=3398,
                                    bases_removed=509700,
                                    library=Library(
                                        library_id='DTOL14550031', library_type_id='PacBio - HiFi'
                                    ),
                                    accession=Accession(
                                        accession_id='ERR13112065',
                                        accession_type_id='Run',
                                        secondary='ERX12483603',
                                        date_submitted='2024-05-17T00:00:00+01:00',
                                        is_deleted=False,
                                    ),
                                    run=Run(
                                        run_id='m84047_240219_121238_s3',
                                        platform_id=6,
                                        centre_id=2,
                                        lims_id='TRACTION-RUN-1132',
                                        element='C1.1',
                                        instrument_name='m84047',
                                        start='2024-02-19T11:01:46+00:00',
                                        complete='2024-02-20T17:26:57+00:00',
                                        plex_count=1,
                                        chemistry='R/P1-C1/5.0-25M',
                                        pacbio_run_metrics=[
                                            PacbioRunMetrics(
                                                run_id='m84047_240219_121238_s3',
                                                movie_minutes=1440,
                                                binding_kit='Revio polymerase kit',
                                                sequencing_kit='Revio sequencing plate',
                                                sequencing_kit_lot_number='033482',
                                                cell_lot_number='1000002283',
                                                include_kinetics='false',
                                                loading_conc=214.0,
                                                control_num_reads=3556,
                                                control_read_length_mean=67141.0,
                                                control_concordance_mean=0.907988,
                                                control_concordance_mode=0.91,
                                                local_base_rate=2.60376,
                                                polymerase_read_bases=919164234856,
                                                polymerase_num_reads=9917451,
                                                polymerase_read_length_mean=92682.0,
                                                unique_molecular_bases=117783101440,
                                                productive_zmws_num=25165824,
                                                p0_num=15179993,
                                                p1_num=9921007,
                                                p2_num=64824,
                                                adapter_dimer_percent=0.0,
                                                short_insert_percent=0.0,
                                                hifi_read_bases=52481919295,
                                                hifi_num_reads=5710242,
                                                hifi_read_length_mean=9190,
                                                hifi_read_quality_median=40,
                                                hifi_number_passes_mean=16.0,
                                                hifi_low_quality_read_quality_median=17,
                                                hifi_barcoded_reads=5667911,
                                                hifi_bases_in_barcoded_reads=52090647829,
                                                folder_ulid='01K0YCTXF8WGJNVF8VVS8FXBRE',
                                                folder=Folder(
                                                    folder_ulid='01K0YCTXF8WGJNVF8VVS8FXBRE',
                                                    folder_location_id='pacbio_run_s3',
                                                    image_file_list=[
                                                        {
                                                            'file': 'readlength_histogram.png',
                                                            'caption': 'Mean readlength histogram',  # noqa: E501
                                                        },
                                                        {
                                                            'file': 'raw_read_length_plot.png',
                                                            'caption': 'Loading evaluation',
                                                        },
                                                        {
                                                            'file': 'hexbin_length_plot.png',
                                                            'caption': 'Insert read length density',  # noqa: E501
                                                        },
                                                        {
                                                            'file': 'base_yield_plot.png',
                                                            'caption': 'Base yield density',
                                                        },
                                                        {
                                                            'file': 'nreads_histogram.png',
                                                            'caption': 'Number of reads per barcode histogram',  # noqa: E501
                                                        },
                                                        {
                                                            'file': 'm5c_detections_hist.png',
                                                            'caption': 'CpG methylation in reads histogram',  # noqa: E501
                                                        },
                                                        {
                                                            'file': 'readLenDist0.png',
                                                            'caption': 'Polymerase read length',
                                                        },
                                                        {
                                                            'file': 'readlength_qv_hist2d.hexbin.png',  # noqa: E501
                                                            'caption': 'Accuracy versus read length density',  # noqa: E501
                                                        },
                                                        {
                                                            'file': 'm5c_detections.png',
                                                            'caption': 'CpG methylation in reads',
                                                        },
                                                        {
                                                            'file': 'ccs_npasses_hist.png',
                                                            'caption': 'Number of passes',
                                                        },
                                                        {
                                                            'file': 'bq_histogram.png',
                                                            'caption': 'Barcode quality distribution',  # noqa: E501
                                                        },
                                                        {
                                                            'file': 'readlength_plot.png',
                                                            'caption': 'Control polymerase read length',  # noqa: E501
                                                        },
                                                        {
                                                            'file': 'concordance_plot.png',
                                                            'caption': 'Control concordance',
                                                        },
                                                        {
                                                            'file': 'ccs_all_readlength_hist_plot.png',  # noqa: E501
                                                            'caption': 'Read length distribution (all)',  # noqa: E501
                                                        },
                                                        {
                                                            'file': 'ccs_hifi_read_length_yield_plot.png',  # noqa: E501
                                                            'caption': 'HiFi yield by read length',  # noqa: E501
                                                        },
                                                        {
                                                            'file': 'ccs_accuracy_hist.png',
                                                            'caption': 'Read quality distribution',  # noqa: E501
                                                        },
                                                        {
                                                            'file': 'ccs_readlength_hist_plot.png',  # noqa: E501
                                                            'caption': 'HiFi read length distribution',  # noqa: E501
                                                        },
                                                        {
                                                            'file': 'nreads.png',
                                                            'caption': 'Number of reads per barcode',  # noqa: E501
                                                        },
                                                    ],
                                                    files_total_bytes=4895736,
                                                ),
                                            )
                                        ],
                                    ),
                                    files=[
                                        File(
                                            id=134661,
                                            data_id='m84047_240219_121238_s3#2089',
                                            name='m84047_240219_121238_s3.hifi_reads.bc2089.bam',
                                            remote_path=(
                                                'irods:/seq/pacbio/r84047_20240219_102003/1_C01'
                                                '/m84047_240219_121238_s3.hifi_reads.bc2089.bam'
                                            ),
                                            insdc_path=(
                                                'https://ftp.sra.ebi.ac.uk/vol1/run/ERR131'
                                                '/ERR13112065'
                                                '/m84047_240219_121238_s3.hifi_reads.bc2089.bam'
                                            ),
                                            size_bytes=20408107049,
                                            md5='0fedeb709610324722cfb27dd3f37d75',
                                            file_type='BAM',
                                            has_methylation=True,
                                            sam_tags=[
                                                'ML:B',
                                                'MM:Z',
                                                'RG:Z',
                                                'ac:B',
                                                'bc:B',
                                                'bl:Z',
                                                'bq:i',
                                                'bt:Z',
                                                'bx:B',
                                                'cx:i',
                                                'ec:f',
                                                'ls:B',
                                                'ma:i',
                                                'np:i',
                                                'qe:i',
                                                'ql:Z',
                                                'qs:i',
                                                'qt:Z',
                                                'rq:f',
                                                'sn:B',
                                                'we:i',
                                                'ws:i',
                                                'zm:i',
                                            ],
                                        )
                                    ],
                                    project_assn=[
                                        Allocation(
                                            id=63001,
                                            project_id='aegis',
                                            data_id='m84047_240219_121238_s3#2089',
                                        ),
                                        Allocation(
                                            id=63002,
                                            project_id='britain-and-ireland',
                                            data_id='m84047_240219_121238_s3#2089',
                                        ),
                                        Allocation(
                                            id=63003,
                                            project_id='darwin',
                                            data_id='m84047_240219_121238_s3#2089',
                                        ),
                                        Allocation(
                                            id=63004,
                                            project_id='tol',
                                            data_id='m84047_240219_121238_s3#2089',
                                        ),
                                        Allocation(
                                            id=63005,
                                            project_id='vgp',
                                            data_id='m84047_240219_121238_s3#2089',
                                        ),
                                    ],
                                    dataset_assn=[
                                        DatasetElement(
                                            id=2620,
                                            data_id='m84047_240219_121238_s3#2089',
                                            dataset_id='01K6ATRHFGXCKPRYPQY2CBXN3W',
                                            dataset=Dataset(
                                                dataset_id='01K6ATRHFGXCKPRYPQY2CBXN3W',
                                                name='pacbio.ccs',
                                                assembly_assn=[
                                                    AssemblyDataset(
                                                        id=246,
                                                        assembly_id=156,
                                                        dataset_id='01K6ATRHFGXCKPRYPQY2CBXN3W',
                                                    ),
                                                    AssemblyDataset(
                                                        id=248,
                                                        assembly_id=157,
                                                        dataset_id='01K6ATRHFGXCKPRYPQY2CBXN3W',
                                                    ),
                                                ],
                                                status_history=[
                                                    DatasetStatus(
                                                        dataset_status_id=1709,
                                                        dataset_id='01K6ATRHFGXCKPRYPQY2CBXN3W',
                                                        status_type_id='Pending',
                                                        status_time=(
                                                            '2025-09-29T14:31:59.396275+01:00'
                                                        ),
                                                    )
                                                ],
                                            ),
                                        )
                                    ],
                                )
                            ],
                        ),
                        Sample(
                            sample_id='DTOL15217660',
                            specimen_id='bRalAqu1',
                            accession_id='SAMEA114299701',
                            accession=Accession(
                                accession_id='SAMEA114299701',
                                accession_type_id='BioSample',
                                is_deleted=False,
                            ),
                            data=[
                                Data(
                                    data_id='ONTRUN-232#PBA64077#21',
                                    study_id=5901,
                                    category='genomic_data',
                                    sample_id='DTOL15217660',
                                    library_id='TRAC-2-12370',
                                    run_id='ONTRUN-232',
                                    processed=1,
                                    date='2024-12-03T12:50:13+00:00',
                                    visibility='Always',
                                    reads=11148681,
                                    bases=46146404036,
                                    read_length_mean=4139.18059329171,
                                    read_length_n50=7799,
                                    read_length_longest=580083,
                                    read_length_shortest=14,
                                    library=Library(
                                        library_id='TRAC-2-12370',
                                        library_type_id='ONT_PromethIon',
                                    ),
                                    run=Run(
                                        run_id='ONTRUN-232',
                                        platform_id=23,
                                        centre_id=2,
                                        element='20',
                                        instrument_name='PC24B148',
                                        start='2024-11-26T13:13:10+00:00',
                                    ),
                                    files=[
                                        File(
                                            id=153247,
                                            data_id='ONTRUN-232#PBA64077#21',
                                            remote_path=(
                                                'irods:/seq/ont/promethion/PC24B148/ONTRUN-232'
                                                '/TRAC-2-12370/20241126_1238_3E_PBA64077_e8f2cb9b'
                                                '/bam_pass'
                                            ),
                                            file_type='RAW_BAM_DIR',
                                        ),
                                        File(
                                            id=153248,
                                            data_id='ONTRUN-232#PBA64077#21',
                                            remote_path=(
                                                'irods:/seq/ont/promethion/offline-basecalls'
                                                '/PC24B148/ONTRUN-232/TRAC-2-12370'
                                                '/20241126_1238_3E_PBA64077_e8f2cb9b/dorado'
                                                '/7.2.13/sup/simplex/normal/pass'
                                            ),
                                            file_type='RECALL_FASTQ_DIR',
                                        ),
                                        File(
                                            id=153425,
                                            data_id='ONTRUN-232#PBA64077#21',
                                            remote_path=(
                                                'irods:/seq/ont/promethion/PC24B148/ONTRUN-232'
                                                '/TRAC-2-12370/20241126_1238_3E_PBA64077_e8f2cb9b'
                                                '/pod5'
                                            ),
                                            file_type='RAW_POD5_DIR',
                                            has_methylation=True,
                                        ),
                                    ],
                                    project_assn=[
                                        Allocation(
                                            id=41667,
                                            project_id='aegis',
                                            data_id='ONTRUN-232#PBA64077#21',
                                        ),
                                        Allocation(
                                            id=41668,
                                            project_id='britain-and-ireland',
                                            data_id='ONTRUN-232#PBA64077#21',
                                        ),
                                        Allocation(
                                            id=41669,
                                            project_id='darwin',
                                            data_id='ONTRUN-232#PBA64077#21',
                                        ),
                                        Allocation(
                                            id=41670,
                                            project_id='tol',
                                            data_id='ONTRUN-232#PBA64077#21',
                                        ),
                                        Allocation(
                                            id=41671,
                                            project_id='vgp',
                                            data_id='ONTRUN-232#PBA64077#21',
                                        ),
                                    ],
                                    dataset_assn=[
                                        DatasetElement(
                                            id=32411,
                                            data_id='ONTRUN-232#PBA64077#21',
                                            dataset_id='01K6X00XKNCBQSPYTG6WD0ABKJ',
                                            dataset=Dataset(
                                                dataset_id='01K6X00XKNCBQSPYTG6WD0ABKJ',
                                                name='ont',
                                                status_history=[
                                                    DatasetStatus(
                                                        dataset_status_id=21724,
                                                        dataset_id='01K6X00XKNCBQSPYTG6WD0ABKJ',
                                                        status_type_id='Pending',
                                                        status_time=(
                                                            '2025-10-06T15:50:16.630054+01:00'
                                                        ),
                                                    )
                                                ],
                                            ),
                                        )
                                    ],
                                )
                            ],
                        ),
                        Sample(
                            sample_id='DTOL16058752',
                            specimen_id='bRalAqu1',
                            accession_id='SAMEA114299701',
                            accession=Accession(
                                accession_id='SAMEA114299701',
                                accession_type_id='BioSample',
                                is_deleted=False,
                            ),
                            data=[
                                Data(
                                    data_id='ONTRUN-304#PBE95016#21#NB09',
                                    study_id=5901,
                                    category='genomic_data',
                                    sample_id='DTOL16058752',
                                    library_id='NT1863132U',
                                    run_id='ONTRUN-304',
                                    processed=1,
                                    tag1_id='NB09',
                                    date='2025-09-14T01:00:02+01:00',
                                    visibility='Always',
                                    reads=10585274,
                                    bases=16071581924,
                                    read_length_mean=1518.29625987953,
                                    read_length_n50=2459,
                                    read_length_longest=767551,
                                    read_length_shortest=63,
                                    library=Library(
                                        library_id='NT1863132U',
                                        library_type_id='ONT_PromethIon_mplx',
                                    ),
                                    run=Run(
                                        run_id='ONTRUN-304',
                                        platform_id=23,
                                        centre_id=2,
                                        instrument_name='PC24B148',
                                        start='2025-09-09T16:46:24+01:00',
                                    ),
                                    files=[
                                        File(
                                            id=154839,
                                            data_id='ONTRUN-304#PBE95016#21#NB09',
                                            remote_path=(
                                                'irods:/seq/ont/promethion/offline-deplexes'
                                                '/PC24B148/ONTRUN-304/NT1863132U'
                                                '/20250909_1434_3E_PBE95016_2a80ed02/dorado/7.6.8'
                                                '/sup/simplex/normal/default/pass/barcode09'
                                            ),
                                            file_type='RECALL_FASTQ_DIR',
                                            has_methylation=False,
                                        )
                                    ],
                                    project_assn=[
                                        Allocation(
                                            id=41973,
                                            project_id='aegis',
                                            data_id='ONTRUN-304#PBE95016#21#NB09',
                                        ),
                                        Allocation(
                                            id=41974,
                                            project_id='britain-and-ireland',
                                            data_id='ONTRUN-304#PBE95016#21#NB09',
                                        ),
                                        Allocation(
                                            id=41975,
                                            project_id='darwin',
                                            data_id='ONTRUN-304#PBE95016#21#NB09',
                                        ),
                                        Allocation(
                                            id=41976,
                                            project_id='tol',
                                            data_id='ONTRUN-304#PBE95016#21#NB09',
                                        ),
                                        Allocation(
                                            id=41977,
                                            project_id='vgp',
                                            data_id='ONTRUN-304#PBE95016#21#NB09',
                                        ),
                                    ],
                                    dataset_assn=[
                                        DatasetElement(
                                            id=32412,
                                            data_id='ONTRUN-304#PBE95016#21#NB09',
                                            dataset_id='01K6X00XKNCBQSPYTG6WD0ABKJ',
                                            dataset=Dataset(
                                                dataset_id='01K6X00XKNCBQSPYTG6WD0ABKJ',
                                                name='ont',
                                                status_history=[
                                                    DatasetStatus(
                                                        dataset_status_id=21724,
                                                        dataset_id='01K6X00XKNCBQSPYTG6WD0ABKJ',
                                                        status_type_id='Pending',
                                                        status_time=(
                                                            '2025-10-06T15:50:16.630054+01:00'
                                                        ),
                                                    )
                                                ],
                                            ),
                                        )
                                    ],
                                )
                            ],
                        ),
                        Sample(
                            sample_id='DTOLRNA14668771',
                            specimen_id='bRalAqu1',
                            accession_id='SAMEA114299701',
                            accession=Accession(
                                accession_id='SAMEA114299701',
                                accession_type_id='BioSample',
                                is_deleted=False,
                            ),
                            data=[
                                Data(
                                    data_id='49280_2#11',
                                    study_id=6327,
                                    category='transcriptomic_data',
                                    sample_id='DTOLRNA14668771',
                                    library_id='SQPP-50358-G:C2',
                                    accession_id='ERR13493954',
                                    run_id='49280_2',
                                    processed=1,
                                    tag1_id='11',
                                    tag2_id='11',
                                    date='2024-08-27T10:39:49+01:00',
                                    lims_qc='pass',
                                    visibility='Always',
                                    reads=125591826,
                                    bases=18964365726,
                                    read_length_mean=151.0,
                                    bases_a=5041998937,
                                    bases_c=4371050043,
                                    bases_g=4492252651,
                                    bases_t=5056804821,
                                    folder_ulid='01J8HD27D98F8FFYV5NDE4B10H',
                                    library=Library(
                                        library_id='SQPP-50358-G:C2', library_type_id='RNA PolyA'
                                    ),
                                    accession=Accession(
                                        accession_id='ERR13493954',
                                        accession_type_id='Run',
                                        secondary='ERX12864221',
                                        date_submitted='2024-08-13T00:00:00+01:00',
                                        is_deleted=False,
                                    ),
                                    run=Run(
                                        run_id='49280_2',
                                        platform_id=8,
                                        centre_id=2,
                                        element='2',
                                        instrument_name='NX2',
                                        complete='2024-08-04T02:59:55+01:00',
                                    ),
                                    files=[
                                        File(
                                            id=144313,
                                            data_id='49280_2#11',
                                            name='49280_2#11.cram',
                                            remote_path=(
                                                'irods:/seq/illumina/runs/49/49280/lane2/plex11'
                                                '/49280_2#11.cram'
                                            ),
                                            insdc_path=(
                                                'https://ftp.sra.ebi.ac.uk/vol1/run/ERR134'
                                                '/ERR13493954/49280_2%2311.cram'
                                            ),
                                            size_bytes=2885723248,
                                            md5='801ab57f7024d2bb93ac8b65646c414d',
                                            file_type='CRAM',
                                            has_methylation=False,
                                            sam_tags=['BC:Z', 'QT:Z', 'RG:Z', 'a3:i', 'ah:i'],
                                        )
                                    ],
                                    project_assn=[
                                        Allocation(
                                            id=32657, project_id='aegis', data_id='49280_2#11'
                                        ),
                                        Allocation(
                                            id=32658,
                                            project_id='britain-and-ireland',
                                            data_id='49280_2#11',
                                        ),
                                        Allocation(
                                            id=32659, project_id='darwin', data_id='49280_2#11'
                                        ),
                                        Allocation(
                                            id=32660, project_id='tol', data_id='49280_2#11'
                                        ),
                                        Allocation(
                                            id=32661, project_id='vgp', data_id='49280_2#11'
                                        ),
                                    ],
                                    dataset_assn=[
                                        DatasetElement(
                                            id=29323,
                                            data_id='49280_2#11',
                                            dataset_id='01K6BPCJJEK063WK6NN58J0A0P',
                                            dataset=Dataset(
                                                dataset_id='01K6BPCJJEK063WK6NN58J0A0P',
                                                name='rna-seq',
                                                status_history=[
                                                    DatasetStatus(
                                                        dataset_status_id=19012,
                                                        dataset_id='01K6BPCJJEK063WK6NN58J0A0P',
                                                        status_type_id='Pending',
                                                        status_time=(
                                                            '2025-09-29T22:34:47.427464+01:00'
                                                        ),
                                                    )
                                                ],
                                            ),
                                        )
                                    ],
                                    folder=Folder(
                                        folder_ulid='01J8HD27D98F8FFYV5NDE4B10H',
                                        folder_location_id='illumina_data_s3',
                                        image_file_list=[
                                            {
                                                'file': '49280_2#11_F0xB00-quals-hm.png',
                                                'caption': 'RNA PolyA Quality Frequencies, Per Cycle Heat Map',  # noqa: E501
                                            },
                                            {
                                                'file': '49280_2#11_F0xB00-acgt-cycles.png',
                                                'caption': 'RNA PolyA A|C|G|T Content Per Cycle',
                                            },
                                            {
                                                'file': '49280_2#11_F0xB00-quals2.png',
                                                'caption': 'RNA PolyA Quality Per Cycle (Split)',
                                            },
                                            {
                                                'file': '49280_2#11_F0xB00-gc-content.png',
                                                'caption': 'RNA PolyA G|C Content',
                                            },
                                            {
                                                'file': '49280_2#11_F0xB00-quals3.png',
                                                'caption': 'RNA PolyA Quality Frequencies, Separate Curve Per Cycle',  # noqa: E501
                                            },
                                            {
                                                'file': '49280_2#11_F0xB00-quals.png',
                                                'caption': 'RNA PolyA Quality Per Cycle (Overlaid)',  # noqa: E501
                                            },
                                        ],
                                        files_total_bytes=160468,
                                    ),
                                )
                            ],
                        ),
                    ],
                    accession=Accession(
                        accession_id='SAMEA113398957',
                        accession_type_id='BioSample',
                        is_deleted=False,
                    ),
                    location=Location(location_id=824, path='3/b/5/0/1/e/Rallus_aquaticus'),
                    assemblies=[
                        Assembly(
                            assembly_id=156,
                            specimen_id='bRalAqu1',
                            name='bRalAqu1.1',
                            description='bRalAqu1.1 assembly for Rallus aquaticus',
                            level='chromosome',
                            is_reference=False,
                            bioproject_accession_id='PRJEB88631',
                            genome_accession_id='GCA_965250365.1',
                            bioproject_accession=Accession(
                                accession_id='PRJEB88631',
                                accession_type_id='BioProject - Species Assembly',
                                secondary='ERP171720',
                                submission='ERA32435027',
                                date_submitted='2025-04-17T00:00:00+01:00',
                                name='bRalAqu1.1',
                                title='bRalAqu1',
                                description=(
                                    'This project provides the genome assembly of Rallus'
                                    ' aquaticus, common name water rail. The assembly is provided'
                                    ' by the Darwin Tree of Life Project (https'
                                ),
                                alias='WSI_primary_bRalAqu1.1',
                                submitter_id='WELLCOME SANGER INSTITUTE',
                                is_deleted=False,
                            ),
                            genome_accession=Accession(
                                accession_id='GCA_965250365.1',
                                accession_type_id='GenBank Genome Assembly',
                                is_deleted=False,
                            ),
                            status_history=[
                                AssemblyStatus(
                                    assembly_status_id=156,
                                    assembly_id=156,
                                    status_type_id='ENA Public',
                                    status_time='2025-04-19T00:00:00+01:00',
                                )
                            ],
                        ),
                        Assembly(
                            assembly_id=157,
                            specimen_id='bRalAqu1',
                            name='bRalAqu1.1 alternate haplotype',
                            description=(
                                'bRalAqu1.1 alternate haplotype assembly for Rallus aquaticus'
                            ),
                            level='contig',
                            is_reference=False,
                            bioproject_accession_id='PRJEB88632',
                            genome_accession_id='GCA_965250415.1',
                            bioproject_accession=Accession(
                                accession_id='PRJEB88632',
                                accession_type_id='BioProject - Species Assembly',
                                secondary='ERP171721',
                                submission='ERA32435028',
                                date_submitted='2025-04-17T00:00:00+01:00',
                                name='bRalAqu1.1 alternate haplotype',
                                title='bRalAqu1 alternate haplotype',
                                description=(
                                    'This project provides the genome assembly of Rallus'
                                    ' aquaticus, common name water rail. The assembly is provided'
                                    ' by the Darwin Tree of Life Project (https'
                                ),
                                alias='WSI_primary_bRalAqu1.1 alternate haplotype',
                                submitter_id='WELLCOME SANGER INSTITUTE',
                                is_deleted=False,
                            ),
                            genome_accession=Accession(
                                accession_id='GCA_965250415.1',
                                accession_type_id='GenBank Genome Assembly',
                                is_deleted=False,
                            ),
                            status_history=[
                                AssemblyStatus(
                                    assembly_status_id=157,
                                    assembly_id=157,
                                    status_type_id='ENA Public',
                                    status_time='2025-04-19T00:00:00+01:00',
                                )
                            ],
                        ),
                    ],
                )
            ],
            data_accession=Accession(
                accession_id='PRJEB75638',
                accession_type_id='BioProject - Species Data',
                secondary='ERP160198',
                submission='ERA29771179',
                date_submitted='2024-05-12T00:00:00+01:00',
                name='bRalAqu',
                title='Rallus aquaticus (water rail), genomic and transcriptomic data',
                description=(
                    'This project collects the genomic and transcriptomic data generated for'
                    ' Rallus aquaticus, common name water rail, to facilitate genome assembly and'
                    ' annotation as part of the Darwin Tree of Life Project (https'
                    '://www.darwintreeoflife.org/). The data under this project are made'
                    ' available subject to the Darwin Tree of Life Open Data Release Policy'
                    ' (https://www.darwintreeoflife.org/project-resources/).'
                ),
                alias='ena-tol-bRalAqu-study-rawdata-20240512',
                submitter_id='WELLCOME SANGER INSTITUTE',
                is_deleted=False,
            ),
            umbrella_accession=Accession(
                accession_id='PRJEB75639',
                accession_type_id='BioProject - Species Umbrella',
                submission='ERA29771181',
                date_submitted='2024-05-12T00:00:00+01:00',
                name='bRalAqu',
                title='Rallus aquaticus (water rail)',
                description=(
                    'This project collects the sequencing data and assemblies generated for'
                    ' Rallus aquaticus, common name water rail, by the Darwin Tree of Life'
                    ' Project (https://www.darwintreeoflife.org/). The data under this project'
                    ' are made available subject to the Darwin Tree of Life Open Data Release'
                    ' Policy (https://www.darwintreeoflife.org/project-resources/).'
                ),
                alias='ena-tol-bRalAqu-study-umbrella-20240512',
                submitter_id='WELLCOME SANGER INSTITUTE',
                is_deleted=False,
                child_assn=[
                    BioprojectLink(
                        id=13251,
                        parent_accession_id='PRJEB75639',
                        child_accession_id='PRJEB88631',
                        link_status='New',
                        child=Accession(
                            accession_id='PRJEB88631',
                            accession_type_id='BioProject - Species Assembly',
                            secondary='ERP171720',
                            submission='ERA32435027',
                            date_submitted='2025-04-17T00:00:00+01:00',
                            name='bRalAqu1.1',
                            title='bRalAqu1',
                            description=(
                                'This project provides the genome assembly of Rallus aquaticus'
                                ', common name water rail. The assembly is provided by the Darwin'
                                ' Tree of Life Project (https'
                            ),
                            alias='WSI_primary_bRalAqu1.1',
                            submitter_id='WELLCOME SANGER INSTITUTE',
                            is_deleted=False,
                        ),
                    ),
                    BioprojectLink(
                        id=13252,
                        parent_accession_id='PRJEB75639',
                        child_accession_id='PRJEB88632',
                        link_status='New',
                        child=Accession(
                            accession_id='PRJEB88632',
                            accession_type_id='BioProject - Species Assembly',
                            secondary='ERP171721',
                            submission='ERA32435028',
                            date_submitted='2025-04-17T00:00:00+01:00',
                            name='bRalAqu1.1 alternate haplotype',
                            title='bRalAqu1 alternate haplotype',
                            description=(
                                'This project provides the genome assembly of Rallus aquaticus'
                                ', common name water rail. The assembly is provided by the Darwin'
                                ' Tree of Life Project (https'
                            ),
                            alias='WSI_primary_bRalAqu1.1 alternate haplotype',
                            submitter_id='WELLCOME SANGER INSTITUTE',
                            is_deleted=False,
                        ),
                    ),
                    BioprojectLink(
                        id=13253,
                        parent_accession_id='PRJEB75639',
                        child_accession_id='PRJEB75638',
                        link_status='New',
                        child=Accession(
                            accession_id='PRJEB75638',
                            accession_type_id='BioProject - Species Data',
                            secondary='ERP160198',
                            submission='ERA29771179',
                            date_submitted='2024-05-12T00:00:00+01:00',
                            name='bRalAqu',
                            title=(
                                'Rallus aquaticus (water rail), genomic and transcriptomic data'
                            ),
                            description=(
                                'This project collects the genomic and transcriptomic data'
                                ' generated for Rallus aquaticus, common name water rail, to'
                                ' facilitate genome assembly and annotation as part of the Darwin'
                                ' Tree of Life Project (https://www.darwintreeoflife.org/). The'
                                ' data under this project are made available subject to the'
                                ' Darwin Tree of Life Open Data Release Policy (https'
                                '://www.darwintreeoflife.org/project-resources/).'
                            ),
                            alias='ena-tol-bRalAqu-study-rawdata-20240512',
                            submitter_id='WELLCOME SANGER INSTITUTE',
                            is_deleted=False,
                        ),
                    ),
                ],
                parent_assn=[
                    BioprojectLink(
                        id=13254,
                        parent_accession_id='PRJEB40665',
                        child_accession_id='PRJEB75639',
                        link_status='New',
                    ),
                    BioprojectLink(
                        id=13255,
                        parent_accession_id='PRJEB43745',
                        child_accession_id='PRJEB75639',
                        link_status='New',
                    ),
                    BioprojectLink(
                        id=13256,
                        parent_accession_id='PRJNA489243',
                        child_accession_id='PRJEB75639',
                        link_status='New',
                        parent=Accession(
                            accession_id='PRJNA489243',
                            accession_type_id='BioProject - Project Umbrella',
                            date_submitted='2018-09-06T00:00:00+01:00',
                            title='Vertebrate Genomes Project',
                            description=(
                                'Reference genomes for all > 70,000 vertebrate species.   The'
                                ' goal of the Vertebrate Genomes Project (VGP) is to generate or'
                                ' collect at least one high-quality, error-free, near gapless'
                                ', chromosome-level, haplotype phased, and annotated reference'
                                ' genome assembly of all extant vertebrate species, and to'
                                ' utilize those genomes to address fundamental questions in'
                                ' biology, disease, and conservation. This umbrella BioProject ID'
                                ' collects all such assemblies that reach these metrics'
                                ', generated by the VGP, collaborators, and others that wish to'
                                ' be grouped under VGP reference genomes, and that are publicly'
                                ' available to the community. The aspired metric minimum to be'
                                ' included in this list as of February 2017 are assemblies that'
                                ' have a contig N50 > 1Mb, scaffold N50 > 10Mb, 90% of the'
                                ' assembly assigned to scaffolds that represent chromosomes, base'
                                ' call accuracy of QV40 or greater, and haplotype phased as much'
                                ' as possible.'
                            ),
                            alias='PRJNA489243',
                            submitter_id='Genome 10K',
                            is_deleted=False,
                        ),
                    ),
                    BioprojectLink(
                        id=21132,
                        parent_accession_id='PRJEB80366',
                        child_accession_id='PRJEB75639',
                        link_status='New',
                        parent=Accession(
                            accession_id='PRJEB80366',
                            accession_type_id='BioProject - Project Umbrella',
                            submission='ERA30823184',
                            date_submitted='2024-09-20T00:00:00+01:00',
                            name='AEGIS',
                            title=(
                                'AEGIS (Ancient Environmental Genomics Initiative for'
                                ' Sustainability)'
                            ),
                            description=(
                                'AEGIS (Ancient Environmental Genomics Initiative for'
                                ' Sustainability) is a multi-centre project, funded by the'
                                ' NovoNordisk Foundation (Denmark) and the Wellcome Trust (UK'
                                ') (https://www.sanger.ac.uk/collaboration/ancient-environmental'
                                '-genomics-initiative-for-sustainability-aegis/). The overarching'
                                ' aims of AEGIS are to develop the essential science and'
                                ' methodology to use ancient eDNA – coupled with other ancient'
                                ' and modern biomolecule-based approaches – to identify important'
                                ' organismal associations and genetic adaptations in natural and'
                                ' agroecosystems that will improve future food security under'
                                ' climate change. At the Wellcome Sanger Institute, the Tree of'
                                ' Life programme (https://www.sanger.ac.uk/programme/tree-of-life'
                                '/) is sequencing to reference standard the genomes of modern'
                                ' species that will enhance the library of genomes available for'
                                ' ancient eDNA mapping.'
                            ),
                            alias='ena-tol-aegis-project-umbrella-20240920',
                            submitter_id='WELLCOME SANGER INSTITUTE',
                            is_deleted=False,
                        ),
                    ),
                ],
            ),
            location=Location(location_id=824, path='3/b/5/0/1/e/Rallus_aquaticus'),
        ),
        Assembly(assembly_id=7103, assembly_status_id=7103),
        Assembly(assembly_id=7104, assembly_status_id=7104),
        Assembly(assembly_id=156, assembly_status_id=156),
        Assembly(assembly_id=157, assembly_status_id=157),
        Dataset(dataset_id='01K6BJYB201CTC53DYQ1M674KK'),
        Dataset(dataset_id='01K6B5R10VC8F9XTXCVGXM50Q2', dataset_status_id=10911),
        Dataset(dataset_id='01K6AW4EBE124C2EEA91HFCA1E'),
        Dataset(dataset_id='01K6BPZJ9ENAJP5C2VRA9KFY2A', dataset_status_id=19599),
        Dataset(dataset_id='01K6BKWEJ26GQ6CTC5WW7A2HDG', dataset_status_id=16531),
        Dataset(dataset_id='01K6BKW5G6FD6N8R67M976W9V9', dataset_status_id=16524),
        Dataset(dataset_id='01K6AW4FD9B0PHTZ6BGWV31K7M', dataset_status_id=3070),
        Dataset(dataset_id='01K6B331TCWW21W4K60YFKMNRW', dataset_status_id=8206),
        Dataset(dataset_id='01K6BJJ6NW4EXP9XBGYDJZED12'),
        Dataset(dataset_id='01K6AS7B9XT21VZZ2CWMV40V08', dataset_status_id=204),
        Dataset(dataset_id='01K6BNNXDTQ6G48M1YDB0DQXYM'),
        Dataset(dataset_id='01K6B4HP8K8MDPQYB63C0HWT6G', dataset_status_id=9685),
        Dataset(dataset_id='01K6ATRHFGXCKPRYPQY2CBXN3W', dataset_status_id=1709),
        Dataset(dataset_id='01K6X00XKNCBQSPYTG6WD0ABKJ'),
        Dataset(dataset_id='01K6BPCJJEK063WK6NN58J0A0P', dataset_status_id=19012),
    ]
