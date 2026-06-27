import streamlit as st

from services.manager_service import get_manager_summary
from components.manager_cards import manager_cards
from components.manager_alerts import manager_alerts

def manager_dashboard_page(data):

    st.title("📈 Manager Dashboard")

    summary = get_manager_summary(data)

    manager_cards(summary)

    st.divider()

    manager_alerts()
