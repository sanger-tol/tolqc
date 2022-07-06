"""add config file

Revision ID: c8b2d6322dbd
Revises: 1bec7c07ef1f
Create Date: 2022-07-05 11:15:56.470758

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import orm

import main.model as model


# revision identifiers, used by Alembic.
revision = 'c8b2d6322dbd'
down_revision = '1bec7c07ef1f'
branch_labels = None
depends_on = None


RAW_CONFIG = '''3537	durbin/rodents	Dissecting behavioural traits of the Grasshopper mouse
3687	durbin/cypriniformes	Zebrafish SAT cell line sequencing
3993	durbin/cichlids	PacBio improvement of A. calliptera cichlid genome assembly
4098	durbin/cypriniformes	[DHTue Seq] Discovar-sequencing for zebrafish DHTue
4099	durbin/cypriniformes	[DHAB Seq] Discovar-sequencing for zebrafish DHAB
4616	vgp/%TXGROUP%	Vertebrate Genome Project_FISH
4629	vgp/%TXGROUP%	Vertebrate Genome Project_MOUSE
4642	vgp/%TXGROUP%	Vertebrate Genome Project_CAECILIAN
5251	vgp/%TXGROUP%	Sanger_VGP_RNAseq
4922	25g/%TXGROUP%	25 Genomes Project
5113	durbin/jiggins	Genome sequencing of Black Soldier Fly
5173	durbin/jiggins	Genome sequencing of the butterfly Heliconius sara
5632	durbin/jiggins	HG_G3264_Evolutionary Genetics of Lepidoptera
5308	durbin/cichlids	Malawi-Tanganyika convergent cichlid sequencing
5732	darwin/%TXGROUP%	DTOL_Darwin Vertebrate Genomes
5733	durbin/cichlids	HG_ Malawi_cichlids_2019
5822	darwin/rnd	DTOL_Darwin R&D
5884	darwin/%TXGROUP%	DTOL_Darwin Lepidoptera
5881	darwin/%TXGROUP%	DTOL_Darwin Protozoa
5853	darwin/%TXGROUP%	DTOL_Darwin Plants
5901	darwin/%TXGROUP%	DTOL_Darwin Tree of Life
5740	lawniczak/badass	BAdASS Project (Best Anopheles Assembly Project)
6101	25g/%TXGROUP%	25 Genomes RNAseq
6327	darwin/%TXGROUP%	DTOL_Darwin Tree of Life RNA
6414	vgp/%TXGROUP%	Tree of Life - VGP
6375	25g/mammals	Otter Population Genomics
6387	darwin/dicots	Oak Population Genomics
6457	asg/%TXGROUP%	Tree of Life - ASG
6524	asg/%TXGROUP%	Tree of Life – ASGRNA
5485	darwin/%TXGROUP%	I3214_Tree of Life (Helminths) R&D
6380	darwin/rnd	Flying Insect Long Read
6552	darwin/%TXGROUP%	DTOL_Apple Day
6529	tol/molluscs	Golden Mussel Genomics Project
6584	tol/molluscs	Blaxter_Golden Mussel Transcriptomics Project
6733	erga/%TXGROUP%	ToL_Blaxter_ WC10686 _ ERGA PI_ DNA
6747	erga/%TXGROUP%	ToL_Blaxter_ WC10686 _ ERGA PI_ RNA
6830	lawniczak/plasmodium	1304-PF-GM-CLAESSENS-LAB
6313	darwin/rnd	ToL Meiofauna R&D
6322	darwin/rnd	ToL Meiofauna RNA R&D
6859	darwin/%TXGROUP%	Boletus edulis complex in the British Isles
6923	tol/%TXGROUP%	Genomic diversity of the lichen genus Stereocaulon
6921	tol/%TXGROUP%	Genomic diversity of the fever fly, Dilophus febrilis
6920	tol/%TXGROUP%	Genomic diversity of British native eyebrights
6919	tol/%TXGROUP%	Genomic diversity of oak (Quercus robur)
6899	tol/%TXGROUP%	Genomics of sexual dimorphism in Viscum album
6898	tol/%TXGROUP%	Genomic diversity of Salix (willow) species
6893	tol/%TXGROUP%	Genomic diversity of Hericium (tooth fungus group, Basidiomycota)
6772	blaxter/%TXGROUP%	ToL_Blaxter_ Reference Genomes_ RNA
6771	blaxter/%TXGROUP%	ToL_Blaxter_ Reference Genomes_ DNA 
6732	blaxter/%TXGROUP%	ToL_Blaxter_WC10687_Littorina popge
6731	durbin/%TXGROUP%	ToL_Durbin_TP10513_SNSF_Evolution_Alaska
6738	durbin/%TXGROUP%	ToL_Durbin_G2756_RNA
6725	durbin/%TXGROUP%	2021 WGS cichlids from Tanzania
6708	durbin/%TXGROUP%	ToL_Durbin_G3130_ Durbin_Malawi-Tanganyika convergent cichlid sequencing
6654	durbin/%TXGROUP%	ToL_Durbin_G3130_SNSF_Brazilian convergent cichlid
6652	durbin/%TXGROUP%	2021 WGS cichlids from lab crosses
6617	durbin/%TXGROUP%	ToL_Durbin_TP10513_SNSF_Evolution_Collection Study_Alaska
6616	durbin/%TXGROUP%	ToL_Durbin_TP10513_SNSF_Evolution_Collection Study_Bern
6592	blaxter/%TXGROUP%	Blaxter_RNA Sequencing for >260 Species of Nematode from 53 Genera - Blaxter Faculty
6585	vgp/%TXGROUP%	VGP_RNASeq
6583	blaxter/%TXGROUP%	Blaxter_Single nematode genomes'''


def __split_line(line):
    lims_id, hierarchy_name, name = line.split('\t')
    return int(lims_id), hierarchy_name, name

def __get_triplets():
    return [
        __split_line(line) for line in RAW_CONFIG.split('\n')
    ]

def __process_triplet(session, i, triplet):
    (lims_id, hierarchy_name, name) = triplet
    session.add(
        model.TolqcTrackConfig(
            id=i,
            lims_id=lims_id,
            hierarchy_name=hierarchy_name,
            name=name
        )
    )

def __add_track_config(session):
    for i, triplet in enumerate(__get_triplets()):
        __process_triplet(session, i, triplet)


def upgrade() -> None:
    bind = op.get_bind()
    session = orm.Session(bind=bind)
    op.create_table('track_config',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('lims_id', sa.INTEGER(), autoincrement=False),
    sa.Column('name', sa.String()),
    sa.Column('hierarchy_name', sa.String()),
    )
    __add_track_config(session)
    session.commit()


def downgrade() -> None:
    pass
