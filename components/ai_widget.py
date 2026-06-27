
import streamlit as st

def ai_widget():

    st.divider()

    st.subheader("🤖 AI Manager V2")

    question = st.text_input(
        "Ask AI Manager"
    )

    if st.button("Ask AI"):
        st.success(
            "AI response will appear here."
        )
