import streamlit as st


def manager_dashboard(summary):

    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)

    col1.metric(
        "Customers",
        summary["customers"]
    )

    col2.metric(
        "Elevators",
        summary["elevators"]
    )

    col3.metric(
        "Contracts",
        summary["contracts"]
    )

    col4.metric(
        "Maintenance",
        summary["maintenance"]
    )