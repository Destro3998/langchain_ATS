import streamlit as st

def show_response(title, response_text):
    """Display AI response nicely."""
    st.subheader(title)
    st.write(response_text)

def render_header(title, subtitle=""):
    st.markdown(f"<h1 style='text-align:center;color:#4F46E5'>{title}</h1>", unsafe_allow_html=True)
    if subtitle:
        st.markdown(f"<p style='text-align:center;color:#555'>{subtitle}</p>", unsafe_allow_html=True)

def render_button(label, key=None):
    return st.button(label, key=key)