import streamlit as st

def signup_page():
    st.title("📝 Create Account")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Sign Up"):
        if username and password:
            st.session_state["users"] = st.session_state.get("users", {})
            if username in st.session_state["users"]:
                st.warning("Username already exists!")
            else:
                st.session_state["users"][username] = password
                st.success("Account created successfully! You can now log in.")
                st.switch_page("pages/login.py")
        else:
            st.error("Please enter both username and password.")

signup_page()
