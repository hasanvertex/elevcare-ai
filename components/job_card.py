import streamlit as st

def job_card(data):

    st.subheader("📋 Assigned Jobs")

    st.dataframe(
        data,
        use_container_width=True
    )
