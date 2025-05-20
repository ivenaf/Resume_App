import streamlit as st

# Set page config
st.set_page_config(
    page_title="QR Code | Nathalie Mugrauer",
    layout="wide",
    page_icon="📱",
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
    
    /* QR code container */
    .qr-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        margin: 50px auto;
        max-width: 600px;
        text-align: center;
    }
    
    .qr-box {
        padding: 30px;
        background-color: white;
        border-radius: 15px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        margin-bottom: 30px;
    }
    </style>
""", unsafe_allow_html=True)

# Load info from constant.py
try:
    from constant import info
except ImportError:
    # Default information if constant.py is not available
    info = {
        "Name": "Nathalie Mugrauer",
        "Email": "example@example.com"
    }

# Page title
st.title("📱 Mobile Access")

# Create QR code section
st.markdown("""
<div class="qr-container">
    <div class="qr-box">
        <h2>Scan this QR Code</h2>
        <p style="margin-bottom: 20px;">Access my interactive resume on your mobile device</p>
        <img src="https://api.qrserver.com/v1/create-qr-code/?size=250x250&data=https://ivenaf-resume-app-1-home-5rj0a4.streamlit.app/" 
             alt="QR Code to access this app" 
             style="width: 250px; height: 250px; margin: 20px 0;">
    </div>
</div>
""", unsafe_allow_html=True)

# Add the text correctly with st.write() instead of HTML in the green box
st.write("Thank you for visiting my interactive resume!")
st.write("Feel free to share this QR code with others who might be interested in my profile.")

# Optional: Add a download button for the QR code image
st.markdown("""
<div style="text-align: center; margin-top: 20px;">
    <a href="https://api.qrserver.com/v1/create-qr-code/?size=250x250&data=https://ivenaf-resume-app-1-home-5rj0a4.streamlit.app/" 
       download="Nathalie_Mugrauer_Resume_QR.png"
       style="text-decoration: none;">
        <button style="
            background-color: #4682B4;
            color: white;
            padding: 10px 15px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
            font-weight: bold;
        ">
            Download QR Code
        </button>
    </a>
</div>
""", unsafe_allow_html=True)