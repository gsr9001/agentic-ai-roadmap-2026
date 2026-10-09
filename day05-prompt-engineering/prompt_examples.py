import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY is not set.")

client = OpenAI(api_key=api_key)


def ask_llm(prompt):
    response = client.responses.create(
        model="gpt-5-mini",
        input=prompt
    )

    return response.output_text


# --------------------------------------------------
# 1. ZERO-SHOT PROMPTING
# --------------------------------------------------

zero_shot_prompt = """
Explain Ohm's Law.
"""

print("\n===== ZERO-SHOT =====")
print(ask_llm(zero_shot_prompt))


# --------------------------------------------------
# 2. ROLE-BASED PROMPTING
# --------------------------------------------------

role_prompt = """
You are an experienced electrical engineering professor.

Explain Ohm's Law to a first-year engineering student
using a simple real-life analogy.
"""

print("\n===== ROLE-BASED =====")
print(ask_llm(role_prompt))


# --------------------------------------------------
# 3. FEW-SHOT PROMPTING
# --------------------------------------------------

few_shot_prompt = """
Convert the following topics into simple explanations.

Example 1:
Topic: Voltage
Explanation: Voltage is the electrical pressure that
pushes current through a circuit.

Example 2:
Topic: Current
Explanation: Current is the flow of electric charge.

Now explain:

Topic: Resistance
"""

print("\n===== FEW-SHOT =====")
print(ask_llm(few_shot_prompt))


# --------------------------------------------------
# 4. OUTPUT FORMATTING
# --------------------------------------------------

format_prompt = """
Explain Ohm's Law.

Return the answer exactly in this format:

Definition:
Real-life analogy:
Formula:
Example:
Key takeaway:
"""

print("\n===== OUTPUT FORMATTING =====")
print(ask_llm(format_prompt))


# --------------------------------------------------
# 5. CONSTRAINTS
# --------------------------------------------------

constraint_prompt = """
Explain Ohm's Law.

Constraints:
- Use simple English.
- Maximum 100 words.
- Use one real-life analogy.
- Include the formula.
- Do not use complex mathematical terminology.
"""

print("\n===== CONSTRAINTS =====")
print(ask_llm(constraint_prompt))