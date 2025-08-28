import streamlit as st
from app.localization import Localization

def render_settings():
    #st.slider("Wie streng soll bewertet werden", ["streng", "großzügig"]) #klappt irgendwie noch nicht
    st.session_state["question_amount"] = st.slider(
        Localization.get("question_amount"), 
        min_value=1, 
        max_value=10, 
        value=st.session_state["question_amount"]
    )
    st.session_state["group_coupled_questions"]  = st.checkbox(
        Localization.get("group_coupled_questions"), 
        value=st.session_state["group_coupled_questions"]
    )
    st.session_state["shuffle_questions"] = st.checkbox(
        Localization.get("shuffle_questions"),
        value=st.session_state["shuffle_questions"]
    )