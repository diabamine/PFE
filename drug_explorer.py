import streamlit as st
from stmol import showmol
import py3Dmol
import pubchempy as pcp
from rdkit import Chem
from rdkit.Chem import Lipinski
from rdkit.Chem import Crippen
from rdkit.Chem import Descriptors
from rdkit.ML.Descriptors.MoleculeDescriptors import MolecularDescriptorCalculator
from rdkit.Chem import AllChem
from rdkit import DataStructs
import os

def convert_smile_to_sdf(smile, name):
    
    mol = Chem.MolFromSmiles(smile)
    hmol = Chem.AddHs(mol)
    AllChem.EmbedMolecule(hmol,AllChem.ETKDG())
    fullpath = os.path.join("compound_files", name)
    writer = Chem.SDWriter(fullpath +'.sdf')
    hmol.SetProp("_Library","%s"%smile)
    hmol.SetProp("_Name","%s"%name)
    hmol.SetProp("_SourceID","%s"%name)
    hmol.SetProp("_SMILES","%s"%smile)
    writer.write(hmol)
    writer.close()
    
    return fullpath +'.sdf'

def search_molecule(mol):
    drug = pcp.get_compounds(mol, 'name')
    return drug[0].isomeric_smiles


def lipinski(mol):
    logp = Crippen.MolLogP(mol)
    mw = Descriptors.MolWt(mol)
    nba = Lipinski.NumHAcceptors(mol)
    nbd = Lipinski.NumHDonors(mol)
    st.markdown('## Lipinski Rule of 5')
    if logp < 5:
        st.metric(label='LogP: ', value=round(logp, 2), delta='< 5')
    else:
        st.metric(label='LogP: ', value=round(logp, 2), delta='< 5', delta_color="inverse")
    if mw < 500:
        st.metric(label='Molecular Weight: ', value=round(Descriptors.MolWt(mol), 2), delta='< 500')
    else:
        st.metric(label='Molecular Weight: ', value=round(Descriptors.MolWt(mol), 2), delta='< 500',
                  delta_color="inverse")
    if nbd < 5:
        st.metric(label='Nb of Hydrogen Donors: ', value=round(Lipinski.NumHDonors(mol), 2), delta='< 5')
    else:
        st.metric(label='Nb of Hydrogen Donors: ', value=round(Lipinski.NumHDonors(mol), 2), delta='< 5',
                  delta_color="inverse")
    if nba < 10:
        st.metric(label='Nb of Hydrogen Acceptors: ', value=round(Lipinski.NumHAcceptors(mol), 2), delta='< 10')
    else:
        st.metric(label='Nb of Hydrogen Acceptors: ', value=round(Lipinski.NumHAcceptors(mol), 2), delta='< 10',
                  delta_color="inverse")


def makeblock(smi):
    mol = Chem.MolFromSmiles(smi)
    mol = Chem.AddHs(mol)
    AllChem.EmbedMolecule(mol)
    mblock = Chem.MolToMolBlock(mol)
    return mblock


def render_mol(xyz):
    xyzview = py3Dmol.view()
    xyzview.addModel(xyz, 'mol')
    xyzview.setStyle({'stick': {}})
    xyzview.setBackgroundColor('white')
    xyzview.zoomTo()
    showmol(xyzview, height=500, width=800)


def showpage():
    st.title('💊 Search Compound')
    compound_smiles = st.text_input('Enter a drug name', 'imatinib')
    blk = makeblock(search_molecule(compound_smiles))

    col1, col2 = st.columns([4, 2])

    with col1:
        render_mol(blk)
        fullpath = convert_smile_to_sdf(search_molecule(compound_smiles), compound_smiles)
        with open(fullpath, "rb") as file:
                btn = st.download_button(
                    label="Download in sdf format",
                    data=file,
                    file_name=compound_smiles+".sdf",
                    mime=None
                )
    with col2:
        lipinski(Chem.MolFromSmiles(search_molecule(compound_smiles)))