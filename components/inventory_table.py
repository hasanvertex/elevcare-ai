
import streamlit as st

def inventory_table(data):

    st.metric(
        "Total Parts",
        len(data)
    )

    st.dataframe(
        data,
        use_container_width=True
    )
