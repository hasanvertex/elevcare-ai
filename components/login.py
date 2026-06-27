import streamlit as st


def login(users):

    st.markdown("""
    <h1 style='text-align:center;'>
    🔐 ElevCare AI Login
    </h1>
    """, unsafe_allow_html=True)

    st.write("")

    username = st.text_input(
        "Username"
    )

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button(
        "Login",
        use_container_width=True
    ):

        user = users[
            (users["username"] == username)
            &
            (users["password"] == password)
        ]

        if len(user) > 0:

            st.session_state.logged_in = True
            st.session_state.user = user.iloc[0]["username"]
            st.session_state.role = user.iloc[0]["role"]

            st.rerun()

        else:

            st.error(
                "Invalid Username or Password"
            )