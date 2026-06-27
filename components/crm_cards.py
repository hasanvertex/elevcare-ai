
import streamlit as st

def crm_cards():

    c1,c2,c3,c4 = st.columns(4)

    c1.metric("Customers","50","+12%")
    c2.metric("Elevators","184","+5%")
    c3.metric("Contracts","45","-2%")
    c4.metric("Maintenance","12","+8%")
