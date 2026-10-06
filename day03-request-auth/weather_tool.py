import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENWEATHER_API_KEY")

if api_key:
    print("Weather API key loaded successfully.")
else:
    print("Weather API key not found.")