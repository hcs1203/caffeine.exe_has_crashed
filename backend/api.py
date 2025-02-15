from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

def get_openai_client():
    """Returns a singleton OpenAI client."""
    api_key = os.getenv("OPENAI_API_KEY")
    return OpenAI(api_key=api_key)

client = get_openai_client()
