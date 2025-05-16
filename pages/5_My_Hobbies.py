import streamlit as st
import base64
from PIL import Image
import io

# Set page config
st.set_page_config(
    page_title="My Hobbies",
    layout="wide",
    page_icon="🎨",
    initial_sidebar_state="expanded"
)

# Function to convert local image to base64 for embedding in HTML
def get_image_base64(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except:
        return ""

# Apply blue theme with aggressive empty element hiding and better card styling
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
    
    /* Hobby card styling */
    .hobby-card {
        background-color: white;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        transition: transform 0.3s, box-shadow 0.3s;
        height: 100%;
        margin-bottom: 20px;
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
    }
    
    .hobby-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 12px rgba(0,0,0,0.15);
    }
    
    .hobby-icon {
        margin-bottom: 15px;
        text-align: center;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 120px;
    }
    
    .hobby-icon img {
        max-height: 120px;
        width: auto;
        display: block;
    }
    
    .hobby-title {
        color: #1E3A5F !important;
        font-size: 22px !important;
        font-weight: bold !important;
        margin-bottom: 10px !important;
        text-align: center !important;
    }
    
    .hobby-description {
        font-size: 16px !important;
        line-height: 1.5 !important;
        text-align: center !important;
    }
    
    /* Hide empty elements */
    .block-container > div:empty,
    div:empty,
    .stMarkdown:empty,
    .element-container:empty,
    div.stMarkdown > div:empty,
    div.row-widget.stButton > button:empty {
        display: none !important;
        height: 0 !important;
        margin: 0 !important;
        padding: 0 !important;
        min-height: 0 !important;
    }
    </style>
""", unsafe_allow_html=True)

# Title and intro
st.title("🎨 My Hobbies & Interests")

# Quote section
st.markdown("""<div style="background-color: #E6F0FF; padding: 20px; border-radius: 10px; margin-bottom: 30px;">
    <p style="font-size: 18px; font-style: italic; text-align: center;">
    "We don't stop playing because we grow old; we grow old because we stop playing." — George Bernard Shaw
    </p>
</div>""", unsafe_allow_html=True)

# Convert all images to base64
yoga_img = get_image_base64("images/yogagirl.png")
running_img = get_image_base64("images/runnergirl.png")
painting_img = get_image_base64("images/colorpalette.png")
trumpet_img = get_image_base64("images/trumpet.png")
family_img = get_image_base64("images/family.png")

# First row - Yoga, Running, Painting
col1, col2, col3 = st.columns(3)

with col1:
    # Complete card with image and text integrated
    st.markdown(f"""
    <div class="hobby-card">
        <div class="hobby-icon">
            <img src="data:image/png;base64,{yoga_img}" width="120">
        </div>
        <h3 class="hobby-title">Yoga</h3>
        <p class="hobby-description">I find my inner peace through yoga.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="hobby-card">
        <div class="hobby-icon">
            <img src="data:image/png;base64,{running_img}" width="120">
        </div>
        <h3 class="hobby-title">Running</h3>
        <p class="hobby-description">Nothing beats a morning run.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="hobby-card">
        <div class="hobby-icon">
            <img src="data:image/png;base64,{painting_img}" width="120">
        </div>
        <h3 class="hobby-title">Painting</h3>
        <p class="hobby-description">I usually get creative in the dark times of the year.</p>
    </div>
    """, unsafe_allow_html=True)

# Add space between rows
st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)

# Second row - Trumpet and Family
col4, col5, _ = st.columns(3)  # Using 3 columns with the last one empty for balance

with col4:
    st.markdown(f"""
    <div class="hobby-card">
        <div class="hobby-icon">
            <img src="data:image/png;base64,{trumpet_img}" width="120">
        </div>
        <h3 class="hobby-title">Playing the Trumpet</h3>
        <p class="hobby-description">Every once in a while, I take out my dusty trumpet.</p>
    </div>
    """, unsafe_allow_html=True)

with col5:
    st.markdown(f"""
    <div class="hobby-card">
        <div class="hobby-icon">
            <img src="data:image/png;base64,{family_img}" width="120">
        </div>
        <h3 class="hobby-title">Family Time</h3>
        <p class="hobby-description">The most precious moments...</p>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("<div style='margin-top: 40px;'></div>", unsafe_allow_html=True)
st.markdown("""
<div style="background-color: #E6F0FF; padding: 20px; border-radius: 10px; text-align: center;">
    <h3 style="color: #1E3A5F !important;">How I Find Balance</h3>
    <p>These hobbies help me maintain a healthy work-life balance and bring different kinds of joy to my life. 
    I believe that nurturing diverse interests makes us more creative problem-solvers in our professional lives too.</p>
</div>
""", unsafe_allow_html=True)