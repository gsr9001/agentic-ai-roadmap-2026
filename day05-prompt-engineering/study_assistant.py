import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY is not set.")

client = OpenAI(api_key=api_key)

question = input("What topic do you want to learn? ")

prompt = f"""
Role:
You are an expert engineering professor and AI tutor.

Context:
The student is learning the topic for the first time.

Task:
Explain the following topic clearly:

{question}

Format:
1. Definition
2. Simple explanation
3. Real-life analogy
4. Example
5. Key takeaway

Constraints:
- Use simple English.
- Assume beginner-level knowledge.
- Avoid unnecessary jargon.
- Keep the explanation concise.
"""

response = client.responses.create(
    model="gpt-5-mini",
    input=prompt
)

print("\n========== AI STUDY ASSISTANT ==========\n")
print(response.output_text)