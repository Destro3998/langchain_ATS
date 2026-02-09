import streamlit as st

def login_page():
    st.title("🔐 Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        users = st.session_state.get("users", {})

        if username in users and users[username] == password:
            st.session_state["authenticated"] = True
            st.session_state["username"] = username
            st.success(f"Welcome back, {username}!")
            st.switch_page("main.py")
        else:
            st.error("Invalid username or password.")

    st.divider()
    st.write("Don't have an account?")
    if st.button("Sign Up", key="signup_btn"):
        st.switch_page("pages/signup.py")

login_page()
