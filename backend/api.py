from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

def get_openai_client():
    """Returns a singleton OpenAI client."""
    api_key = os.getenv("OPENAI_API_KEY")
    return OpenAI(api_key=api_key)

client = get_openai_client()

#completion = client.chat.completions.create(
#  model="gpt-4o",
#  store=True,
#  messages=[
#    {
#        "role": "user", 
#        "content": "write a haiku about ai"
#    }
#  ]
#)

#print(completion.choices[0].message)
