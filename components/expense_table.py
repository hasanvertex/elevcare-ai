
import streamlit as st

def expense_table(data):

    st.metric(
        "Total Expenses",
        len(data)
    )

    st.dataframe(
        data,
        use_container_width=True
    )
