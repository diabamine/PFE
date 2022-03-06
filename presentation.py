import streamlit as st

def showpage():
    st.title("⚕️ Bionever Dashboard")

    with st.expander("Notre équipe"):
        st.markdown("""
           Pour réaliser ce projet nous sommes une équipe de 8 personnes. Afin d’organiser nos travaux, nous avons décidé de nous attribuer des rôles bien définis.   
           Nous avons élaboré un pôle technique composé de Chloé et Antoine pour la partie développement, et de Déborah et Clémence pour la partie data management, présidé par Amine en charge du suivi des modifications apportées au corps du Dashboard.
           Thomas a encadré l’ensemble de l’équipe pour faciliter l’organisation et les échanges entre le pôle technique et les deux autres pôles du projets, composés de Damien et de Juliette.
           """)
        st.image("./images/team.png")


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

    with st.expander("L'origine des données "):
        st.markdown("""
        PubChem est une banque de données américaine de molécules chimiques gérée par le National Center for Biotechnology Information (NCBI), branche de la Bibliothèque nationale de médecine des États-Unis sous l'autorité des National Institutes of Health (NIH).
        PubChem répertorie plusieurs millions de composés en mettant gratuitement en ligne, pour chaque substance, une grande quantité de données de divers ordres : chimique, biochimique, pharmacologique, production, toxicologique, environnemental, etc.  
        (source wikipedia)
        """)
        st.image("./images/PubChem.JPG")

    with st.expander("Règles de lipinski"):
        st.markdown("""
            La règle de Lipinski stipule qu'en général, un médicament actif par voie orale n'a pas plus d'une violation des critères suivants :    
            - Pas plus de 5 liaison hydrogène donneurs (le nombre total d' azote - hydrogène et oxygène -hydrogène obligations )   
            - Pas plus de 10 accepteurs de liaisons hydrogène (tous les atomes d' azote ou d' oxygène )   
            - Une masse moléculaire inférieure à 500 daltons  
            - Un coefficient de partage octanol-eau [10] (log P ) ne dépassant pas 5   
        """)


