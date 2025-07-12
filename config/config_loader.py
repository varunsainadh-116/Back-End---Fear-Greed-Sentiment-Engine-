# Load environment variables from .env file
# This file is responsible for loading configuration settings from environment variables.
# config/config_loader.py

from dotenv import load_dotenv
import os
from pathlib import Path

# Load environment variables from .env file
env_path = Path("config") / ".env"
load_dotenv(dotenv_path=env_path)

# Access variables
TWITTER_BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")
REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
REDDIT_SECRET = os.getenv("REDDIT_SECRET")
NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
