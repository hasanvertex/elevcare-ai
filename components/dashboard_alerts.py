import streamlit as st


def dashboard_alerts(
    active,
    warning,
    expired
):

    st.subheader("Contract Status")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Active",
        active
    )

    col2.metric(
        "Warning",
        warning
    )

    col3.metric(
        "Expired",
        expired
    )
