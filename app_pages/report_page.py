
import streamlit as st

from components.report_buttons import report_buttons

def report_page():

    st.title("📄 PDF Reports")

    report_buttons()

    st.info(
        "PDF export module ready."
    )
