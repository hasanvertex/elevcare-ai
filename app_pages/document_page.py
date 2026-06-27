
import streamlit as st

from components.photo_upload import photo_upload
from components.document_upload import document_upload
from components.photo_gallery import photo_gallery

def document_page():

    st.title("📷 Photos & Documents")

    before_photo, after_photo = photo_upload()

    contract_pdf, handover_pdf = document_upload()

    photo_gallery(
        before_photo,
        after_photo
    )

    if contract_pdf:
        st.success(
            f"Contract: {contract_pdf.name}"
        )

    if handover_pdf:
        st.success(
            f"Handover: {handover_pdf.name}"
        )
