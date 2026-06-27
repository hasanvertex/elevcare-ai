import streamlit as st

def upcoming_calendar(data):
    st.subheader("⏳ Upcoming Visits")
    st.dataframe(data, use_container_width=True)
