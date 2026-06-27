
import streamlit as st

def qr_card(
    elevator_id,
    customer,
    status
):

    st.subheader("📱 Elevator QR")

    st.success(
        f'''
Elevator: {elevator_id}

Customer: {customer}

Status: {status}
'''
    )
