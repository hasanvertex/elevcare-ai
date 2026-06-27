import streamlit as st

from components.elevator_table import elevator_table
from app_pages.forms.elevator_form import elevator_form


def elevators_page(
    elevators,
    maintenance
):

    st.title("🏢 Elevators")

    tab1, tab2 = st.tabs(
        ["Elevator List", "Add Elevator"]
    )

    with tab1:
        elevator_table(elevators)

    with tab2:
        elevator_form()
