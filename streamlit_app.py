import streamlit as st

st.set_page_config(page_title="NigerAI", page_icon="🇳🇪") 
st.image("logo.png", width=200)
st.title("🇳🇪 NigerAI")
st.write("Bienvenue ! Pose ta question pour réviser : Maths, Français, Physique, SVT, Histoire-Géo.")

matiere = st.selectbox("Choisis ta matière :", ["Maths", "Français", "Physique-Chimie", "SVT", "Histoire-Géo", "Anglais"])
question = st.text_input("Ta question :")

if st.button("Demander à NigerAI"):
    if question.strip() == "":
        st.warning("Écris d'abord ta question !")
    else:
        st.success(f"Super question en {matiere} !")
        st.write(f"**Ta question :** {question}")
        st.write("**Réponse de NigerAI :**")
        st.write("Voici comment réfléchir : 1) Relis bien l'énoncé, 2) Identifie ce qu'on te demande, 3) Cherche la formule / la règle du cours, 4) Fais le calcul étape par étape.")
        st.info("Astuce : Pour bien réviser, refais l'exercice sans regarder la correction, puis vérifie.")
        st.write("Si tu veux, pose une autre question ci-dessus !")

st.markdown("---")
st.caption("NigerAI - Fait pour les élèves du Niger")
