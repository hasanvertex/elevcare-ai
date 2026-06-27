
import streamlit as st

from components.work_order_table import work_order_table
from app_pages.forms.work_order_form import work_order_form

def work_order_page(work_orders):

    st.title("📝 Work Orders")

    tab1, tab2 = st.tabs(
        ["Work Orders", "Create Work Order"]
    )

    with tab1:
        work_order_table(work_orders)

    with tab2:
        work_order_form()
