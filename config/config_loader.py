# Load environment variables from .env file
# This file is responsible for loading configuration settings from environment variables.
# config/config_loader.py

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Reddit API Keys
REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
REDDIT_SECRET = os.getenv("REDDIT_SECRET")
REDDIT_USER_AGENT = os.getenv("REDDIT_USER_AGENT")  # ✅ Add this line

# Twitter API
TWITTER_BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")

# News API
NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")

# Groq API
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

