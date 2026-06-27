
import streamlit as st

from components.customer_summary import customer_summary
from components.customer_contracts import customer_contracts
from components.customer_maintenance import customer_maintenance

def customer_details_page(
    customer,
    contracts,
    maintenance
):

    st.title("🏢 Customer Details")

    customer_summary(customer)

    st.divider()

    customer_contracts(contracts)

    st.divider()

    customer_maintenance(maintenance)
