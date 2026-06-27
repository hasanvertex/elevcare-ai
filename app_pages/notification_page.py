
import streamlit as st

from services.notification_service import get_notifications
from components.notification_cards import notification_cards

def notification_page(data):

    st.title("🔔 Notification Center")

    notifications = get_notifications(data)

    notification_cards(notifications)
