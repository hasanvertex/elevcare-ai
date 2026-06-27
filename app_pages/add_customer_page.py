import streamlit as st
import pandas as pd
import os


def add_customer_page():

    st.subheader("➕ Add New Customer")

    with st.form("customer_form"):

        customer_id = st.text_input("Customer ID")
        customer_name = st.text_input("Customer Name")
        company = st.text_input("Company")
        contact_person = st.text_input("Contact Person")
        phone = st.text_input("Phone")
        email = st.text_input("Email")
        address = st.text_area("Address")
        city = st.text_input("City")

        status = st.selectbox(
            "Status",
            ["Active", "Inactive"]
        )

        submitted = st.form_submit_button(
            "Save Customer"
        )

    if submitted:

        if customer_id == "" or customer_name == "":

            st.error(
                "Customer ID and Customer Name are required."
            )

            return

        new_customer = {
            "customer_id": customer_id,
            "customer_name": customer_name,
            "company": company,
            "contact_person": contact_person,
            "phone": phone,
            "email": email,
            "address": address,
            "city": city,
            "status": status
        }

        file_path = "database/customers.csv"

        if os.path.exists(file_path):

            df = pd.read_csv(file_path)

        else:

            df = pd.DataFrame()

        df = pd.concat(
            [df, pd.DataFrame([new_customer])],
            ignore_index=True
        )

        df.to_csv(
            file_path,
            index=False
        )

        st.success(
            "Customer added successfully."
        )

        st.rerun()