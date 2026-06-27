import streamlit as st

from services.data_loader import load_data

from components.sidebar import show_sidebar
from components.page_router import route_page

from components.login import login
from components.session import init_session


st.set_page_config(
    page_title="ElevCare AI ERP",
    page_icon="🚀",
    layout="wide"
)

# ======================
# SESSION
# ======================

init_session()

# ======================
# LOAD DATA
# ======================

data = load_data()

# ======================
# LOGIN
# ======================

if not st.session_state.logged_in:

    login(
        data["users"]
    )

    st.stop()

# ======================
# SIDEBAR
# ======================

selected = show_sidebar()

# ======================
# DASHBOARD VALUES
# ======================

active = 0
warning = 0
expired = 0
alerts = []

# ======================
# ROUTER
# ======================

route_page(
    selected,
    data,
    active,
    warning,
    expired,
    alerts
)