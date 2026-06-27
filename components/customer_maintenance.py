
import streamlit as st

def customer_maintenance(maintenance):

    st.subheader("🔧 Maintenance History")

    st.dataframe(
        maintenance,
        use_container_width=True
    )
