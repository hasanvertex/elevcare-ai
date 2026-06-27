
import streamlit as st
import pandas as pd

def maintenance_trend(maintenance):

    st.subheader("🔧 Maintenance Trend")

    total = len(maintenance)

    data = pd.DataFrame({
        "Visits": [total]
    })

    st.bar_chart(data)
