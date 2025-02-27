import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post

# Custom Styling
st.markdown("""
    <style>
        /* Background and App Styling */
        .stApp {
            background-color: #5A7EC7; /* Adjusted to a medium blue */
            color: #0a1931;
        }
        /* Title Styling */
        .title {
            font-size: 40px;
            font-weight: bold;
            color: #ffffff;
            text-align: center;
            margin-bottom: 5px;
        }
        .subtitle {
            font-size: 22px;
            color: #ffffff;
            text-align: center;
            margin-bottom: 20px;
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
        }
        .stButton > button:hover {
            background-color: #c92a2a;
        }
        /* Output Box */
        .output-box {
            background-color: #ffffff;
            padding: 15px;
            border-radius: 10px;
            box-shadow: 0px 4px 10px rgba(10, 25, 49, 0.2);
            margin-top: 20px;
            font-size: 18px;
            color: #0a1931;
            border-left: 5px solid #0a1931;
        }
    </style>
""", unsafe_allow_html=True)

# Options for Length & Language
length_options = ["Short", "Medium", "Long"]
language_options = ["English", "Hinglish"]

# App Title
st.markdown('<div class="title">🚀 BrandBoost</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI-Powered LinkedIn Post Generator</div>', unsafe_allow_html=True)

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
    st.markdown(f'<div class="output-box">{post}</div>', unsafe_allow_html=True)

    # Copy Button
    st.button("📋 Copy to Clipboard", key="copy_button")

