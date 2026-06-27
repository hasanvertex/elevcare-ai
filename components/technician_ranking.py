
import streamlit as st

def technician_ranking(work_orders):

    st.subheader(
        "🏆 Technician Ranking"
    )

    if len(work_orders) == 0:
        st.info("No work orders found.")
        return

    ranking = (
        work_orders["technician"]
        .value_counts()
        .reset_index()
    )

    ranking.columns = [
        "Technician",
        "Jobs"
    ]

    st.dataframe(
        ranking,
        use_container_width=True
    )
