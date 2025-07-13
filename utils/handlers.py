# utils/handlers.py

from llm.groq_agent import get_trade_suggestion

def handle_text_input(prompt: str) -> str:
    """
    Handles raw user questions like 'What is the sentiment around Ethereum?'
    """
    system_prompt = (
        "You are a crypto investment advisor. Analyze the user's question using your market knowledge, "
        "social media sentiment, and historical behavior."
    )

    full_prompt = f"{prompt}"
    
    return get_trade_suggestion(full_prompt, system_prompt=system_prompt)
