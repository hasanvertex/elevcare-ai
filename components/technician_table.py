import streamlit as st


def technician_table(technicians):

    st.metric(
        "Total Technicians",
        len(technicians)
    )

    st.dataframe(
        technicians,
        use_container_width=True
    )
