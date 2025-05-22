import streamlit as st
import requests
from prompts import generate_prompt

# Set page config before anything else
st.set_page_config(page_title="ELI5 Bot", layout="centered")

# --- CSS Styling
st.markdown("""
    <style>
    /* Full background GIF */
    .stApp {
        # background-image: url("C:\Users\nidhi\OneDrive\Desktop\eli5-bot\background.jpg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }

   
    .stApp::before {
        content: "";
        position: fixed;
        top: 0; left: 0;
        width: 100vw;
        height: 100vh;
        background-color: rgba(255, 255, 255, 0.8);  /* Adjust for light/dark effect */
        z-index: -1;
    }

    h1 {
        text-align: center;
        color: #d94f3a;
        font-size: 4em;
        font-family: Georgia, serif;
        margin-bottom: 0.1em;
    }

    .subtext {
        text-align: center;
        color: #b13b2e;
        font-size: 1.4em;
        margin-bottom: 2em;
        font-family: Georgia, serif;
    }

    .stButton > button {
        background-color: #d94f3a;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 0.6em 1.2em;
        font-size: 1.1em;
        font-family: 'Georgia', serif;
    }

    .stButton > button:hover {
        background-color: #b13b2e;
    }

    .stTextInput > div > div > input,
    .stSelectbox > div {
        margin-left: auto;
        margin-right: auto;
        display: block;
        width: 300px;
    }
    body {
        background-color: #f6e9e4;
    }

    .main {
        background-color: #f6e9e4;
        text-align: center;
        font-family: 'Georgia', serif;
    }

    h1 {
        color: #d94f3a;
        font-size: 4em;
        margin-bottom: 0.1em;
    }

    .subtext {
        color: #b13b2e;
        font-size: 1.4em;
        margin-bottom: 2em;
    }

    input, .stButton > button {
        font-size: 1.1em;
        padding: 0.5em 1em;
        border-radius: 5px;
    }

    .stButton > button {
        background-color: #d94f3a;
        color: white;
        border: none;
        margin-top: 1em;
    }

    .stButton > button:hover {
        background-color: #b13b2e;
    }

    .block-container {
        padding-top: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# --- Header and Description
st.markdown("<h1>ELI-5 Bot 🧠</h1>", unsafe_allow_html=True)
st.markdown("<h5>Explain Like I'm 5 - For simple explanations to not-so-simple topics! </h5>", unsafe_allow_html=True)
st.markdown("<p class='subtext'>Enter a topic and get a fun explanation!</p>", unsafe_allow_html=True)

# --- Inputs
topic = st.text_input("Enter a topic you'd like explained:")
level = st.selectbox("Select explanation level:", ["Beginner", "Intermediate", "Advanced"])

# --- API Setup
api_key = st.secrets["TOGETHER_API_KEY"]
endpoint = "https://api.together.xyz/v1/chat/completions"
model = "mistralai/Mistral-7B-Instruct-v0.1"

# --- Button and API Call
if st.button("Explain"):
    if not topic:
        st.warning("Please enter a topic to explain.")
    else:
        with st.spinner("Thinking..."):
            prompt = generate_prompt(topic, level)
            headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            }
            data = {
                "model": model,
                "messages": [{"role": "user", "content": prompt}]
            }
            response = requests.post(endpoint, headers=headers, json=data)

            if response.status_code == 200:
                answer = response.json()['choices'][0]['message']['content']
                st.markdown("### ✨ Explanation")
                st.success(answer)
            else:
                st.error(f"Error: {response.status_code} - {response.text}")
 