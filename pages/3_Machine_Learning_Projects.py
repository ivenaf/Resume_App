import streamlit as st
import pandas as pd
import numpy as np

# Set page config
st.set_page_config(
    page_title="Machine Learning Projects",
    layout="wide",
    page_icon="🤖",
    initial_sidebar_state="expanded"
)

# Apply blue theme directly
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

# Your ML Project page content goes here
st.title("🤖 Machine Learning Projects")
st.write("*(To be updated regularly with new projects.*)")
st.subheader("1. Insurance Fraud Detection")
st.write("This is an overview of a ***supervised learning, binary classification*** project that detects insurance fraud using a 1000-sample dataset.")
st.write("Click the buttons below to access the GitHub repository and live Streamlit app.")

# Create columns for the buttons
col1, col2, col3 = st.columns([1, 2, 1])

# GitHub repository button
with col2:
    st.markdown("""
    <a href="https://github.com/ivenaf/MLProject_Insurance_Fraud_Classification" target="_blank">
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
            display: inline-block;
            text-align: center;
            text-decoration: none;
            margin-bottom: 10px;
        ">
            <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" 
                 style="height: 20px; vertical-align: middle; margin-right: 10px;">
            Visit GitHub Repository
        </button>
    </a>
    """, unsafe_allow_html=True)
    
    # Add some space between buttons
    st.write("")
    
    # Streamlit app button
    st.markdown("""
    <a href="https://ivenaf-mlproject-insurance-fraud-cla-streamlit-mergedv2-59okgw.streamlit.app/" target="_blank">
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
            display: inline-block;
            text-align: center;
            text-decoration: none;
        ">
            <img src="https://streamlit.io/images/brand/streamlit-mark-color.png" 
                 style="height: 20px; vertical-align: middle; margin-right: 10px;">
            Try the Live Streamlit App
        </button>
    </a>
    """, unsafe_allow_html=True)

st.subheader(" ")
st.subheader("2. In progress...")

# You can add more sections about your project methodology, results, etc.