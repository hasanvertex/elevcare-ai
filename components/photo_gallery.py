
import streamlit as st

def photo_gallery(before_photo, after_photo):

    st.subheader("🖼 Photo Preview")

    col1, col2 = st.columns(2)

    with col1:
        if before_photo:
            st.image(before_photo,
                     caption="Before Service")

    with col2:
        if after_photo:
            st.image(after_photo,
                     caption="After Service")
