
import streamlit as st

def qr_generator(data):

    st.code(data)

    st.info(
        "QR generation service ready."
    )
