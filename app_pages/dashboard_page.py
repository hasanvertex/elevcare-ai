import streamlit as st

from components.crm_header import crm_header
from components.crm_cards import crm_cards
from components.crm_contract_widget import crm_contract_widget
from components.crm_chart import crm_chart
from components.crm_table import crm_table
from components.system_widget import system_widget
from components.ai_widget import ai_widget


def dashboard_page(
    customers,
    elevators,
    contracts,
    maintenance,
    active,
    warning,
    expired,
    alerts
):

    crm_header()

    st.divider()

    crm_cards()

    st.divider()

    crm_contract_widget()

    st.divider()

    crm_chart()

    st.divider()

    system_widget()

    st.divider()

    crm_table()

    st.divider()

    ai_widget()