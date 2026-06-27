import streamlit as st

from services.calendar_service import (
    get_today_visits,
    get_upcoming_visits,
    get_overdue_visits
)

from components.today_visits import today_visits
from components.upcoming_calendar import upcoming_calendar
from components.overdue_visits import overdue_visits

def calendar_page(maintenance):

    st.title("📅 Maintenance Calendar")

    today_data = get_today_visits(maintenance)
    upcoming_data = get_upcoming_visits(maintenance)
    overdue_data = get_overdue_visits(maintenance)

    today_visits(today_data)

    st.divider()

    upcoming_calendar(upcoming_data)

    st.divider()

    overdue_visits(overdue_data)
