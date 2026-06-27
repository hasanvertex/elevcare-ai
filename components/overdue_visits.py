import streamlit as st

def overdue_visits(data):
    st.subheader("❌ Overdue Visits")
    if len(data) == 0:
        st.success("No overdue visits.")
        return
    st.dataframe(data, use_container_width=True)
