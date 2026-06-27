import streamlit as st


def elevator_table(elevators):

    st.metric(
        "Total Elevators",
        len(elevators)
    )

    st.dataframe(
        elevators,
        use_container_width=True
    )
