import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

def get_gemini_response(prompt, pdf_content, job_description):
    """Generate a response from Gemini based on prompt, resume, and job description."""
    response = model.generate_content([prompt, pdf_content[0], job_description])
    return response.text
