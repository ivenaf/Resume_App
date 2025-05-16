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
This page showcases a demonstration of an  SAC example-dashboard I built. 
It highlights some key features and use cases of SAC as a business intelligence tool.
""")

# Create some space
st.write("")


# Google Drive file ID for the video
file_id = "1kGoknBoeG8ptPGi4LImYlGYWNHMBsoaE"

# Display the video using Google Drive embedding with updated parameters
st.markdown("### Watch the Demo Video")
st.markdown(f"""
<div style="display: flex; justify-content: center;">
    <iframe 
        src="https://drive.google.com/file/d/{file_id}/preview" 
        width="800" 
        height="450" 
        frameborder="0"
        allowfullscreen
        allow="autoplay; encrypted-media"
        style="border: none; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);"
    ></iframe>
</div>
""", unsafe_allow_html=True)

# Add a fallback link in case the embedding doesn't work
st.markdown(f"""
<div style="text-align: center; margin-top: 10px; margin-bottom: 30px;">
    <a href="https://drive.google.com/file/d/{file_id}/view" target="_blank" style="color: #4682B4; text-decoration: none; font-size: 14px;">
        If the video doesn't load, click here to watch directly on Google Drive
    </a>
</div>
""", unsafe_allow_html=True)

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