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
    # Google Drive file ID for the resume PDF
    file_id = "1_u0qk1T7ki3-mX45pdMfH--rwBwDjD_L"
    
    # Display the resume using Google Drive embedding
    st.markdown(f"""
    <div style="display: flex; justify-content: center;">
        <iframe 
            src="https://drive.google.com/file/d/{file_id}/preview" 
            width="100%" 
            height="800" 
            style="border: none; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);"
            allowfullscreen>
        </iframe>
    </div>
    """, unsafe_allow_html=True)
        
# Download section
with st.container():
    col1, col2 = st.columns([1, 3])
    
    with col1:
        # Google Drive download link
        st.markdown(f"""
        <div style="margin-top: 20px;">
            <a href="https://drive.google.com/uc?export=download&id={file_id}" target="_blank">
                <button style="
                    background-color: #4682B4;
                    color: white;
                    padding: 12px 20px;
                    border: none;
                    border-radius: 4px;
                    cursor: pointer;
                    font-size: 16px;
                    font-weight: bold;
                    width: 100%;
                ">
                    Download PDF
                </button>
            </a>
        </div>
        """, unsafe_allow_html=True)