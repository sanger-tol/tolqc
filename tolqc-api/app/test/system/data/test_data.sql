--
-- PostgreSQL database dump
--

-- Dumped from database version 12.17 (Debian 12.17-1.pgdg120+1)
-- Dumped by pg_dump version 16.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: accession_type_dict; Type: TABLE DATA; Schema: public; Owner: sts-dev
--

INSERT INTO public.accession_type_dict VALUES ('GenBank Genome Assembly', '^GCA_\d+\.\d+$', 'https://www.ncbi.nlm.nih.gov/datasets/genome/{}/');
INSERT INTO public.accession_type_dict VALUES ('Bio Project', '^PRJ[A-Z]{2}\d+$', 'https://www.ebi.ac.uk/ena/browser/view/{}');
INSERT INTO public.accession_type_dict VALUES ('ENA Run', '^ERR\d+$', 'https://www.ebi.ac.uk/ena/browser/view/{}');
INSERT INTO public.accession_type_dict VALUES ('ENA Experiment', '^ERX\d+$', 'https://www.ebi.ac.uk/ena/browser/view/{}');
INSERT INTO public.accession_type_dict VALUES ('ToL Specimen ID', '^[a-z]{1,2}[A-Z][a-z]{2}[A-Z][a-z]{2,3}\d+$', NULL);
INSERT INTO public.accession_type_dict VALUES ('Bio Sample', '^SAM[A-Z]{2}\d+$', 'https://www.ebi.ac.uk/biosamples/samples/{}');
INSERT INTO public.accession_type_dict VALUES ('ENA Analysis', '^ERZ\d+$', 'https://www.ebi.ac.uk/ena/browser/view/{}');
INSERT INTO public.accession_type_dict VALUES ('SRA Run', '^SRR\d+$', NULL);
INSERT INTO public.accession_type_dict VALUES ('SRA Experiment', '^SRX\d+$', NULL);


--
-- Data for Name: accession; Type: TABLE DATA; Schema: public; Owner: sts-dev
--

