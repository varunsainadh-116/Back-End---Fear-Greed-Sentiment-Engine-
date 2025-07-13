# dashboard/app.py

import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.handlers import handle_text_input


st.title("📊 Sentiment Signal AI - Crypto Assistant")

st.subheader("🧠 Ask anything about crypto sentiment")
user_query = st.text_input("Example: 'What is the sentiment around Ethereum today?'")

if st.button("Get Suggestion"):
    if user_query.strip() != "":
        with st.spinner("Thinking..."):
            response = handle_text_input(user_query)
        st.markdown("### 🤖 LLM Response:")
        st.write(response)
    else:
        st.warning("Please enter a query.")
