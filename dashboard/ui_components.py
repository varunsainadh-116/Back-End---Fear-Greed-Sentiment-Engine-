import streamlit as st

def render_header():
    st.markdown("📊 <h1 style='margin-bottom: 0;'>Sentiment Signal AI - Crypto Assistant</h1>", unsafe_allow_html=True)
    st.markdown("🧠 <h4 style='color:gray;'>Ask anything about crypto sentiment</h4>", unsafe_allow_html=True)
    st.markdown("**Example**: 'What is the sentiment around Ethereum today?'")

def render_response_box(response: str):
    st.markdown("---")
    st.markdown("### 🤖 LLM Response:")
    st.markdown(f"<div class='response-box'>{response}</div>", unsafe_allow_html=True)

def custom_css():
    st.markdown("""
        <style>
        .reportview-container {
            padding: 2rem 4rem;
        }
        .block-container {
            padding: 2rem 4rem;
        }
        .stTextInput > div > div > input {
            font-size: 1.1rem;
            padding: 0.5rem;
        }
        .response-box {
            border: 1px solid #444;
            border-radius: 10px;
            padding: 1.5rem;
            background-color: #111;
            margin-top: 1rem;
        }
        </style>
    """, unsafe_allow_html=True)
