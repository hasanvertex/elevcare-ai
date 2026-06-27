
import streamlit as st


def upcoming_visits(maintenance):

    st.subheader("📅 Upcoming Maintenance")

    if len(maintenance) == 0:
        st.info("No upcoming visits.")
        return

    data = maintenance.head(5)

    for _, row in data.iterrows():

        customer = row.get("customer_id", "-")
        visit = row.get("next_visit", "-")

        st.info(
            f"Customer: {customer} | Next Visit: {visit}"
        )
