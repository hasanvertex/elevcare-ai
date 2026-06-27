
import streamlit as st

from services.qr_service import create_qr_text
from components.qr_generator import qr_generator
from components.qr_card import qr_card

def qr_page():

    st.title("📱 QR Code System")

    elevator_id = st.text_input("Elevator ID")
    customer = st.text_input("Customer")
    status = st.selectbox(
        "Status",
        ["Active", "Warning", "Expired"]
    )
    next_visit = st.text_input("Next Visit")
    technician = st.text_input("Technician")

    if st.button("Generate QR"):

        data = create_qr_text(
            elevator_id,
            customer,
            status,
            next_visit,
            technician
        )

        qr_card(
            elevator_id,
            customer,
            status
        )

        qr_generator(data)
