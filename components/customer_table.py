import streamlit as st


def customer_table(customers):

    st.metric("Total Customers", len(customers))

    st.dataframe(
        customers,
        use_container_width=True
    )
