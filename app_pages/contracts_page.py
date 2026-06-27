import streamlit as st

from components.contract_table import contract_table
from app_pages.forms.contract_form import contract_form


def contracts_page(contracts):

    st.title("📄 Contracts")

    tab1, tab2 = st.tabs(
        ["Contract List", "Add Contract"]
    )

    with tab1:
        contract_table(contracts)

    with tab2:
        contract_form()
