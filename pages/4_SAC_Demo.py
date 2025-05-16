import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
import os

# Set page config
st.set_page_config(
    page_title="SAC Demo",
    layout="wide",
    page_icon="📊",
    initial_sidebar_state="expanded"
)

# Apply blue theme directly (replacing the import)
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

# Page title and description
st.title("📊 My SAC - 2 Minute Demo")

# Create a centered container for the logo
col1, col2, col3 = st.columns([1, 2, 1])


st.markdown("""
This page showcases a demonstration of SAC dashboarding capabilities. 
The demo highlights some key features and use cases of SAC as a business intelligence tool.
""")

# Create some space
st.write("")


# Check if the video file exists
video_path = "images/SAC_recording.mp4"
if os.path.exists(video_path):
    # Create a centered container for the video
    col1, col2, col3 = st.columns([1, 3, 1])
    
    with col2:
        # Use the local video file
        video_file = open(video_path, 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)
        
else:
    st.error(f"Video file not found at {video_path}. Please ensure the file exists.")
    st.info("Place your SAC_recording.mp4 file in the 'images' folder.")

# Add your personal experience with SAC
st.write("")
st.subheader("My Experience with SAP Analytics Cloud")

st.markdown("""
During my time at Vaillant Group from July 2022 to November 2024, I served as a Front-End Data Consultant and SAC Developer within the Business Intelligence Center of Excellence team. My responsibilities included:

- Designing and developing interactive dashboards using SAP Analytics Cloud
- Conducting SAC training sessions for end users
- Analyzing queries in SAP BW.5 and BW/4HANA for SAC compatibility
- Collaborating with business stakeholders to identify reporting needs
- Implementing best practices for data visualization and dashboard design

This experience has given me a thorough understanding of how to leverage SAC to transform business data into actionable insights.
""")