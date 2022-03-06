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

#st.set_page_config(layout=‘wide’)


def search_molecule(mol):
    drug = pcp.get_compounds(mol,'name')
    # show chemical formula
    return drug[0].isomeric_smiles


def to_morganfingerprinting(smile):
    mol = Chem.MolFromSmiles(smile)
    fingerprint = AllChem.GetMorganFingerprintAsBitVect(mol,radius=2,nBits=1024)
    return fingerprint


def similarity(smile1,smile2):
    fing1 = to_morganfingerprinting(smile1)
    fing2 = to_morganfingerprinting(smile2)
    return(DataStructs.TanimotoSimilarity(fing1,fing2),
            DataStructs.DiceSimilarity(fing1,fing2))



def makeblock(smi):
    mol = Chem.MolFromSmiles(smi)
    mol = Chem.AddHs(mol)
    AllChem.EmbedMolecule(mol)
    mblock = Chem.MolToMolBlock(mol)
    return mblock

def render_mol(xyz):
    xyzview = py3Dmol.view()
    xyzview.addModel(xyz,'mol')
    xyzview.setStyle({'stick':{}})
    xyzview.setBackgroundColor('white')
    xyzview.zoomTo()
    showmol(xyzview,height=500,width=800)



def showpage():
    st.title('⚖️ Compound Similarity')
    col1, col2 = st.columns([5,5])

    with col1:
        compound_1 = st.text_input('Enter a drug 1','aciclovir')
        smile_1 = search_molecule(compound_1)
        struct_1 = makeblock(smile_1)
        render_mol(struct_1)
    with col2:
        compound_2 = st.text_input('Enter a drug 2','penciclovir')
        smile_2 = search_molecule(compound_2)
        struct_2 = makeblock(smile_2)
        render_mol(struct_2)

    st.markdown("<h3 style='text-align: center;'>Similarity Score</h3>", unsafe_allow_html=True)

    col3, col4, col5, col6 = st.columns([4.5,2,2,3])
    with col3:
        st.write("")
    with col4:
        tanimoto = similarity(smile_1,smile_2)
        st.metric(label='Tanimoto: ',value=round(tanimoto[0],2))
    with col5:
        dice = similarity(smile_1,smile_2)
        st.metric(label='Dice: ',value=round(dice[1],2))
    with col6:
        st.write("")