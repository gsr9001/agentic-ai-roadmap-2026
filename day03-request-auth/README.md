# Day 3 - Request Authentication

## Objective

Learn how API authentication works and how to securely
manage API keys using environment variables.

## Concepts Learned

- API Authentication
- API Keys
- Environment Variables
- `.env`
- `.env.example`
- `.gitignore`
- python-dotenv
- Secure API key management

## Why API Keys?

Many APIs require authentication before allowing an
application to access their services.

Example:

Python Application
       |
       | API Key
       ↓
External API
       |
       ↓
Response

## Environment Variables

Instead of storing API keys directly in Python code,
we store them in environment variables.

Example:

```text
OPENAI_API_KEY=your_api_key_here