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

#def substructure(mol1,mol2):
def substructure(mol1):
    sub = mol1
    #sub.GetSubstructMatches(mol2)
    st.write("2D structure")
    return sub

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
    st.title('Find Substructure')

    list_choice = ["Drug name", "Smile format"]
    choice = st.selectbox("What would you like to do ?", list_choice)

    if (choice == "Drug name"):
        compound_smiles=st.text_input('Enter a drug name','exanta')

        mol1=Chem.MolFromSmiles(search_molecule(compound_smiles))
        blk=makeblock(search_molecule(compound_smiles))
        render_mol(blk)

        sub = substructure(mol1)
        im=Draw.MolToImage(sub)
        st.image(im)

    if (choice == "Smile format"):
        mol = st.text_input('Enter a subsrtucture in smile format','')

        #3D
        blk = makeblock(mol)
        render_mol(blk)

        #2D 
        mol2=Chem.MolFromSmiles(mol)
        st.image(Chem.Draw.MolToImage(mol2))












