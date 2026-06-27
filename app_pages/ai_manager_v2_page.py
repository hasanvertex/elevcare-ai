import streamlit as st

from services.ai_manager_service import ask_manager

def ai_manager_v2_page(data):

    st.title("🤖 AI Manager V2")

    question = st.text_input(
        "Ask AI Manager"
    )

    if st.button("Ask AI"):

        answer = ask_manager(
            question,
            data
        )

        st.success(answer)
