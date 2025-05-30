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
    page_title="Nathalie Mugrauer | Curriculum Vitae",
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
    
    /* PDF container */
    .pdf-container {
        display: flex;
        justify-content: center;
        width: 100%;
        height: 800px;
        margin: 0 auto;
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
st.title("📄  Curriculum Vitae")

# Function to get base64 encoded PDF from local file
def get_pdf_as_base64(file_path):
    try:
        with open(file_path, "rb") as pdf_file:
            return base64.b64encode(pdf_file.read()).decode('utf-8')
    except Exception as e:
        return None

# Main resume section
with st.container():
    # Google Drive file ID for reference (not used in new implementation)
    file_id = "19laGmycVASmpsRo90GW1XcR9i_lcoosv"
    
    # Try multiple methods to display the resume, starting with the most reliable
    
    # OPTION 1: Check if local PDF exists and display it embedded via base64
    pdf_path = "resume.pdf"  # Update this to your actual path
    base64_pdf = get_pdf_as_base64(pdf_path)
    
    if base64_pdf:
        # Display PDF using base64 encoding (most reliable method)
        st.markdown(f"""
        <div class="pdf-container">
            <iframe 
                src="data:application/pdf;base64,{base64_pdf}" 
                width="100%" 
                height="800" 
                style="border: none; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);"
                allowfullscreen>
            </iframe>
        </div>
        """, unsafe_allow_html=True)
    else:
        # OPTION 2: Use an external PDF viewer that works with Google Drive
        st.markdown(f"""
        <div class="pdf-container">
            <iframe 
                src="https://docs.google.com/viewer?embedded=true&url=https://drive.google.com/uc?export=download%26id={file_id}" 
                width="100%" 
                height="800" 
                style="border: none; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);"
                allowfullscreen>
            </iframe>
        </div>
        """, unsafe_allow_html=True)
        
        # OPTION 3: Display a message if the PDF can't be displayed
        st.info("If the PDF viewer doesn't load properly, please use the download button below.")
        
# Download section
with st.container():
    col1, col2 = st.columns([1, 3])
    
    with col1:
        # Try multiple download options
        
        # OPTION 1: Use Streamlit's built-in download button if local PDF exists
        try:
            if os.path.exists(pdf_path):
                with open(pdf_path, "rb") as pdf_file:
                    btn = st.download_button(
                        label="Download PDF",
                        data=pdf_file,
                        file_name="Nathalie_Mugrauer_CV.pdf",
                        mime="application/pdf",
                        key="download-pdf",
                    )
            else:
                # OPTION 2: Google Drive download link as fallback
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
        except Exception as e:
            st.error(f"Error with download button: {e}")
            
            # OPTION 3: Basic link as a last resort
            st.markdown(f"[Download CV](https://drive.google.com/uc?export=download&id={file_id})")