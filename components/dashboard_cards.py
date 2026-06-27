import streamlit as st

def dashboard_cards(summary):

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Customers", summary["customers"])
    c2.metric("Elevators", summary["elevators"])
    c3.metric("Contracts", summary["contracts"])
    c4.metric("Maintenance", summary["maintenance"])
