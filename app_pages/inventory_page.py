
import streamlit as st

from components.inventory_table import inventory_table
from app_pages.forms.inventory_form import inventory_form

def inventory_page(parts):

    st.title("📦 Inventory")

    tab1, tab2 = st.tabs(
        ["Inventory List", "Add Part"]
    )

    with tab1:
        inventory_table(parts)

    with tab2:
        inventory_form()
