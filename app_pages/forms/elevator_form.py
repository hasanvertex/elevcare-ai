import streamlit as st
from services.elevator_service import save_elevator


def elevator_form():

    with st.form("elevator_form"):

        elevator_id = st.text_input("Elevator ID")
        customer_id = st.text_input("Customer ID")
        elevator_name = st.text_input("Elevator Name")
        capacity = st.text_input("Capacity")
        floors = st.number_input("Floors", min_value=1, step=1)
        status = st.selectbox(
            "Status",
            ["Active", "Inactive"]
        )

        submitted = st.form_submit_button(
            "Save Elevator"
        )

    if submitted:

        data = {
            "elevator_id": elevator_id,
            "customer_id": customer_id,
            "elevator_name": elevator_name,
            "capacity": capacity,
            "floors": floors,
            "status": status
        }

        save_elevator(data)

        st.success("Elevator saved.")
        st.rerun()
