
import streamlit as st
import pandas as pd

def contract_pie_chart(active, warning, expired):

    st.subheader("📊 Contract Status Chart")

    data = pd.DataFrame({
        "Count": [active, warning, expired]
    }, index=["Active", "Warning", "Expired"])

    st.bar_chart(data)
