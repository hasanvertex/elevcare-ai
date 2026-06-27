import streamlit as st
import pandas as pd


def crm_chart():

    data = pd.DataFrame(
        {
            "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
            "Visits": [40, 30, 20, 27, 35, 45]
        }
    )

    st.subheader("📈 Maintenance Trends")

    st.line_chart(
        data.set_index("Month")
    )