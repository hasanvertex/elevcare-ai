import streamlit as st
import pandas as pd


def charts():

    df = pd.DataFrame(
        {
            "Month": ["Jan", "Feb", "Mar", "Apr"],
            "Visits": [20, 30, 40, 35]
        }
    )

    st.line_chart(
        df.set_index("Month")
    )