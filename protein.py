from time import process_time_ns
import streamlit as st
import py3Dmol
from stmol import showmol
from Bio.Seq import Seq
from Bio.Blast import NCBIWWW
from Bio.PDB import *
from pypdb import *
import os
from Bio import Entrez
import re


def data_from_pdb(protein):
    st.write('')
    st.write('')
    st.write('')
    all_info = get_info(protein)
    st.write('Title: ',all_info['citation'][0]['title'])
    st.write('Classification: ',all_info['struct_keywords']['pdbx_keywords'])
    st.write('Type: ',all_info['struct']['pdbx_descriptor'])
    st.write('Method: ',all_info['exptl'][0]['method'])

def get_organism_using_entrez(id):
    Entrez.email = "mohamed-amine.diab@efrei.net"
    handle = Entrez.esearch(db="protein", retmax=10, term=id)
    record = Entrez.read(handle)
    handle.close()
    handle = Entrez.efetch(db="protein", id=record['IdList'][0], retmode='xml')
    res = handle.read().decode(encoding='cp866', errors='ignore' )
    organism = re.findall('<GBSeq_organism>\w+\s\w+', res)[0].replace('<GBSeq_organism>','')
    st.write('Organism: ',organism)
    st.write('')

def showpage():

    pdbl = PDBList()
    base_dir = 'PDB_files'
    extension = ".cif"
    st.title('🔬 Protein explorer')    

    st.sidebar.title('Show Proteins')

    list_choice = ["Choose protein", "Search a PDB structure"]
    choice = st.sidebar.selectbox("What would you like to do ?", list_choice)

    if (choice == "Choose protein"):
        prot_str = '1A2C,1BML,1D5M,1D5X,1D5Z,1D6E,1DEE,1E9F,1FC2,1FCC,1G4U,1GZS,1HE1,1HEZ,1HQR,1HXY,1IBX,1JBU,1JWM,1JWS'
        prot_list = prot_str.split(',')
        bcolor = st.sidebar.color_picker('Background color : ', '#FFFFFF')
        protein = st.sidebar.selectbox('Select protein', prot_list)
        style = st.sidebar.selectbox('Style', ['cartoon', 'line', 'cross', 'stick', 'sphere', 'clicksphere'])
        spin = st.sidebar.checkbox('Spin', value=False)
        xyzview = py3Dmol.view(query='pdb:' + protein)
        xyzview.setStyle({style: {'color': 'spectrum'}})
        xyzview.setBackgroundColor(bcolor)
        if spin:
            xyzview.spin(True)
        else:
            xyzview.spin(False)
        xyzview.zoomTo()
        
        pdbl.retrieve_pdb_file(protein, pdir=base_dir)
        filename = protein + extension
        fullpath = os.path.join(base_dir, filename.lower())

        col1,col2 = st.columns([4,2])
        with col1:
            st.write("3D structure of ",protein," :")
            showmol(xyzview, height=800, width=1000)
        with col2:
            st.write('Protein info ',protein,' :')
            data_from_pdb(protein)
            get_organism_using_entrez(protein)
            with open(fullpath, "rb") as file:
                btn = st.download_button(
                    label="Download in cif format",
                    data=file,
                    file_name=filename.lower(),
                    mime=None
                )


    if (choice == "Search a PDB structure"):
        
        protein = st.text_input("Write PDB id : ",'1A2C')

        bcolor = st.sidebar.color_picker('Background color : ', '#FFFFFF')
        style = st.sidebar.selectbox('Style', ['cartoon', 'line', 'cross', 'stick', 'sphere', 'clicksphere'])
        spin = st.sidebar.checkbox('Spin', value=False)
        xyzview = py3Dmol.view(query='pdb:' + protein)
        xyzview.setStyle({style: {'color': 'spectrum'}})
        xyzview.setBackgroundColor(bcolor)
        if spin:
            xyzview.spin(True)
        else:
            xyzview.spin(False)
        xyzview.zoomTo()

        pdbl.retrieve_pdb_file(protein, pdir=base_dir)
        filename = protein + extension
        fullpath = os.path.join(base_dir, filename.lower())

        col1,col2 = st.columns([4,2])
        with col1:
            st.write("3D structure of ",protein," :")
            showmol(xyzview, height=800, width=1000)
        with col2:
            st.write('Protein info ',protein,' :')
            data_from_pdb(protein)
            get_organism_using_entrez(protein)
            with open(fullpath, "rb") as file:
                btn = st.download_button(
                    label="Download in cif format",
                    data=file,
                    file_name=filename.lower(),
                    mime=None
                )






