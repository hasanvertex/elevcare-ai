
import streamlit as st
from services.inventory_service import save_inventory

def inventory_form():

    with st.form("inventory_form"):

        part_id = st.text_input("Part ID")
        part_name = st.text_input("Part Name")
        quantity = st.number_input("Quantity", min_value=0)
        minimum_stock = st.number_input("Minimum Stock", min_value=0)

        submit = st.form_submit_button(
            "Save Part"
        )

    if submit:

        save_inventory({
            "part_id": part_id,
            "part_name": part_name,
            "quantity": quantity,
            "minimum_stock": minimum_stock
        })

        st.success("Part saved.")
        st.rerun()
