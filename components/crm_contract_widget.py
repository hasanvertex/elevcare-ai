
import streamlit as st

def crm_contract_widget():

    c1,c2,c3 = st.columns(3)

    c1.success("✅ Active : 124")
    c2.warning("⚠ Warning : 12")
    c3.error("❌ Expired : 3")
