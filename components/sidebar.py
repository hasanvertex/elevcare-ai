import streamlit as st


def show_sidebar():

    st.sidebar.markdown(
        """
        # 🚀 ElevCare AI ERP
        """
    )

    st.sidebar.caption("ERP V2")

    selected = st.sidebar.radio(
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
            "📝 Work Orders",
            "📅 Calendar",
            "📷 Documents",
            "📄 Reports",
            "📱 QR Codes",
            "👨‍🔧 Dashboard",
            "📈 Manager Dashboard",
            "🔔 Notifications",
            "🤖 AI Manager V2",
            "📱 Technician Mobile"
        ]
    )

    st.sidebar.divider()

    st.sidebar.success("🟢 System Online")

    return selected