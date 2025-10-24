import streamlit as st

def show_response(title, response_text):
    """Display AI response nicely."""
    st.subheader(title)
    st.write(response_text)
