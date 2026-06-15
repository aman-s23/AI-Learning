from openai import OpenAI
from dotenv import load_dotenv
import os

# Load variables from .env
load_dotenv()

# Create OpenAI client
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# Send request to model
response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
    {
        "role": "system",
        "content": """
        You are a fraud detection engine.

        Return ONLY valid JSON.

        Example format:
        {
            "risk_level": "high",
            "reason": "device reuse",
            "action": "block"
        }
        """
    },
    {
        "role": "user",
        "content": "User created 9 accounts from same device in 2 hours"
    }
]
)

# Print AI response
print(response.choices[0].message.content)