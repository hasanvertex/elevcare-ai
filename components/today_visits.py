import streamlit as st

def today_visits(data):
    st.subheader("📅 Today's Visits")
    if len(data) == 0:
        st.info("No visits today.")
        return
    st.dataframe(data, use_container_width=True)
