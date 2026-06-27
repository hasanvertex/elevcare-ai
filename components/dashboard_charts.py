import streamlit as st

from components.contract_chart import contract_chart
from components.maintenance_chart import maintenance_chart
from components.technician_chart import technician_chart

def dashboard_charts(maintenance, active, warning, expired):

    st.subheader("Analytics")

    contract_chart(active, warning, expired)

    st.divider()

    maintenance_chart(maintenance)

    st.divider()

    technician_chart()
