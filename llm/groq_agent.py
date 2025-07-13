from dotenv import load_dotenv
import os
from groq import Groq

# Explicit path to the .env file inside config/ (or move .env to root and use load_dotenv() alone)
load_dotenv(dotenv_path="config/.env")

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# ✅ Define the Groq client
client = Groq(api_key=GROQ_API_KEY)
def get_trade_suggestion(user_prompt: str, system_prompt: str = "You are a crypto investment advisor.") -> str:
    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"❌ Groq API Error: {e}")
        return "→ Could not fetch suggestion at the moment."
