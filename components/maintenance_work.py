
import streamlit as st

def maintenance_work(record):

    st.subheader("🛠 Work Details")

    st.write("Work Done:")
    st.success(record.get("work_done", "-"))

    st.write("Spare Parts:")
    st.info(record.get("spare_parts", "-"))

    st.write("Remarks:")
    st.warning(record.get("remarks", "-"))
