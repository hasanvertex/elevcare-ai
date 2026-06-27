import streamlit as st

from components.customer_table import customer_table
from app_pages.forms.customer_form import customer_form


def customers_page(
    customers,
    elevators,
    contracts
):

    st.title("👥 Customers")

    tab1, tab2 = st.tabs(
        ["Customer List", "Add Customer"]
    )

    with tab1:
        customer_table(customers)

    with tab2:
        customer_form()
