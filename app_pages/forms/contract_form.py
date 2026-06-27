import streamlit as st
from services.contract_service import save_contract


def contract_form():

    with st.form("contract_form"):

        contract_id = st.text_input("Contract ID")
        customer_id = st.text_input("Customer ID")
        elevator_id = st.text_input("Elevator ID")
        start_date = st.date_input("Start Date")
        end_date = st.date_input("End Date")
        amount = st.number_input("Amount", min_value=0.0)

        submitted = st.form_submit_button(
            "Save Contract"
        )

    if submitted:

        data = {
            "contract_id": contract_id,
            "customer_id": customer_id,
            "elevator_id": elevator_id,
            "start_date": start_date,
            "end_date": end_date,
            "amount": amount
        }

        save_contract(data)

        st.success("Contract saved.")
        st.rerun()
