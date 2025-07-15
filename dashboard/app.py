import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from utils.handlers import handle_text_input
from utils.sentiment_utils import get_sentiment_score
from utils.helpers import extract_ticker
from utils.signal_utils import generate_signal
from dashboard.ui_components import render_trade_signal
from utils.market_utils import get_market_stats


# Page setup
st.set_page_config(page_title="Sentiment Signal AI", layout="centered")

# ---------------- HEADER ----------------
st.markdown("<h1 style='text-align: center;'>📊 Sentiment Signal AI - Crypto Assistant</h1>", unsafe_allow_html=True)
st.markdown(
    "<div style='text-align: center;'>🧠 <strong>Ask anything about crypto sentiment</strong><br><small>Try: <code>What is the sentiment around Ethereum today?</code> or paste a tweet/Reddit link.</small></div>",
    unsafe_allow_html=True
)

st.markdown("")

# ---------------- INPUT ----------------
user_input = st.text_input("🔍 Enter your query or URL", placeholder="e.g., What's the outlook for BTC this week?")

if user_input:
    with st.spinner("⏳ Analyzing market signals..."):
        response = handle_text_input(user_input)

        # Extract ticker, sentiment, price
        ticker = extract_ticker(user_input)
        ticker = ticker if ticker else "BTC"
        sentiment = float(get_sentiment_score(user_input))
        market = get_market_stats(ticker)
        price = float(market["price"].replace("%", ""))
        volatility = market["raw_volatility"]

        signal = generate_signal(sentiment, price, volatility)



        # ---------------- METRICS ----------------
        st.markdown("---")
        st.markdown(f"### 📈 Market Metrics for `{ticker}`")

        col1, col2, col3 = st.columns(3)
        col1.metric(label="🧠 Sentiment Score", value=sentiment)
        col2.metric(label="💸 24h Price Change", value=market["price"])
        col3.metric(label="📊 Volatility", value=market["volatility"])

        
        # Show signal
        render_trade_signal(signal)


        # ---------------- RESPONSE ----------------
        st.markdown("---")
        st.markdown("### 🤖 LLM Response:")
        st.markdown(f"<div style='background-color: #111111; padding: 20px; border-radius: 10px; color: #eeeeee;'>{response}</div>", unsafe_allow_html=True)
