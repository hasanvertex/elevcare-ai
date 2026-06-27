
import streamlit as st

from services.technician_dashboard_service import get_summary
from components.technician_cards import technician_cards
from components.technician_ranking import technician_ranking

def technician_dashboard_page(
    technicians,
    work_orders
):

    st.title(
        "👨‍🔧 Technician Dashboard"
    )

    total_technicians, total_orders, completed, pending = (
        get_summary(
            technicians,
            work_orders
        )
    )

    technician_cards(
        total_technicians,
        total_orders,
        completed,
        pending
    )

    st.divider()

    technician_ranking(
        work_orders
    )
