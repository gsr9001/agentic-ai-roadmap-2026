# Day 5 - Prompt Engineering

## Objective

Learn how to design effective prompts for LLM applications
and understand how prompt structure influences model responses.

## Concepts

- Zero-shot
- Few-shot
- Role-based prompting
- Output formatting
- Constraints
- Prompt refinement

## Prompt Architecture

A good prompt can be structured as:

Role
+
Context
+
Task
+
Format
+
Constraints

## Zero-Shot Prompting

Give the model a task without providing examples.

Example:

Explain Ohm's Law.

## Few-Shot Prompting

Provide examples before asking the model to perform the
actual task.

Example:

Example 1 → desired output

Example 2 → desired output

Actual input → desired output

## Role-Based Prompting

Assign a role to the model.

Example:

You are an experienced electrical engineering professor.

## Output Formatting

Tell the model exactly how the answer should be structured.

Example:

Definition:
Example:
Analogy:
Key takeaway:

## Constraints

Constraints control the response.

Examples:

- Maximum 100 words
- Use simple English
- Give 5 bullet points
- Avoid technical jargon

## Prompt Refinement

Prompt refinement means improving a prompt based on the
quality of the model's response.

Basic prompt:

Explain transformers.

Improved prompt:

You are an electrical engineering professor.
Explain transformers to a first-year engineering student.
Use one real-life analogy and provide the answer in five
sections.

## Project

### AI Study Assistant

The application accepts a topic from the user and generates
a structured explanation using a carefully designed prompt.

## Prompt Flow

User Topic
    ↓
Role
    ↓
Context
    ↓
Task
    ↓
Format
    ↓
Constraints
    ↓
LLM
    ↓
Structured Response

## Technologies

- Python
- OpenAI API
- OpenAI Python SDK
- python-dotenv
- Git
- GitHub

## Security

The real `.env` file is never committed.

Only `.env.example` is included in the repository.