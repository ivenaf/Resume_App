import streamlit as st

st.set_page_config(
    page_title="DPW | Digital Process Flow",
    layout="wide",
    page_icon="🔗",
    initial_sidebar_state="expanded"
)

st.title("🔗 DPW – Digital Process Flow")

st.markdown("""
Welcome to the Digital Process Flow (DPW) demo page.

You can explore the DPW Streamlit app by clicking the link below:
""")

st.markdown("""
<div style="text-align: center; margin: 40px 0;">
    <a href="https://ivenaf-dpw-1--home-ynwloa.streamlit.app/" target="_blank" style="
        background-color: #4682B4;
        color: white;
        padding: 18px 32px;
        border-radius: 8px;
        font-size: 22px;
        font-weight: bold;
        text-decoration: none;
        box-shadow: 0 4px 12px rgba(70,130,180,0.15);
        display: inline-block;
        transition: background 0.2s;
    " onmouseover="this.style.backgroundColor='#1E3A5F';" onmouseout="this.style.backgroundColor='#4682B4';">
        👉 Open DPW Streamlit App
    </a>
</div>
""", unsafe_allow_html=True)

st.info("The DPW app will open in a new browser tab.")