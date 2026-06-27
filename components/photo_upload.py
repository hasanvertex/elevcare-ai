import streamlit as st


def photo_upload():

    st.subheader("📷 Service Photos")

    before_photo = st.file_uploader(
        "Before Service Photo",
        type=["jpg", "jpeg", "png"],
        key="before_service_photo"
    )

    after_photo = st.file_uploader(
        "After Service Photo",
        type=["jpg", "jpeg", "png"],
        key="after_service_photo"
    )

    return before_photo, after_photo