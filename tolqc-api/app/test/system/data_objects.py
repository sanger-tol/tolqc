# SPDX-FileCopyrightText: 2024 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from tolqc.schema.sample_data_models import (
    Accession,
    AccessionTypeDict,
    Allocation,
    Centre,
    Data,
    File,
    Library,
    LibraryType,
    PacbioRunMetrics,
    Platform,
    Project,
    QCDict,
    Run,
    Sample,
    Species,
    Specimen,
    VisibilityDict,
)
from tolqc.schema.system_models import Token, User


def test_data(token: str):
    return [
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
        LibraryType(
            library_type_id='Chromium genome', hierarchy_name='10x', category='genomic_data'
        ),
        LibraryType(
            library_type_id='Haplotagging', hierarchy_name='htag', category='genomic_data'
        ),
        LibraryType(
            library_type_id='HiSeqX PCR free', hierarchy_name='illumina', category='genomic_data'
        ),
        LibraryType(
            library_type_id='PacBio - IsoSeq',
            hierarchy_name='pacbio',
            category='transcriptomic_data',
        ),
        LibraryType(
            library_type_id='Standard', hierarchy_name='illumina', category='genomic_data'
        ),
        LibraryType(library_type_id='Custom'),
        LibraryType(library_type_id='No PCR (Plate)'),
        LibraryType(library_type_id='qPCR only'),
        LibraryType(library_type_id='Pre-quality controlled'),
        LibraryType(library_type_id='Manual Standard WGS (Plate)'),
        LibraryType(library_type_id='Nextera dual index pre quality controlled'),
        LibraryType(library_type_id='Pacbio_Amplicon'),
        LibraryType(
            library_type_id='RNA PolyA',
            hierarchy_name='rna-seq',
            category='transcriptomic_data',
            reporting_category='rnaseq',
        ),
        LibraryType(
            library_type_id='RNA-seq dUTP eukaryotic',
            hierarchy_name='rna-seq',
            category='transcriptomic_data',
            reporting_category='rnaseq',
        ),
        LibraryType(
            library_type_id='RNA-seq dUTP prokaryotic',
            hierarchy_name='rna-seq',
            category='transcriptomic_data',
            reporting_category='rnaseq',
        ),
        LibraryType(
            library_type_id='Small RNA (miRNA)',
            hierarchy_name='rna-seq',
            category='transcriptomic_data',
            reporting_category='rnaseq',
        ),
        LibraryType(
            library_type_id='PacBio - HiFi',
            hierarchy_name='pacbio',
            category='genomic_data',
            reporting_category='pacbio',
        ),
        LibraryType(
            library_type_id='PacBio - HiFi (Microbial)',
            hierarchy_name='pacbio',
            category='genomic_data',
            reporting_category='pacbio',
        ),
        LibraryType(
            library_type_id='PacBio - HiFi (ULI)',
            hierarchy_name='pacbio',
            category='genomic_data',
            reporting_category='pacbio',
        ),
        LibraryType(
            library_type_id='Hi-C',
            hierarchy_name='hic',
            category='genomic_data',
            reporting_category='hic',
        ),
        LibraryType(
            library_type_id='Hi-C - Arima v1',
            hierarchy_name='hic-arima',
            category='genomic_data',
            reporting_category='hic',
        ),
        LibraryType(
            library_type_id='Hi-C - Arima v2',
            hierarchy_name='hic-arima2',
            category='genomic_data',
            reporting_category='hic',
        ),
        LibraryType(
            library_type_id='Hi-C - Dovetail',
            hierarchy_name='hic-dovetail',
            category='genomic_data',
            reporting_category='hic',
        ),
        LibraryType(
            library_type_id='Hi-C - OmniC',
            hierarchy_name='hic-omic',
            category='genomic_data',
            reporting_category='hic',
        ),
        LibraryType(
            library_type_id='Hi-C - Qiagen',
            hierarchy_name='hic-qiagen',
            category='genomic_data',
            reporting_category='hic',
        ),
        LibraryType(library_type_id='PacBio - CLR'),
        LibraryType(library_type_id='RNA Ribo'),
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
        Centre(id=2, name='Wellcome Sanger Institute'),
        QCDict(qc_state='pass'),
        QCDict(qc_state='fail'),
        VisibilityDict(visibility='Always', description='Shown in standard reporting'),
        VisibilityDict(visibility='Testing', description='Sequencing development data'),
        VisibilityDict(visibility='Withdrawn', description='Data has been deleted'),
        VisibilityDict(visibility='MetadataIssue', description='Metadata has issues'),
        VisibilityDict(
            visibility='SampleSwap', description='Data involved in a possible sample swap'
        ),
        Project(
            project_id=17,
            hierarchy_name='darwin/rnd',
            description='DTOL_Darwin R&D',
            study_id=5822,
        ),
        Project(
            project_id=21,
            hierarchy_name='darwin/{}',  # noqa: P103
            description='DTOL_Darwin Tree of Life',
            study_id=5901,
        ),
        Project(
            project_id=24,
            hierarchy_name='darwin/{}',  # noqa: P103
            description='DTOL_Darwin Tree of Life RNA',
            study_id=6327,
        ),
        Species(
            species_id='Brachiomonas submarina',
            hierarchy_name='Brachiomonas_submarina',
            taxon_id=327064,
            taxon_family='Chlamydomonadaceae',
            taxon_order='Chlamydomonadales',
            taxon_phylum='Chlorophyta',
            taxon_group='algae',
            genome_size=293400000,
            chromosome_number=16,
            specimens=[
                Specimen(
                    specimen_id='ucBraSubp1',
                    species_id='Brachiomonas submarina',
                    accession_id='SAMEA7532740',
                    samples=[
                        Sample(
                            sample_id='DTOL_RD10244236',
                            specimen_id='ucBraSubp1',
                            data=[
                                Data(
                                    data_id='37939_1#2',
                                    study_id=5822,
                                    sample_id='DTOL_RD10244236',
                                    library_id='DN805609I:B3',
                                    run_id='37939',
                                    processed=0,
                                    tag_index='2',
                                    tag1_id='18',
                                    tag2_id='18',
                                    date='2021-05-21T10:35:42+01:00',
                                    lims_qc='pass',
                                    visibility='Always',
                                    reads=81186152,
                                    bases=12056143572,
                                    library=Library(
                                        library_id='DN805609I:B3', library_type_id='Haplotagging'
                                    ),
                                    run=Run(
                                        run_id='37939',
                                        platform_id=5,
                                        centre_id=2,
                                        instrument_name='NV22',
                                        complete='2021-05-14T11:44:28+01:00',
                                    ),
                                    files=[
                                        File(
                                            id=112380,
                                            data_id='37939_1#2',
                                            remote_path=(
                                                'irods:/seq/illumina/runs/37/37939/lane1/plex2'
                                                '/37939_1#2.cram'
                                            ),
                                        )
                                    ],
                                    project_assn=[
                                        Allocation(id=115631, project_id=17, data_id='37939_1#2')
                                    ],
                                )
                            ],
                        ),
                        Sample(
                            sample_id='DTOL9310949',
                            specimen_id='ucBraSubp1',
                            data=[
                                Data(
                                    data_id='35344_1#2',
                                    study_id=5901,
                                    sample_id='DTOL9310949',
                                    library_id='DN683544F:A5',
                                    run_id='35344',
                                    processed=1,
                                    tag_index='2',
                                    tag1_id='130',
                                    date='2020-11-13T11:13:32+00:00',
                                    lims_qc='pass',
                                    visibility='Always',
                                    reads=3205550,
                                    bases=484038050,
                                    library=Library(
                                        library_id='DN683544F:A5',
                                        library_type_id='Chromium genome',
                                    ),
                                    run=Run(
                                        run_id='35344',
                                        platform_id=2,
                                        centre_id=2,
                                        instrument_name='HX8',
                                        complete='2020-11-06T10:04:30+00:00',
                                    ),
                                    files=[
                                        File(
                                            id=114489,
                                            data_id='35344_1#2',
                                            remote_path='irods:/seq/35344/35344_1#2.cram',
                                        )
                                    ],
                                    project_assn=[
                                        Allocation(id=117752, project_id=21, data_id='35344_1#2')
                                    ],
                                ),
                                Data(
                                    data_id='35344_1#4',
                                    study_id=5901,
                                    sample_id='DTOL9310949',
                                    library_id='DN683544F:A5',
                                    run_id='35344',
                                    processed=None,
                                    tag_index='4',
                                    tag1_id='132',
                                    date='2020-11-13T11:13:32+00:00',
                                    lims_qc='pass',
                                    visibility='Always',
                                    reads=120600430,
                                    bases=18210664930,
                                    library=Library(
                                        library_id='DN683544F:A5',
                                        library_type_id='Chromium genome',
                                    ),
                                    run=Run(
                                        run_id='35344',
                                        platform_id=2,
                                        centre_id=2,
                                        instrument_name='HX8',
                                        complete='2020-11-06T10:04:30+00:00',
                                    ),
                                    files=[
                                        File(
                                            id=114491,
                                            data_id='35344_1#4',
                                            remote_path='irods:/seq/35344/35344_1#4.cram',
                                        )
                                    ],
                                    project_assn=[
                                        Allocation(id=117754, project_id=21, data_id='35344_1#4')
                                    ],
                                ),
                                Data(
                                    data_id='35344_1#3',
                                    study_id=5901,
                                    sample_id='DTOL9310949',
                                    library_id='DN683544F:A5',
                                    run_id='35344',
                                    processed=0,
                                    tag_index='3',
                                    tag1_id='131',
                                    date='2020-11-13T11:13:32+00:00',
                                    lims_qc='pass',
                                    visibility='Testing',
                                    reads=118915580,
                                    bases=17956252580,
                                    library=Library(
                                        library_id='DN683544F:A5',
                                        library_type_id='Chromium genome',
                                    ),
                                    run=Run(
                                        run_id='35344',
                                        platform_id=2,
                                        centre_id=2,
                                        instrument_name='HX8',
                                        complete='2020-11-06T10:04:30+00:00',
                                    ),
                                    files=[
                                        File(
                                            id=114490,
                                            data_id='35344_1#3',
                                            remote_path='irods:/seq/35344/35344_1#3.cram',
                                        )
                                    ],
                                    project_assn=[
                                        Allocation(id=117753, project_id=21, data_id='35344_1#3')
                                    ],
                                ),
                                Data(
                                    data_id='35344_1#1',
                                    study_id=5901,
                                    sample_id='DTOL9310949',
                                    library_id='DN683544F:A5',
                                    run_id='35344',
                                    processed=0,
                                    tag_index='1',
                                    tag1_id='129',
                                    date='2020-11-13T11:13:32+00:00',
                                    lims_qc='pass',
                                    visibility='Always',
                                    reads=117883578,
                                    bases=17800420278,
                                    library=Library(
                                        library_id='DN683544F:A5',
                                        library_type_id='Chromium genome',
                                    ),
                                    run=Run(
                                        run_id='35344',
                                        platform_id=2,
                                        centre_id=2,
                                        instrument_name='HX8',
                                        complete='2020-11-06T10:04:30+00:00',
                                    ),
                                    files=[
                                        File(
                                            id=114488,
                                            data_id='35344_1#1',
                                            remote_path='irods:/seq/35344/35344_1#1.cram',
                                        )
                                    ],
                                    project_assn=[
                                        Allocation(id=117751, project_id=21, data_id='35344_1#1')
                                    ],
                                ),
                            ],
                        ),
                        Sample(
                            sample_id='DTOL9384820',
                            specimen_id='ucBraSubp1',
                            accession_id='SAMEA7532766',
                            accession=Accession(
                                accession_id='SAMEA7532766', accession_type_id='BioSample'
                            ),
                            data=[
                                Data(
                                    data_id='35528_4#8',
                                    study_id=5901,
                                    sample_id='DTOL9384820',
                                    library_id='DN703060C:H1',
                                    run_id='35528',
                                    processed=1,
                                    tag_index='8',
                                    tag1_id='72',
                                    tag2_id='72',
                                    date='2020-11-24T19:23:18+00:00',
                                    lims_qc='pass',
                                    visibility='Always',
                                    reads=748759474,
                                    bases=113062680574,
                                    library=Library(
                                        library_id='DN703060C:H1',
                                        library_type_id='Hi-C - Arima v2',
                                    ),
                                    run=Run(
                                        run_id='35528',
                                        platform_id=5,
                                        centre_id=2,
                                        instrument_name='NV16',
                                        complete='2020-11-19T08:24:02+00:00',
                                    ),
                                    files=[
                                        File(
                                            id=114697,
                                            data_id='35528_4#8',
                                            remote_path=(
                                                'irods:/seq/illumina/runs/35/35528/lane4/plex8'
                                                '/35528_4#8.cram'
                                            ),
                                        )
                                    ],
                                    project_assn=[
                                        Allocation(id=117960, project_id=21, data_id='35528_4#8')
                                    ],
                                )
                            ],
                        ),
                        Sample(
                            sample_id='DTOL9397431',
                            specimen_id='ucBraSubp1',
                            data=[
                                Data(
                                    data_id='m64089e_210601_133425#1022',
                                    study_id=5901,
                                    sample_id='DTOL9397431',
                                    library_id='DN695911V-H1',
                                    run_id='m64089e_210601_133425',
                                    processed=None,
                                    tag1_id='1022',
                                    date='2021-06-02T23:04:37+01:00',
                                    lims_qc='fail',
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
                                    reads_filtered=0,
                                    library=Library(library_id='DN695911V-H1'),
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
                                        pacbio_run_metrics=[
                                            PacbioRunMetrics(
                                                run_id='m64089e_210601_133425',
                                                movie_minutes=1800,
                                                binding_kit='Sequel II Binding Kit 2.2',
                                                sequencing_kit=(
                                                    'Sequel II Sequencing Plate 2.0 (4 rxn)'
                                                ),
                                                include_kinetics='true',
                                                loading_conc=70.0,
                                                control_num_reads=8197,
                                                control_read_length_mean=27617.0,
                                                polymerase_read_bases=28215924595,
                                                polymerase_num_reads=622368,
                                                polymerase_read_length_mean=45336.0,
                                                polymerase_read_length_n50=160250,
                                                insert_length_mean=12667.0,
                                                insert_length_n50=14750,
                                                unique_molecular_bases=7474866688,
                                                p0_num=7376744,
                                                p1_num=630565,
                                                p2_num=7362,
                                                hifi_read_bases=1295136871,
                                                hifi_num_reads=120696,
                                                hifi_low_quality_num_reads=16141,
                                            )
                                        ],
                                    ),
                                    files=[
                                        File(
                                            id=120785,
                                            data_id='m64089e_210601_133425#1022',
                                            remote_path=(
                                                'irods:/seq/pacbio/r64089e_20210528_093647/4_D01'
                                                '/demultiplex.bc1022_BAK8B_OA'
                                                '--bc1022_BAK8B_OA.bam'
                                            ),
                                        )
                                    ],
                                    project_assn=[
                                        Allocation(
                                            id=124055,
                                            project_id=21,
                                            data_id='m64089e_210601_133425#1022',
                                        )
                                    ],
                                ),
                                Data(
                                    data_id='m64016_201115_112225#1022',
                                    study_id=5901,
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
                                    reads_filtered=1390,
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
                                        pacbio_run_metrics=[
                                            PacbioRunMetrics(run_id='m64016_201115_112225')
                                        ],
                                    ),
                                    files=[
                                        File(
                                            id=143249,
                                            data_id='m64016_201115_112225#1022',
                                            remote_path=(
                                                'irods:/seq/pacbio/r64016_20201112_100113/4_D01'
                                                '/demultiplex.bc1022_BAK8B_OA'
                                                '--bc1022_BAK8B_OA.bam'
                                            ),
                                        )
                                    ],
                                    project_assn=[
                                        Allocation(
                                            id=147115,
                                            project_id=21,
                                            data_id='m64016_201115_112225#1022',
                                        )
                                    ],
                                ),
                            ],
                        ),
                        Sample(
                            sample_id='DTOLRNA9465095',
                            specimen_id='ucBraSubp1',
                            accession_id='SAMEA7532770',
                            accession=Accession(
                                accession_id='SAMEA7532770', accession_type_id='BioSample'
                            ),
                            data=[
                                Data(
                                    data_id='36703_5#4',
                                    study_id=6327,
                                    sample_id='DTOLRNA9465095',
                                    library_id='DN611904M:F3',
                                    run_id='36703',
                                    processed=None,
                                    tag_index='4',
                                    tag1_id='22',
                                    tag2_id='22',
                                    date='2021-03-19T10:56:23+00:00',
                                    lims_qc='pass',
                                    visibility='Always',
                                    reads=41616914,
                                    bases=6284154014,
                                    library=Library(
                                        library_id='DN611904M:F3', library_type_id='RNA PolyA'
                                    ),
                                    run=Run(
                                        run_id='36703',
                                        platform_id=4,
                                        centre_id=2,
                                        instrument_name='HF1',
                                        complete='2021-03-08T10:31:06+00:00',
                                    ),
                                    files=[
                                        File(
                                            id=123947,
                                            data_id='36703_5#4',
                                            remote_path='irods:/seq/36703/36703_5#4.cram',
                                        )
                                    ],
                                    project_assn=[
                                        Allocation(id=127430, project_id=24, data_id='36703_5#4')
                                    ],
                                )
                            ],
                        ),
                    ],
                    accession=Accession(
                        accession_id='SAMEA7532740', accession_type_id='BioSample'
                    ),
                )
            ],
        ),
        Species(
            species_id='Juncus effusus',
            hierarchy_name='Juncus_effusus',
            common_name='common rush',
            taxon_id=13579,
            taxon_family='Juncaceae',
            taxon_order='Poales',
            taxon_phylum='Streptophyta',
            taxon_group='monocots',
            genome_size=293400000,
            chromosome_number=46,
            specimens=[
                Specimen(
                    specimen_id='lpJunEffu1',
                    species_id='Juncus effusus',
                    accession_id='SAMEA7521930',
                    samples=[
                        Sample(
                            sample_id='DTOL9702654',
                            specimen_id='lpJunEffu1',
                            accession_id='SAMEA7521953',
                            accession=Accession(
                                accession_id='SAMEA7521953', accession_type_id='BioSample'
                            ),
                            data=[
                                Data(
                                    data_id='36691_2#8',
                                    study_id=5901,
                                    sample_id='DTOL9702654',
                                    library_id='DN771163M:G8',
                                    run_id='36691',
                                    processed=1,
                                    tag_index='8',
                                    tag1_id='252',
                                    date='2021-03-18T12:16:43+00:00',
                                    lims_qc='pass',
                                    visibility='Always',
                                    reads=210626924,
                                    bases=31804665524,
                                    library=Library(
                                        library_id='DN771163M:G8',
                                        library_type_id='Chromium genome',
                                    ),
                                    run=Run(
                                        run_id='36691',
                                        platform_id=5,
                                        centre_id=2,
                                        instrument_name='NV20',
                                        complete='2021-03-06T05:07:44+00:00',
                                    ),
                                    files=[
                                        File(
                                            id=115167,
                                            data_id='36691_2#8',
                                            remote_path=(
                                                'irods:/seq/illumina/runs/36/36691/lane2/plex8'
                                                '/36691_2#8.cram'
                                            ),
                                        )
                                    ],
                                    project_assn=[
                                        Allocation(id=118430, project_id=21, data_id='36691_2#8')
                                    ],
                                ),
                                Data(
                                    data_id='36691_2#5',
                                    study_id=5901,
                                    sample_id='DTOL9702654',
                                    library_id='DN771163M:G8',
                                    run_id='36691',
                                    processed=1,
                                    tag_index='5',
                                    tag1_id='249',
                                    date='2021-03-18T12:16:43+00:00',
                                    lims_qc='pass',
                                    visibility='Always',
                                    reads=195080402,
                                    bases=29457140702,
                                    library=Library(
                                        library_id='DN771163M:G8',
                                        library_type_id='Chromium genome',
                                    ),
                                    run=Run(
                                        run_id='36691',
                                        platform_id=5,
                                        centre_id=2,
                                        instrument_name='NV20',
                                        complete='2021-03-06T05:07:44+00:00',
                                    ),
                                    files=[
                                        File(
                                            id=115164,
                                            data_id='36691_2#5',
                                            remote_path=(
                                                'irods:/seq/illumina/runs/36/36691/lane2/plex5'
                                                '/36691_2#5.cram'
                                            ),
                                        )
                                    ],
                                    project_assn=[
                                        Allocation(id=118427, project_id=21, data_id='36691_2#5')
                                    ],
                                ),
                                Data(
                                    data_id='36691_2#7',
                                    study_id=5901,
                                    sample_id='DTOL9702654',
                                    library_id='DN771163M:G8',
                                    run_id='36691',
                                    processed=1,
                                    tag_index='7',
                                    tag1_id='251',
                                    date='2021-03-18T12:16:43+00:00',
                                    lims_qc='pass',
                                    visibility='Always',
                                    reads=183614994,
                                    bases=27725864094,
                                    library=Library(
                                        library_id='DN771163M:G8',
                                        library_type_id='Chromium genome',
                                    ),
                                    run=Run(
                                        run_id='36691',
                                        platform_id=5,
                                        centre_id=2,
                                        instrument_name='NV20',
                                        complete='2021-03-06T05:07:44+00:00',
                                    ),
                                    files=[
                                        File(
                                            id=115166,
                                            data_id='36691_2#7',
                                            remote_path=(
                                                'irods:/seq/illumina/runs/36/36691/lane2/plex7'
                                                '/36691_2#7.cram'
                                            ),
                                        )
                                    ],
                                    project_assn=[
                                        Allocation(id=118429, project_id=21, data_id='36691_2#7')
                                    ],
                                ),
                                Data(
                                    data_id='36691_2#6',
                                    study_id=5901,
                                    sample_id='DTOL9702654',
                                    library_id='DN771163M:G8',
                                    run_id='36691',
                                    processed=1,
                                    tag_index='6',
                                    tag1_id='250',
                                    date='2021-03-18T12:16:43+00:00',
                                    lims_qc='pass',
                                    visibility='Always',
                                    reads=206862242,
                                    bases=31236198542,
                                    library=Library(
                                        library_id='DN771163M:G8',
                                        library_type_id='Chromium genome',
                                    ),
                                    run=Run(
                                        run_id='36691',
                                        platform_id=5,
                                        centre_id=2,
                                        instrument_name='NV20',
                                        complete='2021-03-06T05:07:44+00:00',
                                    ),
                                    files=[
                                        File(
                                            id=115165,
                                            data_id='36691_2#6',
                                            remote_path=(
                                                'irods:/seq/illumina/runs/36/36691/lane2/plex6'
                                                '/36691_2#6.cram'
                                            ),
                                        )
                                    ],
                                    project_assn=[
                                        Allocation(id=118428, project_id=21, data_id='36691_2#6')
                                    ],
                                ),
                            ],
                        ),
                        Sample(
                            sample_id='DTOL10341656',
                            specimen_id='lpJunEffu1',
                            accession_id='SAMEA7521954',
                            accession=Accession(
                                accession_id='SAMEA7521954', accession_type_id='BioSample'
                            ),
                            data=[
                                Data(
                                    data_id='40666_2#2',
                                    study_id=5901,
                                    sample_id='DTOL10341656',
                                    library_id='DN826505P:B3',
                                    run_id='40666',
                                    processed=1,
                                    tag_index='2',
                                    tag1_id='90',
                                    tag2_id='90',
                                    date='2021-09-11T11:11:14+01:00',
                                    lims_qc='pass',
                                    visibility='Always',
                                    reads=3345851480,
                                    bases=505223573480,
                                    library=Library(
                                        library_id='DN826505P:B3',
                                        library_type_id='Hi-C - Arima v2',
                                    ),
                                    run=Run(
                                        run_id='40666',
                                        platform_id=5,
                                        centre_id=2,
                                        instrument_name='NV11',
                                        complete='2021-09-05T07:44:37+01:00',
                                    ),
                                    files=[
                                        File(
                                            id=117820,
                                            data_id='40666_2#2',
                                            remote_path=(
                                                'irods:/seq/illumina/runs/40/40666/lane2/plex2'
                                                '/40666_2#2.cram'
                                            ),
                                        )
                                    ],
                                    project_assn=[
                                        Allocation(id=121083, project_id=21, data_id='40666_2#2')
                                    ],
                                )
                            ],
                        ),
                        Sample(
                            sample_id='DTOL9838614',
                            specimen_id='lpJunEffu1',
                            accession_id='SAMEA7521953',
                            accession=Accession(
                                accession_id='SAMEA7521953', accession_type_id='BioSample'
                            ),
                            data=[
                                Data(
                                    data_id='m64097e_210221_172213#1019',
                                    study_id=5901,
                                    sample_id='DTOL9838614',
                                    library_id='DN765124Q-B1',
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
                                    reads_filtered=6869,
                                    library=Library(library_id='DN765124Q-B1'),
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
                                        pacbio_run_metrics=[
                                            PacbioRunMetrics(
                                                run_id='m64097e_210221_172213',
                                                movie_minutes=1440,
                                                binding_kit='Sequel II Binding Kit 2.0',
                                                sequencing_kit=(
                                                    'Sequel II Sequencing Plate 2.0 (4 rxn)'
                                                ),
                                                include_kinetics='true',
                                                loading_conc=45.0,
                                                control_num_reads=3200,
                                                control_read_length_mean=51271.0,
                                                polymerase_read_bases=329209363529,
                                                polymerase_num_reads=4556774,
                                                polymerase_read_length_mean=72246.0,
                                                polymerase_read_length_n50=146877,
                                                insert_length_mean=13239.0,
                                                insert_length_n50=15638,
                                                unique_molecular_bases=57195683840,
                                                p0_num=3352198,
                                                p1_num=4559996,
                                                p2_num=102477,
                                                hifi_read_bases=22632028638,
                                                hifi_num_reads=1863309,
                                                hifi_low_quality_num_reads=345974,
                                            )
                                        ],
                                    ),
                                    files=[
                                        File(
                                            id=121145,
                                            data_id='m64097e_210221_172213#1019',
                                            remote_path=(
                                                'irods:/seq/pacbio/r64097e_20210218_161440/4_D01'
                                                '/demultiplex.bc1019_BAK8B_OA'
                                                '--bc1019_BAK8B_OA.bam'
                                            ),
                                        )
                                    ],
                                    project_assn=[
                                        Allocation(
                                            id=124432,
                                            project_id=21,
                                            data_id='m64097e_210221_172213#1019',
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
                                accession_id='SAMEA7521953', accession_type_id='BioSample'
                            ),
                            data=[
                                Data(
                                    data_id='37935_8#13',
                                    study_id=6327,
                                    sample_id='DTOLRNA10187174',
                                    library_id='DN612239G:G9',
                                    run_id='37935',
                                    processed=1,
                                    tag_index='13',
                                    tag1_id='71',
                                    tag2_id='71',
                                    date='2021-05-25T13:45:59+01:00',
                                    lims_qc='pass',
                                    visibility='Always',
                                    reads=36344960,
                                    bases=5488088960,
                                    library=Library(
                                        library_id='DN612239G:G9', library_type_id='RNA PolyA'
                                    ),
                                    run=Run(
                                        run_id='37935',
                                        platform_id=4,
                                        centre_id=2,
                                        instrument_name='HF2',
                                        complete='2021-05-16T21:08:02+01:00',
                                    ),
                                    files=[
                                        File(
                                            id=124080,
                                            data_id='37935_8#13',
                                            remote_path='irods:/seq/37935/37935_8#13.cram',
                                        )
                                    ],
                                    project_assn=[
                                        Allocation(id=127563, project_id=24, data_id='37935_8#13')
                                    ],
                                )
                            ],
                        ),
                        Sample(
                            sample_id='DTOLRNA14460441',
                            specimen_id='lpJunEffu1',
                            accession_id='SAMEA7521957',
                            accession=Accession(
                                accession_id='SAMEA7521957', accession_type_id='BioSample'
                            ),
                            data=[
                                Data(
                                    data_id='48593_1#25',
                                    study_id=6327,
                                    sample_id='DTOLRNA14460441',
                                    library_id='SQPP-7739-H:B9',
                                    run_id='48593',
                                    processed=1,
                                    tag_index='25',
                                    tag1_id='66',
                                    tag2_id='66',
                                    date='2024-03-15T15:52:57+00:00',
                                    lims_qc='pass',
                                    visibility='Always',
                                    reads=52850970,
                                    bases=7980496470,
                                    library=Library(
                                        library_id='SQPP-7739-H:B9', library_type_id='RNA PolyA'
                                    ),
                                    run=Run(
                                        run_id='48593',
                                        platform_id=8,
                                        centre_id=2,
                                        instrument_name='NX1',
                                        complete='2024-03-08T10:04:27+00:00',
                                    ),
                                    files=[
                                        File(
                                            id=139273,
                                            data_id='48593_1#25',
                                            remote_path=(
                                                'irods:/seq/illumina/runs/48/48593/lane1/plex25'
                                                '/48593_1#25.cram'
                                            ),
                                        )
                                    ],
                                    project_assn=[
                                        Allocation(id=143140, project_id=24, data_id='48593_1#25')
                                    ],
                                )
                            ],
                        ),
                    ],
                    accession=Accession(
                        accession_id='SAMEA7521930', accession_type_id='BioSample'
                    ),
                )
            ],
        ),
        User(
            id=100,
            email='skdsjdkj',
            name='lol',
            registered=True,
        ),
        Token(
            id=200,
            token=token,
            user_id=100
        ),
    ]
