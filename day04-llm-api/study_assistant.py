import os

from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Get API key from .env
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY is not set.")

# Create OpenAI client
client = OpenAI(api_key=api_key)


# Ask the user for a question
question = input("Ask your study question: ")


# Send request to the LLM
response = client.responses.create(
    model="gpt-5-mini",
    input=f"""
You are a helpful engineering study assistant.

Explain the following topic clearly.
Use simple language, examples, and important points.

Question:
{question}
"""
)

# Display the answer
print("\n--- Study Assistant ---")
print(response.output_text)