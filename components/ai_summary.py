
import streamlit as st


def ai_summary(
    active,
    warning,
    expired,
    maintenance_count
):

    st.subheader("🤖 AI Manager Summary")

    st.success(
        f"Active Contracts: {active}"
    )

    st.warning(
        f"Contracts needing attention: {warning}"
    )

    st.error(
        f"Expired Contracts: {expired}"
    )

    st.info(
        f"Maintenance Visits: {maintenance_count}"
    )
