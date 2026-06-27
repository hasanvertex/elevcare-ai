
import streamlit as st
from services.work_order_service import save_work_order

def work_order_form():

    with st.form("work_order_form"):

        work_order_id = st.text_input("Work Order ID")
        customer_id = st.text_input("Customer ID")
        elevator_id = st.text_input("Elevator ID")
        technician = st.text_input("Technician")

        priority = st.selectbox(
            "Priority",
            ["Low", "Medium", "High"]
        )

        status = st.selectbox(
            "Status",
            ["Open", "In Progress", "Completed"]
        )

        due_date = st.date_input("Due Date")

        remarks = st.text_area("Remarks")

        submit = st.form_submit_button(
            "Create Work Order"
        )

    if submit:

        save_work_order({
            "work_order_id": work_order_id,
            "customer_id": customer_id,
            "elevator_id": elevator_id,
            "technician": technician,
            "priority": priority,
            "status": status,
            "due_date": due_date,
            "remarks": remarks
        })

        st.success("Work order created.")
        st.rerun()
