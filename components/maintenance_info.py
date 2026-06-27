
import streamlit as st

def maintenance_info(record):

    st.subheader("🔧 Maintenance Information")

    col1, col2 = st.columns(2)

    col1.info(record.get("customer_id", "-"))
    col2.info(record.get("technician", "-"))

    st.write("Visit Date:", record.get("visit_date", "-"))
    st.write("Next Visit:", record.get("next_visit", "-"))
