from dotenv import load_dotenv
import streamlit as st
from google.generativeai import genai
import streamlit as st
import os
from PIL import Image
import pdf2image

load_dotenv()

st.title("PDF Summarizer")

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    st.write(text)