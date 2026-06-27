
import streamlit as st

from components.maintenance_info import maintenance_info
from components.maintenance_work import maintenance_work

def maintenance_details_page(record):

    st.title("🔧 Maintenance Details")

    maintenance_info(record)

    st.divider()

    maintenance_work(record)
