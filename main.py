from dotenv import load_dotenv
import streamlit as st

from utils.gemini_utils import get_gemini_response
from utils.pdf_utils import input_df_setup
from utils.prompts import input_prompt1, input_prompt2, input_prompt3, input_prompt4

# setup
load_dotenv()

st.set_page_config(
    page_title="ATS Resume Expert",
    page_icon="📄",
    layout="wide"
)


## auth session
if "authenticated" not in st.session_state or not st.session_state.authenticated:
    st.switch_page("pages/login.py")

st.title("🏠 Main Page")
st.write(f"Hello, {st.session_state.get('username', 'Guest')}!")

if st.button("Logout"):
    st.session_state["authenticated"] = False
    st.switch_page("pages/login.py")

# Header
st.markdown("""
    <style>
        .big-title {
            font-size: 42px !important;
            font-weight: 800;
            color: #2C3E50;
            text-align: center;
            margin-bottom: 10px;
        }
        .subtitle {
            font-size: 18px;
            color: #555;
            text-align: center;
            margin-bottom: 30px;
        }
        .stButton>button {
            background-color: #4F46E5;
            color: white;
            border: none;
            border-radius: 8px;
            padding: 10px 20px;
            font-weight: 600;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #4338CA;
            transform: scale(1.03);
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='big-title'>📄 ATS Resume Analyzer</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Upload your resume and job description to get AI-powered feedback, matching, and cover letter generation.</p>", unsafe_allow_html=True)


# Input Section 
col1, col2 = st.columns([1.3, 1])

with col1:
    input_text = st.text_area("🧾 Job Description", placeholder="Paste the job description here...", height=220)

with col2:
    uploaded_file = st.file_uploader("📎 Upload your resume (PDF)", type="pdf")
    if uploaded_file:
        st.success("✅ Resume uploaded successfully!")

# Buttons
st.divider()
st.markdown("### ⚙️ Choose an action:")

col_btn1, col_btn2, col_btn3, col_btn4 = st.columns(4)
with col_btn1:
    submit1 = st.button("📘 Resume Review")
with col_btn2:
    submit2 = st.button("🧠 Skill Improvement")
with col_btn3:
    submit3 = st.button("📊 Match Percentage")
with col_btn4:
    submit4 = st.button("✉️ Generate Cover Letter")

# Response Section
if uploaded_file is None:
    st.warning("📤 Please upload your resume to continue.")
else:
    pdf_content = input_df_setup(uploaded_file)

    if submit1:
        with st.spinner("Analyzing your resume..."):
            response = get_gemini_response(input_prompt1, pdf_content, input_text)
            st.subheader("🧾 Resume Review Result")
            st.write(response)

    elif submit2:
        with st.spinner("Identifying skill improvements..."):
            response = get_gemini_response(input_prompt2, pdf_content, input_text)
            st.subheader("💡 Skill Improvement Suggestions")
            st.write(response)

    elif submit3:
        with st.spinner("Calculating match percentage..."):
            response = get_gemini_response(input_prompt3, pdf_content, input_text)
            st.subheader("📊 Match Analysis")
            st.success(response)
            
    elif submit4:
        with st.spinner("Generating your custom cover letter..."):
            response = get_gemini_response(input_prompt4, pdf_content, input_text)
            st.subheader("✉️ Your Cover Letter")
            st.write(response)
            
            st.download_button(
                label="💾 Download Cover Letter",
                data=response,
                file_name="cover_letter.txt",
                mime="text/plain"
            )
