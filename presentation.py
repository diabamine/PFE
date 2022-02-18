import streamlit as st

def showpage():
    st.title("Projet fin d'études M2 Bio-informatique")

    with st.expander("L'informatique au service du drug design"):
        st.markdown("""
        Le développement de nouveaux médicaments est extrêmement coûteux et long. Le processus prend plusieurs années et des millions de dollars :  
        - Recherche amont : 300M $   
        - Essais cliniques : 500M $
        Pour voir si des composés peuvent être des candidats à un médicament des essais vont être réalisés pour passer de l'ordre du million de molécules potentiellement candidates à entre 5 et 10 candidats pour les phases préclinique.
        """)
        st.image("./images/drugdesign.png")
        st.markdown("""
        L'intérêt de l'informatique pour le drug design est donc de faire un filtrage des molécules via différentes méthodes :   
        - Docking scoring   
        - Vérification des règles de Lipinski
        """)


    with st.expander("Règles de lipinski"):
        st.markdown("""
            La règle de Lipinski stipule qu'en général, un médicament actif par voie orale n'a pas plus d'une violation des critères suivants :    
            - Pas plus de 5 liaison hydrogène donneurs (le nombre total d' azote - hydrogène et oxygène -hydrogène obligations )   
            - Pas plus de 10 accepteurs de liaisons hydrogène (tous les atomes d' azote ou d' oxygène )   
            - Une masse moléculaire inférieure à 500 daltons  
            - Un coefficient de partage octanol-eau [10] (log P ) ne dépassant pas 5   
        """)

