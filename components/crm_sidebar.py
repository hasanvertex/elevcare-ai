
import streamlit as st

def crm_sidebar():

    st.sidebar.title("🚀 ElevCare")
    st.sidebar.caption("CRM Dashboard")

    return st.sidebar.radio(
        "Navigation",
        [
            "📊 Dashboard",
            "👥 Customers",
            "🏢 Elevators",
            "📄 Contracts",
            "🔧 Maintenance",
            "👨‍🔧 Technicians",
            "📦 Inventory",
            "💰 Expenses",
            "📅 Calendar",
            "📄 Reports"
        ]
    )
