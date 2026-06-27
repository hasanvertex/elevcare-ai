import streamlit as st

from components.technician_table import technician_table
from app_pages.forms.technician_form import technician_form


def technicians_page(
    technicians,
    maintenance
):

    st.title("👨‍🔧 Technicians")

    tab1, tab2 = st.tabs(
        ["Technician List", "Add Technician"]
    )

    with tab1:
        technician_table(technicians)

    with tab2:
        technician_form()
