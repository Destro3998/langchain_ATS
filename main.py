from dotenv import load_dotenv
import streamlit as st
from google.generativeai import genai
import streamlit as st
import os
from PIL import Image
import pdf2image

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def get_gemini_response(input, pdf_content, prompt):
    model-genai.GenerativeModel("gemini-2.5-flash")
    response=model.generate_content([input, pdf_content[0], prompt])
    return response.text

def input_df_setup(uploaded_file):
    if uploaded_file is not None:
        # convert the pDF to image
        images=pdf2image.convert_from_bytes(uploaded_file.read())   #convert the PDF to images
        first_page=images[0]  #get the first page
        #convert to bytes
        img_byte_arr=io.BytesIO()  #create a bytesio object 
        first_page.save(img_byte_arr, format="JPEG")
        img_byte_arr=img_byte_arr.getvalue()
        
        pdf_parts = [
                {
                    "mime_type": "image/jpeg",
                    "data": base64.b64encode(img_byte_arr).decode() #encode the image to base64 to send it to the model
                }
            ]
        
        return pdf_parts

    else:
        raise FileNotFoundError("No file uploaded")

## Streamlit App

st.set_page_config(page_title="ATS Resume Expert")
st.header("ATS Tracking System")
input_text=st.text_area("Job Description: ", key="input_text")
uploaded_file=st.file_uploader("Upload your resume: ", type="pdf", key="uploaded_file")

if uploaded_file is not None:
    st.write("PDF uploaded successfully")

submit1 = st.button("Tell me about your resume")
submit2 = st.button("How can I Improve my Skills?")
submit3 = st.button("Percentage match")

input_prompt1 = """
You are an expereineced HR ith Tech Experience in the field of Data Sceince, Full Stack Web Development, 
Big Data Enginnering, Data Analyst, your task is to review the provided resume against the job description for these profiles.
Please shhare your professional evaluation on wheather the candidate's profile aligns with the above mentioned roles and profiles.
Highlight the strengths and weaknesses of thhe applicant in relation to the specificed job requirements.
"""

input_prompt2 = """
You are an Technical Human Resorce Manager with expertise in the field of Data Science, your role is to scrutinize the resume
in light of the job description provided. Share your insights on the candidate suitability for the role from an HR perspective.
Addiotionally, offer advice on echancing the candidate's skills and identify ares for improvement.
"""

