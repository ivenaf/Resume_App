import streamlit as st
import requests
from streamlit_lottie import st_lottie
from streamlit_timeline import timeline
import streamlit.components.v1 as components
from PIL import Image
import base64
import os

# IMPORTANT: Page config must be the first Streamlit command
st.set_page_config(
    page_title="Nathalie Mugrauer | Resumé",
    layout="wide",
    page_icon="🔷",
    initial_sidebar_state="expanded"
)

# Apply the blue theme directly
st.markdown("""
    <style>
    /* Main Content Area */
    .main {
        background-color: #F0F8FF !important; /* Alice Blue - very light blue */
    }
    
    /* App Background */
    .stApp {
        background-color: #F0F8FF !important;
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #1E3A5F !important; /* Dark blue */
        color: white !important;
    }
    
    /* Ensure all sidebar content is white text */
    [data-testid="stSidebar"] p, 
    [data-testid="stSidebar"] span,
    [data-testid="stSidebar"] label,
    [data-testid="stSidebar"] div {
        color: white !important;
    }
    
    /* Header Decoration */
    [data-testid="stDecoration"] {
        background-image: linear-gradient(to right, #1E3A5F, #4682B4, #87CEEB) !important; /* Dark blue to Steel Blue to Sky Blue */
    }
    
    /* Header */
    [data-testid="stHeader"] {
        background-color: #F0F8FF !important;
    }
    
    /* All Buttons */
    button {
        background-color: #4682B4 !important; /* Steel Blue */
        color: white !important;
    }
    
    /* Move content up */
    .main .block-container {
        padding-top: 0 !important;
        margin-top: -80px !important;
    }

    /* Text colors */
    p, span, h1, h2, h3, h4, h5, h6 {
        color: #2C3E50 !important; /* Dark blue-gray for text */
    }
    </style>
""", unsafe_allow_html=True)

# Load info from constant.py
try:
    from constant import info, endorsements, embed_rss
except ImportError:
    # Default information if constant.py is not available
    info = {
        "Name": "Nathalie Mugrauer",
        "Email": "your.email@example.com"
    }
    endorsements = []
    embed_rss = {}

# SECTION 1: Resume Title
st.title("📄  Resumé")

# Main resume section
with st.container():
    # Check multiple locations for the resume PDF
    possible_paths = [
        "images/resume.pdf",
        "files/resume.pdf",
        "resume.pdf",
        "../resume.pdf"
    ]
    
    # Find the first path that exists
    resume_pdf_path = None
    for path in possible_paths:
        if os.path.exists(path):
            resume_pdf_path = path
            break
    
    if resume_pdf_path:
        try:
            # Display PDF using iframe
            with open(resume_pdf_path, "rb") as f:
                base64_pdf = base64.b64encode(f.read()).decode('utf-8')
                pdf_display = f"""
                    <iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="800" 
                    style="border: none; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);" allowfullscreen></iframe>
                """
                st.markdown(pdf_display, unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Error loading resume: {e}")
            st.info(f"Found the file at {resume_pdf_path} but couldn't load it properly.")
    else:
        st.error("Resume PDF file not found")
        st.info("""
        Please add your resume as 'resume.pdf' in one of these locations:
        - 'images/resume.pdf'
        - 'files/resume.pdf'
        - in the main project directory
        """)
        
# Download section
with st.container():

    col1, col2 = st.columns([1, 3])
    
    with col1:
        if resume_pdf_path:
            try:
                with open(resume_pdf_path, "rb") as pdf_file:
                    pdf_bytes = pdf_file.read()
                    st.download_button(
                        label="Download PDF",
                        data=pdf_bytes,
                        file_name="Nathalie_Mugrauer_Resume.pdf",
                        mime="application/pdf"
                    )
            except Exception as e:
                st.error(f"Download error: {e}")
        else:
            st.warning("Resume PDF not available for download")