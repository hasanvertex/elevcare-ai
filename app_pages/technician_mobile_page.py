import streamlit as st

from services.mobile_service import get_pending_jobs
from components.job_card import job_card
from components.visit_form import visit_form

def technician_mobile_page(work_orders):

    st.title("📱 Technician Mobile Dashboard")

    jobs = get_pending_jobs(work_orders)

    job_card(jobs)

    st.divider()

    visit_form()
