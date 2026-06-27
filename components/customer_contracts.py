
import streamlit as st

def customer_contracts(contracts):

    st.subheader("📄 Contracts")

    st.dataframe(
        contracts,
        use_container_width=True
    )
