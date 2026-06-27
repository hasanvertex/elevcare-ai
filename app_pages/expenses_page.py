
import streamlit as st

from components.expense_table import expense_table
from app_pages.forms.expense_form import expense_form

def expenses_page(expenses):

    st.title("💰 Expenses")

    tab1, tab2 = st.tabs(
        ["Expense List", "Add Expense"]
    )

    with tab1:
        expense_table(expenses)

    with tab2:
        expense_form()
