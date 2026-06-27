import streamlit as st

def manager_cards(summary):

    c1, c2, c3 = st.columns(3)
    c4, c5, c6 = st.columns(3)

    c1.metric("Customers", summary["customers"])
    c2.metric("Elevators", summary["elevators"])
    c3.metric("Contracts", summary["contracts"])

    c4.metric("Maintenance", summary["maintenance"])
    c5.metric("Technicians", summary["technicians"])
    c6.metric("Work Orders", summary["work_orders"])
