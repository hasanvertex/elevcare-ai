import streamlit as st
from services.maintenance_service import save_maintenance


def maintenance_form():

    with st.form("maintenance_form"):

        visit_date = st.date_input("Visit Date")
        customer_id = st.text_input("Customer ID")
        elevator_id = st.text_input("Elevator ID")
        technician = st.text_input("Technician")
        remarks = st.text_area("Remarks")
        next_visit = st.date_input("Next Visit")

        submitted = st.form_submit_button(
            "Save Maintenance"
        )

    if submitted:

        data = {
            "visit_date": visit_date,
            "customer_id": customer_id,
            "elevator_id": elevator_id,
            "technician": technician,
            "remarks": remarks,
            "next_visit": next_visit
        }

        save_maintenance(data)

        st.success("Maintenance visit saved.")
        st.rerun()
