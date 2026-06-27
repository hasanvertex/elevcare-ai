
import streamlit as st

def customer_summary(customer):

    st.subheader("👤 Customer Information")

    col1, col2 = st.columns(2)

    col1.write("Customer ID")
    col1.info(customer.get("customer_id", "-"))

    col2.write("Customer Name")
    col2.info(customer.get("customer_name", "-"))
