
import streamlit as st
from services.expense_service import save_expense

def expense_form():

    with st.form("expense_form"):

        expense_id = st.text_input("Expense ID")
        category = st.text_input("Category")
        amount = st.number_input("Amount", min_value=0.0)
        description = st.text_area("Description")

        submit = st.form_submit_button(
            "Save Expense"
        )

    if submit:

        save_expense({
            "expense_id": expense_id,
            "category": category,
            "amount": amount,
            "description": description
        })

        st.success("Expense saved.")
        st.rerun()
