import json
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
    page_title="Nathalie Mugrauer | Interactive Resumé",
    layout="wide",
    page_icon="🔷",
    initial_sidebar_state="expanded"
)

# Apply the blue theme directly with added mobile responsiveness
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
    
    /* Move greeting box up significantly */
    .main .block-container {
        padding-top: 0 !important;
        margin-top: -100px !important;
    }
    
    /* More space between timeline and data tools */
    [data-testid="stVerticalBlock"] > [data-testid="stVerticalBlock"] {
        margin-bottom: 60px;
    }
    
    /* Adjust spacing in greeting box */
    h1 {
        margin-top: 0 !important;
        padding-top: 0 !important;
    }
    
    /* Style for perfectly circular profile picture in greeting box - INCREASED SIZE */
    .profile-pic-greeting {
        width: 220px !important; /* Increased from 180px */
        height: 220px !important; /* Increased from 180px */
        border-radius: 50% !important;
        object-fit: cover !important;
        margin-right: 40px !important; /* Increased margin for better spacing */
    }
    
    /* Greeting container styling - BLUE GRADIENT AND TALLER */
    .greeting-container {
        display: flex;
        align-items: center;
        justify-content: flex-start;
        background-image: linear-gradient(to right, #1E3A5F, #4682B4) !important; /* Dark blue to Steel Blue */
        border-radius: 10px;
        padding: 30px 40px !important; /* Increased padding */
        margin-top: 0;
        min-height: 260px !important; /* Set minimum height to make container taller */
    }
    
    /* Greeting text styling - ensure all text is white */
    .greeting-text {
        color: white !important;
        font-size: 46px !important; /* Increased size */
        margin: 0 !important;
        padding: 0 !important;
    }
    
    /* Intro text styling - ensure all text is white */
    .intro-text {
        color: white !important;
        font-size: 18px !important; /* Increased size */
        margin-top: 15px !important;
        line-height: 1.4 !important; /* Better readability */
    }

    /* Change text colors to match the blue theme */
    p, span, h1, h2, h3, h4, h5, h6 {
        color: #2C3E50 !important; /* Dark blue-gray for text */
    }
    
    /* Data tools icons/labels */
    [data-testid="stVerticalBlock"] p {
        color: #1E3A5F !important; /* Dark blue for labels */
    }

    /* Override any styles that might affect the greeting text color */
    .greeting-container h1,
    .greeting-container p,
    .greeting-container span,
    .greeting-container div {
        color: white !important;
    }
    
    /* Form styling */
    form {
        width: 100%;
    }
    
    input, textarea {
        width: 100%;
        padding: 10px;
        margin-bottom: 10px;
        border-radius: 5px;
        border: 1px solid #ddd;
    }
    
    textarea {
        height: 150px;
    }
    
    button[type="submit"] {
        background-color: #4682B4;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        cursor: pointer;
        font-weight: bold;
    }
    
    button[type="submit"]:hover {
        background-color: #1E3A5F;
    }
    
    /* MOBILE RESPONSIVENESS */
    @media (max-width: 768px) {
        /* Make greeting more compact and centered on mobile */
        .greeting-container {
            flex-direction: column !important;
            align-items: center !important;
            justify-content: center !important;
            text-align: center !important;
            padding: 30px 20px !important;
            height: auto !important;
            min-height: 400px !important;
        }
        
        /* Center profile pic on mobile and give space below */
        .profile-pic-greeting {
            margin-right: 0 !important;
            margin-bottom: 25px !important;
            width: 180px !important;
            height: 180px !important;
        }
        
        /* Adjust greeting text size and center for mobile */
        .greeting-text {
            font-size: 36px !important;
            text-align: center !important;
            line-height: 1.2 !important;
            margin-bottom: 15px !important;
        }
        
        /* Adjust intro text for mobile */
        .intro-text {
            font-size: 18px !important;
            text-align: center !important;
            line-height: 1.5 !important;
            padding: 0 10px !important;
        }
        
        /* Fix data tools section for mobile */
        [data-testid="column"] {
            width: 50% !important;
            flex: 0 0 50% !important;
            padding: 0 10px !important;
            margin-bottom: 20px !important;
        }
        
        /* Move data tools icons closer together on mobile */
        [data-testid="column"] > div {
            padding: 0 !important;
        }
        
        /* Reduce margins between sections on mobile */
        [data-testid="stVerticalBlock"] > div[style*="margin-top"] {
            margin-top: 25px !important;
        }
        
        /* Fix overall spacing on mobile */
        .main .block-container {
            padding: 1rem 0.5rem !important;
            margin-top: -60px !important;
        }
        
        /* Improve form usability on mobile */
        input, textarea {
            font-size: 16px !important; /* Prevents iOS zoom on focus */
        }
        
        /* Make form button full width on mobile */
        button[type="submit"] {
            width: 100% !important;
        }
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
        "Email": "example@example.com",
        "Intro": "Data Scientist | Front-End Data Consultant"
    }

# Load a Lottie animation from a URL
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Apply local CSS styles from a file
def local_css(file_name):
    try:
        with open(file_name) as f:
            st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
    except Exception:
        pass

# Apply local CSS styles from the "style.css" file          
try:
    local_css("style/style.css")
except Exception:
    pass

# Function to convert image to base64 with better error handling
def get_image_as_base64(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except Exception:
        return None

# SECTION 1: GREETING WITH PROFILE PICTURE
# Create a container to organize content
with st.container():
    # Get profile picture as base64 for embedding in HTML
    try:
        image_path = "images/me.jpg"
        img_base64 = get_image_as_base64(image_path)
        
        if img_base64:    
            # Create greeting with profile picture - WITH FORCED WHITE TEXT
            name = info['Name']
            greeting_html = f"""
            <div class="greeting-container">
                <img src="data:image/jpeg;base64,{img_base64}" class="profile-pic-greeting" alt="Nathalie Mugrauer">
                <div style="color: white !important;">
                    <h1 class="greeting-text" style="color: white !important;">Hi, I'm {name} 👋</h1>
                    <p class="intro-text" style="color: white !important;">{info["Intro"]}</p>
                </div>
            </div>
            """
            st.markdown(greeting_html, unsafe_allow_html=True)
        else:
            # Default GitHub-style avatar as fallback
            default_avatar = f"https://ui-avatars.com/api/?name={info['Name'].replace(' ', '+')}&background=1E3A5F&color=fff&size=220"
            greeting_html = f"""
            <div class="greeting-container">
                <img src="{default_avatar}" class="profile-pic-greeting" alt="Nathalie Mugrauer">
                <div style="color: white !important;">
                    <h1 class="greeting-text" style="color: white !important;">Hi, I'm {info['Name']} 👋</h1>
                    <p class="intro-text" style="color: white !important;">{info["Intro"]}</p>
                </div>
            </div>
            """
            st.markdown(greeting_html, unsafe_allow_html=True)
    except Exception:
        # Fallback to the old style if everything fails
        name = info['Name']
        st.markdown(f'''<h1 style="text-align:center;background-image: linear-gradient(to right,#1E3A5F, #4682B4);
                    font-size:60px;border-radius:2%;">
                    <span style="color:#FFFFFF;">Hi, I'm {name}   👋 </span><br>
                    <span style="color:#FFFFFF;font-size:17px;">{info["Intro"]}</span></h1>''', 
                    unsafe_allow_html=True)

# Add substantial space between greeting and timeline
st.markdown("<div style='margin-top: 40px;'></div>", unsafe_allow_html=True)

# SECTION 2: LIFE SNAPSHOT (TIMELINE) - IMPROVED FOR MOBILE
with st.container():
    st.subheader("🚀 Life Snapshot")
    
    # Load timeline data
    try:
        with open('timeline.json', "r") as f:
            timeline_data = json.load(f)
        
        # Apply styling before rendering the timeline - WITH MOBILE FIXES
        st.markdown("""
        <style>
        /* Make timeline taller */
        .timeline-container {
            height: 650px !important;
        }
        
        /* Enhance timeline styles - applied globally */
        .stApp iframe {
            border: none !important;
        }
        
        /* Mobile-specific timeline adjustments */
        @media (max-width: 768px) {
            .timeline-container {
                height: 850px !important; /* Much taller on mobile */
            }
            
            /* Improve timeline visibility on small screens */
            .timeline-container iframe {
                width: 100% !important;
            }
        }
        </style>
        """, unsafe_allow_html=True)
        
        # Display the timeline
        timeline(timeline_data, height=650)
        
    except Exception as e:
        st.error(f"Timeline error: {e}")
        st.info("Make sure 'timeline.json' is in the correct path")

# Add extra space between timeline and data tools
st.markdown("<div style='margin-top: 80px;'></div>", unsafe_allow_html=True)

# SECTION 3: DATA TOOLS - ARRANGED FOR BETTER MOBILE DISPLAY
with st.container():
    st.subheader('⚒️ Some of the data tools I have worked with')
    
    # Add a horizontal separator line
    st.markdown("<hr style='margin: 15px 0 25px 0; border-color: #e0e0e0;'>", unsafe_allow_html=True)
    
    # Create two rows with tools to better handle mobile layout
    # First row
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    
    with col1:
        st.markdown("<div style='text-align: center;'><img src='https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg' width='70' height='70'></div>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #1E3A5F;'>Python</p>", unsafe_allow_html=True)
    
    with col2:
        st.markdown("<div style='text-align: center;'><img src='https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg' width='70' height='70'></div>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #1E3A5F;'>GitHub</p>", unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style='text-align: center;'>
            <div style="display: inline-block; width: 100px; height: 70px; background-color: white; text-align: center;">
                <img src="https://www.sap.com/dam/application/shared/logos/sap-logo-svg.svg" width="70" height="35" style="margin-top: 5px;">
                <div style="font-size: 11px; margin-top: 2px; color: #1E3A5F; font-weight: bold;">Analytics Cloud</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #1E3A5F;'>SAC</p>", unsafe_allow_html=True)
        
    with col4:
        st.markdown("<div style='text-align: center;'><img src='https://jupyter.org/assets/homepage/main-logo.svg' width='70' height='70'></div>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #1E3A5F;'>JupyterLab</p>", unsafe_allow_html=True)
    
    # Add vertical spacing between rows
    st.markdown("<div style='margin-top: 30px;'></div>", unsafe_allow_html=True)

    # Second row of skills
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        st.markdown("<div style='text-align: center;'><img src='https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original.svg' width='70' height='70'></div>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #1E3A5F;'>VS Code</p>", unsafe_allow_html=True)
    
    with col2:
        st.markdown("<div style='text-align: center;'><img src='https://streamlit.io/images/brand/streamlit-mark-color.svg' width='70' height='70'></div>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #1E3A5F;'>Streamlit</p>", unsafe_allow_html=True)
    
    with col3:
        st.markdown("<div style='text-align: center;'><img src='https://scikit-learn.org/stable/_static/scikit-learn-logo-small.png' width='100' height='70'></div>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #1E3A5F;'>Machine Learning</p>", unsafe_allow_html=True)

# Add space before contact form
st.markdown("<div style='margin-top: 60px;'></div>", unsafe_allow_html=True)

# SECTION 4: CONTACT ME (AT THE BOTTOM) - IMPROVED FOR MOBILE
with st.container():
    st.subheader("📨 Contact Me")
    
    # Create a centered container for the form
    st.markdown("""
    <div style="max-width: 800px; margin: 0 auto;">
    """, unsafe_allow_html=True)
    
    contact_form = f"""
    <form action="https://formsubmit.co/{info["Email"]}" method="POST" style="width:100%">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required style="font-size: 16px;">
        <input type="email" name="email" placeholder="Your email" required style="font-size: 16px;">
        <textarea name="message" placeholder="Your message here" required style="font-size: 16px;"></textarea>
        <button type="submit" style="width: 100%; font-size: 16px; padding: 12px;">Send</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)
    
    # Close the centered container
    st.markdown("""
    </div>
    """, unsafe_allow_html=True)