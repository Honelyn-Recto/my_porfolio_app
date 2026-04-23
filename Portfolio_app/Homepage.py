import streamlit as st

# Configure the page
st.set_page_config(page_title="Honelyn Recto | Portfolio", layout="wide")

# Apply custom styles for a dark, elegant theme
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Syne:wght@800&family=DM+Sans&display=swap');
    
    .stApp {
        background-color: #1313;
    }
    .welcome-container {
        text-align: center;
        padding-top: 20vh;
    }
    .name-text {
        font-family: 'Syne', sans-serif;
        font-size: 72px;
        color: #1313;
        margin-bottom: 10px;
    }
    .sub-text {
        font-family: 'DM Sans', sans-serif;
        font-size: 20px;
        color: #23a;
        letter-spacing: 2px;
        text-transform: uppercase;
    }
</style>
""", unsafe_allow_html=True)

# Display the content
st.markdown("""
<div class="welcome-container">
    <div class="sub-text">Welcome to my portfolio</div>
    <h1 class="name-text">Honelyn Recto</h1>
    <p style="color: #1e1e2e; font-size: 18px;">Computer Science Student · Masbate, PH</p>
</div>
""", unsafe_allow_html=True)