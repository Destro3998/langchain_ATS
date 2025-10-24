import streamlit as st
from utils.firebase_config import initialize_firebase, create_user
from utils.ui_helpers import render_header, render_button

# Initialize Firebase once
initialize_firebase()

def login_page():
    st.title("🔐 Login / Signup")

    # Radio option to choose between Login and Signup
    option = st.radio("Select Action:", ["Login", "Signup"])

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    # Signup flow
    if option == "Signup":
        if render_button("Create Account"):
            if email and password:
                try:
                    user = create_user(email, password)
                    st.success(f"Account created for {user.email}")
                except Exception as e:
                    st.error(f"Error creating account: {e}")
            else:
                st.warning("Please enter both email and password.")

    # Login flow (simulated for now)
    elif option == "Login":
        if render_button("Login"):
            if email and password:
                # Simulate login: store user in session_state
                st.session_state["user"] = email
                st.success(f"Logged in successfully as {email}")
            else:
                st.warning("Please enter both email and password.")

# Run the page
login_page()