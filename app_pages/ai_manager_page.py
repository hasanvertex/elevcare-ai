
import streamlit as st
from services.ai_service import ask_ai

def ai_manager_page(data):

    st.title("🤖 AI Manager")

    question = st.text_input(
        "Ask AI Manager"
    )

    if st.button("Ask"):

        answer = ask_ai(
            question,
            data
        )

        st.success(answer)
