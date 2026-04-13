import streamlit as st
from router import Router

# Initialisation globale
if "router" not in st.session_state:
    st.session_state.router = Router()
    st.session_state.history = []

router = st.session_state.router

# --- UI ---
st.set_page_config(page_title="Assistant DIH", page_icon="⚖️")
st.title("⚖️ Assistant Intelligent — Droit International Humanitaire")

st.markdown("""
Cet assistant combine :
- **RAG** (documents internes DIH)
- **Agents** (calcul, météo, recherche web)
- **Mémoire conversationnelle**
""")

# Champ utilisateur
query = st.text_input("Pose ta question :", placeholder="Ex : Quelle est la définition du génocide ?")

if query:
    # Router → Agent ou RAG ou Chat
    answer = router.route(query)

    # Sauvegarde dans l'historique
    st.session_state.history.append(("Vous", query))
    st.session_state.history.append(("Assistant", answer))

    # Affichage
    st.markdown("### 💬 Réponse")
    st.write(answer)

# Historique
st.markdown("---")
st.markdown("### 🕒 Historique de conversation")

for speaker, msg in st.session_state.history:
    if speaker == "Vous":
        st.markdown(f"**🧑 Vous :** {msg}")
    else:
        st.markdown(f"**🤖 Assistant :** {msg}")
