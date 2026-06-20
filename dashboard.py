import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title="ElevCare AI",
    layout="wide"
)

contracts = pd.read_csv("database/contracts.csv")
elevators = pd.read_csv("database/elevators.csv")
maintenance = pd.read_csv("database/maintenance.csv")
customers = pd.read_csv("database/customers.csv")

st.sidebar.title("🚀 ElevCare AI")

menu = st.sidebar.radio(
    "Menu",
    ["Dashboard", "Contracts", "Maintenance"]
)

st.title("🚀 ElevCare AI Dashboard")

col1, col2, col3 = st.columns(3)

col1.metric("Contracts", len(contracts))
col2.metric("Elevators", len(elevators))
col3.metric("Visits", len(maintenance))

today = datetime.today()

alerts = []

for _, row in contracts.iterrows():

    end_date = datetime.strptime(
        row["end_date"],
        "%m/%d/%Y"
    )

    days = (end_date - today).days

    if days <= 30:
        alerts.append(
            f"{row['customer_id']} contract expires in {days} days."
        )

if alerts:

    st.divider()

    st.subheader("⚠ Contract Alerts")

    for alert in alerts:
        st.warning(alert)

st.divider()

search = st.text_input(
    "🔍 Search Customer ID"
)

if search:
    contracts = contracts[
        contracts["customer_id"].str.contains(
            search,
            case=False
        )
    ]

col1, col2 = st.columns(2)

with col1:
    st.subheader("📄 Contracts")
    st.dataframe(
        contracts,
        use_container_width=True
    )

with col2:
    st.subheader("🏢 Elevators")
    st.dataframe(
        elevators,
        use_container_width=True
    )

st.divider()

st.subheader("🔧 Maintenance Visits")

st.dataframe(
    maintenance,
    use_container_width=True
)

st.download_button(
    "Download Contracts CSV",
    contracts.to_csv(index=False),
    "contracts.csv",
    "text/csv"
)

st.divider()

st.subheader("🤖 Ask ElevCare AI")

question = st.text_input(
    "Ask a question"
)

if st.button("Ask AI"):

    if "expire" in question.lower():

        nearest = contracts.copy()

        nearest["date"] = pd.to_datetime(
            nearest["end_date"]
        )

        nearest = nearest.sort_values("date")

        st.success(
            "The contract that expires soonest:"
        )

        st.dataframe(
            nearest.head(1)
        )

    elif "maintenance" in question.lower():

        st.success(
            "Latest maintenance visit:"
        )

        st.dataframe(
            maintenance.tail(1)
        )

    else:

        st.info(
            "Please ask about contracts or maintenance."
        )