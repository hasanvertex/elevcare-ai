
import streamlit as st

def technician_cards(
    total_technicians,
    total_orders,
    completed,
    pending
):

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Technicians",
        total_technicians
    )

    c2.metric(
        "Work Orders",
        total_orders
    )

    c3.metric(
        "Completed",
        completed
    )

    c4.metric(
        "Pending",
        pending
    )