INSERT INTO public.accession VALUES ('SAMEA13840482', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA13840472', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA13840460', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA13840478', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA13840462', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA12362595', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA12362597', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA12362596', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA9089040', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA9089041', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA9089042', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA9089044', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA9089043', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA9089045', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA9089046', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA9089047', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA9089048', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA9089049', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA9089050', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA9089051', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA9089052', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA9089053', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA9089054', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA13840469', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA9089039', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA9335427', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA9335274', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA9089056', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA9089055', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA13831117', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA13831067', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA13831138', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA13831088', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA13831107', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA13831057', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA13831140', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA13831090', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA13831130', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA13831080', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA13831110', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA13831060', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA13831143', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA13831093', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA13831125', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA13831075', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA13831096', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA13831046', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA13831109', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA13831059', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA13831132', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA13831082', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA10270795', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA10270683', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA10270788', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA10270673', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA10270802', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA10270690', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA10270804', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA10270692', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA10270842', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA10270740', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA10270835', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA10270730', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA13831135', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA13831085', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA13831100', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA13831050', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA13831137', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA13831087', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA9067702', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA9067607', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA112816492', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA112816472', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA112816504', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA112816484', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA10270801', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA10270689', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA112816608', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA112816588', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA112816491', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA112816680', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA112816669', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA10270793', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA10270794', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA10270682', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA10270875', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA10270697', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA7521953', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA7521954', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.accession VALUES ('SAMEA7521930', 'Bio Sample', NULL, NULL, NULL, NULL, NULL);


--
-- Data for Name: centre; Type: TABLE DATA; Schema: public; Owner: sts-dev
--

INSERT INTO public.centre VALUES (2, 'Wellcome Sanger Institute', NULL);


--
-- Data for Name: library_type; Type: TABLE DATA; Schema: public; Owner: sts-dev
--

INSERT INTO public.library_type VALUES ('Chromium genome', '10x', 'genomic_data', NULL, NULL, NULL);
INSERT INTO public.library_type VALUES ('Haplotagging', 'htag', 'genomic_data', NULL, NULL, NULL);
INSERT INTO public.library_type VALUES ('Hi-C', 'hic', 'genomic_data', NULL, NULL, NULL);
INSERT INTO public.library_type VALUES ('Hi-C - Arima v1', 'hic-arima', 'genomic_data', NULL, NULL, NULL);
INSERT INTO public.library_type VALUES ('Hi-C - Arima v2', 'hic-arima2', 'genomic_data', NULL, NULL, NULL);
INSERT INTO public.library_type VALUES ('Hi-C - Dovetail', 'hic-dovetail', 'genomic_data', NULL, NULL, NULL);
INSERT INTO public.library_type VALUES ('Hi-C - OmniC', 'hic-omic', 'genomic_data', NULL, NULL, NULL);
INSERT INTO public.library_type VALUES ('Hi-C - Qiagen', 'hic-qiagen', 'genomic_data', NULL, NULL, NULL);
INSERT INTO public.library_type VALUES ('HiSeqX PCR free', 'illumina', 'genomic_data', NULL, NULL, NULL);
INSERT INTO public.library_type VALUES ('PacBio - HiFi', 'pacbio', 'genomic_data', NULL, NULL, NULL);
INSERT INTO public.library_type VALUES ('PacBio - HiFi (Microbial)', 'pacbio', 'genomic_data', NULL, NULL, NULL);
INSERT INTO public.library_type VALUES ('PacBio - HiFi (ULI)', 'pacbio', 'genomic_data', NULL, NULL, NULL);
INSERT INTO public.library_type VALUES ('PacBio - IsoSeq', 'pacbio', 'transcriptomic_data', NULL, NULL, NULL);
INSERT INTO public.library_type VALUES ('RNA PolyA', 'rna-seq', 'transcriptomic_data', NULL, NULL, NULL);
INSERT INTO public.library_type VALUES ('RNA-seq dUTP eukaryotic', 'rna-seq', 'transcriptomic_data', NULL, NULL, NULL);
INSERT INTO public.library_type VALUES ('RNA-seq dUTP prokaryotic', 'rna-seq', 'transcriptomic_data', NULL, NULL, NULL);
INSERT INTO public.library_type VALUES ('Small RNA (miRNA)', 'rna-seq', 'transcriptomic_data', NULL, NULL, NULL);
INSERT INTO public.library_type VALUES ('Standard', 'illumina', 'genomic_data', NULL, NULL, NULL);
INSERT INTO public.library_type VALUES ('Custom', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.library_type VALUES ('No PCR (Plate)', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.library_type VALUES ('qPCR only', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.library_type VALUES ('Pre-quality controlled', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.library_type VALUES ('Manual Standard WGS (Plate)', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.library_type VALUES ('Nextera dual index pre quality controlled', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.library_type VALUES ('Pacbio_Amplicon', NULL, NULL, NULL, NULL, NULL);


--
-- Data for Name: library; Type: TABLE DATA; Schema: public; Owner: sts-dev
--

INSERT INTO public.library VALUES ('NT1630870I', 'Pre-quality controlled', NULL);
INSERT INTO public.library VALUES ('NT1630871J', 'Pre-quality controlled', NULL);
INSERT INTO public.library VALUES ('NT1630872K', 'Pre-quality controlled', NULL);
INSERT INTO public.library VALUES ('NT1630873L', 'Pre-quality controlled', NULL);
INSERT INTO public.library VALUES ('NT1630874M', 'Pre-quality controlled', NULL);
INSERT INTO public.library VALUES ('NT1630875N', 'Pre-quality controlled', NULL);
INSERT INTO public.library VALUES ('NT1630876O', 'Pre-quality controlled', NULL);
INSERT INTO public.library VALUES ('NT1630877P', 'Pre-quality controlled', NULL);
INSERT INTO public.library VALUES ('NT1630878Q', 'Pre-quality controlled', NULL);
INSERT INTO public.library VALUES ('NT1630879R', 'Pre-quality controlled', NULL);
INSERT INTO public.library VALUES ('NT1630880K', 'Pre-quality controlled', NULL);
INSERT INTO public.library VALUES ('NT1630881L', 'Pre-quality controlled', NULL);
INSERT INTO public.library VALUES ('NT1631003A', 'Pre-quality controlled', NULL);
INSERT INTO public.library VALUES ('NT1631004B', 'Pre-quality controlled', NULL);
INSERT INTO public.library VALUES ('NT1631005C', 'Pre-quality controlled', NULL);
INSERT INTO public.library VALUES ('NT1631006D', 'Pre-quality controlled', NULL);
INSERT INTO public.library VALUES ('NT1631007E', 'Pre-quality controlled', NULL);
INSERT INTO public.library VALUES ('NT1631008F', 'Pre-quality controlled', NULL);
INSERT INTO public.library VALUES ('NT1631009G', 'Pre-quality controlled', NULL);
INSERT INTO public.library VALUES ('NT1631010W', 'Pre-quality controlled', NULL);
INSERT INTO public.library VALUES ('NT1631011A', 'Pre-quality controlled', NULL);
INSERT INTO public.library VALUES ('NT1631012B', 'Pre-quality controlled', NULL);
INSERT INTO public.library VALUES ('NT1631013C', 'Pre-quality controlled', NULL);
INSERT INTO public.library VALUES ('NT1631014D', 'Pre-quality controlled', NULL);
INSERT INTO public.library VALUES ('DN805609I:E3', 'Haplotagging', NULL);
INSERT INTO public.library VALUES ('DN871923L:E11', 'Haplotagging', NULL);
INSERT INTO public.library VALUES ('DN871923L:G11', 'Haplotagging', NULL);
INSERT INTO public.library VALUES ('DN871923L:F11', 'Haplotagging', NULL);
INSERT INTO public.library VALUES ('DN871923L:H11', 'Haplotagging', NULL);
INSERT INTO public.library VALUES ('DN871923L:A2', 'Haplotagging', NULL);
INSERT INTO public.library VALUES ('DN905711L:B1', 'Hi-C - OmniC', NULL);
INSERT INTO public.library VALUES ('SQPP-1772-H:A1', 'Hi-C - Arima v2', NULL);
INSERT INTO public.library VALUES ('SQPP-1772-H:A2', 'Hi-C - Arima v2', NULL);
INSERT INTO public.library VALUES ('SQPP-1772-H:D2', 'Hi-C - Arima v2', NULL);
INSERT INTO public.library VALUES ('DN881045S:B10', 'RNA PolyA', NULL);
INSERT INTO public.library VALUES ('DN881045S:D10', 'RNA PolyA', NULL);
INSERT INTO public.library VALUES ('DN855199N-G1', NULL, NULL);
INSERT INTO public.library VALUES ('DN887103M-F4', NULL, NULL);
INSERT INTO public.library VALUES ('DN887104N-F4', NULL, NULL);
INSERT INTO public.library VALUES ('DN855199N-B2', NULL, NULL);
INSERT INTO public.library VALUES ('DN855199N-C2', NULL, NULL);
INSERT INTO public.library VALUES ('DN855199N-D2', NULL, NULL);
INSERT INTO public.library VALUES ('DN891078J-D1', NULL, NULL);
INSERT INTO public.library VALUES ('DN891079K-D1', NULL, NULL);
INSERT INTO public.library VALUES ('DTOL_RD12710417', 'PacBio - HiFi', NULL);
INSERT INTO public.library VALUES ('DTOL_RD13129891', 'PacBio - HiFi', NULL);
INSERT INTO public.library VALUES ('DTOL_RD13680853', 'PacBio - HiFi', NULL);
INSERT INTO public.library VALUES ('NT1652453N', 'Hi-C - Arima v2', NULL);
INSERT INTO public.library VALUES ('DN716902N:C11', 'Chromium genome', NULL);
INSERT INTO public.library VALUES ('NT1652454O', 'Hi-C - Arima v2', NULL);
INSERT INTO public.library VALUES ('DN847892H:C10', 'Haplotagging', NULL);
INSERT INTO public.library VALUES ('DN606678N:B7', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN606678N:C7', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN606678N:D7', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN606678N:E7', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN606678N:F7', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN606678N:G7', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN606678N:H7', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN606678N:A8', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN606678N:B8', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN606678N:C8', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN606678N:D8', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN606678N:E8', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN606678N:F8', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN606678N:G8', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN606678N:H8', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN798399W-G3', NULL, NULL);
INSERT INTO public.library VALUES ('DN798399W-G2', NULL, NULL);
INSERT INTO public.library VALUES ('DN798399W-B2', NULL, NULL);
INSERT INTO public.library VALUES ('DN801931W-A1', NULL, NULL);
INSERT INTO public.library VALUES ('DN798399W-D2', NULL, NULL);
INSERT INTO public.library VALUES ('DN798399W-E2', NULL, NULL);
INSERT INTO public.library VALUES ('DN798399W-F2', NULL, NULL);
INSERT INTO public.library VALUES ('DN798399W-H2', NULL, NULL);
INSERT INTO public.library VALUES ('DN798399W-A3', NULL, NULL);
INSERT INTO public.library VALUES ('DN798399W-B3', NULL, NULL);
INSERT INTO public.library VALUES ('DN798399W-C2', NULL, NULL);
INSERT INTO public.library VALUES ('DTOL_RD13796825', 'PacBio - HiFi', NULL);
INSERT INTO public.library VALUES ('DN922367N-A1', NULL, NULL);
INSERT INTO public.library VALUES ('DN881300O:D8', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN881228A:C1', 'RNA PolyA', NULL);
INSERT INTO public.library VALUES ('DN881300O:E8', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN881300O:F8', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN881300O:A1', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN881300O:B1', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN881300O:C1', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN881300O:D1', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN881300O:E1', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN881300O:F1', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN881300O:G1', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN881300O:H1', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN881300O:A2', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN881300O:B2', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN881300O:C2', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN881300O:D2', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN881300O:E2', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN881300O:F2', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN881300O:G2', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN881300O:H2', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN881300O:A3', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN881300O:B3', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN881300O:C3', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN881300O:D3', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN881300O:E3', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN881300O:F3', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN881300O:G3', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN881300O:H3', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN881300O:A4', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN881300O:B4', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN881300O:C4', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN881300O:D4', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN881300O:E4', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN881300O:F4', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN881300O:G4', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN881300O:H4', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN881300O:A5', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN881300O:B5', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN881300O:C5', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN881300O:D5', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN881300O:E5', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN881300O:F5', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN881300O:G5', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN881300O:H5', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN881300O:A6', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN881300O:B6', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN881300O:C6', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN881300O:D6', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN881300O:E6', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN881300O:F6', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN881300O:G6', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN881300O:H6', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN881300O:A7', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN881300O:B7', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN881300O:C7', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN881300O:D7', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN881300O:E7', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN881300O:F7', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN881300O:G7', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN881300O:H7', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN881300O:A8', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN881300O:B8', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN881300O:C8', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN881300O:G8', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN881300O:H8', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN881300O:A9', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN881300O:B9', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN881300O:C9', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN881300O:D9', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN881300O:E9', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN881300O:F9', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN881300O:G9', 'Standard', NULL);
INSERT INTO public.library VALUES ('DN805609I:D3', 'Haplotagging', NULL);
INSERT INTO public.library VALUES ('DN690780I:B10', 'Chromium genome', NULL);
INSERT INTO public.library VALUES ('DN871923L:A11', 'Haplotagging', NULL);
INSERT INTO public.library VALUES ('DN871923L:C11', 'Haplotagging', NULL);
INSERT INTO public.library VALUES ('DN871923L:B11', 'Haplotagging', NULL);
INSERT INTO public.library VALUES ('DN871923L:D11', 'Haplotagging', NULL);
INSERT INTO public.library VALUES ('DN871923L:A1', 'Haplotagging', NULL);
INSERT INTO public.library VALUES ('DN905711L:A1', 'Hi-C - OmniC', NULL);
INSERT INTO public.library VALUES ('DN881045S:C10', 'RNA PolyA', NULL);
INSERT INTO public.library VALUES ('DN881045S:E10', 'RNA PolyA', NULL);
INSERT INTO public.library VALUES ('DN881045S:F10', 'RNA PolyA', NULL);
INSERT INTO public.library VALUES ('DN881045S:G10', 'RNA PolyA', NULL);
INSERT INTO public.library VALUES ('DN881045S:H10', 'RNA PolyA', NULL);
INSERT INTO public.library VALUES ('DN881045S:A11', 'RNA PolyA', NULL);
INSERT INTO public.library VALUES ('DN881045S:B11', 'RNA PolyA', NULL);
INSERT INTO public.library VALUES ('DN881045S:C11', 'RNA PolyA', NULL);
INSERT INTO public.library VALUES ('DN881045S:D11', 'RNA PolyA', NULL);
INSERT INTO public.library VALUES ('DN881045S:E11', 'RNA PolyA', NULL);
INSERT INTO public.library VALUES ('DN881045S:F11', 'RNA PolyA', NULL);
INSERT INTO public.library VALUES ('DN739243A-A1', NULL, NULL);
INSERT INTO public.library VALUES ('DN855199N-A1', NULL, NULL);
INSERT INTO public.library VALUES ('DN855199N-F1', NULL, NULL);
INSERT INTO public.library VALUES ('DN855199N-E1', NULL, NULL);
INSERT INTO public.library VALUES ('DN855199N-D1', NULL, NULL);
INSERT INTO public.library VALUES ('DN882539Q-D1', NULL, NULL);
INSERT INTO public.library VALUES ('DN891078J-C1', NULL, NULL);
INSERT INTO public.library VALUES ('DN891079K-C1', NULL, NULL);
INSERT INTO public.library VALUES ('DN889188S-A1', NULL, NULL);
INSERT INTO public.library VALUES ('DN909105L-A1', NULL, NULL);
INSERT INTO public.library VALUES ('DTOL_RD12710414', 'PacBio - HiFi', NULL);
INSERT INTO public.library VALUES ('DTOL_RD12925574', 'PacBio - HiFi (ULI)', NULL);
INSERT INTO public.library VALUES ('DTOL_RD13129888', 'PacBio - HiFi', NULL);
INSERT INTO public.library VALUES ('DTOL_RD13179106', 'PacBio - HiFi', NULL);
INSERT INTO public.library VALUES ('DTOL_RD13680850', 'PacBio - HiFi', NULL);
INSERT INTO public.library VALUES ('DTOL_RD13698057', 'PacBio - HiFi (ULI)', NULL);
INSERT INTO public.library VALUES ('DTOL_RD13698061', 'PacBio - HiFi (ULI)', NULL);
INSERT INTO public.library VALUES ('DTOL_RD13698073', 'PacBio - HiFi (ULI)', NULL);
INSERT INTO public.library VALUES ('DTOL_RD13698078', 'PacBio - HiFi (ULI)', NULL);
INSERT INTO public.library VALUES ('DN847892H:D2', 'Haplotagging', NULL);
INSERT INTO public.library VALUES ('DN847892H:A10', 'Haplotagging', NULL);
INSERT INTO public.library VALUES ('DN760937C-A1', NULL, NULL);
INSERT INTO public.library VALUES ('DN847892H:B10', 'Haplotagging', NULL);
INSERT INTO public.library VALUES ('DN611904M:D3', 'RNA PolyA', NULL);
INSERT INTO public.library VALUES ('DTOL_RD13796827', 'PacBio - HiFi', NULL);
INSERT INTO public.library VALUES ('DTOL_RD13796826', 'PacBio - HiFi', NULL);
INSERT INTO public.library VALUES ('DN886472H-A1', NULL, NULL);
INSERT INTO public.library VALUES ('DN897878L-A1', NULL, NULL);
INSERT INTO public.library VALUES ('DTOL_RD14472939', 'PacBio - HiFi (ULI)', NULL);
INSERT INTO public.library VALUES ('DTOL_RD14472941', 'PacBio - HiFi (ULI)', NULL);
INSERT INTO public.library VALUES ('DTOL_RD14472943', 'PacBio - HiFi (ULI)', NULL);
INSERT INTO public.library VALUES ('DTOL_RD14472945', 'PacBio - HiFi (ULI)', NULL);
INSERT INTO public.library VALUES ('DTOL_RD14472940', 'PacBio - HiFi (ULI)', NULL);
INSERT INTO public.library VALUES ('DTOL_RD14472942', 'PacBio - HiFi (ULI)', NULL);
INSERT INTO public.library VALUES ('DTOL_RD14472944', 'PacBio - HiFi (ULI)', NULL);
INSERT INTO public.library VALUES ('DTOL_RD14472946', 'PacBio - HiFi (ULI)', NULL);
INSERT INTO public.library VALUES ('DTOL_RD13897813', 'PacBio - HiFi', NULL);
INSERT INTO public.library VALUES ('DTOL_RD13897814', 'PacBio - HiFi', NULL);
INSERT INTO public.library VALUES ('DTOL_RD13897815', 'PacBio - HiFi', NULL);
INSERT INTO public.library VALUES ('DTOL_RD14006912', 'PacBio - HiFi', NULL);
INSERT INTO public.library VALUES ('DN878737Q-H1', NULL, NULL);
INSERT INTO public.library VALUES ('DN887103M-A3', NULL, NULL);
INSERT INTO public.library VALUES ('DN887104N-A3', NULL, NULL);
INSERT INTO public.library VALUES ('DN902173S-A1', NULL, NULL);
INSERT INTO public.library VALUES ('DN921237A-A1', NULL, NULL);
INSERT INTO public.library VALUES ('DN904278L-A1', NULL, NULL);
INSERT INTO public.library VALUES ('DN923824V-A1', NULL, NULL);
INSERT INTO public.library VALUES ('DN906267Q-A1', NULL, NULL);
INSERT INTO public.library VALUES ('DN922353H-G1', NULL, NULL);
INSERT INTO public.library VALUES ('DN771163M:G8', 'Chromium genome', NULL);
INSERT INTO public.library VALUES ('DN826505P:B3', 'Hi-C - Arima v2', NULL);
INSERT INTO public.library VALUES ('DN765124Q-B1', NULL, NULL);
INSERT INTO public.library VALUES ('DN612239G:G9', 'RNA PolyA', NULL);


--
-- Data for Name: platform; Type: TABLE DATA; Schema: public; Owner: sts-dev
--

INSERT INTO public.platform VALUES (1, 'Illumina', 'HiSeq');
INSERT INTO public.platform VALUES (2, 'Illumina', 'HiSeqX');
INSERT INTO public.platform VALUES (4, 'Illumina', 'HiSeq 4000');
INSERT INTO public.platform VALUES (5, 'Illumina', 'NovaSeq');
INSERT INTO public.platform VALUES (6, 'PacBio', 'Revio');
INSERT INTO public.platform VALUES (7, 'Illumina', 'MiSeq');
INSERT INTO public.platform VALUES (3, 'PacBio', 'Sequel IIe');


--
-- Data for Name: qc_dict; Type: TABLE DATA; Schema: public; Owner: sts-dev
--

INSERT INTO public.qc_dict VALUES ('pass');
INSERT INTO public.qc_dict VALUES ('fail');


--
-- Data for Name: run; Type: TABLE DATA; Schema: public; Owner: sts-dev
--

INSERT INTO public.run VALUES ('34714', NULL, NULL, 5, 2, NULL, NULL, 'NV15', NULL, '2020-07-29 09:07:48+01');
INSERT INTO public.run VALUES ('34781', NULL, NULL, 5, 2, NULL, NULL, 'NV1', NULL, '2020-08-06 10:02:32+01');
INSERT INTO public.run VALUES ('37940', NULL, NULL, 5, 2, NULL, NULL, 'NV23', NULL, '2021-05-14 13:09:52+01');
INSERT INTO public.run VALUES ('41302', NULL, NULL, 5, 2, NULL, NULL, 'NV4', NULL, '2021-10-05 09:50:42+01');
INSERT INTO public.run VALUES ('41305', NULL, NULL, 5, 2, NULL, NULL, 'NV2', NULL, '2021-10-05 09:52:18+01');
INSERT INTO public.run VALUES ('41306', NULL, NULL, 5, 2, NULL, NULL, 'NV2', NULL, '2021-10-05 10:07:29+01');
INSERT INTO public.run VALUES ('43500', NULL, NULL, 5, 2, NULL, NULL, 'NV5', NULL, '2022-02-05 04:39:07+00');
INSERT INTO public.run VALUES ('45763', NULL, NULL, 5, 2, NULL, NULL, 'NV16', NULL, '2022-09-04 05:32:18+01');
INSERT INTO public.run VALUES ('46644', NULL, NULL, 5, 2, NULL, NULL, 'NV4', NULL, '2023-01-21 09:35:52+00');
INSERT INTO public.run VALUES ('m64228e_210913_122131', NULL, NULL, 3, 2, '86455', 'D1', 'm64228e', '2021-09-09 14:50:07+01', '2021-09-14 21:50:17+01');
INSERT INTO public.run VALUES ('m64228e_210912_060838', NULL, NULL, 3, 2, '86455', 'C1', 'm64228e', '2021-09-09 14:50:07+01', '2021-09-14 21:50:17+01');
INSERT INTO public.run VALUES ('m64178e_211105_051438', NULL, NULL, 3, 2, '87671', 'B1', 'm64178e', '2021-11-03 18:08:11+00', '2021-11-09 05:30:36+00');
INSERT INTO public.run VALUES ('m64094e_211106_093042', NULL, NULL, 3, 2, '87654', 'C1', 'm64094e', '2021-11-03 15:24:50+00', '2021-11-09 00:51:09+00');
INSERT INTO public.run VALUES ('m64228e_211105_115646', NULL, NULL, 3, 2, '87727', 'A1', 'm64228e', '2021-11-05 11:46:31+00', '2021-11-11 08:12:23+00');
INSERT INTO public.run VALUES ('m64228e_211106_225141', NULL, NULL, 3, 2, '87727', 'B1', 'm64228e', '2021-11-05 11:46:31+00', '2021-11-11 08:12:23+00');
INSERT INTO public.run VALUES ('m64228e_211108_094826', NULL, NULL, 3, 2, '87727', 'C1', 'm64228e', '2021-11-05 11:46:31+00', '2021-11-11 08:12:23+00');
INSERT INTO public.run VALUES ('m64178e_211115_123002', NULL, NULL, 3, 2, '87938', 'C1', 'm64178e', '2021-11-12 18:24:50+00', '2021-11-18 06:57:31+00');
INSERT INTO public.run VALUES ('m64178e_211116_212829', NULL, NULL, 3, 2, '87938', 'D1', 'm64178e', '2021-11-12 18:24:50+00', '2021-11-18 06:57:31+00');
INSERT INTO public.run VALUES ('m64230e_220423_112659', NULL, NULL, 3, 2, 'TRACTION-RUN-97', 'C1', 'm64230e', '2022-04-20 15:12:41+01', '2022-04-26 08:03:32+01');
INSERT INTO public.run VALUES ('m64230e_220424_203712', NULL, NULL, 3, 2, 'TRACTION-RUN-97', 'D1', 'm64230e', '2022-04-20 15:12:41+01', '2022-04-26 08:03:32+01');
INSERT INTO public.run VALUES ('m64089e_220922_160600', NULL, NULL, 3, 2, 'TRACTION-RUN-263', 'A1', 'm64089e', '2022-09-22 15:55:49+01', '2022-09-27 12:23:23+01');
INSERT INTO public.run VALUES ('m64089e_220923_210112', NULL, NULL, 3, 2, 'TRACTION-RUN-263', 'B1', 'm64089e', '2022-09-22 15:55:49+01', '2022-09-27 12:23:23+01');
INSERT INTO public.run VALUES ('m64089e_220925_015808', NULL, NULL, 3, 2, 'TRACTION-RUN-263', 'C1', 'm64089e', '2022-09-22 15:55:49+01', '2022-09-27 12:23:23+01');
INSERT INTO public.run VALUES ('m64089e_220926_065548', NULL, NULL, 3, 2, 'TRACTION-RUN-263', 'D1', 'm64089e', '2022-09-22 15:55:49+01', '2022-09-27 12:23:23+01');
INSERT INTO public.run VALUES ('m84047_230425_130728_s4', NULL, NULL, 6, 2, 'TRACTION-RUN-562', 'D1', 'm84047', '2023-04-25 11:27:49+01', '2023-04-26 18:01:11+01');
INSERT INTO public.run VALUES ('m84047_230505_155651_s1', NULL, NULL, 6, 2, 'TRACTION-RUN-580', 'A1', 'm84047', '2023-05-05 14:54:13+01', '2023-05-06 22:32:37+01');
INSERT INTO public.run VALUES ('m84047_230517_174928_s2', NULL, NULL, 6, 2, 'TRACTION-RUN-581', 'B1', 'm84047', '2023-05-17 17:12:07+01', '2023-05-18 22:33:49+01');
INSERT INTO public.run VALUES ('35874', NULL, NULL, 2, 2, NULL, NULL, 'HX4', NULL, '2020-12-13 08:31:21+00');
INSERT INTO public.run VALUES ('35990', NULL, NULL, 5, 2, NULL, NULL, 'NV20', NULL, '2020-12-19 07:28:32+00');
INSERT INTO public.run VALUES ('40280', NULL, NULL, 5, 2, NULL, NULL, 'NV15', NULL, '2021-08-18 12:37:35+01');
INSERT INTO public.run VALUES ('37363', NULL, NULL, 5, 2, NULL, NULL, 'NV20', NULL, '2021-04-15 03:01:29+01');
INSERT INTO public.run VALUES ('m64230e_210705_101703', NULL, NULL, 3, 2, '84025', 'C1', 'm64230e', '2021-07-02 17:39:50+01', '2021-07-08 03:55:57+01');
INSERT INTO public.run VALUES ('m64097e_210617_142108', NULL, NULL, 3, 2, '83439', 'A1', 'm64097e', '2021-06-17 14:08:08+01', '2021-06-22 20:13:15+01');
INSERT INTO public.run VALUES ('m64094e_210430_115816', NULL, NULL, 3, 2, '81880', 'A1', 'm64094e', '2021-04-30 11:47:59+01', '2021-05-05 18:37:54+01');
INSERT INTO public.run VALUES ('m64097e_210621_084307', NULL, NULL, 3, 2, '83439', 'D1', 'm64097e', '2021-06-17 14:08:08+01', '2021-06-22 20:13:15+01');
INSERT INTO public.run VALUES ('m64097e_210425_025051', NULL, NULL, 3, 2, '81618', 'C1', 'm64097e', '2021-04-22 14:07:27+01', '2021-04-27 21:11:12+01');
INSERT INTO public.run VALUES ('m64097e_210508_212855', NULL, NULL, 3, 2, '82085', 'B1', 'm64097e', '2021-05-07 15:18:05+01', '2021-05-12 21:22:29+01');
INSERT INTO public.run VALUES ('m64174e_210501_195526', NULL, NULL, 3, 2, '81885', 'B1', 'm64174e', '2021-04-30 13:35:53+01', '2021-05-05 20:27:22+01');
INSERT INTO public.run VALUES ('m64174e_210503_021816', NULL, NULL, 3, 2, '81885', 'C1', 'm64174e', '2021-04-30 13:35:53+01', '2021-05-05 20:27:22+01');
INSERT INTO public.run VALUES ('m64174e_210504_084057', NULL, NULL, 3, 2, '81885', 'D1', 'm64174e', '2021-04-30 13:35:53+01', '2021-05-05 20:27:22+01');
INSERT INTO public.run VALUES ('m64094e_210501_180717', NULL, NULL, 3, 2, '81880', 'B1', 'm64094e', '2021-04-30 11:47:59+01', '2021-05-05 18:37:54+01');
INSERT INTO public.run VALUES ('m64094e_210503_002936', NULL, NULL, 3, 2, '81880', 'C1', 'm64094e', '2021-04-30 11:47:59+01', '2021-05-05 18:37:54+01');
INSERT INTO public.run VALUES ('m64094e_210504_065204', NULL, NULL, 3, 2, '81880', 'D1', 'm64094e', '2021-04-30 11:47:59+01', '2021-05-05 18:37:54+01');
INSERT INTO public.run VALUES ('m64221e_230913_152616', NULL, NULL, 3, 2, 'TRACTION-RUN-822', 'A1', 'm64221e', '2023-09-13 15:16:10+01', '2023-09-18 08:39:23+01');
INSERT INTO public.run VALUES ('m64230e_220219_230553', NULL, NULL, 3, 2, '90455', 'B1', 'm64230e', '2022-02-18 13:59:06+00', '2022-02-23 23:16:05+00');
INSERT INTO public.run VALUES ('45733', NULL, NULL, 5, 2, NULL, NULL, 'NV10', NULL, '2022-09-01 05:08:47+01');
INSERT INTO public.run VALUES ('44268', NULL, NULL, 4, 2, NULL, NULL, 'HF2', NULL, '2022-03-21 23:39:51+00');
INSERT INTO public.run VALUES ('37939', NULL, NULL, 5, 2, NULL, NULL, 'NV22', NULL, '2021-05-14 11:44:28+01');
INSERT INTO public.run VALUES ('35281', NULL, NULL, 2, 2, NULL, NULL, 'HX8', NULL, '2020-10-25 10:01:21+00');
INSERT INTO public.run VALUES ('m64174e_210130_144539', NULL, NULL, 3, 2, '79394', 'C1', 'm64174e', '2021-01-28 14:05:50+00', '2021-02-01 14:26:21+00');
INSERT INTO public.run VALUES ('m64228e_210909_150013', NULL, NULL, 3, 2, '86455', 'A1', 'm64228e', '2021-09-09 14:50:07+01', '2021-09-14 21:50:17+01');
INSERT INTO public.run VALUES ('m64228e_210910_210956', NULL, NULL, 3, 2, '86455', 'B1', 'm64228e', '2021-09-09 14:50:07+01', '2021-09-14 21:50:17+01');
INSERT INTO public.run VALUES ('m64094e_211025_104111', NULL, NULL, 3, 2, '87437', 'C1', 'm64094e', '2021-10-22 15:48:21+01', '2021-10-28 07:36:27+01');
INSERT INTO public.run VALUES ('m64174e_211103_153104', NULL, NULL, 3, 2, '87660', 'A1', 'm64174e', '2021-11-03 15:20:49+00', '2021-11-09 04:03:28+00');
INSERT INTO public.run VALUES ('m64178e_211112_183448', NULL, NULL, 3, 2, '87938', 'A1', 'm64178e', '2021-11-12 18:24:50+00', '2021-11-18 06:57:31+00');
INSERT INTO public.run VALUES ('m64178e_211114_033110', NULL, NULL, 3, 2, '87938', 'B1', 'm64178e', '2021-11-12 18:24:50+00', '2021-11-18 06:57:31+00');
INSERT INTO public.run VALUES ('m64221e_211117_160848', NULL, NULL, 3, 2, '88033', 'A1', 'm64221e', '2021-11-17 15:58:45+00', '2021-11-23 10:25:49+00');
INSERT INTO public.run VALUES ('m64174e_220128_000029', NULL, NULL, 3, 2, '89795', 'B1', 'm64174e', '2022-01-26 14:53:37+00', '2022-01-31 23:41:36+00');
INSERT INTO public.run VALUES ('m64228e_220423_113317', NULL, NULL, 3, 2, 'TRACTION-RUN-96', 'C1', 'm64228e', '2022-04-20 15:12:27+01', '2022-04-26 08:17:44+01');
INSERT INTO public.run VALUES ('m64228e_220424_205021', NULL, NULL, 3, 2, 'TRACTION-RUN-96', 'D1', 'm64228e', '2022-04-20 15:12:27+01', '2022-04-26 08:17:44+01');
INSERT INTO public.run VALUES ('m64094e_220811_122820', NULL, NULL, 3, 2, 'TRACTION-RUN-200', 'A1', 'm64094e', '2022-08-11 12:18:15+01', '2022-08-16 04:54:07+01');
INSERT INTO public.run VALUES ('m64094e_220812_172220', NULL, NULL, 3, 2, 'TRACTION-RUN-200', 'B1', 'm64094e', '2022-08-11 12:18:15+01', '2022-08-16 04:54:07+01');
INSERT INTO public.run VALUES ('m64094e_220813_205234', NULL, NULL, 3, 2, 'TRACTION-RUN-200', 'C1', 'm64094e', '2022-08-11 12:18:15+01', '2022-08-16 04:54:07+01');
INSERT INTO public.run VALUES ('m64094e_220815_002611', NULL, NULL, 3, 2, 'TRACTION-RUN-200', 'D1', 'm64094e', '2022-08-11 12:18:15+01', '2022-08-16 04:54:07+01');
INSERT INTO public.run VALUES ('m64174e_221108_072343', NULL, NULL, 3, 2, 'TRACTION-RUN-330', 'D1', 'm64174e', '2022-11-04 16:27:38+00', '2022-11-09 12:49:29+00');
INSERT INTO public.run VALUES ('m84047_230425_113454_s1', NULL, NULL, 6, 2, 'TRACTION-RUN-562', 'A1', 'm84047', '2023-04-25 11:27:49+01', '2023-04-26 18:01:11+01');
INSERT INTO public.run VALUES ('m64016e_230429_173736', NULL, NULL, 3, 2, 'TRACTION-RUN-569', 'B1', 'm64016e', '2023-04-28 14:02:52+01', '2023-05-07 21:31:46+01');
INSERT INTO public.run VALUES ('m84047_230706_152551_s2', NULL, NULL, 6, 2, 'TRACTION-RUN-681', 'D1', 'm84047', '2023-07-06 14:52:57+01', '2023-07-07 20:09:38+01');
INSERT INTO public.run VALUES ('m64125e_210211_151547', NULL, NULL, 3, 2, '79750', 'A1', 'm64125e', '2021-02-11 15:05:45+00', '2021-02-15 21:53:29+00');
INSERT INTO public.run VALUES ('36703', NULL, NULL, 4, 2, NULL, NULL, 'HF1', NULL, '2021-03-08 10:31:06+00');
INSERT INTO public.run VALUES ('m64221e_230816_183713', NULL, NULL, 3, 2, 'TRACTION-RUN-770', 'B1', 'm64221e', '2023-08-15 13:29:45+01', '2023-08-25 01:21:36+01');
INSERT INTO public.run VALUES ('m64221e_230815_134000', NULL, NULL, 3, 2, 'TRACTION-RUN-770', 'A1', 'm64221e', '2023-08-15 13:29:45+01', '2023-08-25 01:21:36+01');
INSERT INTO public.run VALUES ('m64221e_211110_155624', NULL, NULL, 3, 2, '87862', 'A1', 'm64221e', '2021-11-10 15:46:28+00', '2021-11-16 04:22:27+00');
INSERT INTO public.run VALUES ('m64097e_211204_084129', NULL, NULL, 3, 2, '88488', 'C1', 'm64097e', '2021-12-01 16:04:48+00', '2021-12-07 01:27:28+00');
INSERT INTO public.run VALUES ('m84047_231120_144131_s1', NULL, NULL, 6, 2, 'TRACTION-RUN-950', 'A1', 'm84047', '2023-11-20 14:33:34+00', '2023-11-21 19:53:09+00');
INSERT INTO public.run VALUES ('m84047_231120_151150_s2', NULL, NULL, 6, 2, 'TRACTION-RUN-950', 'B1', 'm84047', '2023-11-20 14:33:34+00', '2023-11-21 19:53:09+00');
INSERT INTO public.run VALUES ('m64228e_231127_153346', NULL, NULL, 3, 2, 'TRACTION-RUN-972', 'A1', 'm64228e', '2023-11-27 15:23:29+00', '2023-12-06 23:29:26+00');
INSERT INTO public.run VALUES ('m64228e_231128_184021', NULL, NULL, 3, 2, 'TRACTION-RUN-972', 'B1', 'm64228e', '2023-11-27 15:23:29+00', '2023-12-06 23:29:26+00');
INSERT INTO public.run VALUES ('m64089e_231202_200225', NULL, NULL, 3, 2, 'TRACTION-RUN-978', 'C1', 'm64089e', '2023-11-30 12:45:27+00', '2023-12-05 04:52:54+00');
INSERT INTO public.run VALUES ('m64089e_231221_145323', NULL, NULL, 3, 2, 'TRACTION-RUN-1019', 'A1', 'm64089e', '2023-12-21 14:43:26+00', '2023-12-26 03:40:39+00');
INSERT INTO public.run VALUES ('m64221e_211029_115402', NULL, NULL, 3, 2, '87570', 'A1', 'm64221e', '2021-10-29 11:43:59+01', '2021-10-29 14:51:42+01');
INSERT INTO public.run VALUES ('m64125e_211103_175849', NULL, NULL, 3, 2, '87670', 'A1', 'm64125e', '2021-11-03 17:48:50+00', '2021-11-09 02:52:57+00');
INSERT INTO public.run VALUES ('m64089e_211106_112750', NULL, NULL, 3, 2, '87653', 'C1', 'm64089e', '2021-11-03 15:24:47+00', '2021-11-09 04:33:35+00');
INSERT INTO public.run VALUES ('m64229e_211215_184451', NULL, NULL, 3, 2, '88929', 'A1', 'm64229e', '2021-12-15 18:32:27+00', '2021-12-21 05:40:56+00');
INSERT INTO public.run VALUES ('m64230e_220221_063339', NULL, NULL, 3, 2, '90455', 'C1', 'm64230e', '2022-02-18 13:59:06+00', '2022-02-23 23:16:05+00');
INSERT INTO public.run VALUES ('m64221e_211216_143308', NULL, NULL, 3, 2, '88934', 'A1', 'm64221e', '2021-12-16 14:22:58+00', '2021-12-21 00:29:04+00');
INSERT INTO public.run VALUES ('m64094e_220306_084547', NULL, NULL, 3, 2, '90770', 'C1', 'm64094e', '2022-03-03 16:23:37+00', '2022-03-09 02:29:01+00');
INSERT INTO public.run VALUES ('m64178e_220109_104526', NULL, NULL, 3, 2, '89276', 'C1', 'm64178e', '2022-01-06 18:24:04+00', '2022-01-12 05:18:53+00');
INSERT INTO public.run VALUES ('m64016e_220309_153701', NULL, NULL, 3, 2, '90903', 'A1', 'm64016e', '2022-03-09 15:26:53+00', '2022-03-15 00:45:09+00');
INSERT INTO public.run VALUES ('36691', NULL, NULL, 5, 2, NULL, NULL, 'NV20', NULL, '2021-03-06 05:07:44+00');
INSERT INTO public.run VALUES ('40666', NULL, NULL, 5, 2, NULL, NULL, 'NV11', NULL, '2021-09-05 07:44:37+01');
INSERT INTO public.run VALUES ('m64097e_210221_172213', NULL, NULL, 3, 2, '79924', 'D1', 'm64097e', '2021-02-18 16:18:11+00', '2021-02-22 23:07:55+00');
INSERT INTO public.run VALUES ('37935', NULL, NULL, 4, 2, NULL, NULL, 'HF2', NULL, '2021-05-16 21:08:02+01');


--
-- Data for Name: sex; Type: TABLE DATA; Schema: public; Owner: sts-dev
--



--
-- Data for Name: species; Type: TABLE DATA; Schema: public; Owner: sts-dev
--

INSERT INTO public.species VALUES ('Quercus robur', 'Quercus_robur', NULL, 'pedunculate oak', 38942, 'Fagaceae', 'Fagales', 'Streptophyta', 'dicots', 1017120000, 24, NULL, NULL);
INSERT INTO public.species VALUES ('Adalia bipunctata', 'Adalia_bipunctata', NULL, NULL, 7084, 'Coccinellidae', 'Coleoptera', 'Arthropoda', 'insects', 352080000, 20, NULL, NULL);
INSERT INTO public.species VALUES ('Juncus effusus', 'Juncus_effusus', NULL, 'common rush', 13579, 'Juncaceae', 'Poales', 'Streptophyta', 'monocots', 293400000, 46, NULL, NULL);


--
-- Data for Name: specimen; Type: TABLE DATA; Schema: public; Owner: sts-dev
--

INSERT INTO public.specimen VALUES ('dhQueRobu1', NULL, NULL, 'Quercus robur', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('dhQueRobu2', NULL, NULL, 'Quercus robur', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('dhQueRobu3', NULL, NULL, 'Quercus robur', NULL, NULL, 'SAMEA9089039', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('dhQueRobu87', NULL, NULL, 'Quercus robur', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('dhQueRobu5', NULL, NULL, 'Quercus robur', NULL, NULL, 'SAMEA9335274', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('dhQueRobu89', NULL, NULL, 'Quercus robur', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('dhQueRobu90', NULL, NULL, 'Quercus robur', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('dhQueRobu20', NULL, NULL, 'Quercus robur', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('dhQueRobu21', NULL, NULL, 'Quercus robur', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('dhQueRobu22', NULL, NULL, 'Quercus robur', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('dhQueRobu23', NULL, NULL, 'Quercus robur', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('dhQueRobu24', NULL, NULL, 'Quercus robur', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('dhQueRobu25', NULL, NULL, 'Quercus robur', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('dhQueRobu26', NULL, NULL, 'Quercus robur', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('dhQueRobu27', NULL, NULL, 'Quercus robur', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('dhQueRobu28', NULL, NULL, 'Quercus robur', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('dhQueRobu29', NULL, NULL, 'Quercus robur', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('dhQueRobu30', NULL, NULL, 'Quercus robur', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('dhQueRobu31', NULL, NULL, 'Quercus robur', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('dhQueRobu32', NULL, NULL, 'Quercus robur', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('dhQueRobu33', NULL, NULL, 'Quercus robur', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('dhQueRobu34', NULL, NULL, 'Quercus robur', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('dhQueRobu35', NULL, NULL, 'Quercus robur', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('dhQueRobu36', NULL, NULL, 'Quercus robur', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('dhQueRobu37', NULL, NULL, 'Quercus robur', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('dhQueRobu38', NULL, NULL, 'Quercus robur', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('dhQueRobu39', NULL, NULL, 'Quercus robur', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('dhQueRobu40', NULL, NULL, 'Quercus robur', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('dhQueRobu41', NULL, NULL, 'Quercus robur', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('dhQueRobu42', NULL, NULL, 'Quercus robur', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('dhQueRobu43', NULL, NULL, 'Quercus robur', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('dhQueRobu44', NULL, NULL, 'Quercus robur', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('dhQueRobu45', NULL, NULL, 'Quercus robur', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('dhQueRobu46', NULL, NULL, 'Quercus robur', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('dhQueRobu47', NULL, NULL, 'Quercus robur', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('dhQueRobu48', NULL, NULL, 'Quercus robur', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('dhQueRobu49', NULL, NULL, 'Quercus robur', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('dhQueRobu50', NULL, NULL, 'Quercus robur', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('dhQueRobu51', NULL, NULL, 'Quercus robur', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('dhQueRobu52', NULL, NULL, 'Quercus robur', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('dhQueRobu53', NULL, NULL, 'Quercus robur', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('dhQueRobu54', NULL, NULL, 'Quercus robur', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('dhQueRobu55', NULL, NULL, 'Quercus robur', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('dhQueRobu56', NULL, NULL, 'Quercus robur', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('dhQueRobu57', NULL, NULL, 'Quercus robur', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('dhQueRobu58', NULL, NULL, 'Quercus robur', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('dhQueRobu59', NULL, NULL, 'Quercus robur', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('dhQueRobu61', NULL, NULL, 'Quercus robur', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('dhQueRobu62', NULL, NULL, 'Quercus robur', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('dhQueRobu63', NULL, NULL, 'Quercus robur', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('dhQueRobu65', NULL, NULL, 'Quercus robur', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('dhQueRobu67', NULL, NULL, 'Quercus robur', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('dhQueRobu68', NULL, NULL, 'Quercus robur', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('dhQueRobu69', NULL, NULL, 'Quercus robur', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('dhQueRobu70', NULL, NULL, 'Quercus robur', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('dhQueRobu71', NULL, NULL, 'Quercus robur', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('dhQueRobu72', NULL, NULL, 'Quercus robur', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('dhQueRobu73', NULL, NULL, 'Quercus robur', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('dhQueRobu74', NULL, NULL, 'Quercus robur', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('dhQueRobu75', NULL, NULL, 'Quercus robur', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('dhQueRobu76', NULL, NULL, 'Quercus robur', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('dhQueRobu77', NULL, NULL, 'Quercus robur', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('dhQueRobu80', NULL, NULL, 'Quercus robur', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('dhQueRobu81', NULL, NULL, 'Quercus robur', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('dhQueRobu84', NULL, NULL, 'Quercus robur', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('dhQueRobu85', NULL, NULL, 'Quercus robur', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('dhQueRobu91', NULL, NULL, 'Quercus robur', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('dhQueRobu60', NULL, NULL, 'Quercus robur', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('dhQueRobu64', NULL, NULL, 'Quercus robur', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('dhQueRobu66', NULL, NULL, 'Quercus robur', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('dhQueRobu78', NULL, NULL, 'Quercus robur', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('dhQueRobu79', NULL, NULL, 'Quercus robur', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('dhQueRobu82', NULL, NULL, 'Quercus robur', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('dhQueRobu86', NULL, NULL, 'Quercus robur', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('dhQueRobu88', NULL, NULL, 'Quercus robur', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('icAdaBipu1', NULL, NULL, 'Adalia bipunctata', NULL, NULL, 'SAMEA9089055', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('icAdaBipu8', NULL, NULL, 'Adalia bipunctata', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('icAdaBipu11', NULL, NULL, 'Adalia bipunctata', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('icAdaBipu125', NULL, NULL, 'Adalia bipunctata', NULL, NULL, 'SAMEA13831067', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('icAdaBipu146', NULL, NULL, 'Adalia bipunctata', NULL, NULL, 'SAMEA13831088', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('icAdaBipu115', NULL, NULL, 'Adalia bipunctata', NULL, NULL, 'SAMEA13831057', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('icAdaBipu148', NULL, NULL, 'Adalia bipunctata', NULL, NULL, 'SAMEA13831090', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('icAdaBipu138', NULL, NULL, 'Adalia bipunctata', NULL, NULL, 'SAMEA13831080', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('icAdaBipu118', NULL, NULL, 'Adalia bipunctata', NULL, NULL, 'SAMEA13831060', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('icAdaBipu151', NULL, NULL, 'Adalia bipunctata', NULL, NULL, 'SAMEA13831093', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('icAdaBipu133', NULL, NULL, 'Adalia bipunctata', NULL, NULL, 'SAMEA13831075', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('icAdaBipu104', NULL, NULL, 'Adalia bipunctata', NULL, NULL, 'SAMEA13831046', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('icAdaBipu117', NULL, NULL, 'Adalia bipunctata', NULL, NULL, 'SAMEA13831059', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('icAdaBipu140', NULL, NULL, 'Adalia bipunctata', NULL, NULL, 'SAMEA13831082', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('icAdaBipu3', NULL, NULL, 'Adalia bipunctata', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('icAdaBipu9', NULL, NULL, 'Adalia bipunctata', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('icAdaBipu22', NULL, NULL, 'Adalia bipunctata', NULL, NULL, 'SAMEA10270683', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('icAdaBipu15', NULL, NULL, 'Adalia bipunctata', NULL, NULL, 'SAMEA10270673', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('icAdaBipu29', NULL, NULL, 'Adalia bipunctata', NULL, NULL, 'SAMEA10270690', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('icAdaBipu36', NULL, NULL, 'Adalia bipunctata', NULL, NULL, 'SAMEA10270692', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('icAdaBipu64', NULL, NULL, 'Adalia bipunctata', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('icAdaBipu69', NULL, NULL, 'Adalia bipunctata', NULL, NULL, 'SAMEA10270740', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('icAdaBipu62', NULL, NULL, 'Adalia bipunctata', NULL, NULL, 'SAMEA10270730', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('icAdaBipu143', NULL, NULL, 'Adalia bipunctata', NULL, NULL, 'SAMEA13831085', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('icAdaBipu108', NULL, NULL, 'Adalia bipunctata', NULL, NULL, 'SAMEA13831050', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('icAdaBipu145', NULL, NULL, 'Adalia bipunctata', NULL, NULL, 'SAMEA13831087', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('icAdaBipu6', NULL, NULL, 'Adalia bipunctata', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('icAdaBipu88', NULL, NULL, 'Adalia bipunctata', NULL, NULL, 'SAMEA9067607', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('icAdaBipu2', NULL, NULL, 'Adalia bipunctata', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('icAdaBipu218', NULL, NULL, 'Adalia bipunctata', NULL, NULL, 'SAMEA112816472', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('icAdaBipu230', NULL, NULL, 'Adalia bipunctata', NULL, NULL, 'SAMEA112816484', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('icAdaBipu28', NULL, NULL, 'Adalia bipunctata', NULL, NULL, 'SAMEA10270689', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('icAdaBipu31', NULL, NULL, 'Adalia bipunctata', NULL, NULL, 'SAMEA10270692', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('icAdaBipu274', NULL, NULL, 'Adalia bipunctata', NULL, NULL, 'SAMEA112816588', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('icAdaBipu217', NULL, NULL, 'Adalia bipunctata', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('icAdaBipu315', NULL, NULL, 'Adalia bipunctata', NULL, NULL, 'SAMEA112816669', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.specimen VALUES ('icAdaBipu20', NULL, NULL, 'Adalia bipunctata', NULL, NULL, 'SAMEA10270682', NULL, NULL, NULL, '2024-01-16 14:44:31.407348+00', '7');
INSERT INTO public.specimen VALUES ('icAdaBipu32', NULL, NULL, 'Adalia bipunctata', NULL, NULL, 'SAMEA10270697', NULL, NULL, NULL, '2024-01-16 14:44:31.407348+00', '7');
INSERT INTO public.specimen VALUES ('icAdaBipu33', NULL, NULL, 'Adalia bipunctata', NULL, NULL, 'SAMEA10270697', NULL, NULL, NULL, '2024-01-16 14:44:31.407348+00', '7');
INSERT INTO public.specimen VALUES ('icAdaBipu34', NULL, NULL, 'Adalia bipunctata', NULL, NULL, 'SAMEA10270697', NULL, NULL, NULL, '2024-01-16 14:44:31.407348+00', '7');
INSERT INTO public.specimen VALUES ('lpJunEffu1', NULL, NULL, 'Juncus effusus', NULL, NULL, 'SAMEA7521930', NULL, NULL, NULL, NULL, NULL);


--
-- Data for Name: sample; Type: TABLE DATA; Schema: public; Owner: sts-dev
--

INSERT INTO public.sample VALUES ('DTOL_RD9128913', NULL, NULL, 'dhQueRobu1', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD9128914', NULL, NULL, 'dhQueRobu1', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD9128915', NULL, NULL, 'dhQueRobu1', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD9128916', NULL, NULL, 'dhQueRobu1', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD9128917', NULL, NULL, 'dhQueRobu1', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD9128918', NULL, NULL, 'dhQueRobu1', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD9128919', NULL, NULL, 'dhQueRobu1', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD9128920', NULL, NULL, 'dhQueRobu1', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD9128921', NULL, NULL, 'dhQueRobu1', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD9128922', NULL, NULL, 'dhQueRobu1', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD9128923', NULL, NULL, 'dhQueRobu1', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD9128924', NULL, NULL, 'dhQueRobu1', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD9129045', NULL, NULL, 'dhQueRobu2', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD9129046', NULL, NULL, 'dhQueRobu2', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD9129047', NULL, NULL, 'dhQueRobu2', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD9129048', NULL, NULL, 'dhQueRobu2', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD9129049', NULL, NULL, 'dhQueRobu2', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD9129050', NULL, NULL, 'dhQueRobu2', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD9129051', NULL, NULL, 'dhQueRobu2', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD9129052', NULL, NULL, 'dhQueRobu2', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD9129053', NULL, NULL, 'dhQueRobu2', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD9129054', NULL, NULL, 'dhQueRobu2', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD9129055', NULL, NULL, 'dhQueRobu2', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD9129056', NULL, NULL, 'dhQueRobu2', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD10244239', NULL, NULL, 'dhQueRobu3', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD11009762', NULL, NULL, 'dhQueRobu3', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD11534048', NULL, NULL, 'dhQueRobu3', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD12811540', NULL, NULL, 'dhQueRobu3', 'SAMEA13840482', NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD12811546', NULL, NULL, 'dhQueRobu3', 'SAMEA13840472', NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD12811550', NULL, NULL, 'dhQueRobu3', 'SAMEA13840460', NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD13133243', NULL, NULL, 'dhQueRobu3', 'SAMEA13840478', NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD13133245', NULL, NULL, 'dhQueRobu3', 'SAMEA13840478', NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD10880862', NULL, NULL, 'dhQueRobu3', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD11235048', NULL, NULL, 'dhQueRobu3', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD10880865', NULL, NULL, 'dhQueRobu3', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD10880866', NULL, NULL, 'dhQueRobu3', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD10880867', NULL, NULL, 'dhQueRobu3', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD11239438', NULL, NULL, 'dhQueRobu3', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD12710417', NULL, NULL, 'dhQueRobu3', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD13129891', NULL, NULL, 'dhQueRobu3', 'SAMEA13840478', NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD13680853', NULL, NULL, 'dhQueRobu3', 'SAMEA13840462', NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL9475841', NULL, NULL, 'dhQueRobu3', 'SAMEA12362595', NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL9384858', NULL, NULL, 'dhQueRobu3', 'SAMEA12362597', NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL9475842', NULL, NULL, 'dhQueRobu3', 'SAMEA12362596', NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL10597087', NULL, NULL, 'dhQueRobu3', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('OakPopGen9912158', NULL, NULL, 'dhQueRobu3', 'SAMEA9089040', NULL, NULL);
INSERT INTO public.sample VALUES ('OakPopGen9912159', NULL, NULL, 'dhQueRobu3', 'SAMEA9089041', NULL, NULL);
INSERT INTO public.sample VALUES ('OakPopGen9912160', NULL, NULL, 'dhQueRobu3', 'SAMEA9089042', NULL, NULL);
INSERT INTO public.sample VALUES ('OakPopGen9912161', NULL, NULL, 'dhQueRobu3', 'SAMEA9089044', NULL, NULL);
INSERT INTO public.sample VALUES ('OakPopGen9912162', NULL, NULL, 'dhQueRobu3', 'SAMEA9089043', NULL, NULL);
INSERT INTO public.sample VALUES ('OakPopGen9912163', NULL, NULL, 'dhQueRobu3', 'SAMEA9089045', NULL, NULL);
INSERT INTO public.sample VALUES ('OakPopGen9912164', NULL, NULL, 'dhQueRobu3', 'SAMEA9089046', NULL, NULL);
INSERT INTO public.sample VALUES ('OakPopGen9912165', NULL, NULL, 'dhQueRobu3', 'SAMEA9089047', NULL, NULL);
INSERT INTO public.sample VALUES ('OakPopGen9912166', NULL, NULL, 'dhQueRobu3', 'SAMEA9089048', NULL, NULL);
INSERT INTO public.sample VALUES ('OakPopGen9912167', NULL, NULL, 'dhQueRobu3', 'SAMEA9089049', NULL, NULL);
INSERT INTO public.sample VALUES ('OakPopGen9912168', NULL, NULL, 'dhQueRobu3', 'SAMEA9089050', NULL, NULL);
INSERT INTO public.sample VALUES ('OakPopGen9912169', NULL, NULL, 'dhQueRobu3', 'SAMEA9089051', NULL, NULL);
INSERT INTO public.sample VALUES ('OakPopGen9912170', NULL, NULL, 'dhQueRobu3', 'SAMEA9089052', NULL, NULL);
INSERT INTO public.sample VALUES ('OakPopGen9912171', NULL, NULL, 'dhQueRobu3', 'SAMEA9089053', NULL, NULL);
INSERT INTO public.sample VALUES ('OakPopGen9912172', NULL, NULL, 'dhQueRobu3', 'SAMEA9089054', NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL10185088', NULL, NULL, 'dhQueRobu3', 'SAMEA9089054', NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL10185080', NULL, NULL, 'dhQueRobu3', 'SAMEA9089046', NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL10185075', NULL, NULL, 'dhQueRobu3', 'SAMEA9089040', NULL, NULL);
INSERT INTO public.sample VALUES ('OakPopGen10218312', NULL, NULL, 'dhQueRobu3', 'SAMEA9089042', NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL10185077', NULL, NULL, 'dhQueRobu3', 'SAMEA9089044', NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL10185078', NULL, NULL, 'dhQueRobu3', 'SAMEA9089043', NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL10185079', NULL, NULL, 'dhQueRobu3', 'SAMEA9089045', NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL10185081', NULL, NULL, 'dhQueRobu3', 'SAMEA9089047', NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL10185082', NULL, NULL, 'dhQueRobu3', 'SAMEA9089048', NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL10185083', NULL, NULL, 'dhQueRobu3', 'SAMEA9089049', NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL10185076', NULL, NULL, 'dhQueRobu3', 'SAMEA9089041', NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD13796825', NULL, NULL, 'dhQueRobu3', 'SAMEA13840469', NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD12215773', NULL, NULL, 'dhQueRobu3', 'SAMEA9089045', NULL, NULL);
INSERT INTO public.sample VALUES ('OAK_WW1512935160', NULL, NULL, 'dhQueRobu87', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('DTOLRNA11521361', NULL, NULL, 'dhQueRobu5', 'SAMEA9335427', NULL, NULL);
INSERT INTO public.sample VALUES ('OAK_WW1512935162', NULL, NULL, 'dhQueRobu89', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('OAK_WW1512935163', NULL, NULL, 'dhQueRobu90', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('OAK_WW1512935093', NULL, NULL, 'dhQueRobu20', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('OAK_WW1512935094', NULL, NULL, 'dhQueRobu21', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('OAK_WW1512935095', NULL, NULL, 'dhQueRobu22', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('OAK_WW1512935096', NULL, NULL, 'dhQueRobu23', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('OAK_WW1512935097', NULL, NULL, 'dhQueRobu24', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('OAK_WW1512935098', NULL, NULL, 'dhQueRobu25', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('OAK_WW1512935099', NULL, NULL, 'dhQueRobu26', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('OAK_WW1512935100', NULL, NULL, 'dhQueRobu27', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('OAK_WW1512935101', NULL, NULL, 'dhQueRobu28', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('OAK_WW1512935102', NULL, NULL, 'dhQueRobu29', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('OAK_WW1512935103', NULL, NULL, 'dhQueRobu30', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('OAK_WW1512935104', NULL, NULL, 'dhQueRobu31', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('OAK_WW1512935105', NULL, NULL, 'dhQueRobu32', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('OAK_WW1512935106', NULL, NULL, 'dhQueRobu33', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('OAK_WW1512935107', NULL, NULL, 'dhQueRobu34', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('OAK_WW1512935108', NULL, NULL, 'dhQueRobu35', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('OAK_WW1512935109', NULL, NULL, 'dhQueRobu36', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('OAK_WW1512935110', NULL, NULL, 'dhQueRobu37', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('OAK_WW1512935111', NULL, NULL, 'dhQueRobu38', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('OAK_WW1512935112', NULL, NULL, 'dhQueRobu39', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('OAK_WW1512935113', NULL, NULL, 'dhQueRobu40', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('OAK_WW1512935114', NULL, NULL, 'dhQueRobu41', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('OAK_WW1512935115', NULL, NULL, 'dhQueRobu42', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('OAK_WW1512935116', NULL, NULL, 'dhQueRobu43', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('OAK_WW1512935117', NULL, NULL, 'dhQueRobu44', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('OAK_WW1512935118', NULL, NULL, 'dhQueRobu45', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('OAK_WW1512935119', NULL, NULL, 'dhQueRobu46', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('OAK_WW1512935120', NULL, NULL, 'dhQueRobu47', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('OAK_WW1512935121', NULL, NULL, 'dhQueRobu48', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('OAK_WW1512935122', NULL, NULL, 'dhQueRobu49', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('OAK_WW1512935123', NULL, NULL, 'dhQueRobu50', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('OAK_WW1512935124', NULL, NULL, 'dhQueRobu51', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('OAK_WW1512935125', NULL, NULL, 'dhQueRobu52', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('OAK_WW1512935126', NULL, NULL, 'dhQueRobu53', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('OAK_WW1512935127', NULL, NULL, 'dhQueRobu54', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('OAK_WW1512935128', NULL, NULL, 'dhQueRobu55', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('OAK_WW1512935129', NULL, NULL, 'dhQueRobu56', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('OAK_WW1512935130', NULL, NULL, 'dhQueRobu57', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('OAK_WW1512935131', NULL, NULL, 'dhQueRobu58', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('OAK_WW1512935132', NULL, NULL, 'dhQueRobu59', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('OAK_WW1512935134', NULL, NULL, 'dhQueRobu61', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('OAK_WW1512935135', NULL, NULL, 'dhQueRobu62', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('OAK_WW1512935136', NULL, NULL, 'dhQueRobu63', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('OAK_WW1512935138', NULL, NULL, 'dhQueRobu65', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('OAK_WW1512935140', NULL, NULL, 'dhQueRobu67', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('OAK_WW1512935141', NULL, NULL, 'dhQueRobu68', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('OAK_WW1512935142', NULL, NULL, 'dhQueRobu69', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('OAK_WW1512935143', NULL, NULL, 'dhQueRobu70', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('OAK_WW1512935144', NULL, NULL, 'dhQueRobu71', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('OAK_WW1512935145', NULL, NULL, 'dhQueRobu72', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('OAK_WW1512935146', NULL, NULL, 'dhQueRobu73', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('OAK_WW1512935147', NULL, NULL, 'dhQueRobu74', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('OAK_WW1512935148', NULL, NULL, 'dhQueRobu75', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('OAK_WW1512935149', NULL, NULL, 'dhQueRobu76', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('OAK_WW1512935150', NULL, NULL, 'dhQueRobu77', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('OAK_WW1512935153', NULL, NULL, 'dhQueRobu80', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('OAK_WW1512935154', NULL, NULL, 'dhQueRobu81', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('OAK_WW1512935157', NULL, NULL, 'dhQueRobu84', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('OAK_WW1512935158', NULL, NULL, 'dhQueRobu85', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('OAK_WW1512935164', NULL, NULL, 'dhQueRobu91', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('OAK_WW1512935133', NULL, NULL, 'dhQueRobu60', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('OAK_WW1512935137', NULL, NULL, 'dhQueRobu64', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('OAK_WW1512935139', NULL, NULL, 'dhQueRobu66', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('OAK_WW1512935151', NULL, NULL, 'dhQueRobu78', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('OAK_WW1512935152', NULL, NULL, 'dhQueRobu79', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('OAK_WW1512935155', NULL, NULL, 'dhQueRobu82', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('OAK_WW1512935159', NULL, NULL, 'dhQueRobu86', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('OAK_WW1512935161', NULL, NULL, 'dhQueRobu88', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD10244238', NULL, NULL, 'icAdaBipu1', 'SAMEA9089056', NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL9330374', NULL, NULL, 'icAdaBipu1', 'SAMEA9089056', NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD11009761', NULL, NULL, 'icAdaBipu8', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD11534047', NULL, NULL, 'icAdaBipu11', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD13133244', NULL, NULL, 'icAdaBipu125', 'SAMEA13831117', NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD13133246', NULL, NULL, 'icAdaBipu146', 'SAMEA13831138', NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD13133247', NULL, NULL, 'icAdaBipu115', 'SAMEA13831107', NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD13133248', NULL, NULL, 'icAdaBipu148', 'SAMEA13831140', NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD13133249', NULL, NULL, 'icAdaBipu138', 'SAMEA13831130', NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD13133250', NULL, NULL, 'icAdaBipu118', 'SAMEA13831110', NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD13133251', NULL, NULL, 'icAdaBipu151', 'SAMEA13831143', NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD13133252', NULL, NULL, 'icAdaBipu133', 'SAMEA13831125', NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD13133253', NULL, NULL, 'icAdaBipu104', 'SAMEA13831096', NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD13133254', NULL, NULL, 'icAdaBipu117', 'SAMEA13831109', NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD13133255', NULL, NULL, 'icAdaBipu140', 'SAMEA13831132', NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD9672026', NULL, NULL, 'icAdaBipu3', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD10880856', NULL, NULL, 'icAdaBipu9', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD10880861', NULL, NULL, 'icAdaBipu9', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD10880860', NULL, NULL, 'icAdaBipu9', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD10880859', NULL, NULL, 'icAdaBipu9', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL11239534', NULL, NULL, 'icAdaBipu22', 'SAMEA10270795', NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD11239437', NULL, NULL, 'icAdaBipu15', 'SAMEA10270788', NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD11337313', NULL, NULL, 'icAdaBipu29', 'SAMEA10270802', NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD11768271', NULL, NULL, 'icAdaBipu36', 'SAMEA10270804', NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD12710414', NULL, NULL, 'icAdaBipu64', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD12925574', NULL, NULL, 'icAdaBipu69', 'SAMEA10270842', NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD13129888', NULL, NULL, 'icAdaBipu62', 'SAMEA10270835', NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD13179106', NULL, NULL, 'icAdaBipu143', 'SAMEA13831135', NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD13680850', NULL, NULL, 'icAdaBipu108', 'SAMEA13831100', NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD13698057', NULL, NULL, 'icAdaBipu145', 'SAMEA13831137', NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD13698061', NULL, NULL, 'icAdaBipu145', 'SAMEA13831137', NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD13698073', NULL, NULL, 'icAdaBipu145', 'SAMEA13831137', NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD13698078', NULL, NULL, 'icAdaBipu145', 'SAMEA13831137', NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL10597091', NULL, NULL, 'icAdaBipu6', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL10597085', NULL, NULL, 'icAdaBipu6', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD9815503', NULL, NULL, 'icAdaBipu6', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL10597086', NULL, NULL, 'icAdaBipu88', 'SAMEA9067702', NULL, NULL);
INSERT INTO public.sample VALUES ('DTOLRNA9465093', NULL, NULL, 'icAdaBipu2', NULL, NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD13796827', NULL, NULL, 'icAdaBipu218', 'SAMEA112816492', NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD13796826', NULL, NULL, 'icAdaBipu230', 'SAMEA112816504', NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD11297496', NULL, NULL, 'icAdaBipu28', 'SAMEA10270801', NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD11474737', NULL, NULL, 'icAdaBipu31', 'SAMEA10270804', NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD14472939', NULL, NULL, 'icAdaBipu274', 'SAMEA112816608', NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD14472941', NULL, NULL, 'icAdaBipu274', 'SAMEA112816608', NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD14472943', NULL, NULL, 'icAdaBipu274', 'SAMEA112816608', NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD14472945', NULL, NULL, 'icAdaBipu274', 'SAMEA112816608', NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD14472940', NULL, NULL, 'icAdaBipu274', 'SAMEA112816608', NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD14472942', NULL, NULL, 'icAdaBipu274', 'SAMEA112816608', NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD14472944', NULL, NULL, 'icAdaBipu274', 'SAMEA112816608', NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD14472946', NULL, NULL, 'icAdaBipu274', 'SAMEA112816608', NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD13897813', NULL, NULL, 'icAdaBipu217', 'SAMEA112816491', NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD13897814', NULL, NULL, 'icAdaBipu217', 'SAMEA112816491', NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD13897815', NULL, NULL, 'icAdaBipu217', 'SAMEA112816491', NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD14006912', NULL, NULL, 'icAdaBipu315', 'SAMEA112816680', NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL11204070', NULL, NULL, 'icAdaBipu20', 'SAMEA10270793', NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD11235035', NULL, NULL, 'icAdaBipu20', 'SAMEA10270794', NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD11543447', NULL, NULL, 'icAdaBipu32', 'SAMEA10270804', NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD12178943', NULL, NULL, 'icAdaBipu32', 'SAMEA10270875', NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD11611908', NULL, NULL, 'icAdaBipu33', 'SAMEA10270804', NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD12265682', NULL, NULL, 'icAdaBipu33', 'SAMEA10270875', NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD11680407', NULL, NULL, 'icAdaBipu34', 'SAMEA10270804', NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL_RD12215299', NULL, NULL, 'icAdaBipu34', 'SAMEA10270875', NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL9702654', NULL, NULL, 'lpJunEffu1', 'SAMEA7521953', NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL10341656', NULL, NULL, 'lpJunEffu1', 'SAMEA7521954', NULL, NULL);
INSERT INTO public.sample VALUES ('DTOL9838614', NULL, NULL, 'lpJunEffu1', 'SAMEA7521953', NULL, NULL);
INSERT INTO public.sample VALUES ('DTOLRNA10187174', NULL, NULL, 'lpJunEffu1', 'SAMEA7521953', NULL, NULL);


--
-- Data for Name: visibility_dict; Type: TABLE DATA; Schema: public; Owner: sts-dev
--

INSERT INTO public.visibility_dict VALUES ('Always', 'Shown in standard reporting');
INSERT INTO public.visibility_dict VALUES ('Testing', 'Sequencing development data');
INSERT INTO public.visibility_dict VALUES ('Withdrawn', 'Data has been deleted');


--
-- Data for Name: data; Type: TABLE DATA; Schema: public; Owner: sts-dev
--

INSERT INTO public.data VALUES (115350, '34714#13', NULL, 'DTOL_RD9128913', 'NT1630870I', NULL, '34714', NULL, '13', '4272', '4356', '2020-08-05 11:54:38+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115351, '34714#14', NULL, 'DTOL_RD9128914', 'NT1630871J', NULL, '34714', NULL, '14', '4273', '4356', '2020-08-05 11:54:38+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115352, '34714#15', NULL, 'DTOL_RD9128915', 'NT1630872K', NULL, '34714', NULL, '15', '4274', '4356', '2020-08-05 11:54:38+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115353, '34714#16', NULL, 'DTOL_RD9128916', 'NT1630873L', NULL, '34714', NULL, '16', '4275', '4356', '2020-08-05 11:54:38+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115354, '34714#17', NULL, 'DTOL_RD9128917', 'NT1630874M', NULL, '34714', NULL, '17', '4276', '4356', '2020-08-05 11:54:38+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115355, '34714#18', NULL, 'DTOL_RD9128918', 'NT1630875N', NULL, '34714', NULL, '18', '4277', '4356', '2020-08-05 11:54:38+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115356, '34714#19', NULL, 'DTOL_RD9128919', 'NT1630876O', NULL, '34714', NULL, '19', '4278', '4356', '2020-08-05 11:54:38+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115357, '34714#20', NULL, 'DTOL_RD9128920', 'NT1630877P', NULL, '34714', NULL, '20', '4279', '4356', '2020-08-05 11:54:38+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115358, '34714#21', NULL, 'DTOL_RD9128921', 'NT1630878Q', NULL, '34714', NULL, '21', '4280', '4356', '2020-08-05 11:54:38+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115359, '34714#22', NULL, 'DTOL_RD9128922', 'NT1630879R', NULL, '34714', NULL, '22', '4281', '4356', '2020-08-05 11:54:38+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115360, '34714#23', NULL, 'DTOL_RD9128923', 'NT1630880K', NULL, '34714', NULL, '23', '4282', '4356', '2020-08-05 11:54:38+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115361, '34714#24', NULL, 'DTOL_RD9128924', 'NT1630881L', NULL, '34714', NULL, '24', '4283', '4356', '2020-08-05 11:54:38+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115578, '34781_2#73', NULL, 'DTOL_RD9129045', 'NT1631003A', NULL, '34781', NULL, '73', '4332', '4356', '2020-08-07 11:11:01+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115579, '34781_2#74', NULL, 'DTOL_RD9129046', 'NT1631004B', NULL, '34781', NULL, '74', '4333', '4356', '2020-08-07 11:11:01+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115580, '34781_2#75', NULL, 'DTOL_RD9129047', 'NT1631005C', NULL, '34781', NULL, '75', '4334', '4356', '2020-08-07 11:11:01+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115581, '34781_2#76', NULL, 'DTOL_RD9129048', 'NT1631006D', NULL, '34781', NULL, '76', '4335', '4356', '2020-08-07 11:11:01+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115582, '34781_2#77', NULL, 'DTOL_RD9129049', 'NT1631007E', NULL, '34781', NULL, '77', '4336', '4356', '2020-08-07 11:11:01+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115583, '34781_2#78', NULL, 'DTOL_RD9129050', 'NT1631008F', NULL, '34781', NULL, '78', '4337', '4356', '2020-08-07 11:11:01+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115584, '34781_2#79', NULL, 'DTOL_RD9129051', 'NT1631009G', NULL, '34781', NULL, '79', '4338', '4356', '2020-08-07 11:11:01+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115585, '34781_2#80', NULL, 'DTOL_RD9129052', 'NT1631010W', NULL, '34781', NULL, '80', '4339', '4356', '2020-08-07 11:11:01+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115586, '34781_2#81', NULL, 'DTOL_RD9129053', 'NT1631011A', NULL, '34781', NULL, '81', '4340', '4356', '2020-08-07 11:11:01+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115587, '34781_2#82', NULL, 'DTOL_RD9129054', 'NT1631012B', NULL, '34781', NULL, '82', '4341', '4356', '2020-08-07 11:11:01+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115588, '34781_2#83', NULL, 'DTOL_RD9129055', 'NT1631013C', NULL, '34781', NULL, '83', '4342', '4356', '2020-08-07 11:11:01+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115589, '34781_2#84', NULL, 'DTOL_RD9129056', 'NT1631014D', NULL, '34781', NULL, '84', '4343', '4356', '2020-08-07 11:11:01+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115635, '37940_1#1', NULL, 'DTOL_RD10244239', 'DN805609I:E3', NULL, '37940', NULL, '1', '21', '21', '2021-05-20 17:34:50+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115645, '41302_1#2', NULL, 'DTOL_RD11009762', 'DN871923L:E11', NULL, '41302', NULL, '2', '85', '85', '2022-03-28 11:37:30+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115648, '41302_2#2', NULL, 'DTOL_RD11009762', 'DN871923L:G11', NULL, '41302', NULL, '2', '87', '87', '2022-03-28 11:37:30+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115651, '41305_1#2', NULL, 'DTOL_RD11009762', 'DN871923L:F11', NULL, '41305', NULL, '2', '86', '86', '2022-03-29 12:44:24+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115654, '41305_2#2', NULL, 'DTOL_RD11009762', 'DN871923L:H11', NULL, '41305', NULL, '2', '88', '88', '2022-03-29 12:44:24+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115657, '41306#2', NULL, 'DTOL_RD11009762', 'DN871923L:A2', NULL, '41306', NULL, '2', '2', '2', '2022-03-29 12:56:35+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115662, '43500_1#2', NULL, 'DTOL_RD11534048', 'DN905711L:B1', NULL, '43500', NULL, '2', '6511', '6512', '2022-02-09 11:35:15+00', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115666, '45763_1#1', NULL, 'DTOL_RD12811540', 'SQPP-1772-H:A1', NULL, '45763', NULL, '1', '1', '1', '2022-09-06 17:35:24+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115669, '45763_2#1', NULL, 'DTOL_RD12811546', 'SQPP-1772-H:A2', NULL, '45763', NULL, '1', '9', '9', '2022-09-06 17:35:24+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115672, '45763_2#4', NULL, 'DTOL_RD12811550', 'SQPP-1772-H:D2', NULL, '45763', NULL, '4', '12', '12', '2022-09-06 17:35:24+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115684, '46644_1#74', NULL, 'DTOL_RD13133243', 'DN881045S:B10', NULL, '46644', NULL, '74', '74', '74', '2023-02-10 13:45:45+00', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115686, '46644_1#76', NULL, 'DTOL_RD13133245', 'DN881045S:D10', NULL, '46644', NULL, '76', '76', '76', '2023-02-10 13:45:45+00', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115724, 'm64228e_210913_122131#1011', NULL, 'DTOL_RD10880862', 'DN855199N-G1', NULL, 'm64228e_210913_122131', NULL, NULL, '1011', NULL, '2021-09-14 21:50:17+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115726, 'm64228e_210912_060838#1011', NULL, 'DTOL_RD10880862', 'DN855199N-G1', NULL, 'm64228e_210912_060838', NULL, NULL, '1011', NULL, '2021-09-14 21:50:17+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115756, 'm64178e_211105_051438#1017', NULL, 'DTOL_RD11235048', 'DN887103M-F4', NULL, 'm64178e_211105_051438', NULL, NULL, '1017', NULL, '2021-11-09 05:30:36+00', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115764, 'm64094e_211106_093042#1001', NULL, 'DTOL_RD11235048', 'DN887104N-F4', NULL, 'm64094e_211106_093042', NULL, NULL, '1001', NULL, '2021-11-09 00:51:09+00', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115771, 'm64228e_211105_115646', NULL, 'DTOL_RD10880865', 'DN855199N-B2', NULL, 'm64228e_211105_115646', NULL, NULL, NULL, NULL, '2021-11-11 08:12:23+00', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115772, 'm64228e_211106_225141', NULL, 'DTOL_RD10880866', 'DN855199N-C2', NULL, 'm64228e_211106_225141', NULL, NULL, NULL, NULL, '2021-11-11 08:12:23+00', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115773, 'm64228e_211108_094826', NULL, 'DTOL_RD10880867', 'DN855199N-D2', NULL, 'm64228e_211108_094826', NULL, NULL, NULL, NULL, '2021-11-11 08:12:23+00', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115783, 'm64178e_211115_123002#1008', NULL, 'DTOL_RD11239438', 'DN891078J-D1', NULL, 'm64178e_211115_123002', NULL, NULL, '1008', NULL, '2021-11-18 06:57:31+00', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115784, 'm64178e_211116_212829#1012', NULL, 'DTOL_RD11239438', 'DN891079K-D1', NULL, 'm64178e_211116_212829', NULL, NULL, '1012', NULL, '2021-11-18 06:57:31+00', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115834, 'm64230e_220423_112659#bc1018_BAK8B_OA', NULL, 'DTOL_RD12710417', 'DTOL_RD12710417', NULL, 'm64230e_220423_112659', NULL, NULL, 'bc1018_BAK8B_OA', NULL, '2022-04-26 08:03:32+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115836, 'm64230e_220424_203712#bc1018_BAK8B_OA', NULL, 'DTOL_RD12710417', 'DTOL_RD12710417', NULL, 'm64230e_220424_203712', NULL, NULL, 'bc1018_BAK8B_OA', NULL, '2022-04-26 08:03:32+01', 'fail', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115867, 'm64089e_220922_160600#bc1020_BAK8B_OA', NULL, 'DTOL_RD13129891', 'DTOL_RD13129891', NULL, 'm64089e_220922_160600', NULL, NULL, 'bc1020_BAK8B_OA', NULL, '2022-09-27 12:23:23+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115871, 'm64089e_220923_210112#bc1020_BAK8B_OA', NULL, 'DTOL_RD13129891', 'DTOL_RD13129891', NULL, 'm64089e_220923_210112', NULL, NULL, 'bc1020_BAK8B_OA', NULL, '2022-09-27 12:23:23+01', 'fail', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115875, 'm64089e_220925_015808#bc1020_BAK8B_OA', NULL, 'DTOL_RD13129891', 'DTOL_RD13129891', NULL, 'm64089e_220925_015808', NULL, NULL, 'bc1020_BAK8B_OA', NULL, '2022-09-27 12:23:23+01', 'fail', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115879, 'm64089e_220926_065548#bc1020_BAK8B_OA', NULL, 'DTOL_RD13129891', 'DTOL_RD13129891', NULL, 'm64089e_220926_065548', NULL, NULL, 'bc1020_BAK8B_OA', NULL, '2022-09-27 12:23:23+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115917, 'm84047_230425_130728_s4#bc2004', NULL, 'DTOL_RD13680853', 'DTOL_RD13680853', NULL, 'm84047_230425_130728_s4', NULL, NULL, 'bc2004', NULL, '2023-04-28 12:38:51+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115923, 'm84047_230505_155651_s1#bc2004', NULL, 'DTOL_RD13680853', 'DTOL_RD13680853', NULL, 'm84047_230505_155651_s1', NULL, NULL, 'bc2004', NULL, '2023-05-10 11:31:36+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115925, 'm84047_230517_174928_s2#bc2004', NULL, 'DTOL_RD13680853', 'DTOL_RD13680853', NULL, 'm84047_230517_174928_s2', NULL, NULL, 'bc2004', NULL, '2023-05-19 16:36:18+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (118045, '35874_7#2', NULL, 'DTOL9475841', 'NT1652453N', NULL, '35874', NULL, '2', '2032', '2033', '2021-01-07 11:18:33+00', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (118047, '35874_8#2', NULL, 'DTOL9475841', 'NT1652453N', NULL, '35874', NULL, '2', '2032', '2033', '2021-01-07 11:18:33+00', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (118070, '35990_2#9', NULL, 'DTOL9384858', 'DN716902N:C11', NULL, '35990', NULL, '9', '329', NULL, '2020-12-24 14:03:03+00', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (118071, '35990_2#10', NULL, 'DTOL9384858', 'DN716902N:C11', NULL, '35990', NULL, '10', '330', NULL, '2020-12-24 14:03:03+00', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (118072, '35990_2#11', NULL, 'DTOL9384858', 'DN716902N:C11', NULL, '35990', NULL, '11', '331', NULL, '2020-12-24 14:03:03+00', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (118073, '35990_2#12', NULL, 'DTOL9384858', 'DN716902N:C11', NULL, '35990', NULL, '12', '332', NULL, '2020-12-24 14:03:03+00', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (118121, '35874_7#3', NULL, 'DTOL9475842', 'NT1652454O', NULL, '35874', NULL, '3', '2046', '2047', '2021-01-07 11:18:33+00', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (118122, '35874_8#3', NULL, 'DTOL9475842', 'NT1652454O', NULL, '35874', NULL, '3', '2046', '2047', '2021-01-07 11:18:33+00', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (120929, '40280#4', NULL, 'DTOL10597087', 'DN847892H:C10', NULL, '40280', NULL, '4', '75', '75', '2021-08-19 16:51:52+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (128828, '37363_2#1', NULL, 'OakPopGen9912158', 'DN606678N:B7', NULL, '37363', NULL, '1', '50', '50', '2021-04-19 14:42:30+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (128829, '37363_2#2', NULL, 'OakPopGen9912159', 'DN606678N:C7', NULL, '37363', NULL, '2', '51', '51', '2021-04-19 14:42:30+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (128830, '37363_2#3', NULL, 'OakPopGen9912160', 'DN606678N:D7', NULL, '37363', NULL, '3', '52', '52', '2021-04-19 14:42:30+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (128831, '37363_2#4', NULL, 'OakPopGen9912161', 'DN606678N:E7', NULL, '37363', NULL, '4', '53', '53', '2021-04-19 14:42:30+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (128832, '37363_2#5', NULL, 'OakPopGen9912162', 'DN606678N:F7', NULL, '37363', NULL, '5', '54', '54', '2021-04-19 14:42:30+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (128833, '37363_2#6', NULL, 'OakPopGen9912163', 'DN606678N:G7', NULL, '37363', NULL, '6', '55', '55', '2021-04-19 14:42:30+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (128834, '37363_2#7', NULL, 'OakPopGen9912164', 'DN606678N:H7', NULL, '37363', NULL, '7', '56', '56', '2021-04-19 14:42:30+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (128835, '37363_2#8', NULL, 'OakPopGen9912165', 'DN606678N:A8', NULL, '37363', NULL, '8', '57', '57', '2021-04-19 14:42:30+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (128836, '37363_2#9', NULL, 'OakPopGen9912166', 'DN606678N:B8', NULL, '37363', NULL, '9', '58', '58', '2021-04-19 14:42:30+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (128837, '37363_2#10', NULL, 'OakPopGen9912167', 'DN606678N:C8', NULL, '37363', NULL, '10', '59', '59', '2021-04-19 14:42:30+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (128838, '37363_2#11', NULL, 'OakPopGen9912168', 'DN606678N:D8', NULL, '37363', NULL, '11', '60', '60', '2021-04-19 14:42:30+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (128839, '37363_2#12', NULL, 'OakPopGen9912169', 'DN606678N:E8', NULL, '37363', NULL, '12', '61', '61', '2021-04-19 14:42:30+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (128840, '37363_2#13', NULL, 'OakPopGen9912170', 'DN606678N:F8', NULL, '37363', NULL, '13', '62', '62', '2021-04-19 14:42:30+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (128841, '37363_2#14', NULL, 'OakPopGen9912171', 'DN606678N:G8', NULL, '37363', NULL, '14', '63', '63', '2021-04-19 14:42:30+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (128842, '37363_2#15', NULL, 'OakPopGen9912172', 'DN606678N:H8', NULL, '37363', NULL, '15', '64', '64', '2021-04-19 14:42:30+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (128843, 'm64230e_210705_101703#1020', NULL, 'DTOL10185088', 'DN798399W-G3', NULL, 'm64230e_210705_101703', NULL, NULL, '1020', NULL, '2021-07-08 03:55:57+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (128844, 'm64097e_210617_142108#1010', NULL, 'DTOL10185080', 'DN798399W-G2', NULL, 'm64097e_210617_142108', NULL, NULL, '1010', NULL, '2021-06-22 20:13:15+01', 'fail', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (128850, 'm64094e_210430_115816#1010', NULL, 'DTOL10185080', 'DN798399W-G2', NULL, 'm64094e_210430_115816', NULL, NULL, '1010', NULL, '2021-05-05 18:37:54+01', 'fail', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (128845, 'm64097e_210621_084307#1001', NULL, 'DTOL10185075', 'DN798399W-B2', NULL, 'm64097e_210621_084307', NULL, NULL, '1001', NULL, '2021-06-22 20:13:15+01', 'fail', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (128854, 'm64097e_210425_025051#1001', NULL, 'DTOL10185075', 'DN798399W-B2', NULL, 'm64097e_210425_025051', NULL, NULL, '1001', NULL, '2021-04-27 21:11:12+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (128846, 'm64097e_210508_212855#1003', NULL, 'OakPopGen10218312', 'DN801931W-A1', NULL, 'm64097e_210508_212855', NULL, NULL, '1003', NULL, '2021-05-12 21:22:29+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (128847, 'm64174e_210501_195526#1003', NULL, 'DTOL10185077', 'DN798399W-D2', NULL, 'm64174e_210501_195526', NULL, NULL, '1003', NULL, '2021-05-05 20:27:22+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (128848, 'm64174e_210503_021816#1008', NULL, 'DTOL10185078', 'DN798399W-E2', NULL, 'm64174e_210503_021816', NULL, NULL, '1008', NULL, '2021-05-05 20:27:22+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (128849, 'm64174e_210504_084057#1009', NULL, 'DTOL10185079', 'DN798399W-F2', NULL, 'm64174e_210504_084057', NULL, NULL, '1009', NULL, '2021-05-05 20:27:22+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (128851, 'm64094e_210501_180717#1011', NULL, 'DTOL10185081', 'DN798399W-H2', NULL, 'm64094e_210501_180717', NULL, NULL, '1011', NULL, '2021-05-05 18:37:54+01', 'fail', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (128852, 'm64094e_210503_002936#1012', NULL, 'DTOL10185082', 'DN798399W-A3', NULL, 'm64094e_210503_002936', NULL, NULL, '1012', NULL, '2021-05-05 18:37:54+01', 'fail', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (128853, 'm64094e_210504_065204#1015', NULL, 'DTOL10185083', 'DN798399W-B3', NULL, 'm64094e_210504_065204', NULL, NULL, '1015', NULL, '2021-05-05 18:37:54+01', 'fail', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (128855, 'm64097e_210425_025051#1002', NULL, 'DTOL10185076', 'DN798399W-C2', NULL, 'm64097e_210425_025051', NULL, NULL, '1002', NULL, '2021-04-27 21:11:12+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (134379, 'm64221e_230913_152616#bc2021', NULL, 'DTOL_RD13796825', 'DTOL_RD13796825', NULL, 'm64221e_230913_152616', NULL, NULL, 'bc2021', NULL, '2023-09-22 15:09:35+01', 'fail', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (134805, 'm64230e_220219_230553#1020', NULL, 'DTOL_RD12215773', 'DN922367N-A1', NULL, 'm64230e_220219_230553', NULL, NULL, '1020', NULL, NULL, NULL, NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (131441, '45733#60', NULL, 'OAK_WW1512935160', 'DN881300O:D8', NULL, '45733', NULL, '60', '60', '60', '2022-09-05 16:35:03+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (127652, '44268_5#3', NULL, 'DTOLRNA11521361', 'DN881228A:C1', NULL, '44268', NULL, '3', '3', '3', '2022-03-25 13:51:33+00', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (131442, '45733#61', NULL, 'OAK_WW1512935162', 'DN881300O:E8', NULL, '45733', NULL, '61', '61', '61', '2022-09-05 16:35:03+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (131443, '45733#62', NULL, 'OAK_WW1512935163', 'DN881300O:F8', NULL, '45733', NULL, '62', '62', '62', '2022-09-05 16:35:03+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (131382, '45733#1', NULL, 'OAK_WW1512935093', 'DN881300O:A1', NULL, '45733', NULL, '1', '1', '1', '2022-09-05 16:35:03+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (131383, '45733#2', NULL, 'OAK_WW1512935094', 'DN881300O:B1', NULL, '45733', NULL, '2', '2', '2', '2022-09-05 16:35:03+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (131384, '45733#3', NULL, 'OAK_WW1512935095', 'DN881300O:C1', NULL, '45733', NULL, '3', '3', '3', '2022-09-05 16:35:03+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (131385, '45733#4', NULL, 'OAK_WW1512935096', 'DN881300O:D1', NULL, '45733', NULL, '4', '4', '4', '2022-09-05 16:35:03+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (131386, '45733#5', NULL, 'OAK_WW1512935097', 'DN881300O:E1', NULL, '45733', NULL, '5', '5', '5', '2022-09-05 16:35:03+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (131387, '45733#6', NULL, 'OAK_WW1512935098', 'DN881300O:F1', NULL, '45733', NULL, '6', '6', '6', '2022-09-05 16:35:03+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (131388, '45733#7', NULL, 'OAK_WW1512935099', 'DN881300O:G1', NULL, '45733', NULL, '7', '7', '7', '2022-09-05 16:35:03+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (131389, '45733#8', NULL, 'OAK_WW1512935100', 'DN881300O:H1', NULL, '45733', NULL, '8', '8', '8', '2022-09-05 16:35:03+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (131390, '45733#9', NULL, 'OAK_WW1512935101', 'DN881300O:A2', NULL, '45733', NULL, '9', '9', '9', '2022-09-05 16:35:03+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (131391, '45733#10', NULL, 'OAK_WW1512935102', 'DN881300O:B2', NULL, '45733', NULL, '10', '10', '10', '2022-09-05 16:35:03+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (131392, '45733#11', NULL, 'OAK_WW1512935103', 'DN881300O:C2', NULL, '45733', NULL, '11', '11', '11', '2022-09-05 16:35:03+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (131393, '45733#12', NULL, 'OAK_WW1512935104', 'DN881300O:D2', NULL, '45733', NULL, '12', '12', '12', '2022-09-05 16:35:03+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (131394, '45733#13', NULL, 'OAK_WW1512935105', 'DN881300O:E2', NULL, '45733', NULL, '13', '13', '13', '2022-09-05 16:35:03+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (131395, '45733#14', NULL, 'OAK_WW1512935106', 'DN881300O:F2', NULL, '45733', NULL, '14', '14', '14', '2022-09-05 16:35:03+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (131396, '45733#15', NULL, 'OAK_WW1512935107', 'DN881300O:G2', NULL, '45733', NULL, '15', '15', '15', '2022-09-05 16:35:03+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (131397, '45733#16', NULL, 'OAK_WW1512935108', 'DN881300O:H2', NULL, '45733', NULL, '16', '16', '16', '2022-09-05 16:35:03+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (131398, '45733#17', NULL, 'OAK_WW1512935109', 'DN881300O:A3', NULL, '45733', NULL, '17', '17', '17', '2022-09-05 16:35:03+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (131399, '45733#18', NULL, 'OAK_WW1512935110', 'DN881300O:B3', NULL, '45733', NULL, '18', '18', '18', '2022-09-05 16:35:03+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (131400, '45733#19', NULL, 'OAK_WW1512935111', 'DN881300O:C3', NULL, '45733', NULL, '19', '19', '19', '2022-09-05 16:35:03+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (131401, '45733#20', NULL, 'OAK_WW1512935112', 'DN881300O:D3', NULL, '45733', NULL, '20', '20', '20', '2022-09-05 16:35:03+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (131402, '45733#21', NULL, 'OAK_WW1512935113', 'DN881300O:E3', NULL, '45733', NULL, '21', '21', '21', '2022-09-05 16:35:03+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (131403, '45733#22', NULL, 'OAK_WW1512935114', 'DN881300O:F3', NULL, '45733', NULL, '22', '22', '22', '2022-09-05 16:35:03+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (131404, '45733#23', NULL, 'OAK_WW1512935115', 'DN881300O:G3', NULL, '45733', NULL, '23', '23', '23', '2022-09-05 16:35:03+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (131405, '45733#24', NULL, 'OAK_WW1512935116', 'DN881300O:H3', NULL, '45733', NULL, '24', '24', '24', '2022-09-05 16:35:03+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (131406, '45733#25', NULL, 'OAK_WW1512935117', 'DN881300O:A4', NULL, '45733', NULL, '25', '25', '25', '2022-09-05 16:35:03+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (131407, '45733#26', NULL, 'OAK_WW1512935118', 'DN881300O:B4', NULL, '45733', NULL, '26', '26', '26', '2022-09-05 16:35:03+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (131408, '45733#27', NULL, 'OAK_WW1512935119', 'DN881300O:C4', NULL, '45733', NULL, '27', '27', '27', '2022-09-05 16:35:03+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (131409, '45733#28', NULL, 'OAK_WW1512935120', 'DN881300O:D4', NULL, '45733', NULL, '28', '28', '28', '2022-09-05 16:35:03+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (131410, '45733#29', NULL, 'OAK_WW1512935121', 'DN881300O:E4', NULL, '45733', NULL, '29', '29', '29', '2022-09-05 16:35:03+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (131411, '45733#30', NULL, 'OAK_WW1512935122', 'DN881300O:F4', NULL, '45733', NULL, '30', '30', '30', '2022-09-05 16:35:03+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (131412, '45733#31', NULL, 'OAK_WW1512935123', 'DN881300O:G4', NULL, '45733', NULL, '31', '31', '31', '2022-09-05 16:35:03+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (131413, '45733#32', NULL, 'OAK_WW1512935124', 'DN881300O:H4', NULL, '45733', NULL, '32', '32', '32', '2022-09-05 16:35:03+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (131414, '45733#33', NULL, 'OAK_WW1512935125', 'DN881300O:A5', NULL, '45733', NULL, '33', '33', '33', '2022-09-05 16:35:03+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (131415, '45733#34', NULL, 'OAK_WW1512935126', 'DN881300O:B5', NULL, '45733', NULL, '34', '34', '34', '2022-09-05 16:35:03+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (131416, '45733#35', NULL, 'OAK_WW1512935127', 'DN881300O:C5', NULL, '45733', NULL, '35', '35', '35', '2022-09-05 16:35:03+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (131417, '45733#36', NULL, 'OAK_WW1512935128', 'DN881300O:D5', NULL, '45733', NULL, '36', '36', '36', '2022-09-05 16:35:03+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (131418, '45733#37', NULL, 'OAK_WW1512935129', 'DN881300O:E5', NULL, '45733', NULL, '37', '37', '37', '2022-09-05 16:35:03+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (131419, '45733#38', NULL, 'OAK_WW1512935130', 'DN881300O:F5', NULL, '45733', NULL, '38', '38', '38', '2022-09-05 16:35:03+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (131420, '45733#39', NULL, 'OAK_WW1512935131', 'DN881300O:G5', NULL, '45733', NULL, '39', '39', '39', '2022-09-05 16:35:03+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (131421, '45733#40', NULL, 'OAK_WW1512935132', 'DN881300O:H5', NULL, '45733', NULL, '40', '40', '40', '2022-09-05 16:35:03+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (131422, '45733#41', NULL, 'OAK_WW1512935134', 'DN881300O:A6', NULL, '45733', NULL, '41', '41', '41', '2022-09-05 16:35:03+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (131423, '45733#42', NULL, 'OAK_WW1512935135', 'DN881300O:B6', NULL, '45733', NULL, '42', '42', '42', '2022-09-05 16:35:03+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (131424, '45733#43', NULL, 'OAK_WW1512935136', 'DN881300O:C6', NULL, '45733', NULL, '43', '43', '43', '2022-09-05 16:35:03+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (131425, '45733#44', NULL, 'OAK_WW1512935138', 'DN881300O:D6', NULL, '45733', NULL, '44', '44', '44', '2022-09-05 16:35:03+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (131426, '45733#45', NULL, 'OAK_WW1512935140', 'DN881300O:E6', NULL, '45733', NULL, '45', '45', '45', '2022-09-05 16:35:03+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (131427, '45733#46', NULL, 'OAK_WW1512935141', 'DN881300O:F6', NULL, '45733', NULL, '46', '46', '46', '2022-09-05 16:35:03+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (131428, '45733#47', NULL, 'OAK_WW1512935142', 'DN881300O:G6', NULL, '45733', NULL, '47', '47', '47', '2022-09-05 16:35:03+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (131429, '45733#48', NULL, 'OAK_WW1512935143', 'DN881300O:H6', NULL, '45733', NULL, '48', '48', '48', '2022-09-05 16:35:03+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (131430, '45733#49', NULL, 'OAK_WW1512935144', 'DN881300O:A7', NULL, '45733', NULL, '49', '49', '49', '2022-09-05 16:35:03+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (131431, '45733#50', NULL, 'OAK_WW1512935145', 'DN881300O:B7', NULL, '45733', NULL, '50', '50', '50', '2022-09-05 16:35:03+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (131432, '45733#51', NULL, 'OAK_WW1512935146', 'DN881300O:C7', NULL, '45733', NULL, '51', '51', '51', '2022-09-05 16:35:03+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (131433, '45733#52', NULL, 'OAK_WW1512935147', 'DN881300O:D7', NULL, '45733', NULL, '52', '52', '52', '2022-09-05 16:35:03+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (131434, '45733#53', NULL, 'OAK_WW1512935148', 'DN881300O:E7', NULL, '45733', NULL, '53', '53', '53', '2022-09-05 16:35:03+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (131435, '45733#54', NULL, 'OAK_WW1512935149', 'DN881300O:F7', NULL, '45733', NULL, '54', '54', '54', '2022-09-05 16:35:03+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (131436, '45733#55', NULL, 'OAK_WW1512935150', 'DN881300O:G7', NULL, '45733', NULL, '55', '55', '55', '2022-09-05 16:35:03+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (131437, '45733#56', NULL, 'OAK_WW1512935153', 'DN881300O:H7', NULL, '45733', NULL, '56', '56', '56', '2022-09-05 16:35:03+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (131438, '45733#57', NULL, 'OAK_WW1512935154', 'DN881300O:A8', NULL, '45733', NULL, '57', '57', '57', '2022-09-05 16:35:03+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (131439, '45733#58', NULL, 'OAK_WW1512935157', 'DN881300O:B8', NULL, '45733', NULL, '58', '58', '58', '2022-09-05 16:35:03+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (131440, '45733#59', NULL, 'OAK_WW1512935158', 'DN881300O:C8', NULL, '45733', NULL, '59', '59', '59', '2022-09-05 16:35:03+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (131444, '45733#63', NULL, 'OAK_WW1512935164', 'DN881300O:G8', NULL, '45733', NULL, '63', '63', '63', '2022-09-05 16:35:03+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (131445, '45733#64', NULL, 'OAK_WW1512935133', 'DN881300O:H8', NULL, '45733', NULL, '64', '64', '64', '2022-09-05 16:35:03+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (131446, '45733#65', NULL, 'OAK_WW1512935137', 'DN881300O:A9', NULL, '45733', NULL, '65', '65', '65', '2022-09-05 16:35:03+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (131447, '45733#66', NULL, 'OAK_WW1512935139', 'DN881300O:B9', NULL, '45733', NULL, '66', '66', '66', '2022-09-05 16:35:03+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (131448, '45733#67', NULL, 'OAK_WW1512935151', 'DN881300O:C9', NULL, '45733', NULL, '67', '67', '67', '2022-09-05 16:35:03+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (131449, '45733#68', NULL, 'OAK_WW1512935152', 'DN881300O:D9', NULL, '45733', NULL, '68', '68', '68', '2022-09-05 16:35:03+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (131450, '45733#69', NULL, 'OAK_WW1512935155', 'DN881300O:E9', NULL, '45733', NULL, '69', '69', '69', '2022-09-05 16:35:03+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (131451, '45733#70', NULL, 'OAK_WW1512935159', 'DN881300O:F9', NULL, '45733', NULL, '70', '70', '70', '2022-09-05 16:35:03+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (131452, '45733#71', NULL, 'OAK_WW1512935161', 'DN881300O:G9', NULL, '45733', NULL, '71', '71', '71', '2022-09-05 16:35:03+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115632, '37939_1#3', NULL, 'DTOL_RD10244238', 'DN805609I:D3', NULL, '37939', NULL, '3', '20', '20', '2021-05-21 10:35:42+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (117569, '35281_2#1', NULL, 'DTOL9330374', 'DN690780I:B10', NULL, '35281', NULL, '1', '293', NULL, '2020-11-16 11:10:05+00', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (117570, '35281_2#2', NULL, 'DTOL9330374', 'DN690780I:B10', NULL, '35281', NULL, '2', '294', NULL, '2020-11-16 11:10:05+00', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (117571, '35281_2#3', NULL, 'DTOL9330374', 'DN690780I:B10', NULL, '35281', NULL, '3', '295', NULL, '2020-11-16 11:10:05+00', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (117572, '35281_2#4', NULL, 'DTOL9330374', 'DN690780I:B10', NULL, '35281', NULL, '4', '296', NULL, '2020-11-16 11:10:05+00', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115644, '41302_1#1', NULL, 'DTOL_RD11009761', 'DN871923L:A11', NULL, '41302', NULL, '1', '81', '81', '2022-03-28 11:37:30+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115647, '41302_2#1', NULL, 'DTOL_RD11009761', 'DN871923L:C11', NULL, '41302', NULL, '1', '83', '83', '2022-03-28 11:37:30+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115650, '41305_1#1', NULL, 'DTOL_RD11009761', 'DN871923L:B11', NULL, '41305', NULL, '1', '82', '82', '2022-03-29 12:44:24+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115653, '41305_2#1', NULL, 'DTOL_RD11009761', 'DN871923L:D11', NULL, '41305', NULL, '1', '84', '84', '2022-03-29 12:44:24+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115656, '41306#1', NULL, 'DTOL_RD11009761', 'DN871923L:A1', NULL, '41306', NULL, '1', '1', '1', '2022-03-29 12:56:35+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115661, '43500_1#1', NULL, 'DTOL_RD11534047', 'DN905711L:A1', NULL, '43500', NULL, '1', '6510', '1828', '2022-02-09 11:35:15+00', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115685, '46644_1#75', NULL, 'DTOL_RD13133244', 'DN881045S:C10', NULL, '46644', NULL, '75', '75', '75', '2023-02-10 13:45:45+00', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115687, '46644_1#77', NULL, 'DTOL_RD13133246', 'DN881045S:E10', NULL, '46644', NULL, '77', '77', '77', '2023-02-10 13:45:45+00', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115688, '46644_1#78', NULL, 'DTOL_RD13133247', 'DN881045S:F10', NULL, '46644', NULL, '78', '78', '78', '2023-02-10 13:45:45+00', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115689, '46644_1#79', NULL, 'DTOL_RD13133248', 'DN881045S:G10', NULL, '46644', NULL, '79', '79', '79', '2023-02-10 13:45:45+00', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115690, '46644_1#80', NULL, 'DTOL_RD13133249', 'DN881045S:H10', NULL, '46644', NULL, '80', '80', '80', '2023-02-10 13:45:45+00', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115691, '46644_1#81', NULL, 'DTOL_RD13133250', 'DN881045S:A11', NULL, '46644', NULL, '81', '81', '81', '2023-02-10 13:45:45+00', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115692, '46644_1#82', NULL, 'DTOL_RD13133251', 'DN881045S:B11', NULL, '46644', NULL, '82', '82', '82', '2023-02-10 13:45:45+00', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115693, '46644_1#83', NULL, 'DTOL_RD13133252', 'DN881045S:C11', NULL, '46644', NULL, '83', '83', '83', '2023-02-10 13:45:45+00', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115694, '46644_1#84', NULL, 'DTOL_RD13133253', 'DN881045S:D11', NULL, '46644', NULL, '84', '84', '84', '2023-02-10 13:45:45+00', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115695, '46644_1#85', NULL, 'DTOL_RD13133254', 'DN881045S:E11', NULL, '46644', NULL, '85', '85', '85', '2023-02-10 13:45:45+00', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115696, '46644_1#86', NULL, 'DTOL_RD13133255', 'DN881045S:F11', NULL, '46644', NULL, '86', '86', '86', '2023-02-10 13:45:45+00', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115713, 'm64174e_210130_144539#1015', NULL, 'DTOL_RD9672026', 'DN739243A-A1', NULL, 'm64174e_210130_144539', NULL, NULL, '1015', NULL, '2021-02-01 14:26:21+00', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115725, 'm64228e_210909_150013#1010', NULL, 'DTOL_RD10880856', 'DN855199N-A1', NULL, 'm64228e_210909_150013', NULL, NULL, '1010', NULL, '2021-09-14 21:50:17+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115727, 'm64228e_210910_210956#1010', NULL, 'DTOL_RD10880856', 'DN855199N-A1', NULL, 'm64228e_210910_210956', NULL, NULL, '1010', NULL, '2021-09-14 21:50:17+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115738, 'm64094e_211025_104111#1002', NULL, 'DTOL_RD10880861', 'DN855199N-F1', NULL, 'm64094e_211025_104111', NULL, NULL, '1002', NULL, '2021-10-28 07:36:27+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115739, 'm64094e_211025_104111#1003', NULL, 'DTOL_RD10880860', 'DN855199N-E1', NULL, 'm64094e_211025_104111', NULL, NULL, '1003', NULL, '2021-10-28 07:36:27+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115740, 'm64094e_211025_104111#1008', NULL, 'DTOL_RD10880859', 'DN855199N-D1', NULL, 'm64094e_211025_104111', NULL, NULL, '1008', NULL, '2021-10-28 07:36:27+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115750, 'm64174e_211103_153104#1008', NULL, 'DTOL11239534', 'DN882539Q-D1', NULL, 'm64174e_211103_153104', NULL, NULL, '1008', NULL, '2021-11-09 04:03:28+00', 'fail', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115781, 'm64178e_211112_183448#1003', NULL, 'DTOL_RD11239437', 'DN891078J-C1', NULL, 'm64178e_211112_183448', NULL, NULL, '1003', NULL, '2021-11-18 06:57:31+00', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115782, 'm64178e_211114_033110#1011', NULL, 'DTOL_RD11239437', 'DN891079K-C1', NULL, 'm64178e_211114_033110', NULL, NULL, '1011', NULL, '2021-11-18 06:57:31+00', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115792, 'm64221e_211117_160848#1009', NULL, 'DTOL_RD11337313', 'DN889188S-A1', NULL, 'm64221e_211117_160848', NULL, NULL, '1009', NULL, '2021-11-23 10:25:49+00', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115811, 'm64174e_220128_000029#1003', NULL, 'DTOL_RD11768271', 'DN909105L-A1', NULL, 'm64174e_220128_000029', NULL, NULL, '1003', NULL, '2022-01-31 23:41:36+00', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115837, 'm64228e_220423_113317#bc1016_BAK8B_OA', NULL, 'DTOL_RD12710414', 'DTOL_RD12710414', NULL, 'm64228e_220423_113317', NULL, NULL, 'bc1016_BAK8B_OA', NULL, '2022-04-26 08:17:44+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115838, 'm64228e_220424_205021#bc1016_BAK8B_OA', NULL, 'DTOL_RD12710414', 'DTOL_RD12710414', NULL, 'm64228e_220424_205021', NULL, NULL, 'bc1016_BAK8B_OA', NULL, '2022-04-26 08:17:44+01', 'fail', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115842, 'm64094e_220811_122820#bc1003_BAK8A_OA', NULL, 'DTOL_RD12925574', 'DTOL_RD12925574', NULL, 'm64094e_220811_122820', NULL, NULL, 'bc1003_BAK8A_OA', NULL, '2022-08-16 04:54:07+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115845, 'm64094e_220812_172220#bc1003_BAK8A_OA', NULL, 'DTOL_RD12925574', 'DTOL_RD12925574', NULL, 'm64094e_220812_172220', NULL, NULL, 'bc1003_BAK8A_OA', NULL, '2022-08-16 04:54:07+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115848, 'm64094e_220813_205234#bc1003_BAK8A_OA', NULL, 'DTOL_RD12925574', 'DTOL_RD12925574', NULL, 'm64094e_220813_205234', NULL, NULL, 'bc1003_BAK8A_OA', NULL, '2022-08-16 04:54:07+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115851, 'm64094e_220815_002611#bc1003_BAK8A_OA', NULL, 'DTOL_RD12925574', 'DTOL_RD12925574', NULL, 'm64094e_220815_002611', NULL, NULL, 'bc1003_BAK8A_OA', NULL, '2022-08-16 04:54:07+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115864, 'm64089e_220922_160600#bc1016_BAK8B_OA', NULL, 'DTOL_RD13129888', 'DTOL_RD13129888', NULL, 'm64089e_220922_160600', NULL, NULL, 'bc1016_BAK8B_OA', NULL, '2022-09-27 12:23:23+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115868, 'm64089e_220923_210112#bc1016_BAK8B_OA', NULL, 'DTOL_RD13129888', 'DTOL_RD13129888', NULL, 'm64089e_220923_210112', NULL, NULL, 'bc1016_BAK8B_OA', NULL, '2022-09-27 12:23:23+01', 'fail', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115872, 'm64089e_220925_015808#bc1016_BAK8B_OA', NULL, 'DTOL_RD13129888', 'DTOL_RD13129888', NULL, 'm64089e_220925_015808', NULL, NULL, 'bc1016_BAK8B_OA', NULL, '2022-09-27 12:23:23+01', 'fail', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115876, 'm64089e_220926_065548#bc1016_BAK8B_OA', NULL, 'DTOL_RD13129888', 'DTOL_RD13129888', NULL, 'm64089e_220926_065548', NULL, NULL, 'bc1016_BAK8B_OA', NULL, '2022-09-27 12:23:23+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115888, 'm64174e_221108_072343#bc1009_BAK8A_OA', NULL, 'DTOL_RD13179106', 'DTOL_RD13179106', NULL, 'm64174e_221108_072343', NULL, NULL, 'bc1009_BAK8A_OA', NULL, '2022-11-16 00:00:00+00', 'fail', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115918, 'm84047_230425_113454_s1#bc2001', NULL, 'DTOL_RD13680850', 'DTOL_RD13680850', NULL, 'm84047_230425_113454_s1', NULL, NULL, 'bc2001', NULL, '2023-05-10 14:11:42+01', 'fail', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115920, 'm64016e_230429_173736#bc2001', NULL, 'DTOL_RD13680850', 'DTOL_RD13680850', NULL, 'm64016e_230429_173736', NULL, NULL, 'bc2001', NULL, '2023-05-12 13:32:08+01', 'fail', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115927, 'm84047_230706_152551_s2#bc2041', NULL, 'DTOL_RD13698057', 'DTOL_RD13698057', NULL, 'm84047_230706_152551_s2', NULL, NULL, 'bc2041', NULL, '2023-07-11 11:11:51+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115928, 'm84047_230706_152551_s2#bc2042', NULL, 'DTOL_RD13698061', 'DTOL_RD13698061', NULL, 'm84047_230706_152551_s2', NULL, NULL, 'bc2042', NULL, '2023-07-11 11:11:51+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115929, 'm84047_230706_152551_s2#bc2043', NULL, 'DTOL_RD13698073', 'DTOL_RD13698073', NULL, 'm84047_230706_152551_s2', NULL, NULL, 'bc2043', NULL, '2023-07-11 11:11:51+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115930, 'm84047_230706_152551_s2#bc2044', NULL, 'DTOL_RD13698078', 'DTOL_RD13698078', NULL, 'm84047_230706_152551_s2', NULL, NULL, 'bc2044', NULL, '2023-07-11 11:11:51+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (120926, '40280#1', NULL, 'DTOL10597091', 'DN847892H:D2', NULL, '40280', NULL, '1', '12', '12', '2021-08-19 16:51:52+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (120927, '40280#2', NULL, 'DTOL10597085', 'DN847892H:A10', NULL, '40280', NULL, '2', '73', '73', '2021-08-19 16:51:52+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (134799, 'm64125e_210211_151547#1010', NULL, 'DTOL_RD9815503', 'DN760937C-A1', NULL, 'm64125e_210211_151547', NULL, NULL, '1010', NULL, NULL, NULL, NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (120928, '40280#3', NULL, 'DTOL10597086', 'DN847892H:B10', NULL, '40280', NULL, '3', '74', '74', '2021-08-19 16:51:52+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (127428, '36703_5#2', NULL, 'DTOLRNA9465093', 'DN611904M:D3', NULL, '36703', NULL, '2', '20', '20', '2021-03-19 10:56:23+00', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (133566, 'm64221e_230816_183713#bc2023', NULL, 'DTOL_RD13796827', 'DTOL_RD13796827', NULL, 'm64221e_230816_183713', NULL, NULL, 'bc2023', NULL, '2023-09-01 14:33:00+01', 'fail', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (133565, 'm64221e_230815_134000#bc2022', NULL, 'DTOL_RD13796826', 'DTOL_RD13796826', NULL, 'm64221e_230815_134000', NULL, NULL, 'bc2022', NULL, '2023-09-01 14:30:54+01', 'fail', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (134802, 'm64221e_211110_155624#1010', NULL, 'DTOL_RD11297496', 'DN886472H-A1', NULL, 'm64221e_211110_155624', NULL, NULL, '1010', NULL, NULL, NULL, NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (134804, 'm64097e_211204_084129#1021', NULL, 'DTOL_RD11474737', 'DN897878L-A1', NULL, 'm64097e_211204_084129', NULL, NULL, '1021', NULL, NULL, NULL, NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (136203, 'm84047_231120_144131_s1#bc2053', NULL, 'DTOL_RD14472939', 'DTOL_RD14472939', NULL, 'm84047_231120_144131_s1', NULL, NULL, 'bc2053', NULL, '2023-11-22 13:33:09+00', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (136204, 'm84047_231120_144131_s1#bc2055', NULL, 'DTOL_RD14472941', 'DTOL_RD14472941', NULL, 'm84047_231120_144131_s1', NULL, NULL, 'bc2055', NULL, '2023-11-22 13:33:09+00', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (136205, 'm84047_231120_144131_s1#bc2057', NULL, 'DTOL_RD14472943', 'DTOL_RD14472943', NULL, 'm84047_231120_144131_s1', NULL, NULL, 'bc2057', NULL, '2023-11-22 13:33:09+00', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (136206, 'm84047_231120_144131_s1#bc2059', NULL, 'DTOL_RD14472945', 'DTOL_RD14472945', NULL, 'm84047_231120_144131_s1', NULL, NULL, 'bc2059', NULL, '2023-11-22 13:33:09+00', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (136207, 'm84047_231120_151150_s2#bc2054', NULL, 'DTOL_RD14472940', 'DTOL_RD14472940', NULL, 'm84047_231120_151150_s2', NULL, NULL, 'bc2054', NULL, '2023-11-22 13:33:51+00', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (136208, 'm84047_231120_151150_s2#bc2056', NULL, 'DTOL_RD14472942', 'DTOL_RD14472942', NULL, 'm84047_231120_151150_s2', NULL, NULL, 'bc2056', NULL, '2023-11-22 13:33:51+00', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (136209, 'm84047_231120_151150_s2#bc2058', NULL, 'DTOL_RD14472944', 'DTOL_RD14472944', NULL, 'm84047_231120_151150_s2', NULL, NULL, 'bc2058', NULL, '2023-11-22 13:33:51+00', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (136210, 'm84047_231120_151150_s2#bc2060', NULL, 'DTOL_RD14472946', 'DTOL_RD14472946', NULL, 'm84047_231120_151150_s2', NULL, NULL, 'bc2060', NULL, '2023-11-22 13:33:51+00', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (136405, 'm64228e_231127_153346#bc2045', NULL, 'DTOL_RD13897813', 'DTOL_RD13897813', NULL, 'm64228e_231127_153346', NULL, NULL, 'bc2045', NULL, '2023-12-07 12:19:10+00', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (136428, 'm64228e_231128_184021#bc2046', NULL, 'DTOL_RD13897814', 'DTOL_RD13897814', NULL, 'm64228e_231128_184021', NULL, NULL, 'bc2046', NULL, '2023-12-07 12:19:01+00', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (136649, 'm64089e_231202_200225#bc2047', NULL, 'DTOL_RD13897815', 'DTOL_RD13897815', NULL, 'm64089e_231202_200225', NULL, NULL, 'bc2047', NULL, '2023-12-05 10:53:44+00', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (136865, 'm64089e_231221_145323#bc2079', NULL, 'DTOL_RD14006912', 'DTOL_RD14006912', NULL, 'm64089e_231221_145323', NULL, NULL, 'bc2079', NULL, '2024-01-02 15:04:33+00', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115747, 'm64221e_211029_115402#1020', NULL, 'DTOL11204070', 'DN878737Q-H1', NULL, 'm64221e_211029_115402', NULL, NULL, '1020', NULL, '2021-10-29 14:51:42+01', 'fail', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115758, 'm64125e_211103_175849#1011', NULL, 'DTOL_RD11235035', 'DN887103M-A3', NULL, 'm64125e_211103_175849', NULL, NULL, '1011', NULL, '2021-11-09 02:52:57+00', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115767, 'm64089e_211106_112750#1019', NULL, 'DTOL_RD11235035', 'DN887104N-A3', NULL, 'm64089e_211106_112750', NULL, NULL, '1019', NULL, '2021-11-09 04:33:35+00', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115805, 'm64229e_211215_184451#1018', NULL, 'DTOL_RD11543447', 'DN902173S-A1', NULL, 'm64229e_211215_184451', NULL, NULL, '1018', NULL, '2021-12-21 05:40:56+00', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (134806, 'm64230e_220221_063339#1009', NULL, 'DTOL_RD12178943', 'DN921237A-A1', NULL, 'm64230e_220221_063339', NULL, NULL, '1009', NULL, NULL, NULL, NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115806, 'm64221e_211216_143308#1017', NULL, 'DTOL_RD11611908', 'DN904278L-A1', NULL, 'm64221e_211216_143308', NULL, NULL, '1017', NULL, '2021-12-21 00:29:04+00', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (134808, 'm64094e_220306_084547#1001', NULL, 'DTOL_RD12265682', 'DN923824V-A1', NULL, 'm64094e_220306_084547', NULL, NULL, '1001', NULL, NULL, NULL, NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115807, 'm64178e_220109_104526#1012', NULL, 'DTOL_RD11680407', 'DN906267Q-A1', NULL, 'm64178e_220109_104526', NULL, NULL, '1012', NULL, '2022-01-12 05:18:53+00', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (115830, 'm64016e_220309_153701#1012', NULL, 'DTOL_RD12215299', 'DN922353H-G1', NULL, 'm64016e_220309_153701', NULL, NULL, '1012', NULL, '2022-03-15 00:45:09+00', 'fail', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (118427, '36691_2#5', NULL, 'DTOL9702654', 'DN771163M:G8', NULL, '36691', NULL, '5', '249', NULL, '2021-03-18 12:16:43+00', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (118428, '36691_2#6', NULL, 'DTOL9702654', 'DN771163M:G8', NULL, '36691', NULL, '6', '250', NULL, '2021-03-18 12:16:43+00', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (118429, '36691_2#7', NULL, 'DTOL9702654', 'DN771163M:G8', NULL, '36691', NULL, '7', '251', NULL, '2021-03-18 12:16:43+00', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (118430, '36691_2#8', NULL, 'DTOL9702654', 'DN771163M:G8', NULL, '36691', NULL, '8', '252', NULL, '2021-03-18 12:16:43+00', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (121083, '40666_2#2', NULL, 'DTOL10341656', 'DN826505P:B3', NULL, '40666', NULL, '2', '90', '90', '2021-09-11 11:11:14+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (124432, 'm64097e_210221_172213#1019', NULL, 'DTOL9838614', 'DN765124Q-B1', NULL, 'm64097e_210221_172213', NULL, NULL, '1019', NULL, '2021-02-22 23:07:55+00', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.data VALUES (127563, '37935_8#13', NULL, 'DTOLRNA10187174', 'DN612239G:G9', NULL, '37935', NULL, '13', '71', '71', '2021-05-25 13:45:59+01', 'pass', NULL, NULL, 'Always', NULL, NULL, NULL, NULL, NULL, NULL, NULL);


--
-- Data for Name: project; Type: TABLE DATA; Schema: public; Owner: sts-dev
--

INSERT INTO public.project VALUES (17, 'darwin/rnd', 'DTOL_Darwin R&D', 5822, NULL);
INSERT INTO public.project VALUES (21, 'darwin/{}', 'DTOL_Darwin Tree of Life', 5901, NULL);
INSERT INTO public.project VALUES (27, 'darwin/dicots', 'Oak Population Genomics', 6387, NULL);
INSERT INTO public.project VALUES (44, 'tol/{}', 'Genomic diversity of oak (Quercus robur)', 6919, NULL);
INSERT INTO public.project VALUES (24, 'darwin/{}', 'DTOL_Darwin Tree of Life RNA', 6327, NULL);


--
-- Data for Name: allocation; Type: TABLE DATA; Schema: public; Owner: sts-dev
--

INSERT INTO public.allocation VALUES (115350, 17, 115350, NULL);
INSERT INTO public.allocation VALUES (115351, 17, 115351, NULL);
INSERT INTO public.allocation VALUES (115352, 17, 115352, NULL);
INSERT INTO public.allocation VALUES (115353, 17, 115353, NULL);
INSERT INTO public.allocation VALUES (115354, 17, 115354, NULL);
INSERT INTO public.allocation VALUES (115355, 17, 115355, NULL);
INSERT INTO public.allocation VALUES (115356, 17, 115356, NULL);
INSERT INTO public.allocation VALUES (115357, 17, 115357, NULL);
INSERT INTO public.allocation VALUES (115358, 17, 115358, NULL);
INSERT INTO public.allocation VALUES (115359, 17, 115359, NULL);
INSERT INTO public.allocation VALUES (115360, 17, 115360, NULL);
INSERT INTO public.allocation VALUES (115361, 17, 115361, NULL);
INSERT INTO public.allocation VALUES (115578, 17, 115578, NULL);
INSERT INTO public.allocation VALUES (115579, 17, 115579, NULL);
INSERT INTO public.allocation VALUES (115580, 17, 115580, NULL);
INSERT INTO public.allocation VALUES (115581, 17, 115581, NULL);
INSERT INTO public.allocation VALUES (115582, 17, 115582, NULL);
INSERT INTO public.allocation VALUES (115583, 17, 115583, NULL);
INSERT INTO public.allocation VALUES (115584, 17, 115584, NULL);
INSERT INTO public.allocation VALUES (115585, 17, 115585, NULL);
INSERT INTO public.allocation VALUES (115586, 17, 115586, NULL);
INSERT INTO public.allocation VALUES (115587, 17, 115587, NULL);
INSERT INTO public.allocation VALUES (115588, 17, 115588, NULL);
INSERT INTO public.allocation VALUES (115589, 17, 115589, NULL);
INSERT INTO public.allocation VALUES (115635, 17, 115635, NULL);
INSERT INTO public.allocation VALUES (115645, 17, 115645, NULL);
INSERT INTO public.allocation VALUES (115648, 17, 115648, NULL);
INSERT INTO public.allocation VALUES (115651, 17, 115651, NULL);
INSERT INTO public.allocation VALUES (115654, 17, 115654, NULL);
INSERT INTO public.allocation VALUES (115657, 17, 115657, NULL);
INSERT INTO public.allocation VALUES (115662, 17, 115662, NULL);
INSERT INTO public.allocation VALUES (115666, 17, 115666, NULL);
INSERT INTO public.allocation VALUES (115669, 17, 115669, NULL);
INSERT INTO public.allocation VALUES (115672, 17, 115672, NULL);
INSERT INTO public.allocation VALUES (115684, 17, 115684, NULL);
INSERT INTO public.allocation VALUES (115686, 17, 115686, NULL);
INSERT INTO public.allocation VALUES (115724, 17, 115724, NULL);
INSERT INTO public.allocation VALUES (115726, 17, 115726, NULL);
INSERT INTO public.allocation VALUES (115756, 17, 115756, NULL);
INSERT INTO public.allocation VALUES (115764, 17, 115764, NULL);
INSERT INTO public.allocation VALUES (115771, 17, 115771, NULL);
INSERT INTO public.allocation VALUES (115772, 17, 115772, NULL);
INSERT INTO public.allocation VALUES (115773, 17, 115773, NULL);
INSERT INTO public.allocation VALUES (115783, 17, 115783, NULL);
INSERT INTO public.allocation VALUES (115784, 17, 115784, NULL);
INSERT INTO public.allocation VALUES (115834, 17, 115834, NULL);
INSERT INTO public.allocation VALUES (115836, 17, 115836, NULL);
INSERT INTO public.allocation VALUES (115867, 17, 115867, NULL);
INSERT INTO public.allocation VALUES (115871, 17, 115871, NULL);
INSERT INTO public.allocation VALUES (115875, 17, 115875, NULL);
INSERT INTO public.allocation VALUES (115879, 17, 115879, NULL);
INSERT INTO public.allocation VALUES (115917, 17, 115917, NULL);
INSERT INTO public.allocation VALUES (115923, 17, 115923, NULL);
INSERT INTO public.allocation VALUES (115925, 17, 115925, NULL);
INSERT INTO public.allocation VALUES (118045, 21, 118045, NULL);
INSERT INTO public.allocation VALUES (118047, 21, 118047, NULL);
INSERT INTO public.allocation VALUES (118070, 21, 118070, NULL);
INSERT INTO public.allocation VALUES (118071, 21, 118071, NULL);
INSERT INTO public.allocation VALUES (118072, 21, 118072, NULL);
INSERT INTO public.allocation VALUES (118073, 21, 118073, NULL);
INSERT INTO public.allocation VALUES (118121, 21, 118121, NULL);
INSERT INTO public.allocation VALUES (118122, 21, 118122, NULL);
INSERT INTO public.allocation VALUES (120929, 21, 120929, NULL);
INSERT INTO public.allocation VALUES (128828, 27, 128828, NULL);
INSERT INTO public.allocation VALUES (128829, 27, 128829, NULL);
INSERT INTO public.allocation VALUES (128830, 27, 128830, NULL);
INSERT INTO public.allocation VALUES (128831, 27, 128831, NULL);
INSERT INTO public.allocation VALUES (128832, 27, 128832, NULL);
INSERT INTO public.allocation VALUES (128833, 27, 128833, NULL);
INSERT INTO public.allocation VALUES (128834, 27, 128834, NULL);
INSERT INTO public.allocation VALUES (128835, 27, 128835, NULL);
INSERT INTO public.allocation VALUES (128836, 27, 128836, NULL);
INSERT INTO public.allocation VALUES (128837, 27, 128837, NULL);
INSERT INTO public.allocation VALUES (128838, 27, 128838, NULL);
INSERT INTO public.allocation VALUES (128839, 27, 128839, NULL);
INSERT INTO public.allocation VALUES (128840, 27, 128840, NULL);
INSERT INTO public.allocation VALUES (128841, 27, 128841, NULL);
INSERT INTO public.allocation VALUES (128842, 27, 128842, NULL);
INSERT INTO public.allocation VALUES (128843, 27, 128843, NULL);
INSERT INTO public.allocation VALUES (128844, 27, 128844, NULL);
INSERT INTO public.allocation VALUES (128850, 27, 128850, NULL);
INSERT INTO public.allocation VALUES (128845, 27, 128845, NULL);
INSERT INTO public.allocation VALUES (128854, 27, 128854, NULL);
INSERT INTO public.allocation VALUES (128846, 27, 128846, NULL);
INSERT INTO public.allocation VALUES (128847, 27, 128847, NULL);
INSERT INTO public.allocation VALUES (128848, 27, 128848, NULL);
INSERT INTO public.allocation VALUES (128849, 27, 128849, NULL);
INSERT INTO public.allocation VALUES (128851, 27, 128851, NULL);
INSERT INTO public.allocation VALUES (128852, 27, 128852, NULL);
INSERT INTO public.allocation VALUES (128853, 27, 128853, NULL);
INSERT INTO public.allocation VALUES (128855, 27, 128855, NULL);
INSERT INTO public.allocation VALUES (134380, 17, 134379, NULL);
INSERT INTO public.allocation VALUES (134806, 17, 134805, NULL);
INSERT INTO public.allocation VALUES (131441, 44, 131441, NULL);
INSERT INTO public.allocation VALUES (127652, 24, 127652, NULL);
INSERT INTO public.allocation VALUES (131442, 44, 131442, NULL);
INSERT INTO public.allocation VALUES (131443, 44, 131443, NULL);
INSERT INTO public.allocation VALUES (131382, 44, 131382, NULL);
INSERT INTO public.allocation VALUES (131383, 44, 131383, NULL);
INSERT INTO public.allocation VALUES (131384, 44, 131384, NULL);
INSERT INTO public.allocation VALUES (131385, 44, 131385, NULL);
INSERT INTO public.allocation VALUES (131386, 44, 131386, NULL);
INSERT INTO public.allocation VALUES (131387, 44, 131387, NULL);
INSERT INTO public.allocation VALUES (131388, 44, 131388, NULL);
INSERT INTO public.allocation VALUES (131389, 44, 131389, NULL);
INSERT INTO public.allocation VALUES (131390, 44, 131390, NULL);
INSERT INTO public.allocation VALUES (131391, 44, 131391, NULL);
INSERT INTO public.allocation VALUES (131392, 44, 131392, NULL);
INSERT INTO public.allocation VALUES (131393, 44, 131393, NULL);
INSERT INTO public.allocation VALUES (131394, 44, 131394, NULL);
INSERT INTO public.allocation VALUES (131395, 44, 131395, NULL);
INSERT INTO public.allocation VALUES (131396, 44, 131396, NULL);
INSERT INTO public.allocation VALUES (131397, 44, 131397, NULL);
INSERT INTO public.allocation VALUES (131398, 44, 131398, NULL);
INSERT INTO public.allocation VALUES (131399, 44, 131399, NULL);
INSERT INTO public.allocation VALUES (131400, 44, 131400, NULL);
INSERT INTO public.allocation VALUES (131401, 44, 131401, NULL);
INSERT INTO public.allocation VALUES (131402, 44, 131402, NULL);
INSERT INTO public.allocation VALUES (131403, 44, 131403, NULL);
INSERT INTO public.allocation VALUES (131404, 44, 131404, NULL);
INSERT INTO public.allocation VALUES (131405, 44, 131405, NULL);
INSERT INTO public.allocation VALUES (131406, 44, 131406, NULL);
INSERT INTO public.allocation VALUES (131407, 44, 131407, NULL);
INSERT INTO public.allocation VALUES (131408, 44, 131408, NULL);
INSERT INTO public.allocation VALUES (131409, 44, 131409, NULL);
INSERT INTO public.allocation VALUES (131410, 44, 131410, NULL);
INSERT INTO public.allocation VALUES (131411, 44, 131411, NULL);
INSERT INTO public.allocation VALUES (131412, 44, 131412, NULL);
INSERT INTO public.allocation VALUES (131413, 44, 131413, NULL);
INSERT INTO public.allocation VALUES (131414, 44, 131414, NULL);
INSERT INTO public.allocation VALUES (131415, 44, 131415, NULL);
INSERT INTO public.allocation VALUES (131416, 44, 131416, NULL);
INSERT INTO public.allocation VALUES (131417, 44, 131417, NULL);
INSERT INTO public.allocation VALUES (131418, 44, 131418, NULL);
INSERT INTO public.allocation VALUES (131419, 44, 131419, NULL);
INSERT INTO public.allocation VALUES (131420, 44, 131420, NULL);
INSERT INTO public.allocation VALUES (131421, 44, 131421, NULL);
INSERT INTO public.allocation VALUES (131422, 44, 131422, NULL);
INSERT INTO public.allocation VALUES (131423, 44, 131423, NULL);
INSERT INTO public.allocation VALUES (131424, 44, 131424, NULL);
INSERT INTO public.allocation VALUES (131425, 44, 131425, NULL);
INSERT INTO public.allocation VALUES (131426, 44, 131426, NULL);
INSERT INTO public.allocation VALUES (131427, 44, 131427, NULL);
INSERT INTO public.allocation VALUES (131428, 44, 131428, NULL);
INSERT INTO public.allocation VALUES (131429, 44, 131429, NULL);
INSERT INTO public.allocation VALUES (131430, 44, 131430, NULL);
INSERT INTO public.allocation VALUES (131431, 44, 131431, NULL);
INSERT INTO public.allocation VALUES (131432, 44, 131432, NULL);
INSERT INTO public.allocation VALUES (131433, 44, 131433, NULL);
INSERT INTO public.allocation VALUES (131434, 44, 131434, NULL);
INSERT INTO public.allocation VALUES (131435, 44, 131435, NULL);
INSERT INTO public.allocation VALUES (131436, 44, 131436, NULL);
INSERT INTO public.allocation VALUES (131437, 44, 131437, NULL);
INSERT INTO public.allocation VALUES (131438, 44, 131438, NULL);
INSERT INTO public.allocation VALUES (131439, 44, 131439, NULL);
INSERT INTO public.allocation VALUES (131440, 44, 131440, NULL);
INSERT INTO public.allocation VALUES (131444, 44, 131444, NULL);
INSERT INTO public.allocation VALUES (131445, 44, 131445, NULL);
INSERT INTO public.allocation VALUES (131446, 44, 131446, NULL);
INSERT INTO public.allocation VALUES (131447, 44, 131447, NULL);
INSERT INTO public.allocation VALUES (131448, 44, 131448, NULL);
INSERT INTO public.allocation VALUES (131449, 44, 131449, NULL);
INSERT INTO public.allocation VALUES (131450, 44, 131450, NULL);
INSERT INTO public.allocation VALUES (131451, 44, 131451, NULL);
INSERT INTO public.allocation VALUES (131452, 44, 131452, NULL);
INSERT INTO public.allocation VALUES (115632, 17, 115632, NULL);
INSERT INTO public.allocation VALUES (117569, 21, 117569, NULL);
INSERT INTO public.allocation VALUES (117570, 21, 117570, NULL);
INSERT INTO public.allocation VALUES (117571, 21, 117571, NULL);
INSERT INTO public.allocation VALUES (117572, 21, 117572, NULL);
INSERT INTO public.allocation VALUES (115644, 17, 115644, NULL);
INSERT INTO public.allocation VALUES (115647, 17, 115647, NULL);
INSERT INTO public.allocation VALUES (115650, 17, 115650, NULL);
INSERT INTO public.allocation VALUES (115653, 17, 115653, NULL);
INSERT INTO public.allocation VALUES (115656, 17, 115656, NULL);
INSERT INTO public.allocation VALUES (115661, 17, 115661, NULL);
INSERT INTO public.allocation VALUES (115685, 17, 115685, NULL);
INSERT INTO public.allocation VALUES (115687, 17, 115687, NULL);
INSERT INTO public.allocation VALUES (115688, 17, 115688, NULL);
INSERT INTO public.allocation VALUES (115689, 17, 115689, NULL);
INSERT INTO public.allocation VALUES (115690, 17, 115690, NULL);
INSERT INTO public.allocation VALUES (115691, 17, 115691, NULL);
INSERT INTO public.allocation VALUES (115692, 17, 115692, NULL);
INSERT INTO public.allocation VALUES (115693, 17, 115693, NULL);
INSERT INTO public.allocation VALUES (115694, 17, 115694, NULL);
INSERT INTO public.allocation VALUES (115695, 17, 115695, NULL);
INSERT INTO public.allocation VALUES (115696, 17, 115696, NULL);
INSERT INTO public.allocation VALUES (115713, 17, 115713, NULL);
INSERT INTO public.allocation VALUES (115725, 17, 115725, NULL);
INSERT INTO public.allocation VALUES (115727, 17, 115727, NULL);
INSERT INTO public.allocation VALUES (115738, 17, 115738, NULL);
INSERT INTO public.allocation VALUES (115739, 17, 115739, NULL);
INSERT INTO public.allocation VALUES (115740, 17, 115740, NULL);
INSERT INTO public.allocation VALUES (115750, 17, 115750, NULL);
INSERT INTO public.allocation VALUES (115781, 17, 115781, NULL);
INSERT INTO public.allocation VALUES (115782, 17, 115782, NULL);
INSERT INTO public.allocation VALUES (115792, 17, 115792, NULL);
INSERT INTO public.allocation VALUES (115811, 17, 115811, NULL);
INSERT INTO public.allocation VALUES (115837, 17, 115837, NULL);
INSERT INTO public.allocation VALUES (115838, 17, 115838, NULL);
INSERT INTO public.allocation VALUES (115842, 17, 115842, NULL);
INSERT INTO public.allocation VALUES (115845, 17, 115845, NULL);
INSERT INTO public.allocation VALUES (115848, 17, 115848, NULL);
INSERT INTO public.allocation VALUES (115851, 17, 115851, NULL);
INSERT INTO public.allocation VALUES (115864, 17, 115864, NULL);
INSERT INTO public.allocation VALUES (115868, 17, 115868, NULL);
INSERT INTO public.allocation VALUES (115872, 17, 115872, NULL);
INSERT INTO public.allocation VALUES (115876, 17, 115876, NULL);
INSERT INTO public.allocation VALUES (115888, 17, 115888, NULL);
INSERT INTO public.allocation VALUES (115918, 17, 115918, NULL);
INSERT INTO public.allocation VALUES (115920, 17, 115920, NULL);
INSERT INTO public.allocation VALUES (115927, 17, 115927, NULL);
INSERT INTO public.allocation VALUES (115928, 17, 115928, NULL);
INSERT INTO public.allocation VALUES (115929, 17, 115929, NULL);
INSERT INTO public.allocation VALUES (115930, 17, 115930, NULL);
INSERT INTO public.allocation VALUES (120926, 21, 120926, NULL);
INSERT INTO public.allocation VALUES (120927, 21, 120927, NULL);
INSERT INTO public.allocation VALUES (134800, 17, 134799, NULL);
INSERT INTO public.allocation VALUES (120928, 21, 120928, NULL);
INSERT INTO public.allocation VALUES (127428, 24, 127428, NULL);
INSERT INTO public.allocation VALUES (133567, 17, 133566, NULL);
INSERT INTO public.allocation VALUES (133566, 17, 133565, NULL);
INSERT INTO public.allocation VALUES (134803, 17, 134802, NULL);
INSERT INTO public.allocation VALUES (134805, 17, 134804, NULL);
INSERT INTO public.allocation VALUES (136204, 17, 136203, NULL);
INSERT INTO public.allocation VALUES (136205, 17, 136204, NULL);
INSERT INTO public.allocation VALUES (136206, 17, 136205, NULL);
INSERT INTO public.allocation VALUES (136207, 17, 136206, NULL);
INSERT INTO public.allocation VALUES (136208, 17, 136207, NULL);
INSERT INTO public.allocation VALUES (136209, 17, 136208, NULL);
INSERT INTO public.allocation VALUES (136210, 17, 136209, NULL);
INSERT INTO public.allocation VALUES (136211, 17, 136210, NULL);
INSERT INTO public.allocation VALUES (136406, 17, 136405, NULL);
INSERT INTO public.allocation VALUES (136429, 17, 136428, NULL);
INSERT INTO public.allocation VALUES (136650, 17, 136649, NULL);
INSERT INTO public.allocation VALUES (136866, 17, 136865, NULL);
INSERT INTO public.allocation VALUES (115747, 17, 115747, NULL);
INSERT INTO public.allocation VALUES (115758, 17, 115758, NULL);
INSERT INTO public.allocation VALUES (115767, 17, 115767, NULL);
INSERT INTO public.allocation VALUES (115805, 17, 115805, NULL);
INSERT INTO public.allocation VALUES (134807, 17, 134806, NULL);
INSERT INTO public.allocation VALUES (115806, 17, 115806, NULL);
INSERT INTO public.allocation VALUES (134809, 17, 134808, NULL);
INSERT INTO public.allocation VALUES (115807, 17, 115807, NULL);
INSERT INTO public.allocation VALUES (115830, 17, 115830, NULL);
INSERT INTO public.allocation VALUES (118427, 21, 118427, NULL);
INSERT INTO public.allocation VALUES (118428, 21, 118428, NULL);
INSERT INTO public.allocation VALUES (118429, 21, 118429, NULL);
INSERT INTO public.allocation VALUES (118430, 21, 118430, NULL);
INSERT INTO public.allocation VALUES (121083, 21, 121083, NULL);
INSERT INTO public.allocation VALUES (124432, 21, 124432, NULL);
INSERT INTO public.allocation VALUES (127563, 24, 127563, NULL);


--
-- Data for Name: assembly_component_type; Type: TABLE DATA; Schema: public; Owner: sts-dev
--



--
-- Data for Name: dataset; Type: TABLE DATA; Schema: public; Owner: sts-dev
--



--
-- Data for Name: software_version; Type: TABLE DATA; Schema: public; Owner: sts-dev
--



--
-- Data for Name: assembly; Type: TABLE DATA; Schema: public; Owner: sts-dev
--



--
-- Data for Name: assembly_metrics; Type: TABLE DATA; Schema: public; Owner: sts-dev
--



--
-- Data for Name: assembly_source; Type: TABLE DATA; Schema: public; Owner: sts-dev
--



--
-- Data for Name: assembly_status_type; Type: TABLE DATA; Schema: public; Owner: sts-dev
--



--
-- Data for Name: assembly_status; Type: TABLE DATA; Schema: public; Owner: sts-dev
--



--
-- Data for Name: barcode_metrics; Type: TABLE DATA; Schema: public; Owner: sts-dev
--



--
-- Data for Name: busco_lineage; Type: TABLE DATA; Schema: public; Owner: sts-dev
--



--
-- Data for Name: busco_metrics; Type: TABLE DATA; Schema: public; Owner: sts-dev
--



--
-- Data for Name: contigviz_metrics; Type: TABLE DATA; Schema: public; Owner: sts-dev
--



--
-- Data for Name: dataset_element; Type: TABLE DATA; Schema: public; Owner: sts-dev
--



--
-- Data for Name: dataset_status_type; Type: TABLE DATA; Schema: public; Owner: sts-dev
--



--
-- Data for Name: dataset_status; Type: TABLE DATA; Schema: public; Owner: sts-dev
--



--
-- Data for Name: file; Type: TABLE DATA; Schema: public; Owner: sts-dev
--

INSERT INTO public.file VALUES (112099, 115350, NULL, NULL, '/seq/illumina/runs/34/34714/plex13/34714#13.cram', NULL, NULL);
INSERT INTO public.file VALUES (112100, 115351, NULL, NULL, '/seq/illumina/runs/34/34714/plex14/34714#14.cram', NULL, NULL);
INSERT INTO public.file VALUES (112101, 115352, NULL, NULL, '/seq/illumina/runs/34/34714/plex15/34714#15.cram', NULL, NULL);
INSERT INTO public.file VALUES (112102, 115353, NULL, NULL, '/seq/illumina/runs/34/34714/plex16/34714#16.cram', NULL, NULL);
INSERT INTO public.file VALUES (112103, 115354, NULL, NULL, '/seq/illumina/runs/34/34714/plex17/34714#17.cram', NULL, NULL);
INSERT INTO public.file VALUES (112104, 115355, NULL, NULL, '/seq/illumina/runs/34/34714/plex18/34714#18.cram', NULL, NULL);
INSERT INTO public.file VALUES (112105, 115356, NULL, NULL, '/seq/illumina/runs/34/34714/plex19/34714#19.cram', NULL, NULL);
INSERT INTO public.file VALUES (112106, 115357, NULL, NULL, '/seq/illumina/runs/34/34714/plex20/34714#20.cram', NULL, NULL);
INSERT INTO public.file VALUES (112107, 115358, NULL, NULL, '/seq/illumina/runs/34/34714/plex21/34714#21.cram', NULL, NULL);
INSERT INTO public.file VALUES (112108, 115359, NULL, NULL, '/seq/illumina/runs/34/34714/plex22/34714#22.cram', NULL, NULL);
INSERT INTO public.file VALUES (112109, 115360, NULL, NULL, '/seq/illumina/runs/34/34714/plex23/34714#23.cram', NULL, NULL);
INSERT INTO public.file VALUES (112110, 115361, NULL, NULL, '/seq/illumina/runs/34/34714/plex24/34714#24.cram', NULL, NULL);
INSERT INTO public.file VALUES (112327, 115578, NULL, NULL, '/seq/illumina/runs/34/34781/lane2/plex73/34781_2#73.cram', NULL, NULL);
INSERT INTO public.file VALUES (112328, 115579, NULL, NULL, '/seq/illumina/runs/34/34781/lane2/plex74/34781_2#74.cram', NULL, NULL);
INSERT INTO public.file VALUES (112329, 115580, NULL, NULL, '/seq/illumina/runs/34/34781/lane2/plex75/34781_2#75.cram', NULL, NULL);
INSERT INTO public.file VALUES (112330, 115581, NULL, NULL, '/seq/illumina/runs/34/34781/lane2/plex76/34781_2#76.cram', NULL, NULL);
INSERT INTO public.file VALUES (112331, 115582, NULL, NULL, '/seq/illumina/runs/34/34781/lane2/plex77/34781_2#77.cram', NULL, NULL);
INSERT INTO public.file VALUES (112332, 115583, NULL, NULL, '/seq/illumina/runs/34/34781/lane2/plex78/34781_2#78.cram', NULL, NULL);
INSERT INTO public.file VALUES (112333, 115584, NULL, NULL, '/seq/illumina/runs/34/34781/lane2/plex79/34781_2#79.cram', NULL, NULL);
INSERT INTO public.file VALUES (112334, 115585, NULL, NULL, '/seq/illumina/runs/34/34781/lane2/plex80/34781_2#80.cram', NULL, NULL);
INSERT INTO public.file VALUES (112335, 115586, NULL, NULL, '/seq/illumina/runs/34/34781/lane2/plex81/34781_2#81.cram', NULL, NULL);
INSERT INTO public.file VALUES (112336, 115587, NULL, NULL, '/seq/illumina/runs/34/34781/lane2/plex82/34781_2#82.cram', NULL, NULL);
INSERT INTO public.file VALUES (112337, 115588, NULL, NULL, '/seq/illumina/runs/34/34781/lane2/plex83/34781_2#83.cram', NULL, NULL);
INSERT INTO public.file VALUES (112338, 115589, NULL, NULL, '/seq/illumina/runs/34/34781/lane2/plex84/34781_2#84.cram', NULL, NULL);
INSERT INTO public.file VALUES (112384, 115635, NULL, NULL, '/seq/illumina/runs/37/37940/lane1/plex1/37940_1#1.cram', NULL, NULL);
INSERT INTO public.file VALUES (112394, 115645, NULL, NULL, '/seq/illumina/runs/41/41302/lane1/plex2/41302_1#2.cram', NULL, NULL);
INSERT INTO public.file VALUES (112397, 115648, NULL, NULL, '/seq/illumina/runs/41/41302/lane2/plex2/41302_2#2.cram', NULL, NULL);
INSERT INTO public.file VALUES (112400, 115651, NULL, NULL, '/seq/illumina/runs/41/41305/lane1/plex2/41305_1#2.cram', NULL, NULL);
INSERT INTO public.file VALUES (112403, 115654, NULL, NULL, '/seq/illumina/runs/41/41305/lane2/plex2/41305_2#2.cram', NULL, NULL);
INSERT INTO public.file VALUES (112406, 115657, NULL, NULL, '/seq/illumina/runs/41/41306/plex2/41306#2.cram', NULL, NULL);
INSERT INTO public.file VALUES (112411, 115662, NULL, NULL, '/seq/illumina/runs/43/43500/lane1/plex2/43500_1#2.cram', NULL, NULL);
INSERT INTO public.file VALUES (112415, 115666, NULL, NULL, '/seq/illumina/runs/45/45763/lane1/plex1/45763_1#1.cram', NULL, NULL);
INSERT INTO public.file VALUES (112418, 115669, NULL, NULL, '/seq/illumina/runs/45/45763/lane2/plex1/45763_2#1.cram', NULL, NULL);
INSERT INTO public.file VALUES (112421, 115672, NULL, NULL, '/seq/illumina/runs/45/45763/lane2/plex4/45763_2#4.cram', NULL, NULL);
INSERT INTO public.file VALUES (112433, 115684, NULL, NULL, '/seq/illumina/runs/46/46644/lane1/plex74/46644_1#74.cram', NULL, NULL);
INSERT INTO public.file VALUES (112435, 115686, NULL, NULL, '/seq/illumina/runs/46/46644/lane1/plex76/46644_1#76.cram', NULL, NULL);
INSERT INTO public.file VALUES (112472, 115724, NULL, NULL, '/seq/pacbio/r64228e_20210909_144906/4_D01/demultiplex.bc1011_BAK8A_OA--bc1011_BAK8A_OA.bam', NULL, NULL);
INSERT INTO public.file VALUES (112474, 115726, NULL, NULL, '/seq/pacbio/r64228e_20210909_144906/3_C01/demultiplex.bc1011_BAK8A_OA--bc1011_BAK8A_OA.bam', NULL, NULL);
INSERT INTO public.file VALUES (112497, 115756, NULL, NULL, '/seq/pacbio/r64178e_20211103_180723/2_B01/demultiplex.bc1017_BAK8B_OA--bc1017_BAK8B_OA.bam', NULL, NULL);
INSERT INTO public.file VALUES (112505, 115764, NULL, NULL, '/seq/pacbio/r64094e_20211103_151814/3_C01/demultiplex.bc1001_BAK8A_OA--bc1001_BAK8A_OA.bam', NULL, NULL);
INSERT INTO public.file VALUES (112512, 115771, NULL, NULL, '/seq/pacbio/r64228e_20211105_101524/1_A01/m64228e_211105_115646.hifi_reads.bam', NULL, NULL);
INSERT INTO public.file VALUES (112513, 115772, NULL, NULL, '/seq/pacbio/r64228e_20211105_101524/2_B01/m64228e_211106_225141.hifi_reads.bam', NULL, NULL);
INSERT INTO public.file VALUES (112514, 115773, NULL, NULL, '/seq/pacbio/r64228e_20211105_101524/3_C01/m64228e_211108_094826.hifi_reads.bam', NULL, NULL);
INSERT INTO public.file VALUES (112524, 115783, NULL, NULL, '/seq/pacbio/r64178e_20211112_181830/3_C01/demultiplex.bc1008_BAK8A_OA--bc1008_BAK8A_OA.bam', NULL, NULL);
INSERT INTO public.file VALUES (112525, 115784, NULL, NULL, '/seq/pacbio/r64178e_20211112_181830/4_D01/demultiplex.bc1012_BAK8A_OA--bc1012_BAK8A_OA.bam', NULL, NULL);
INSERT INTO public.file VALUES (112575, 115834, NULL, NULL, '/seq/pacbio/r64230e_20220420_151101/3_C01/demultiplex.bc1018_BAK8B_OA--bc1018_BAK8B_OA.bam', NULL, NULL);
INSERT INTO public.file VALUES (112577, 115836, NULL, NULL, '/seq/pacbio/r64230e_20220420_151101/4_D01/demultiplex.bc1018_BAK8B_OA--bc1018_BAK8B_OA.bam', NULL, NULL);
INSERT INTO public.file VALUES (112608, 115867, NULL, NULL, '/seq/pacbio/r64089e_20220922_153656/1_A01/m64089e_220922_160600.hifi_reads.bc1020_BAK8B_OA--bc1020_BAK8B_OA.bam', NULL, NULL);
INSERT INTO public.file VALUES (112612, 115871, NULL, NULL, '/seq/pacbio/r64089e_20220922_153656/2_B01/m64089e_220923_210112.hifi_reads.bc1020_BAK8B_OA--bc1020_BAK8B_OA.bam', NULL, NULL);
INSERT INTO public.file VALUES (112616, 115875, NULL, NULL, '/seq/pacbio/r64089e_20220922_153656/3_C01/m64089e_220925_015808.hifi_reads.bc1020_BAK8B_OA--bc1020_BAK8B_OA.bam', NULL, NULL);
INSERT INTO public.file VALUES (112620, 115879, NULL, NULL, '/seq/pacbio/r64089e_20220922_153656/4_D01/m64089e_220926_065548.hifi_reads.bc1020_BAK8B_OA--bc1020_BAK8B_OA.bam', NULL, NULL);
INSERT INTO public.file VALUES (112658, 115917, NULL, NULL, '/seq/pacbio/r84047_20230425_112441/1_D01/m84047_230425_130728_s4.hifi_reads.bc2004.bam', NULL, NULL);
INSERT INTO public.file VALUES (112664, 115923, NULL, NULL, '/seq/pacbio/r84047_20230505_145319/1_A01/m84047_230505_155651_s1.hifi_reads.bc2004.bam', NULL, NULL);
INSERT INTO public.file VALUES (112666, 115925, NULL, NULL, '/seq/pacbio/r84047_20230517_171143/1_B01/m84047_230517_174928_s2.hifi_reads.bc2004.bam', NULL, NULL);
INSERT INTO public.file VALUES (114782, 118045, NULL, NULL, '/seq/35874/35874_7#2.cram', NULL, NULL);
INSERT INTO public.file VALUES (114784, 118047, NULL, NULL, '/seq/35874/35874_8#2.cram', NULL, NULL);
INSERT INTO public.file VALUES (114807, 118070, NULL, NULL, '/seq/illumina/runs/35/35990/lane2/plex9/35990_2#9.cram', NULL, NULL);
INSERT INTO public.file VALUES (114808, 118071, NULL, NULL, '/seq/illumina/runs/35/35990/lane2/plex10/35990_2#10.cram', NULL, NULL);
INSERT INTO public.file VALUES (114809, 118072, NULL, NULL, '/seq/illumina/runs/35/35990/lane2/plex11/35990_2#11.cram', NULL, NULL);
INSERT INTO public.file VALUES (114810, 118073, NULL, NULL, '/seq/illumina/runs/35/35990/lane2/plex12/35990_2#12.cram', NULL, NULL);
INSERT INTO public.file VALUES (114858, 118121, NULL, NULL, '/seq/35874/35874_7#3.cram', NULL, NULL);
INSERT INTO public.file VALUES (114859, 118122, NULL, NULL, '/seq/35874/35874_8#3.cram', NULL, NULL);
INSERT INTO public.file VALUES (117666, 120929, NULL, NULL, '/seq/illumina/runs/40/40280/plex4/40280#4.cram', NULL, NULL);
INSERT INTO public.file VALUES (125327, 128828, NULL, NULL, '/seq/illumina/runs/37/37363/lane2/plex1/37363_2#1.cram', NULL, NULL);
INSERT INTO public.file VALUES (125328, 128829, NULL, NULL, '/seq/illumina/runs/37/37363/lane2/plex2/37363_2#2.cram', NULL, NULL);
INSERT INTO public.file VALUES (125329, 128830, NULL, NULL, '/seq/illumina/runs/37/37363/lane2/plex3/37363_2#3.cram', NULL, NULL);
INSERT INTO public.file VALUES (125330, 128831, NULL, NULL, '/seq/illumina/runs/37/37363/lane2/plex4/37363_2#4.cram', NULL, NULL);
INSERT INTO public.file VALUES (125331, 128832, NULL, NULL, '/seq/illumina/runs/37/37363/lane2/plex5/37363_2#5.cram', NULL, NULL);
INSERT INTO public.file VALUES (125332, 128833, NULL, NULL, '/seq/illumina/runs/37/37363/lane2/plex6/37363_2#6.cram', NULL, NULL);
INSERT INTO public.file VALUES (125333, 128834, NULL, NULL, '/seq/illumina/runs/37/37363/lane2/plex7/37363_2#7.cram', NULL, NULL);
INSERT INTO public.file VALUES (125334, 128835, NULL, NULL, '/seq/illumina/runs/37/37363/lane2/plex8/37363_2#8.cram', NULL, NULL);
INSERT INTO public.file VALUES (125335, 128836, NULL, NULL, '/seq/illumina/runs/37/37363/lane2/plex9/37363_2#9.cram', NULL, NULL);
INSERT INTO public.file VALUES (125336, 128837, NULL, NULL, '/seq/illumina/runs/37/37363/lane2/plex10/37363_2#10.cram', NULL, NULL);
INSERT INTO public.file VALUES (125337, 128838, NULL, NULL, '/seq/illumina/runs/37/37363/lane2/plex11/37363_2#11.cram', NULL, NULL);
INSERT INTO public.file VALUES (125338, 128839, NULL, NULL, '/seq/illumina/runs/37/37363/lane2/plex12/37363_2#12.cram', NULL, NULL);
INSERT INTO public.file VALUES (125339, 128840, NULL, NULL, '/seq/illumina/runs/37/37363/lane2/plex13/37363_2#13.cram', NULL, NULL);
INSERT INTO public.file VALUES (125340, 128841, NULL, NULL, '/seq/illumina/runs/37/37363/lane2/plex14/37363_2#14.cram', NULL, NULL);
INSERT INTO public.file VALUES (125341, 128842, NULL, NULL, '/seq/illumina/runs/37/37363/lane2/plex15/37363_2#15.cram', NULL, NULL);
INSERT INTO public.file VALUES (125342, 128843, NULL, NULL, '/seq/pacbio/r64230e_20210702_173842/3_C01/demultiplex.bc1020_BAK8B_OA--bc1020_BAK8B_OA.bam', NULL, NULL);
INSERT INTO public.file VALUES (125343, 128844, NULL, NULL, '/seq/pacbio/r64097e_20210617_140634/1_A01/demultiplex.bc1010_BAK8A_OA--bc1010_BAK8A_OA.bam', NULL, NULL);
INSERT INTO public.file VALUES (125349, 128850, NULL, NULL, '/seq/pacbio/r64094e_20210430_114544/1_A01/demultiplex.bc1010_BAK8A_OA--bc1010_BAK8A_OA.bam', NULL, NULL);
INSERT INTO public.file VALUES (125344, 128845, NULL, NULL, '/seq/pacbio/r64097e_20210617_140634/4_D01/demultiplex.bc1001_BAK8A_OA--bc1001_BAK8A_OA.bam', NULL, NULL);
INSERT INTO public.file VALUES (125353, 128854, NULL, NULL, '/seq/pacbio/r64097e_20210422_140606/3_C01/demultiplex.bc1001_BAK8A_OA--bc1001_BAK8A_OA.bam', NULL, NULL);
INSERT INTO public.file VALUES (125345, 128846, NULL, NULL, '/seq/pacbio/r64097e_20210507_151625/2_B01/demultiplex.bc1003_BAK8A_OA--bc1003_BAK8A_OA.bam', NULL, NULL);
INSERT INTO public.file VALUES (125346, 128847, NULL, NULL, '/seq/pacbio/r64174e_20210430_133442/2_B01/demultiplex.bc1003_BAK8A_OA--bc1003_BAK8A_OA.bam', NULL, NULL);
INSERT INTO public.file VALUES (125347, 128848, NULL, NULL, '/seq/pacbio/r64174e_20210430_133442/3_C01/demultiplex.bc1008_BAK8A_OA--bc1008_BAK8A_OA.bam', NULL, NULL);
INSERT INTO public.file VALUES (125348, 128849, NULL, NULL, '/seq/pacbio/r64174e_20210430_133442/4_D01/demultiplex.bc1009_BAK8A_OA--bc1009_BAK8A_OA.bam', NULL, NULL);
INSERT INTO public.file VALUES (125350, 128851, NULL, NULL, '/seq/pacbio/r64094e_20210430_114544/2_B01/demultiplex.bc1011_BAK8A_OA--bc1011_BAK8A_OA.bam', NULL, NULL);
INSERT INTO public.file VALUES (125351, 128852, NULL, NULL, '/seq/pacbio/r64094e_20210430_114544/3_C01/demultiplex.bc1012_BAK8A_OA--bc1012_BAK8A_OA.bam', NULL, NULL);
INSERT INTO public.file VALUES (125352, 128853, NULL, NULL, '/seq/pacbio/r64094e_20210430_114544/4_D01/demultiplex.bc1015_BAK8B_OA--bc1015_BAK8B_OA.bam', NULL, NULL);
INSERT INTO public.file VALUES (125354, 128855, NULL, NULL, '/seq/pacbio/r64097e_20210422_140606/3_C01/demultiplex.bc1002_BAK8A_OA--bc1002_BAK8A_OA.bam', NULL, NULL);
INSERT INTO public.file VALUES (130867, 134379, NULL, NULL, '/seq/pacbio/r64221e_20230913_151208/1_A01/demultiplex.bc2021--bc2021.bam', NULL, NULL);
INSERT INTO public.file VALUES (131292, 134805, NULL, NULL, '/seq/pacbio/r64230e_20220218_135813/2_B01/demultiplex.bc1020T--bc1020T.bam', NULL, NULL);
INSERT INTO public.file VALUES (127866, 131441, NULL, NULL, '/seq/illumina/runs/45/45733/plex60/45733#60.cram', NULL, NULL);
INSERT INTO public.file VALUES (124169, 127652, NULL, NULL, '/seq/44268/44268_5#3.cram', NULL, NULL);
INSERT INTO public.file VALUES (127867, 131442, NULL, NULL, '/seq/illumina/runs/45/45733/plex61/45733#61.cram', NULL, NULL);
INSERT INTO public.file VALUES (127868, 131443, NULL, NULL, '/seq/illumina/runs/45/45733/plex62/45733#62.cram', NULL, NULL);
INSERT INTO public.file VALUES (127807, 131382, NULL, NULL, '/seq/illumina/runs/45/45733/plex1/45733#1.cram', NULL, NULL);
INSERT INTO public.file VALUES (127808, 131383, NULL, NULL, '/seq/illumina/runs/45/45733/plex2/45733#2.cram', NULL, NULL);
INSERT INTO public.file VALUES (127809, 131384, NULL, NULL, '/seq/illumina/runs/45/45733/plex3/45733#3.cram', NULL, NULL);
INSERT INTO public.file VALUES (127810, 131385, NULL, NULL, '/seq/illumina/runs/45/45733/plex4/45733#4.cram', NULL, NULL);
INSERT INTO public.file VALUES (127811, 131386, NULL, NULL, '/seq/illumina/runs/45/45733/plex5/45733#5.cram', NULL, NULL);
INSERT INTO public.file VALUES (127812, 131387, NULL, NULL, '/seq/illumina/runs/45/45733/plex6/45733#6.cram', NULL, NULL);
INSERT INTO public.file VALUES (127813, 131388, NULL, NULL, '/seq/illumina/runs/45/45733/plex7/45733#7.cram', NULL, NULL);
INSERT INTO public.file VALUES (127814, 131389, NULL, NULL, '/seq/illumina/runs/45/45733/plex8/45733#8.cram', NULL, NULL);
INSERT INTO public.file VALUES (127815, 131390, NULL, NULL, '/seq/illumina/runs/45/45733/plex9/45733#9.cram', NULL, NULL);
INSERT INTO public.file VALUES (127816, 131391, NULL, NULL, '/seq/illumina/runs/45/45733/plex10/45733#10.cram', NULL, NULL);
INSERT INTO public.file VALUES (127817, 131392, NULL, NULL, '/seq/illumina/runs/45/45733/plex11/45733#11.cram', NULL, NULL);
INSERT INTO public.file VALUES (127818, 131393, NULL, NULL, '/seq/illumina/runs/45/45733/plex12/45733#12.cram', NULL, NULL);
INSERT INTO public.file VALUES (127819, 131394, NULL, NULL, '/seq/illumina/runs/45/45733/plex13/45733#13.cram', NULL, NULL);
INSERT INTO public.file VALUES (127820, 131395, NULL, NULL, '/seq/illumina/runs/45/45733/plex14/45733#14.cram', NULL, NULL);
INSERT INTO public.file VALUES (127821, 131396, NULL, NULL, '/seq/illumina/runs/45/45733/plex15/45733#15.cram', NULL, NULL);
INSERT INTO public.file VALUES (127822, 131397, NULL, NULL, '/seq/illumina/runs/45/45733/plex16/45733#16.cram', NULL, NULL);
INSERT INTO public.file VALUES (127823, 131398, NULL, NULL, '/seq/illumina/runs/45/45733/plex17/45733#17.cram', NULL, NULL);
INSERT INTO public.file VALUES (127824, 131399, NULL, NULL, '/seq/illumina/runs/45/45733/plex18/45733#18.cram', NULL, NULL);
INSERT INTO public.file VALUES (127825, 131400, NULL, NULL, '/seq/illumina/runs/45/45733/plex19/45733#19.cram', NULL, NULL);
INSERT INTO public.file VALUES (127826, 131401, NULL, NULL, '/seq/illumina/runs/45/45733/plex20/45733#20.cram', NULL, NULL);
INSERT INTO public.file VALUES (127827, 131402, NULL, NULL, '/seq/illumina/runs/45/45733/plex21/45733#21.cram', NULL, NULL);
INSERT INTO public.file VALUES (127828, 131403, NULL, NULL, '/seq/illumina/runs/45/45733/plex22/45733#22.cram', NULL, NULL);
INSERT INTO public.file VALUES (127829, 131404, NULL, NULL, '/seq/illumina/runs/45/45733/plex23/45733#23.cram', NULL, NULL);
INSERT INTO public.file VALUES (127830, 131405, NULL, NULL, '/seq/illumina/runs/45/45733/plex24/45733#24.cram', NULL, NULL);
INSERT INTO public.file VALUES (127831, 131406, NULL, NULL, '/seq/illumina/runs/45/45733/plex25/45733#25.cram', NULL, NULL);
INSERT INTO public.file VALUES (127832, 131407, NULL, NULL, '/seq/illumina/runs/45/45733/plex26/45733#26.cram', NULL, NULL);
INSERT INTO public.file VALUES (127833, 131408, NULL, NULL, '/seq/illumina/runs/45/45733/plex27/45733#27.cram', NULL, NULL);
INSERT INTO public.file VALUES (127834, 131409, NULL, NULL, '/seq/illumina/runs/45/45733/plex28/45733#28.cram', NULL, NULL);
INSERT INTO public.file VALUES (127835, 131410, NULL, NULL, '/seq/illumina/runs/45/45733/plex29/45733#29.cram', NULL, NULL);
INSERT INTO public.file VALUES (127836, 131411, NULL, NULL, '/seq/illumina/runs/45/45733/plex30/45733#30.cram', NULL, NULL);
INSERT INTO public.file VALUES (127837, 131412, NULL, NULL, '/seq/illumina/runs/45/45733/plex31/45733#31.cram', NULL, NULL);
INSERT INTO public.file VALUES (127838, 131413, NULL, NULL, '/seq/illumina/runs/45/45733/plex32/45733#32.cram', NULL, NULL);
INSERT INTO public.file VALUES (127839, 131414, NULL, NULL, '/seq/illumina/runs/45/45733/plex33/45733#33.cram', NULL, NULL);
INSERT INTO public.file VALUES (127840, 131415, NULL, NULL, '/seq/illumina/runs/45/45733/plex34/45733#34.cram', NULL, NULL);
INSERT INTO public.file VALUES (127841, 131416, NULL, NULL, '/seq/illumina/runs/45/45733/plex35/45733#35.cram', NULL, NULL);
INSERT INTO public.file VALUES (127842, 131417, NULL, NULL, '/seq/illumina/runs/45/45733/plex36/45733#36.cram', NULL, NULL);
INSERT INTO public.file VALUES (127843, 131418, NULL, NULL, '/seq/illumina/runs/45/45733/plex37/45733#37.cram', NULL, NULL);
INSERT INTO public.file VALUES (127844, 131419, NULL, NULL, '/seq/illumina/runs/45/45733/plex38/45733#38.cram', NULL, NULL);
INSERT INTO public.file VALUES (127845, 131420, NULL, NULL, '/seq/illumina/runs/45/45733/plex39/45733#39.cram', NULL, NULL);
INSERT INTO public.file VALUES (127846, 131421, NULL, NULL, '/seq/illumina/runs/45/45733/plex40/45733#40.cram', NULL, NULL);
INSERT INTO public.file VALUES (127847, 131422, NULL, NULL, '/seq/illumina/runs/45/45733/plex41/45733#41.cram', NULL, NULL);
INSERT INTO public.file VALUES (127848, 131423, NULL, NULL, '/seq/illumina/runs/45/45733/plex42/45733#42.cram', NULL, NULL);
INSERT INTO public.file VALUES (127849, 131424, NULL, NULL, '/seq/illumina/runs/45/45733/plex43/45733#43.cram', NULL, NULL);
INSERT INTO public.file VALUES (127850, 131425, NULL, NULL, '/seq/illumina/runs/45/45733/plex44/45733#44.cram', NULL, NULL);
INSERT INTO public.file VALUES (127851, 131426, NULL, NULL, '/seq/illumina/runs/45/45733/plex45/45733#45.cram', NULL, NULL);
INSERT INTO public.file VALUES (127852, 131427, NULL, NULL, '/seq/illumina/runs/45/45733/plex46/45733#46.cram', NULL, NULL);
INSERT INTO public.file VALUES (127853, 131428, NULL, NULL, '/seq/illumina/runs/45/45733/plex47/45733#47.cram', NULL, NULL);
INSERT INTO public.file VALUES (127854, 131429, NULL, NULL, '/seq/illumina/runs/45/45733/plex48/45733#48.cram', NULL, NULL);
INSERT INTO public.file VALUES (127855, 131430, NULL, NULL, '/seq/illumina/runs/45/45733/plex49/45733#49.cram', NULL, NULL);
INSERT INTO public.file VALUES (127856, 131431, NULL, NULL, '/seq/illumina/runs/45/45733/plex50/45733#50.cram', NULL, NULL);
INSERT INTO public.file VALUES (127857, 131432, NULL, NULL, '/seq/illumina/runs/45/45733/plex51/45733#51.cram', NULL, NULL);
INSERT INTO public.file VALUES (127858, 131433, NULL, NULL, '/seq/illumina/runs/45/45733/plex52/45733#52.cram', NULL, NULL);
INSERT INTO public.file VALUES (127859, 131434, NULL, NULL, '/seq/illumina/runs/45/45733/plex53/45733#53.cram', NULL, NULL);
INSERT INTO public.file VALUES (127860, 131435, NULL, NULL, '/seq/illumina/runs/45/45733/plex54/45733#54.cram', NULL, NULL);
INSERT INTO public.file VALUES (127861, 131436, NULL, NULL, '/seq/illumina/runs/45/45733/plex55/45733#55.cram', NULL, NULL);
INSERT INTO public.file VALUES (127862, 131437, NULL, NULL, '/seq/illumina/runs/45/45733/plex56/45733#56.cram', NULL, NULL);
INSERT INTO public.file VALUES (127863, 131438, NULL, NULL, '/seq/illumina/runs/45/45733/plex57/45733#57.cram', NULL, NULL);
INSERT INTO public.file VALUES (127864, 131439, NULL, NULL, '/seq/illumina/runs/45/45733/plex58/45733#58.cram', NULL, NULL);
INSERT INTO public.file VALUES (127865, 131440, NULL, NULL, '/seq/illumina/runs/45/45733/plex59/45733#59.cram', NULL, NULL);
INSERT INTO public.file VALUES (127869, 131444, NULL, NULL, '/seq/illumina/runs/45/45733/plex63/45733#63.cram', NULL, NULL);
INSERT INTO public.file VALUES (127870, 131445, NULL, NULL, '/seq/illumina/runs/45/45733/plex64/45733#64.cram', NULL, NULL);
INSERT INTO public.file VALUES (127871, 131446, NULL, NULL, '/seq/illumina/runs/45/45733/plex65/45733#65.cram', NULL, NULL);
INSERT INTO public.file VALUES (127872, 131447, NULL, NULL, '/seq/illumina/runs/45/45733/plex66/45733#66.cram', NULL, NULL);
INSERT INTO public.file VALUES (127873, 131448, NULL, NULL, '/seq/illumina/runs/45/45733/plex67/45733#67.cram', NULL, NULL);
INSERT INTO public.file VALUES (127874, 131449, NULL, NULL, '/seq/illumina/runs/45/45733/plex68/45733#68.cram', NULL, NULL);
INSERT INTO public.file VALUES (127875, 131450, NULL, NULL, '/seq/illumina/runs/45/45733/plex69/45733#69.cram', NULL, NULL);
INSERT INTO public.file VALUES (127876, 131451, NULL, NULL, '/seq/illumina/runs/45/45733/plex70/45733#70.cram', NULL, NULL);
INSERT INTO public.file VALUES (127877, 131452, NULL, NULL, '/seq/illumina/runs/45/45733/plex71/45733#71.cram', NULL, NULL);
INSERT INTO public.file VALUES (112381, 115632, NULL, NULL, '/seq/illumina/runs/37/37939/lane1/plex3/37939_1#3.cram', NULL, NULL);
INSERT INTO public.file VALUES (114306, 117569, NULL, NULL, '/seq/35281/35281_2#1.cram', NULL, NULL);
INSERT INTO public.file VALUES (114307, 117570, NULL, NULL, '/seq/35281/35281_2#2.cram', NULL, NULL);
INSERT INTO public.file VALUES (114308, 117571, NULL, NULL, '/seq/35281/35281_2#3.cram', NULL, NULL);
INSERT INTO public.file VALUES (114309, 117572, NULL, NULL, '/seq/35281/35281_2#4.cram', NULL, NULL);
INSERT INTO public.file VALUES (112393, 115644, NULL, NULL, '/seq/illumina/runs/41/41302/lane1/plex1/41302_1#1.cram', NULL, NULL);
INSERT INTO public.file VALUES (112396, 115647, NULL, NULL, '/seq/illumina/runs/41/41302/lane2/plex1/41302_2#1.cram', NULL, NULL);
INSERT INTO public.file VALUES (112399, 115650, NULL, NULL, '/seq/illumina/runs/41/41305/lane1/plex1/41305_1#1.cram', NULL, NULL);
INSERT INTO public.file VALUES (112402, 115653, NULL, NULL, '/seq/illumina/runs/41/41305/lane2/plex1/41305_2#1.cram', NULL, NULL);
INSERT INTO public.file VALUES (112405, 115656, NULL, NULL, '/seq/illumina/runs/41/41306/plex1/41306#1.cram', NULL, NULL);
INSERT INTO public.file VALUES (112410, 115661, NULL, NULL, '/seq/illumina/runs/43/43500/lane1/plex1/43500_1#1.cram', NULL, NULL);
INSERT INTO public.file VALUES (112434, 115685, NULL, NULL, '/seq/illumina/runs/46/46644/lane1/plex75/46644_1#75.cram', NULL, NULL);
INSERT INTO public.file VALUES (112436, 115687, NULL, NULL, '/seq/illumina/runs/46/46644/lane1/plex77/46644_1#77.cram', NULL, NULL);
INSERT INTO public.file VALUES (112437, 115688, NULL, NULL, '/seq/illumina/runs/46/46644/lane1/plex78/46644_1#78.cram', NULL, NULL);
INSERT INTO public.file VALUES (112438, 115689, NULL, NULL, '/seq/illumina/runs/46/46644/lane1/plex79/46644_1#79.cram', NULL, NULL);
INSERT INTO public.file VALUES (112439, 115690, NULL, NULL, '/seq/illumina/runs/46/46644/lane1/plex80/46644_1#80.cram', NULL, NULL);
INSERT INTO public.file VALUES (112440, 115691, NULL, NULL, '/seq/illumina/runs/46/46644/lane1/plex81/46644_1#81.cram', NULL, NULL);
INSERT INTO public.file VALUES (112441, 115692, NULL, NULL, '/seq/illumina/runs/46/46644/lane1/plex82/46644_1#82.cram', NULL, NULL);
INSERT INTO public.file VALUES (112442, 115693, NULL, NULL, '/seq/illumina/runs/46/46644/lane1/plex83/46644_1#83.cram', NULL, NULL);
INSERT INTO public.file VALUES (112443, 115694, NULL, NULL, '/seq/illumina/runs/46/46644/lane1/plex84/46644_1#84.cram', NULL, NULL);
INSERT INTO public.file VALUES (112444, 115695, NULL, NULL, '/seq/illumina/runs/46/46644/lane1/plex85/46644_1#85.cram', NULL, NULL);
INSERT INTO public.file VALUES (112445, 115696, NULL, NULL, '/seq/illumina/runs/46/46644/lane1/plex86/46644_1#86.cram', NULL, NULL);
INSERT INTO public.file VALUES (112462, 115713, NULL, NULL, '/seq/pacbio/r64174e_20210128_140447/3_C01/demultiplex.bc1015_BAK8B_OA--bc1015_BAK8B_OA.bam', NULL, NULL);
INSERT INTO public.file VALUES (112473, 115725, NULL, NULL, '/seq/pacbio/r64228e_20210909_144906/1_A01/demultiplex.bc1010_BAK8A_OA--bc1010_BAK8A_OA.bam', NULL, NULL);
INSERT INTO public.file VALUES (112475, 115727, NULL, NULL, '/seq/pacbio/r64228e_20210909_144906/2_B01/demultiplex.bc1010_BAK8A_OA--bc1010_BAK8A_OA.bam', NULL, NULL);
INSERT INTO public.file VALUES (112480, 115738, NULL, NULL, '/seq/pacbio/r64094e_20211022_154726/3_C01/demultiplex.bc1002_BAK8A_OA--bc1002_BAK8A_OA.bam', NULL, NULL);
INSERT INTO public.file VALUES (112481, 115739, NULL, NULL, '/seq/pacbio/r64094e_20211022_154726/3_C01/demultiplex.bc1003_BAK8A_OA--bc1003_BAK8A_OA.bam', NULL, NULL);
INSERT INTO public.file VALUES (112482, 115740, NULL, NULL, '/seq/pacbio/r64094e_20211022_154726/3_C01/demultiplex.bc1008_BAK8A_OA--bc1008_BAK8A_OA.bam', NULL, NULL);
INSERT INTO public.file VALUES (112491, 115750, NULL, NULL, '/seq/pacbio/r64174e_20211103_151946/1_A01/demultiplex.bc1008_BAK8A_OA--bc1008_BAK8A_OA.bam', NULL, NULL);
INSERT INTO public.file VALUES (112522, 115781, NULL, NULL, '/seq/pacbio/r64178e_20211112_181830/1_A01/demultiplex.bc1003_BAK8A_OA--bc1003_BAK8A_OA.bam', NULL, NULL);
INSERT INTO public.file VALUES (112523, 115782, NULL, NULL, '/seq/pacbio/r64178e_20211112_181830/2_B01/demultiplex.bc1011_BAK8A_OA--bc1011_BAK8A_OA.bam', NULL, NULL);
INSERT INTO public.file VALUES (112533, 115792, NULL, NULL, '/seq/pacbio/r64221e_20211117_155737/1_A01/demultiplex.bc1009_BAK8A_OA--bc1009_BAK8A_OA.bam', NULL, NULL);
INSERT INTO public.file VALUES (112552, 115811, NULL, NULL, '/seq/pacbio/r64174e_20220126_125838/2_B01/demultiplex.bc1003T--bc1003T.bam', NULL, NULL);
INSERT INTO public.file VALUES (112578, 115837, NULL, NULL, '/seq/pacbio/r64228e_20220420_151038/3_C01/demultiplex.bc1016_BAK8B_OA--bc1016_BAK8B_OA.bam', NULL, NULL);
INSERT INTO public.file VALUES (112579, 115838, NULL, NULL, '/seq/pacbio/r64228e_20220420_151038/4_D01/demultiplex.bc1016_BAK8B_OA--bc1016_BAK8B_OA.bam', NULL, NULL);
INSERT INTO public.file VALUES (112583, 115842, NULL, NULL, '/seq/pacbio/r64094e_20220811_121728/1_A01/demultiplex.bc1003_BAK8A_OA--bc1003_BAK8A_OA.bam', NULL, NULL);
INSERT INTO public.file VALUES (112586, 115845, NULL, NULL, '/seq/pacbio/r64094e_20220811_121728/2_B01/demultiplex.bc1003_BAK8A_OA--bc1003_BAK8A_OA.bam', NULL, NULL);
INSERT INTO public.file VALUES (112589, 115848, NULL, NULL, '/seq/pacbio/r64094e_20220811_121728/3_C01/demultiplex.bc1003_BAK8A_OA--bc1003_BAK8A_OA.bam', NULL, NULL);
INSERT INTO public.file VALUES (112592, 115851, NULL, NULL, '/seq/pacbio/r64094e_20220811_121728/4_D01/demultiplex.bc1003_BAK8A_OA--bc1003_BAK8A_OA.bam', NULL, NULL);
INSERT INTO public.file VALUES (112605, 115864, NULL, NULL, '/seq/pacbio/r64089e_20220922_153656/1_A01/m64089e_220922_160600.hifi_reads.bc1016_BAK8B_OA--bc1016_BAK8B_OA.bam', NULL, NULL);
INSERT INTO public.file VALUES (112609, 115868, NULL, NULL, '/seq/pacbio/r64089e_20220922_153656/2_B01/m64089e_220923_210112.hifi_reads.bc1016_BAK8B_OA--bc1016_BAK8B_OA.bam', NULL, NULL);
INSERT INTO public.file VALUES (112613, 115872, NULL, NULL, '/seq/pacbio/r64089e_20220922_153656/3_C01/m64089e_220925_015808.hifi_reads.bc1016_BAK8B_OA--bc1016_BAK8B_OA.bam', NULL, NULL);
INSERT INTO public.file VALUES (112617, 115876, NULL, NULL, '/seq/pacbio/r64089e_20220922_153656/4_D01/m64089e_220926_065548.hifi_reads.bc1016_BAK8B_OA--bc1016_BAK8B_OA.bam', NULL, NULL);
INSERT INTO public.file VALUES (112629, 115888, NULL, NULL, '/seq/pacbio/r64174e_20221104_162617/4_D01/demultiplex.bc1009_BAK8A_OA--bc1009_BAK8A_OA.bam', NULL, NULL);
INSERT INTO public.file VALUES (112659, 115918, NULL, NULL, '/seq/pacbio/r84047_20230425_112441/1_A01/m84047_230425_113454_s1.hifi_reads.bc2001.bam', NULL, NULL);
INSERT INTO public.file VALUES (112661, 115920, NULL, NULL, '/seq/pacbio/r64016e_20230428_140149/2_B01/demultiplex.bc2001--bc2001.bam', NULL, NULL);
INSERT INTO public.file VALUES (112668, 115927, NULL, NULL, '/seq/pacbio/r84047_20230706_145219/1_D01/m84047_230706_152551_s2.hifi_reads.bc2041.bam', NULL, NULL);
INSERT INTO public.file VALUES (112669, 115928, NULL, NULL, '/seq/pacbio/r84047_20230706_145219/1_D01/m84047_230706_152551_s2.hifi_reads.bc2042.bam', NULL, NULL);
INSERT INTO public.file VALUES (112670, 115929, NULL, NULL, '/seq/pacbio/r84047_20230706_145219/1_D01/m84047_230706_152551_s2.hifi_reads.bc2043.bam', NULL, NULL);
INSERT INTO public.file VALUES (112671, 115930, NULL, NULL, '/seq/pacbio/r84047_20230706_145219/1_D01/m84047_230706_152551_s2.hifi_reads.bc2044.bam', NULL, NULL);
INSERT INTO public.file VALUES (117663, 120926, NULL, NULL, '/seq/illumina/runs/40/40280/plex1/40280#1.cram', NULL, NULL);
INSERT INTO public.file VALUES (117664, 120927, NULL, NULL, '/seq/illumina/runs/40/40280/plex2/40280#2.cram', NULL, NULL);
INSERT INTO public.file VALUES (131286, 134799, NULL, NULL, '/seq/pacbio/r64125e_20210211_150459/1_A01/demultiplex.bc1010_BAK8A_OA--bc1010_BAK8A_OA.bam', NULL, NULL);
INSERT INTO public.file VALUES (117665, 120928, NULL, NULL, '/seq/illumina/runs/40/40280/plex3/40280#3.cram', NULL, NULL);
INSERT INTO public.file VALUES (123945, 127428, NULL, NULL, '/seq/36703/36703_5#2.cram', NULL, NULL);
INSERT INTO public.file VALUES (130055, 133566, NULL, NULL, '/seq/pacbio/r64221e_20230815_132711/2_B01/demultiplex.bc2023--bc2023.bam', NULL, NULL);
INSERT INTO public.file VALUES (130054, 133565, NULL, NULL, '/seq/pacbio/r64221e_20230815_132711/1_A01/demultiplex.bc2022--bc2022.bam', NULL, NULL);
INSERT INTO public.file VALUES (131289, 134802, NULL, NULL, '/seq/pacbio/r64221e_20211110_154532/1_A01/demultiplex.bc1010_BAK8A_OA--bc1010_BAK8A_OA.bam', NULL, NULL);
INSERT INTO public.file VALUES (131291, 134804, NULL, NULL, '/seq/pacbio/r64097e_20211201_160412/3_C01/demultiplex.bc1021_BAK8B_OA--bc1021_BAK8B_OA.bam', NULL, NULL);
INSERT INTO public.file VALUES (132721, 136203, NULL, NULL, '/seq/pacbio/r84047_20231120_143308/1_A01/m84047_231120_144131_s1.hifi_reads.bc2053.bam', NULL, NULL);
INSERT INTO public.file VALUES (132722, 136204, NULL, NULL, '/seq/pacbio/r84047_20231120_143308/1_A01/m84047_231120_144131_s1.hifi_reads.bc2055.bam', NULL, NULL);
INSERT INTO public.file VALUES (132723, 136205, NULL, NULL, '/seq/pacbio/r84047_20231120_143308/1_A01/m84047_231120_144131_s1.hifi_reads.bc2057.bam', NULL, NULL);
INSERT INTO public.file VALUES (132724, 136206, NULL, NULL, '/seq/pacbio/r84047_20231120_143308/1_A01/m84047_231120_144131_s1.hifi_reads.bc2059.bam', NULL, NULL);
INSERT INTO public.file VALUES (132725, 136207, NULL, NULL, '/seq/pacbio/r84047_20231120_143308/1_B01/m84047_231120_151150_s2.hifi_reads.bc2054.bam', NULL, NULL);
INSERT INTO public.file VALUES (132726, 136208, NULL, NULL, '/seq/pacbio/r84047_20231120_143308/1_B01/m84047_231120_151150_s2.hifi_reads.bc2056.bam', NULL, NULL);
INSERT INTO public.file VALUES (132727, 136209, NULL, NULL, '/seq/pacbio/r84047_20231120_143308/1_B01/m84047_231120_151150_s2.hifi_reads.bc2058.bam', NULL, NULL);
INSERT INTO public.file VALUES (132728, 136210, NULL, NULL, '/seq/pacbio/r84047_20231120_143308/1_B01/m84047_231120_151150_s2.hifi_reads.bc2060.bam', NULL, NULL);
INSERT INTO public.file VALUES (133103, 136405, NULL, NULL, '/seq/pacbio/r64228e_20231127_144807/1_A01/m64228e_231127_153346.hifi_reads.bc2045--bc2045.bam', NULL, NULL);
INSERT INTO public.file VALUES (133104, 136428, NULL, NULL, '/seq/pacbio/r64228e_20231127_144807/2_B01/m64228e_231128_184021.hifi_reads.bc2046--bc2046.bam', NULL, NULL);
INSERT INTO public.file VALUES (133072, 136649, NULL, NULL, '/seq/pacbio/r64089e_20231130_101714/3_C01/m64089e_231202_200225.hifi_reads.bc2047--bc2047.bam', NULL, NULL);
INSERT INTO public.file VALUES (133290, 136865, NULL, NULL, '/seq/pacbio/r64089e_20231221_144247/1_A01/m64089e_231221_145323.hifi_reads.bc2079--bc2079.bam', NULL, NULL);
INSERT INTO public.file VALUES (112499, 115758, NULL, NULL, '/seq/pacbio/r64125e_20211103_174807/1_A01/demultiplex.bc1011_BAK8A_OA--bc1011_BAK8A_OA.bam', NULL, NULL);
INSERT INTO public.file VALUES (112508, 115767, NULL, NULL, '/seq/pacbio/r64089e_20211103_151809/3_C01/demultiplex.bc1019_BAK8B_OA--bc1019_BAK8B_OA.bam', NULL, NULL);
INSERT INTO public.file VALUES (112546, 115805, NULL, NULL, '/seq/pacbio/r64229e_20211215_183108/1_A01/demultiplex.bc1018_BAK8B_OA--bc1018_BAK8B_OA.bam', NULL, NULL);
INSERT INTO public.file VALUES (131293, 134806, NULL, NULL, '/seq/pacbio/r64230e_20220218_135813/3_C01/demultiplex.bc1009_BAK8A_OA--bc1009_BAK8A_OA.bam', NULL, NULL);
INSERT INTO public.file VALUES (112547, 115806, NULL, NULL, '/seq/pacbio/r64221e_20211216_134727/1_A01/demultiplex.bc1017_BAK8B_OA--bc1017_BAK8B_OA.bam', NULL, NULL);
INSERT INTO public.file VALUES (131295, 134808, NULL, NULL, '/seq/pacbio/r64094e_20220303_161411/3_C01/demultiplex.bc1001_BAK8A_OA--bc1001_BAK8A_OA.bam', NULL, NULL);
INSERT INTO public.file VALUES (112548, 115807, NULL, NULL, '/seq/pacbio/r64178e_20220106_182328/3_C01/demultiplex.bc1012_BAK8A_OA--bc1012_BAK8A_OA.bam', NULL, NULL);
INSERT INTO public.file VALUES (112571, 115830, NULL, NULL, '/seq/pacbio/r64016e_20220309_151959/1_A01/demultiplex.bc1012T--bc1012T.bam', NULL, NULL);
INSERT INTO public.file VALUES (115164, 118427, NULL, NULL, '/seq/illumina/runs/36/36691/lane2/plex5/36691_2#5.cram', NULL, NULL);
INSERT INTO public.file VALUES (115165, 118428, NULL, NULL, '/seq/illumina/runs/36/36691/lane2/plex6/36691_2#6.cram', NULL, NULL);
INSERT INTO public.file VALUES (115166, 118429, NULL, NULL, '/seq/illumina/runs/36/36691/lane2/plex7/36691_2#7.cram', NULL, NULL);
INSERT INTO public.file VALUES (115167, 118430, NULL, NULL, '/seq/illumina/runs/36/36691/lane2/plex8/36691_2#8.cram', NULL, NULL);
INSERT INTO public.file VALUES (117820, 121083, NULL, NULL, '/seq/illumina/runs/40/40666/lane2/plex2/40666_2#2.cram', NULL, NULL);
INSERT INTO public.file VALUES (121145, 124432, NULL, NULL, '/seq/pacbio/r64097e_20210218_161440/4_D01/demultiplex.bc1019_BAK8B_OA--bc1019_BAK8B_OA.bam', NULL, NULL);
INSERT INTO public.file VALUES (124080, 127563, NULL, NULL, '/seq/37935/37935_8#13.cram', NULL, NULL);


--
-- Data for Name: review_dict; Type: TABLE DATA; Schema: public; Owner: sts-dev
--



--
-- Data for Name: genomescope_metrics; Type: TABLE DATA; Schema: public; Owner: sts-dev
--



--
-- Data for Name: markerscan_metrics; Type: TABLE DATA; Schema: public; Owner: sts-dev
--



--
-- Data for Name: merqury_metrics; Type: TABLE DATA; Schema: public; Owner: sts-dev
--



--
-- Data for Name: offspring; Type: TABLE DATA; Schema: public; Owner: sts-dev
--



--
-- Data for Name: pacbio_run_metrics; Type: TABLE DATA; Schema: public; Owner: sts-dev
--

INSERT INTO public.pacbio_run_metrics VALUES ('m64228e_210913_122131', 1800, 'Sequel II Binding Kit 2.0', 'Sequel II Sequencing Plate 2.0 (4 rxn)', 'true', 80, 5501, 49484, 365971708624, 7093836, 51590, 143750, 13606, 18750, 88952045568, 333998, 7099337, 581336, 18117312007, 1810562, 401090);
INSERT INTO public.pacbio_run_metrics VALUES ('m64228e_210912_060838', 1800, 'Sequel II Binding Kit 2.2', 'Sequel II Sequencing Plate 2.0 (4 rxn)', 'true', 80, 17325, 33802, 382311696238, 6273205, 60944, 182750, 14206, 23750, 78462779392, 1324628, 6290530, 399513, 14856427333, 1744344, 305548);
INSERT INTO public.pacbio_run_metrics VALUES ('m64178e_211105_051438', 1800, 'Sequel II Binding Kit 2.2', 'Sequel II Sequencing Plate 2.0 (4 rxn)', 'true', 80, 11655, 43707, 357153319051, 5999345, 59532, 198483, 13617, 23287, 70020530176, 1717602, 6011071, 285998, 12446662253, 1545684, 257002);
INSERT INTO public.pacbio_run_metrics VALUES ('m64094e_211106_093042', 1800, 'Sequel II Binding Kit 2.2', 'Sequel II Sequencing Plate 2.0 (4 rxn)', 'true', 80, 12115, 43775, 387638942593, 5809461, 66725, 204566, 14867, 21998, 74951524352, 2058950, 5821595, 134126, 14607584503, 1632710, 265236);
INSERT INTO public.pacbio_run_metrics VALUES ('m64228e_211105_115646', 1800, 'Sequel II Binding Kit 2.2', 'Sequel II Sequencing Plate 2.0 (4 rxn)', 'false', 80, 13981, 47352, 598119767909, 5850500, 102233, 209113, 17852, 26429, 89219694592, 1884352, 5864505, 265814, 28802004038, 2786835, 417302);
INSERT INTO public.pacbio_run_metrics VALUES ('m64228e_211106_225141', 1800, 'Sequel II Binding Kit 2.2', 'Sequel II Sequencing Plate 2.0 (4 rxn)', 'false', 80, 14038, 47018, 596283185594, 6436565, 92639, 190410, 17031, 20179, 95156305920, 1245434, 6450631, 318606, 30379425978, 2769457, 578245);
INSERT INTO public.pacbio_run_metrics VALUES ('m64228e_211108_094826', 1800, 'Sequel II Binding Kit 2.2', 'Sequel II Sequencing Plate 2.0 (4 rxn)', 'false', 80, 14793, 46808, 634771303793, 5786916, 109690, 222473, 18377, 27303, 92844941312, 1907537, 5801742, 305392, 30461970621, 2846337, 382649);
INSERT INTO public.pacbio_run_metrics VALUES ('m64178e_211115_123002', 1800, 'Sequel II Binding Kit 2.2', 'Sequel II Sequencing Plate 2.0 (4 rxn)', 'false', 60, 35501, 31849, 253374473473, 4819375, 52574, 199925, 12541, 19108, 55866929152, 2883349, 4854925, 276397, 10903486899, 1022402, 145391);
INSERT INTO public.pacbio_run_metrics VALUES ('m64178e_211116_212829', 1800, 'Sequel II Binding Kit 2.2', 'Sequel II Sequencing Plate 2.0 (4 rxn)', 'false', 80, 32960, 32186, 359493211861, 5176771, 69443, 203814, 12248, 20160, 54660673536, 2550282, 5209791, 254598, 13843057382, 1729035, 220572);
INSERT INTO public.pacbio_run_metrics VALUES ('m64230e_220423_112659', 1800, 'Sequel II Binding Kit 2.2', 'Sequel II Sequencing Plate 2.0 (4 rxn)', 'true', 130, 18174, 57013, 384832182282, 5245661, 73362, 184750, 25459, 59750, 122239188992, 2485278, 5263835, 265558, 16781726587, 1227593, 276007);
INSERT INTO public.pacbio_run_metrics VALUES ('m64230e_220424_203712', 1800, 'Sequel II Binding Kit 2.2', 'Sequel II Sequencing Plate 2.0 (4 rxn)', 'true', 130, 24595, 44912, 189186878966, 6087564, 31078, 109250, 14802, 34250, 84896415744, 749775, 6112159, 1152737, 5669451096, 501092, 197207);
INSERT INTO public.pacbio_run_metrics VALUES ('m64089e_220922_160600', 1440, 'Sequel II Binding Kit 3.2', 'Sequel II Sequencing Plate 2.0 (4 rxn)', 'true', 119, 2249, 81911, 481132405381, 6265781, 76787, 172250, 16900, 21250, 96400826368, 1423329, 6268030, 323312, 29027696933, 2107825, NULL);
INSERT INTO public.pacbio_run_metrics VALUES ('m64089e_220923_210112', 1440, 'Sequel II Binding Kit 3.2', 'Sequel II Sequencing Plate 2.0 (4 rxn)', 'true', 110, 7985, 98383, 68280068784, 628591, 108624, 215250, 16738, 18250, 9486319616, 7364645, 636576, 13450, 4129252921, 307769, NULL);
INSERT INTO public.pacbio_run_metrics VALUES ('m64089e_220925_015808', 1440, 'Sequel II Binding Kit 3.2', 'Sequel II Sequencing Plate 2.0 (4 rxn)', 'true', 111, 5143, 101612, 51682134240, 458370, 112752, 220750, 17160, 18750, 7140539392, 7541449, 463513, 9709, 3354266923, 229423, NULL);
INSERT INTO public.pacbio_run_metrics VALUES ('m64089e_220926_065548', 1440, 'Sequel II Binding Kit 3.2', 'Sequel II Sequencing Plate 2.0 (4 rxn)', 'true', 141, 5873, 90069, 253254521515, 2484227, 101945, 207750, 16976, 19750, 38715691008, 5472368, 2490100, 52203, 16774617247, 1127949, NULL);
INSERT INTO public.pacbio_run_metrics VALUES ('m84047_230425_130728_s4', 1440, 'Revio polymerase kit', 'Revio sequencing plate', 'false', 42, 4970, 73596, 700563080969, 7691877, 91078, 154250, 11740, 16750, 81209532416, 17363180, 7696847, 105797, 40580515054, 4760267, NULL);
INSERT INTO public.pacbio_run_metrics VALUES ('m84047_230505_155651_s1', 1440, 'Revio polymerase kit', 'Revio sequencing plate', 'false', 247, 2077, 57781, 1051850016310, 18456488, 56991, 112750, 12036, 18750, 190853021696, 5969853, 18458565, 737406, 58104768378, 7649947, NULL);
INSERT INTO public.pacbio_run_metrics VALUES ('m84047_230517_174928_s2', 1440, 'Revio polymerase kit', 'Revio sequencing plate', 'false', 148, 2987, 64030, 1042136259179, 13248466, 78661, 154750, 12010, 17250, 144621289472, 11633478, 13251453, 280893, 64694801278, 6786657, NULL);
INSERT INTO public.pacbio_run_metrics VALUES ('m64230e_210705_101703', 1800, 'Sequel II Binding Kit 2.2', 'Sequel II Sequencing Plate 2.0 (4 rxn)', 'true', 55, 25737, 33798, 280968685126, 4519194, 62172, 221750, 12634, 20250, 50160414720, 3353461, 4544931, 116279, 10196902390, 1263166, 139931);
INSERT INTO public.pacbio_run_metrics VALUES ('m64097e_210617_142108', 1800, 'Sequel II Binding Kit 2.0', 'Sequel II Sequencing Plate 2.0 (4 rxn)', 'true', 90, 2571, 47597, 74750094038, 1779993, 41995, 170250, 10899, 20250, 18597128192, 6100015, 1782564, 132092, 4640623677, 308646, 65189);
INSERT INTO public.pacbio_run_metrics VALUES ('m64094e_210430_115816', 1800, 'Sequel II Binding Kit 2.0', 'Sequel II Sequencing Plate 2.0 (4 rxn)', 'true', 80, 2493, 52074, 72761511723, 1364026, 53343, 176250, 12094, 19750, 15936306176, 6558896, 1366519, 89256, 4957952068, 316388, 55943);
INSERT INTO public.pacbio_run_metrics VALUES ('m64097e_210621_084307', 1800, 'Sequel II Binding Kit 2.0', 'Sequel II Sequencing Plate 2.0 (4 rxn)', 'true', 110, 2224, 43764, 65157610201, 1075091, 60607, 171750, 13298, 18750, 13474009088, 6901861, 1077315, 35495, 4135474551, 305781, 55303);
INSERT INTO public.pacbio_run_metrics VALUES ('m64097e_210425_025051', 1800, 'Sequel II Binding Kit 2.0', 'Sequel II Sequencing Plate 2.0 (4 rxn)', 'true', 80, 2184, 47162, 272641862996, 4721987, 57739, 150750, 15321, 20750, 68301385728, 3160264, 4724171, 130236, 16780033599, 1181872, 278348);
INSERT INTO public.pacbio_run_metrics VALUES ('m64097e_210508_212855', 1800, 'Sequel II Binding Kit 2.0', 'Sequel II Sequencing Plate 2.0 (4 rxn)', 'true', 65, 1653, 43687, 232510407521, 4133342, 56252, 161250, 14390, 19750, 56084566016, 3749864, 4134995, 129812, 14579988651, 1058733, 213191);
INSERT INTO public.pacbio_run_metrics VALUES ('m64174e_210501_195526', 1800, 'Sequel II Binding Kit 2.0', 'Sequel II Sequencing Plate 2.0 (4 rxn)', 'true', 80, 4417, 49558, 283860620750, 5072853, 55957, 142750, 13758, 20250, 66257358848, 2804637, 5077270, 132764, 16565317047, 1390272, 328318);
INSERT INTO public.pacbio_run_metrics VALUES ('m64174e_210503_021816', 1800, 'Sequel II Binding Kit 2.0', 'Sequel II Sequencing Plate 2.0 (4 rxn)', 'true', 80, 5059, 54178, 200698880544, 3462176, 57969, 164750, 12165, 18250, 40218943488, 4470294, 3467235, 77142, 11677270923, 996669, 183529);
INSERT INTO public.pacbio_run_metrics VALUES ('m64174e_210504_084057', 1800, 'Sequel II Binding Kit 2.0', 'Sequel II Sequencing Plate 2.0 (4 rxn)', 'true', 75, 4317, 54161, 258041222506, 4086377, 63147, 157250, 14837, 20750, 57753485312, 3778917, 4090694, 145060, 16526760836, 1167361, 261081);
INSERT INTO public.pacbio_run_metrics VALUES ('m64094e_210501_180717', 1800, 'Sequel II Binding Kit 2.0', 'Sequel II Sequencing Plate 2.0 (4 rxn)', 'true', 80, 4574, 52727, 42001092119, 928002, 45260, 164250, 13920, 23250, 12368517120, 7020821, 932576, 61274, 2453552916, 161236, 31946);
INSERT INTO public.pacbio_run_metrics VALUES ('m64094e_210503_002936', 1800, 'Sequel II Binding Kit 2.0', 'Sequel II Sequencing Plate 2.0 (4 rxn)', 'true', 80, 7700, 54305, 19135724236, 441319, 43360, 167250, 14305, 25750, 6043042304, 7532427, 449019, 33225, 975725687, 74256, 11156);
INSERT INTO public.pacbio_run_metrics VALUES ('m64094e_210504_065204', 1800, 'Sequel II Binding Kit 2.0', 'Sequel II Sequencing Plate 2.0 (4 rxn)', 'true', 80, 4711, 53316, 24879072078, 499284, 49830, 175750, 13132, 20750, 6157792256, 7475453, 503995, 35223, 1490590834, 104018, 17688);
INSERT INTO public.pacbio_run_metrics VALUES ('m64221e_230913_152616', 1440, 'Sequel II Binding Kit 3.2', 'Sequel II Sequencing Plate 2.0 (4 rxn)', 'false', 73, 2459, 81402, 123845133910, 4813464, 25729, 102750, 9705, 20750, 44174602240, 2529761, 4815923, 668987, 4058417320, 566372, NULL);
INSERT INTO public.pacbio_run_metrics VALUES ('m64230e_220219_230553', 1800, 'Sequel II Binding Kit 2.2', 'Sequel II Sequencing Plate 2.0 (4 rxn)', 'false', 105, 11915, 44934, 464789014692, 6318588, 73559, 193750, 15803, 23750, 85939044352, 1482690, 6330503, 201478, 18328354975, 2081225, 378287);
INSERT INTO public.pacbio_run_metrics VALUES ('m64174e_210130_144539', 1440, 'Sequel II Binding Kit 2.0', 'Sequel II Sequencing Plate 2.0 (4 rxn)', 'true', 70, 3587, 52623, 396588881313, 5874371, 67511, 135177, 16008, 19925, 88485339136, 1740356, 5877999, 396316, 26217136083, 2118116, 424094);
INSERT INTO public.pacbio_run_metrics VALUES ('m64228e_210909_150013', 1800, 'Sequel II Binding Kit 2.2', 'Sequel II Sequencing Plate 2.0 (4 rxn)', 'true', 80, 22544, 33361, 332524378994, 5086096, 65379, 194750, 15084, 27750, 67687825408, 2686658, 5108640, 219373, 13206884909, 1530945, 195937);
INSERT INTO public.pacbio_run_metrics VALUES ('m64228e_210910_210956', 1800, 'Sequel II Binding Kit 2.0', 'Sequel II Sequencing Plate 2.0 (4 rxn)', 'true', 80, 6787, 44619, 359672423576, 6959902, 51678, 141750, 14183, 20250, 92717858816, 588628, 6966689, 459354, 19031685223, 1803099, 338334);
INSERT INTO public.pacbio_run_metrics VALUES ('m64094e_211025_104111', 1800, 'Sequel II Binding Kit 2.2', 'Sequel II Sequencing Plate 2.0 (4 rxn)', 'false', 80, 19080, 55653, 466486476306, 5406745, 86278, 203593, 16150, 26048, 72948867072, 2358099, 5426043, 230529, 19975606047, 2116495, 362381);
INSERT INTO public.pacbio_run_metrics VALUES ('m64174e_211103_153104', 1800, 'Sequel II Binding Kit 2.2', 'Sequel II Sequencing Plate 2.0 (4 rxn)', 'true', 77, 21374, 37594, 72822408783, 1795411, 40560, 219250, 9789, 18250, 16020074496, 6089665, 1816785, 108221, 2577954781, 297124, 26541);
INSERT INTO public.pacbio_run_metrics VALUES ('m64178e_211112_183448', 1800, 'Sequel II Binding Kit 2.2', 'Sequel II Sequencing Plate 2.0 (4 rxn)', 'false', 75, 37730, 38914, 457398258483, 5223348, 87568, 220140, 14226, 19748, 63120080896, 2625685, 5261124, 127862, 19352031979, 2101744, 295831);
INSERT INTO public.pacbio_run_metrics VALUES ('m64178e_211114_033110', 1800, 'Sequel II Binding Kit 2.2', 'Sequel II Sequencing Plate 2.0 (4 rxn)', 'false', 80, 35158, 34618, 504068378419, 5103919, 98761, 227541, 13094, 20276, 56116867072, 2711602, 5139118, 163951, 18992150732, 2503995, 247691);
INSERT INTO public.pacbio_run_metrics VALUES ('m64221e_211117_160848', 1800, 'Sequel II Binding Kit 2.2', 'Sequel II Sequencing Plate 2.0 (4 rxn)', 'true', 73, 37655, 34640, 340692185874, 4743179, 71827, 213104, 14200, 21953, 59157237760, 3106389, 4780890, 127392, 14913661276, 1551022, 170473);
INSERT INTO public.pacbio_run_metrics VALUES ('m64174e_220128_000029', 1800, 'Sequel II Binding Kit 2.2', 'Sequel II Sequencing Plate 2.0 (4 rxn)', 'true', 90, 4465, 42365, 555831739850, 6986664, 79556, 183750, 15561, 23750, 94370373632, 760749, 6991129, 262793, 24503015457, 2688236, 487568);
INSERT INTO public.pacbio_run_metrics VALUES ('m64228e_220423_113317', 1800, 'Sequel II Binding Kit 2.2', 'Sequel II Sequencing Plate 2.0 (4 rxn)', 'true', 130, 14673, 56644, 570830471507, 5804066, 98350, 214250, 17450, 21750, 88681791488, 2029140, 5818739, 166792, 30682665085, 2493812, 380021);
INSERT INTO public.pacbio_run_metrics VALUES ('m64228e_220424_205021', 1800, 'Sequel II Binding Kit 2.2', 'Sequel II Sequencing Plate 2.0 (4 rxn)', 'true', 130, 22800, 48503, 348110160166, 5787637, 60147, 180750, 17190, 34750, 87822172160, 1611870, 5810437, 592364, 14589917711, 1297533, 293199);
INSERT INTO public.pacbio_run_metrics VALUES ('m64094e_220811_122820', 1440, 'Sequel II Binding Kit 2.2', 'Sequel II Sequencing Plate 2.0 (4 rxn)', 'false', 80, 3600, 44239, 407387740732, 4313227, 94451, 196250, 12535, 12250, 47661748224, 3577991, 4316827, 119853, 20341044706, 2242290, 269012);
INSERT INTO public.pacbio_run_metrics VALUES ('m64094e_220812_172220', 1440, 'Sequel II Binding Kit 2.2', 'Sequel II Sequencing Plate 2.0 (4 rxn)', 'false', 80, 6585, 47401, 452397893649, 4910579, 92127, 192750, 13688, 14250, 58132443136, 2941071, 4917164, 156436, 22726878332, 2433837, 329305);
INSERT INTO public.pacbio_run_metrics VALUES ('m64094e_220813_205234', 1440, 'Sequel II Binding Kit 2.2', 'Sequel II Sequencing Plate 2.0 (4 rxn)', 'false', 80, 5200, 46913, 453385030422, 4994883, 90770, 187250, 13561, 13750, 59216424960, 2880844, 5000083, 133744, 23210789289, 2503615, 340681);
INSERT INTO public.pacbio_run_metrics VALUES ('m64094e_220815_002611', 1440, 'Sequel II Binding Kit 2.2', 'Sequel II Sequencing Plate 2.0 (4 rxn)', 'false', 80, 3739, 45834, 477023234226, 5212611, 91513, 188250, 13981, 15250, 63087988736, 2630206, 5216350, 168115, 23708420499, 2602683, 352646);
INSERT INTO public.pacbio_run_metrics VALUES ('m64174e_221108_072343', 1440, 'Sequel II Binding Kit 3.2', 'Sequel II Sequencing Plate 2.0 (4 rxn)', 'true', 53, 30, 73591, 2319271307, 23713, 97806, 228250, 16576, 22250, 355488672, 7984874, 23743, 6054, 139002207, 9990, NULL);
INSERT INTO public.pacbio_run_metrics VALUES ('m84047_230425_113454_s1', 1440, 'Revio polymerase kit', 'Revio sequencing plate', 'false', 43, 534, 87386, 106764384080, 888112, 120215, 179750, 14056, 21250, 10550540288, 24270071, 888646, 7107, 5302183570, 608827, NULL);
INSERT INTO public.pacbio_run_metrics VALUES ('m64016e_230429_173736', 1440, 'Sequel II Binding Kit 3.2', 'Sequel II Sequencing Plate 2.0 (4 rxn)', 'false', 65, 839, 103915, 217505173565, 1723291, 126215, 219750, 16410, 40750, 20103563264, 6265894, 1724130, 24647, 7976159616, 1093026, NULL);
INSERT INTO public.pacbio_run_metrics VALUES ('m84047_230706_152551_s2', 1440, 'Revio polymerase kit', 'Revio sequencing plate', 'false', 230, 2958, 70592, 1450242252122, 16884014, 85894, 150750, 11832, 11750, 176328605696, 7986950, 16886972, 291902, 89771516387, 10167387, NULL);
INSERT INTO public.pacbio_run_metrics VALUES ('m64125e_210211_151547', 1440, 'Sequel II Binding Kit 2.0', 'Sequel II Sequencing Plate 2.0 (4 rxn)', 'true', 80, 3322, 50415, 148762487950, 1914819, 77690, 158706, 15720, 19771, 28387481600, 6058062, 1918168, 38441, 11587255800, 781723, 121119);
INSERT INTO public.pacbio_run_metrics VALUES ('m64221e_230816_183713', 1440, 'Sequel II Binding Kit 3.2', 'Sequel II Sequencing Plate 2.0 (4 rxn)', 'false', 67, 1208, 98026, 1900363114, 149629, 12700, 53750, 10062, 40250, 1493779200, 7826510, 150837, 37324, 6568913, 2682, NULL);
INSERT INTO public.pacbio_run_metrics VALUES ('m64221e_230815_134000', 1440, 'Sequel II Binding Kit 3.2', 'Sequel II Sequencing Plate 2.0 (4 rxn)', 'false', 42, 5163, 95762, 149259899288, 4183985, 35674, 133250, 11017, 22750, 41895088128, 3328952, 4189148, 496571, 4890620981, 683660, NULL);
INSERT INTO public.pacbio_run_metrics VALUES ('m64221e_211110_155624', 1800, 'Sequel II Binding Kit 2.2', 'Sequel II Sequencing Plate 2.0 (4 rxn)', 'true', 80, 61093, 40051, 377569898004, 5118412, 73767, 192750, 19443, 65250, 83531694080, 2668647, 5179505, 166519, 12197001188, 1697494, 217725);
INSERT INTO public.pacbio_run_metrics VALUES ('m64097e_211204_084129', 1800, 'Sequel II Binding Kit 2.2', 'Sequel II Sequencing Plate 2.0 (4 rxn)', 'true', 65, 25483, 41676, 381281500236, 4421865, 86226, 224750, 13442, 20750, 49823379456, 3456621, 4447348, 110702, 14975514421, 1813262, 206780);
INSERT INTO public.pacbio_run_metrics VALUES ('m84047_231120_144131_s1', 1440, 'Revio polymerase kit', 'Revio sequencing plate', 'false', 248, 3705, 62806, 1132958084250, 15431696, 73418, 137250, 15063, 16250, 213950464000, 9351713, 15435401, 378710, 86420069758, 7155691, NULL);
INSERT INTO public.pacbio_run_metrics VALUES ('m84047_231120_151150_s2', 1440, 'Revio polymerase kit', 'Revio sequencing plate', 'false', 236, 4199, 70018, 1401677599432, 15880513, 88264, 156750, 11725, 11750, 160028753920, 8898774, 15884712, 382338, 80870124555, 9503757, NULL);
INSERT INTO public.pacbio_run_metrics VALUES ('m64228e_231127_153346', 1440, 'Sequel II Binding Kit 3.2', 'Sequel II Sequencing Plate 2.0 (4 rxn)', 'false', 83, 1166, 80216, 515398078705, 6206131, 83047, 171750, 12035, 14250, 63543472128, 1557716, 6207297, 249658, 22829242358, 3036045, NULL);
INSERT INTO public.pacbio_run_metrics VALUES ('m64228e_231128_184021', 1440, 'Sequel II Binding Kit 3.2', 'Sequel II Sequencing Plate 2.0 (4 rxn)', 'false', 78, 1495, 82846, 479628349068, 5959893, 80476, 171250, 14284, 23250, 74681458688, 1734477, 5961388, 318806, 22239130305, 2705676, NULL);
INSERT INTO public.pacbio_run_metrics VALUES ('m64089e_231202_200225', 1440, 'Sequel II Binding Kit 3.2', 'Sequel II Sequencing Plate 2.0 (4 rxn)', 'false', 88, 2244, 93551, 515248551617, 5692744, 90510, 191250, 13563, 20250, 62034632704, 2072608, 5694988, 247075, 22542480439, 2830927, NULL);
INSERT INTO public.pacbio_run_metrics VALUES ('m64089e_231221_145323', 1440, 'Sequel II Binding Kit 3.2', 'Sequel II Sequencing Plate 2.0 (4 rxn)', 'false', 75, 2166, 87098, 416001898820, 4962565, 83828, 173750, 19252, 40250, 85437063168, 2875931, 4964731, 174009, 19830179326, 2060894, NULL);
INSERT INTO public.pacbio_run_metrics VALUES ('m64221e_211029_115402', 1800, 'Sequel II Binding Kit 2.2', 'Sequel II Sequencing Plate 2.0 (4 rxn)', 'true', 80, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.pacbio_run_metrics VALUES ('m64125e_211103_175849', 1800, 'Sequel II Binding Kit 2.2', 'Sequel II Sequencing Plate 2.0 (4 rxn)', 'true', 80, 7436, 42034, 553151067878, 6585777, 83991, 201925, 16852, 28340, 92938305536, 1229822, 6593231, 191618, 21418695862, 2493942, 429683);
INSERT INTO public.pacbio_run_metrics VALUES ('m64089e_211106_112750', 1800, 'Sequel II Binding Kit 2.2', 'Sequel II Sequencing Plate 2.0 (4 rxn)', 'true', 80, 11567, 47201, 547049291282, 5976633, 91531, 213407, 19178, 33279, 96287375360, 1861997, 5988224, 164450, 22173562388, 2285201, 389640);
INSERT INTO public.pacbio_run_metrics VALUES ('m64229e_211215_184451', 1800, 'Sequel II Binding Kit 2.2', 'Sequel II Sequencing Plate 2.0 (4 rxn)', 'true', 75, 59532, 46929, 327532775053, 5447893, 60121, 190250, 14087, 24250, 66998550528, 2213878, 5507425, 293368, 12248452645, 1420604, 228720);
INSERT INTO public.pacbio_run_metrics VALUES ('m64230e_220221_063339', 1800, 'Sequel II Binding Kit 2.2', 'Sequel II Sequencing Plate 2.0 (4 rxn)', 'false', 125, 4679, 42282, 531170227138, 7175106, 74030, 178250, 17088, 29250, 104928403456, 559724, 7179785, 275162, 20427871505, 2449121, 495597);
INSERT INTO public.pacbio_run_metrics VALUES ('m64221e_211216_143308', 1800, 'Sequel II Binding Kit 2.2', 'Sequel II Sequencing Plate 2.0 (4 rxn)', 'true', 130, 11116, 47404, 501229569339, 6315292, 79368, 201250, 15225, 23250, 81867579392, 1428185, 6326408, 260078, 21060621766, 2350462, 349190);
INSERT INTO public.pacbio_run_metrics VALUES ('m64094e_220306_084547', 1800, 'Sequel II Binding Kit 2.2', 'Sequel II Sequencing Plate 2.0 (4 rxn)', 'true', 115, 15739, 25448, 312257099154, 4752627, 65702, 208750, 12081, 19750, 50510405632, 2992741, 4768366, 253564, 13030324144, 1498277, 188945);
INSERT INTO public.pacbio_run_metrics VALUES ('m64178e_220109_104526', 1800, 'Sequel II Binding Kit 2.2', 'Sequel II Sequencing Plate 2.0 (4 rxn)', 'true', 90, 28669, 39205, 306451871975, 3169889, 96676, 244750, 15226, 22750, 39712731136, 4751754, 3198558, 64359, 12285197833, 1349911, 119282);
INSERT INTO public.pacbio_run_metrics VALUES ('m64016e_220309_153701', 1800, 'Sequel II Binding Kit 2.2', 'Sequel II Sequencing Plate 2.0 (4 rxn)', 'false', 130, 1121, 28845, 16993174926, 238065, 71380, 194750, 27740, 76750, 6267414528, 7759991, 239186, 15494, 359621759, 56232, 3933);
INSERT INTO public.pacbio_run_metrics VALUES ('m64097e_210221_172213', 1440, 'Sequel II Binding Kit 2.0', 'Sequel II Sequencing Plate 2.0 (4 rxn)', 'true', 45, 3200, 51271, 329209363529, 4556774, 72246, 146877, 13239, 15638, 57195683840, 3352198, 4559996, 102477, 22632028638, 1863309, 345974);


--
-- Data for Name: ploidyplot_metrics; Type: TABLE DATA; Schema: public; Owner: sts-dev
--



--
-- Data for Name: specimen_status_type; Type: TABLE DATA; Schema: public; Owner: sts-dev
--



--
-- Data for Name: specimen_status; Type: TABLE DATA; Schema: public; Owner: sts-dev
--



--
-- Name: allocation_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sts-dev
--

SELECT pg_catalog.setval('public.allocation_id_seq', 1, false);


--
-- Name: assembly_assembly_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sts-dev
--

SELECT pg_catalog.setval('public.assembly_assembly_id_seq', 1, false);


--
-- Name: assembly_metrics_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sts-dev
--

SELECT pg_catalog.setval('public.assembly_metrics_id_seq', 1, false);


--
-- Name: assembly_source_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sts-dev
--

SELECT pg_catalog.setval('public.assembly_source_id_seq', 1, false);


--
-- Name: assembly_status_assembly_status_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sts-dev
--

SELECT pg_catalog.setval('public.assembly_status_assembly_status_id_seq', 1, false);


--
-- Name: barcode_metrics_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sts-dev
--

SELECT pg_catalog.setval('public.barcode_metrics_id_seq', 1, false);


--
-- Name: busco_lineage_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sts-dev
--

SELECT pg_catalog.setval('public.busco_lineage_id_seq', 1, false);


--
-- Name: busco_metrics_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sts-dev
--

SELECT pg_catalog.setval('public.busco_metrics_id_seq', 1, false);


--
-- Name: centre_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sts-dev
--

SELECT pg_catalog.setval('public.centre_id_seq', 1, false);


--
-- Name: contigviz_metrics_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sts-dev
--

SELECT pg_catalog.setval('public.contigviz_metrics_id_seq', 1, false);


--
-- Name: data_data_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sts-dev
--

SELECT pg_catalog.setval('public.data_data_id_seq', 1, false);


--
-- Name: dataset_element_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sts-dev
--

SELECT pg_catalog.setval('public.dataset_element_id_seq', 1, false);


--
-- Name: dataset_status_dataset_status_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sts-dev
--

SELECT pg_catalog.setval('public.dataset_status_dataset_status_id_seq', 1, false);


--
-- Name: file_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sts-dev
--

SELECT pg_catalog.setval('public.file_id_seq', 1, false);


--
-- Name: genomescope_metrics_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sts-dev
--

SELECT pg_catalog.setval('public.genomescope_metrics_id_seq', 1, false);


--
-- Name: markerscan_metrics_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sts-dev
--

SELECT pg_catalog.setval('public.markerscan_metrics_id_seq', 1, false);


--
-- Name: merqury_metrics_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sts-dev
--

SELECT pg_catalog.setval('public.merqury_metrics_id_seq', 1, false);


--
-- Name: offspring_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sts-dev
--

SELECT pg_catalog.setval('public.offspring_id_seq', 1, false);


--
-- Name: platform_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sts-dev
--

SELECT pg_catalog.setval('public.platform_id_seq', 1, false);


--
-- Name: ploidyplot_metrics_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sts-dev
--

SELECT pg_catalog.setval('public.ploidyplot_metrics_id_seq', 1, false);


--
-- Name: project_project_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sts-dev
--

SELECT pg_catalog.setval('public.project_project_id_seq', 1, false);


--
-- Name: software_version_software_version_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sts-dev
--

SELECT pg_catalog.setval('public.software_version_software_version_id_seq', 1, false);


--
-- Name: specimen_status_specimen_status_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sts-dev
--

SELECT pg_catalog.setval('public.specimen_status_specimen_status_id_seq', 1, false);


--
-- PostgreSQL database dump complete
--

