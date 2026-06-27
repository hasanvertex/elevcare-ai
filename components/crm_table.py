
import streamlit as st
import pandas as pd

def crm_table():

    data = pd.DataFrame(
        {
            "Technician":["Kevin","Aron","Josh","Tanisha"],
            "Role":[
                "Senior Technician",
                "Maintenance Lead",
                "Dispatcher",
                "Technician"
            ],
            "Status":[
                "Active",
                "Busy",
                "Active",
                "Leave"
            ]
        }
    )

    st.subheader("👨‍🔧 Technician Performance")
    st.dataframe(data, use_container_width=True)
