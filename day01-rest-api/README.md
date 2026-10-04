# Day 1 - REST APIs

## Objective

Learn the fundamentals of REST APIs and understand how Python
applications communicate with external services.

## Concepts Learned

- API
- Client
- Server
- HTTP
- GET
- JSON
- Status Codes
- Python Requests Library
- Nested JSON

## HTTP Request Flow

Python Client
      |
      | GET Request
      ↓
REST API Server
      |
      | JSON Response
      ↓
Python Application

## Status Codes

| Code | Meaning |
|------|---------|
| 200  | OK |
| 201  | Created |
| 400  | Bad Request |
| 401  | Unauthorized |
| 403  | Forbidden |
| 404  | Not Found |
| 500  | Internal Server Error |

## Programs

### 1. basic_api.py

Sends a GET request to the JSONPlaceholder API and displays
the complete JSON response.

### 2. user_api.py

Retrieves a specific user and extracts:

- Name
- Email
- City
- Company

## Technologies Used

- Python
- Requests
- REST API
- JSON
- Git
- GitHub

## How to Run

Install the requests library:

```bash
pip install requests