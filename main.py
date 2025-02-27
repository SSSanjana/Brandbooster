import streamlit as st
import pyperclip
from few_shot import FewShotPosts
from post_generator import generate_post

# Custom Styling
st.markdown("""
    <style>
        /* Background and App Styling */
        .stApp {
            background: linear-gradient(135deg, #1e3c72, #2a5298);
            color: #ffffff;
        }
        /* Title Styling */
        .title-container {
            text-align: center;
            margin-bottom: 20px;
        }
        .title {
            font-size: 42px;
            font-weight: 800;
            font-family: 'Poppins', sans-serif;
            color: #ffffff;
            text-transform: uppercase;
            letter-spacing: 2px;
        }
        .subtitle {
            font-size: 22px;
            font-weight: 500;
            font-family: 'Lora', serif;
            color: #e0e0e0;
        }
        /* Dropdown and Button Styling */
        .stSelectbox, .stButton > button {
            border-radius: 10px;
        }
        .stButton > button {
            background-color: #e63946;
            color: white;
            font-weight: bold;
            border: none;
            padding: 10px 20px;
            transition: 0.3s ease-in-out;
            font-size: 16px;
            font-family: 'Poppins', sans-serif;
        }
        .stButton > button:hover {
            background-color: #c92a2a;
        }
        /* Output Box */
        .output-box {
            background-color: #ffffff;
            padding: 15px;
            border-radius: 10px;
            box-shadow: 0px 4px 10px rgba(255, 255, 255, 0.2);
            margin-top: 20px;
            font-size: 18px;
            color: #0a1931;
            border-left: 5px solid #ffffff;
            font-family: 'Lora', serif;
        }
    </style>
""", unsafe_allow_html=True)

# Options for Length & Language
length_options = ["Short", "Medium", "Long"]
language_options = ["English", "Hinglish"]

# App Title
st.markdown(
    '<div class="title-container"><div class="title">🚀 BrandBoost</div><div class="subtitle">AI-Powered LinkedIn Post Generator</div></div>',
    unsafe_allow_html=True)

# Layout for Inputs
fs = FewShotPosts()
tags = fs.get_tags()

col1, col2, col3 = st.columns(3)

with col1:
    selected_tag = st.selectbox("🔖 Topic", options=tags)

with col2:
    selected_length = st.selectbox("📏 Length", options=length_options)

with col3:
    selected_language = st.selectbox("🗣️ Language", options=language_options)

# Generate Button with Spinner
if st.button("✨ Generate Post"):
    with st.spinner("Generating your LinkedIn post..."):
        post = generate_post(selected_length, selected_language, selected_tag)

    # Display the Generated Post Inside a Box
    st.markdown("**Copy this post:**")
    st.code(post, language="markdown")  # Use `st.code` for clean formatting

    # Copy to Clipboard Button
    if st.button("📋 Copy to Clipboard"):
        pyperclip.copy(post)
        st.success("Copied to clipboard!")

