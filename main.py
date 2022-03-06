import streamlit as st

import protein
import file_loader
import drug_explorer
import similarity
import substructure
import presentation
import how_it_works

st.set_page_config(
    page_title="Bionever",
    page_icon="⚕️",
    layout="wide"
)
st.sidebar.image("./images/logo.png")
st.sidebar.title("Menu")
menu = st.sidebar.radio('',
    ("Home", "How it works", "Drug explorer", "Similarity", "Substructure", "Protein")
)
if (menu == "Home"):
    presentation.showpage()
if (menu == "Drug explorer"):
    drug_explorer.showpage()
if (menu == "Similarity"):
    similarity.showpage()
if (menu == "Substructure"):
    substructure.showpage()
if (menu == "Protein"):
    protein.showpage()
if (menu == "How it works"):
    how_it_works.showpage()


st.sidebar.write('')
st.sidebar.write('')
st.sidebar.write('')
link = '[GitHub](https://github.com/diabamine/PFE)'
st.sidebar.markdown(link, unsafe_allow_html=True)