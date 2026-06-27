
import streamlit as st

def notification_cards(notifications):

    st.subheader("🔔 Notifications")

    if len(notifications) == 0:
        st.success("No notifications.")
        return

    for item in notifications:
        st.warning(item)
