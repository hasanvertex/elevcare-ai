import streamlit as st


def maintenance_table(maintenance):

    st.metric(
        "Total Visits",
        len(maintenance)
    )

    st.dataframe(
        maintenance,
        use_container_width=True
    )
