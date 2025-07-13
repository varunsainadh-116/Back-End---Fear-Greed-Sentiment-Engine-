from dotenv import load_dotenv
import os
from groq import Groq

# Explicit path to the .env file inside config/ (or move .env to root and use load_dotenv() alone)
load_dotenv(dotenv_path="config/.env")

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# ✅ Define the Groq client
client = Groq(api_key=GROQ_API_KEY)

def get_trade_suggestion(prompt: str) -> str:
    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",  # You can also test with llama3-70b-8192 if needed
            messages=[
                {"role": "system", "content": "You are a crypto investment advisor."},
                {"role": "user", "content": prompt},
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"❌ Groq API Error: {e}")
        return "→ Could not fetch suggestion at the moment."
