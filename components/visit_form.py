import streamlit as st

def visit_form():

    st.subheader("✅ Complete Visit")

    st.text_area("Visit Remarks")

    st.file_uploader(
        "Upload Photo",
        type=["jpg","jpeg","png"]
    )

    st.button("Complete Visit")
