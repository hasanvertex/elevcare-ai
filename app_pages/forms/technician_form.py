import streamlit as st
from services.technician_service import save_technician


def technician_form():

    with st.form("technician_form"):

        technician_id = st.text_input("Technician ID")
        technician_name = st.text_input("Technician Name")
        phone = st.text_input("Phone")
        email = st.text_input("Email")

        status = st.selectbox(
            "Status",
            ["Active", "Inactive"]
        )

        submitted = st.form_submit_button(
            "Save Technician"
        )

    if submitted:

        data = {
            "technician_id": technician_id,
            "technician_name": technician_name,
            "phone": phone,
            "email": email,
            "status": status
        }

        save_technician(data)

        st.success("Technician saved.")
        st.rerun()
