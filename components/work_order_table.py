
import streamlit as st

def work_order_table(data):

    st.metric(
        "Total Work Orders",
        len(data)
    )

    st.dataframe(
        data,
        use_container_width=True
    )
