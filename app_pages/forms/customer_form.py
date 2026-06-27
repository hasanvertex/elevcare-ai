import streamlit as st
from services.customer_service import save_customer


def customer_form():

    with st.form("customer_form"):

        customer_id = st.text_input("Customer ID")
        customer_name = st.text_input("Customer Name")
        company = st.text_input("Company")
        phone = st.text_input("Phone")

        submitted = st.form_submit_button(
            "Save Customer"
        )

    if submitted:

        data = {
            "customer_id": customer_id,
            "customer_name": customer_name,
            "company": company,
            "phone": phone
        }

        save_customer(data)

        st.success("Customer saved.")
        st.rerun()
