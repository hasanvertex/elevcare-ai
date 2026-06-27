import streamlit as st


def maintenance_chart(maintenance):

    st.subheader("🔧 Maintenance")

    st.metric(
        "Total Visits",
        len(maintenance)
    )
