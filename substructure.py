import streamlit as st
from stmol import showmol
import py3Dmol
import pubchempy as pcp
from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem import Lipinski
from rdkit.Chem import Crippen
from rdkit.Chem import Descriptors
from rdkit.ML.Descriptors.MoleculeDescriptors import MolecularDescriptorCalculator
from rdkit.Chem import AllChem
from rdkit import DataStructs


def search_molecule(mol):
    drug = pcp.get_compounds(mol,'name')
    # show chemical formula
    return drug[0].isomeric_smiles

def substructure(mol1,mol2):
    sub = mol1
    sub.GetSubstructMatches(mol2)
    st.write("2D structure")
    im=Draw.MolToImage(sub)
    st.image(im)

def makeblock(smi):
    mol = Chem.MolFromSmiles(smi)
    mol = Chem.AddHs(mol)
    AllChem.EmbedMolecule(mol)
    mblock = Chem.MolToMolBlock(mol) 
    return mblock

def render_mol(xyz):
    st.write("3D structure")
    xyzview = py3Dmol.view()
    xyzview.addModel(xyz,'mol')
    xyzview.setStyle({'stick':{}})
    xyzview.setBackgroundColor('white')
    xyzview.zoomTo()
    showmol(xyzview,height=500,width=800)

def showpage():
    st.title('⚛️ Find Substructure')

    
    compound_smiles=st.text_input('Enter a drug name','exanta')
    smile_2=st.text_input('Enter a SMILE formula','C=O')

    col1, col2 = st.columns([2,2])

    mol1=Chem.MolFromSmiles(search_molecule(compound_smiles))
    mol2=Chem.MolFromSmiles(smile_2)
    blk=makeblock(search_molecule(compound_smiles))
    with col1:
        render_mol(blk)
    
    with col2:
        substructure(mol1,mol2)
    










