import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
from streamlit_option_menu import option_menu
from streamlit_float import *

st.set_page_config(
    page_title="ElevCare AI",
    page_icon="🚀",
    layout="wide"
)

float_init()

# --------------------------
# LOAD DATA
# --------------------------

contracts = pd.read_csv("database/contracts.csv")
elevators = pd.read_csv("database/elevators.csv")
maintenance = pd.read_csv("database/maintenance.csv")
customers = pd.read_csv("database/customers.csv")

today = datetime.today()

expired = 0
warning = 0
active = 0

alerts = []

for _, row in contracts.iterrows():

    try:
        end_date = pd.to_datetime(row["end_date"])
        days = (end_date - today).days

        if days < 0:
            expired += 1

        elif days <= 30:
            warning += 1

            alerts.append({
                "Customer": row["customer_id"],
                "Days Left": days,
                "End Date": row["end_date"]
            })

        else:
            active += 1

    except:
        pass

# --------------------------
# SIDEBAR
# --------------------------

with st.sidebar:

    st.markdown("# 🚀 ElevCare AI")

    selected = option_menu(
        "Menu",
        ["Dashboard", "Contracts", "Maintenance"],
        icons=["speedometer2", "file-earmark-text", "tools"],
        default_index=0,
    )

# --------------------------
# DASHBOARD
# --------------------------

if selected == "Dashboard":

    st.title("🚀 ElevCare AI Dashboard")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Contracts", len(contracts))
    c2.metric("Elevators", len(elevators))
    c3.metric("Visits", len(maintenance))
    c4.metric("Expiring", warning)

    st.divider()

    left, right = st.columns(2)

    with left:

        chart_data = pd.DataFrame({
            "Status": [
                "Active",
                "Expiring",
                "Expired"
            ],
            "Count": [
                active,
                warning,
                expired
            ]
        })

        fig = px.pie(
            chart_data,
            names="Status",
            values="Count",
            title="Contract Status"
        )

        st.plotly_chart(
            fig,
            width="stretch"
        )

    with right:

        tech_chart = (
            maintenance["technician"]
            .value_counts()
            .reset_index()
        )

        tech_chart.columns = [
            "Technician",
            "Visits"
        ]

        fig2 = px.bar(
            tech_chart,
            x="Technician",
            y="Visits",
            title="Technician Performance"
        )

        st.plotly_chart(
            fig2,
            width="stretch"
        )

    st.divider()

    st.subheader("⚠ Expiring Contracts")

    if len(alerts):

        st.dataframe(
            pd.DataFrame(alerts),
            width="stretch"
        )

    else:

        st.success("No expiring contracts.")

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("📄 Contracts")

        st.dataframe(
            contracts.head(10),
            width="stretch"
        )

    with col2:

        st.subheader("🏢 Elevators")

        st.dataframe(
            elevators.head(10),
            width="stretch"
        )

    st.divider()

    st.subheader("🔧 Recent Maintenance")

    st.dataframe(
        maintenance.tail(10),
        width="stretch"
    )

# --------------------------
# CONTRACTS PAGE
# --------------------------

elif selected == "Contracts":

    st.title("📄 Contracts")

    search = st.text_input(
        "Search Customer ID"
    )

    data = contracts

    if search:

        data = contracts[
            contracts["customer_id"]
            .astype(str)
            .str.contains(
                search,
                case=False
            )
        ]

    st.dataframe(
        data,
        width="stretch"
    )

# --------------------------
# MAINTENANCE PAGE
# --------------------------

elif selected == "Maintenance":

    st.title("🔧 Maintenance Visits")

    technician = st.selectbox(
        "Select Technician",
        ["All"] + sorted(
            maintenance["technician"]
            .dropna()
            .unique()
            .tolist()
        )
    )

    if technician == "All":

        data = maintenance

    else:

        data = maintenance[
            maintenance["technician"]
            == technician
        ]

    st.dataframe(
        data,
        width="stretch"
    )

# --------------------------
# FLOATING CHATBOT
# --------------------------

chat_css = """
position: fixed;
bottom: 20px;
right: 20px;
width: 350px;
background-color: white;
padding: 15px;
border-radius: 20px;
box-shadow: 0 0 20px rgba(0,0,0,0.2);
z-index: 999;
"""

with st.container():

    st.markdown("### 🤖 ElevCare AI")

    question = st.text_input(
        "Ask anything..."
    )

    if st.button("Ask AI"):

        q = question.lower()

        if "expire" in q:

            nearest = contracts.copy()

            nearest["date"] = pd.to_datetime(
                nearest["end_date"]
            )

            nearest = nearest.sort_values(
                "date"
            )

            st.success(
                "Nearest expiring contract:"
            )

            st.dataframe(
                nearest.head(1)
            )

        elif "ahmed" in q:

            result = maintenance[
                maintenance["technician"]
                .str.lower()
                .str.contains("ahmed")
            ]

            st.dataframe(result)

        elif "emergency" in q:

            result = maintenance[
                maintenance["remarks"]
                .str.lower()
                .str.contains("emergency")
            ]

            st.dataframe(result)

        elif "expire soon" in q:

            st.dataframe(
                pd.DataFrame(alerts)
            )

        else:

            st.info(
                "Ask about contracts, technicians or maintenance."
            )

    float_parent(css=chat_css)