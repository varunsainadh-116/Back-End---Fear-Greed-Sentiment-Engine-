# Load environment variables from .env file
# This file is responsible for loading configuration settings from environment variables.
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="config/.env")

TWITTER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")
GROQ_KEY = os.getenv("GROQ_API_KEY")
