# Day 4 - LLM API

## Objective

Learn how to connect a Python application to an LLM API
and build a simple AI-powered study assistant.

## Concepts Learned

- LLM
- LLM API
- API Key
- Environment Variables
- Prompt
- Model
- API Request
- AI-generated Response
- OpenAI Python SDK

## Architecture

User
  |
  | Question
  ↓
Study Assistant
  |
  | API Request
  ↓
LLM API
  |
  | Generated Response
  ↓
Study Assistant
  |
  ↓
User

## Project

### AI Study Assistant

The application accepts a study question from the user
and sends it to an LLM.

The LLM generates an easy-to-understand answer.

## Example

Input:

```text
Explain Ohm's Law.