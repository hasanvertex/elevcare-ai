import streamlit as st

from components.maintenance_table import maintenance_table
from app_pages.forms.maintenance_form import maintenance_form


def maintenance_page(maintenance):

    st.title("🔧 Maintenance")

    tab1, tab2 = st.tabs(
        ["Maintenance List", "Add Visit"]
    )

    with tab1:
        maintenance_table(maintenance)

    with tab2:
        maintenance_form()
