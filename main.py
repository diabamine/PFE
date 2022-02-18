import streamlit as st

#import des autres pages
import protein
import file_loader
import drug_explorer
import similarity
import substructure
import presentation


menu = st.sidebar.radio(
    "MENU",
    ("Présentation","Drug explorer", "File loader", "Protein", "Similarity", "Substructure")
)
if (menu == "Présentation"):
    presentation.showpage()
if (menu == "Drug explorer"):
    drug_explorer.showpage()
if (menu == "File loader"):
    file_loader.showpage()
if (menu == "Protein"):
    protein.showpage()
if (menu == "Similarity"):
    similarity.showpage()
if (menu == "Substructure"):
    substructure.showpage()
