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


from rdkit.Chem import rdDepictor
from rdkit.Chem.Draw import rdMolDraw2D
from IPython.display import SVG
from svglib.svglib import svg2rlg
#from reportlab.graphics import renderPDF, renderPM


st.title('Find Substructure')

# tried to convert substructure molecule into svg to be display bu streamlit image component -> fail
def increase_resolution(mol, substructure, size=(400, 200)):
    rdDepictor.Compute2DCoords(mol)
    Chem.Kekulize(mol) # Localize the benzene ring bonds
    
    drawer = rdMolDraw2D.MolDraw2DSVG(size[0], size[1])
    
    # highlightAtoms expects only one tuple, not tuple of tuples. So it needs to be merged into a single tuple
    matches = sum(mol.GetSubstructMatches(substructure), ())
    drawer.DrawMolecule(mol, highlightAtoms=matches)
    
    drawer.FinishDrawing()
    svg = drawer.GetDrawingText()
    
    return SVG(svg.replace('svg:',''))



def search_molecule(mol):
    drug = pcp.get_compounds(mol,'name')
    # show chemical formula
    return drug[0].isomeric_smiles

def substructure(mol1,mol2):
    sub = mol1
    sub.GetSubstructMatches(mol2)
    return sub

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

compound_smiles=st.text_input('Enter a drug name','exanta')
mol = st.text_input('Enter a a subsrtucture in smile format','C=O')
mol1=Chem.MolFromSmiles(search_molecule(compound_smiles))
mol2=Chem.MolFromSmiles(mol)

blk=makeblock(search_molecule(compound_smiles))
#render_mol(blk)

# mol display right but the substructure highlight do not appear
#sub = substructure(mol1,mol2)
#im=Draw.MolToImage(sub)


sub = increase_resolution(mol1, mol2)
# convert svg image into byte-like object 
drawing = svg2rlg(sub)
st.image(drawing)