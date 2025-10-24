from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai
import streamlit as st
import os
from PIL import Image
import pdf2image
from urllib3 import response
import io
import base64

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def get_gemini_response(input_text, pdf_content, prompt):
    response = model.generate_content([input_text, pdf_content[0], prompt])
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
You are an experienced HR professional with strong technical expertise in Data Science, 
Full Stack Web Development, Big Data Engineering, and Data Analysis. Your task is to review 
the candidate’s resume and provide a comprehensive professional evaluation of how well it aligns 
with these roles. Highlight the candidate’s key strengths, relevant experience, and achievements, 
as well as any notable gaps or weaknesses in relation to the skills and qualifications typically 
required for these positions.
"""


input_prompt2 = """
You are a seasoned Technical HR Manager specializing in Data Science, Full Stack Web Development, 
Big Data Engineering, and Data Analysis. Review the candidate’s resume and identify specific areas 
where the candidate can improve to become a stronger fit for these roles. Provide detailed, actionable 
feedback on both technical and soft skills, and suggest relevant tools, technologies, certifications, 
or learning paths that would enhance the candidate’s professional growth and employability.
"""


input_prompt3 = """
You are an expert Technical Recruiter with a deep understanding of hiring standards in Data Science, 
Full Stack Web Development, Big Data Engineering, and Data Analysis roles. Evaluate the candidate’s 
resume against the provided job description and determine how well it matches the requirements. 
Provide a clear percentage match score (0–100%) and briefly explain what factors contributed most 
to the score, including relevant skills, experience alignment, and areas that could be improved.
"""


if submit1:
    if uploaded_file is not None:
        pdf_content = input_df_setup(uploaded_file)
        response = get_gemini_response(input_prompt1, pdf_content, input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please uplaod the resume")

elif submit2:
    if uploaded_file is not None:
        pdf_content = input_df_setup(uploaded_file)
        response = get_gemini_response(input_prompt2, pdf_content, input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please uplaod the resume")

elif submit3:
    if uploaded_file is not None:
        pdf_content = input_df_setup(uploaded_file)
        response = get_gemini_response(input_prompt3, pdf_content, input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please uplaod the resume")



