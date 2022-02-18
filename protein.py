import streamlit as st
import py3Dmol
from stmol import showmol
from Bio.Seq import Seq
from Bio.Blast import NCBIWWW



def showpage():
    st.sidebar.title('Show Proteins')

    list_choice = ["Write sequence", "Choose protein"]
    choice = st.sidebar.selectbox("What would you like to do ?", list_choice)

    if (choice == "Choose protein"):
        prot_str = '1A2C,1BML,1D5M,1D5X,1D5Z,1D6E,1DEE,1E9F,1FC2,1FCC,1G4U,1GZS,1HE1,1HEZ,1HQR,1HXY,1IBX,1JBU,1JWM,1JWS'
        prot_list = prot_str.split(',')
        bcolor = st.sidebar.color_picker('Background color : ', '#000000')
        protein = st.sidebar.selectbox('Select protein', prot_list)
        style = st.sidebar.selectbox('Style', ['line', 'cross', 'stick', 'sphere', 'cartoon', 'clicksphere'])
        spin = st.sidebar.checkbox('Spin', value=False)
        xyzview = py3Dmol.view(query='pdb:' + protein)
        xyzview.setStyle({style: {'color': 'spectrum'}})
        xyzview.setBackgroundColor(bcolor)
        if spin:
            xyzview.spin(True)
        else:
            xyzview.spin(False)
        xyzview.zoomTo()
        showmol(xyzview, height=800, width=1000)

    if (choice == "Write sequence"):
        cond = 0
        sequence = st.text_input("Write sequence (Capitals letters) : ")

        list_nt = ['A','C', 'T', 'G']
        list_comparison = list(set(sequence) - set(list_nt))
        if len(list_comparison) != 0:
            st.write('The sequence has unknown nucleotides : ', list_comparison)
            cond = 1
        if (cond == 0): #If the sequence is ok; with no unknown nucleotide
            ADN = Seq(sequence)
            protein = ADN.translate()
            st.write(protein.translate())

            se = "MVLSTADKNNVKTTWDKIGGHAPEYVAEGLTRMFTSFPTTKTYFHHIDVSPGSGDIKAHGKKVADALTTAVGHLDDLPTALSTLSDVHAHKLRVDPVNFKFLNHCLLVTLAAHLGADFTPSIHASLDKFFASVSTVLTSKYR"

            
            #result_handleB = NCBIWWW.qblast("blastp", "pdb", record.format("fasta"), ncbi_gi=False, descriptions= "1", alignments="1", format_type="XML", hitlist_size="1", entrez_query=se)
			#blast_recordsB = NCBIXML.read(result_handleB)

			#st.write(blast_recordsB)
			#st.write(result_handleB)


            #t = NCBIWWW.qblast(program='blastp', database='pdb',sequence=se)
            #st.write(t)
            #xyzview = py3Dmol.view(query='pdb:' + protein)
            #xyzview.spin(False)
            #showmol(xyzview, height=800, width=1000)


            #Structure 3D a partir du code smile






