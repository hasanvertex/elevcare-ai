
import streamlit as st

def crm_header():
    c1,c2 = st.columns([4,1])

    with c1:
        st.title("🚀 ElevCare AI ERP")
        st.caption("Welcome back to your dashboard")

    with c2:
        st.write("")
        st.button("🔔")
