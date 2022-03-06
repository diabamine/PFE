import streamlit as st

def showpage():
    st.title("🧠 How it works")

    
    st.markdown("""
    Ce dashboard a été conçu en utilisant les différents composants décrit sur le schéma suivant:
    """)
    st.image("./images/diagram.png")
    st.markdown("""
    Le programme envoie des requêtes aux différentes bases de données et les traite pour assurer leur affichage
    - Différentes API ont été utlilisées pour collecter les données (Pubchem, NCBI, Protein Data Bank)
    - Le module RDKIT a été utilisé pour manipuler les objects moléculaire collecter depuis les bases
    - Le module Streamlit a été utlisé pour construire un dashboard responsive permettant une navigation fluide et intuitive
    """)


   