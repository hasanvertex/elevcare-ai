
import streamlit as st

def document_upload():

    st.subheader("📄 Documents")

    contract_pdf = st.file_uploader(
        "Contract PDF",
        type=["pdf"],
        key="contract_pdf"
    )

    handover_pdf = st.file_uploader(
        "Handover Document",
        type=["pdf"],
        key="handover_pdf"
    )

    return contract_pdf, handover_pdf
