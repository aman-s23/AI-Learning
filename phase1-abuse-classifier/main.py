from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

content = input("Enter content to classify: ")

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    temperature=0,
    messages=[
        {
            "role": "system",
            "content": """
You are a Trust & Safety abuse classifier.

Classify the user's content into exactly one abuse_type:
- spam
- impersonation
- harassment
- copyright
- safe


Risk level must be exactly one of:
- low
- medium
- high

Action must be exactly one of:
- allow
- review
- remove

Return ONLY valid JSON in this format:
{
  "abuse_type": "",
  "risk_level": "",
  "action": "",
  "reasoning": ""
}
"""
        },
        {
            "role": "user",
            "content": content
        }
    ]
)

print(response.choices[0].message.content)