import streamlit as st
import pandas as pd


def contract_table(contracts):

    st.subheader("📄 Contract List")

    if len(contracts) == 0:
        st.info("No contracts found.")
        return

    df = pd.DataFrame(contracts)

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )