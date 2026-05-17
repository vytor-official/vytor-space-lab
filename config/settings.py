import os

APP_NAME = "Vytor Space Intelligence"
NASA_API_KEY = os.getenv("NASA_API_KEY", "")
NASA_APOD_URL = f"https://api.nasa.gov/planetary/apod?api_key={NASA_API_KEY}"
NASA_ASTEROID_URL = f"https://api.nasa.gov/neo/rest/v1/feed?api_key={NASA_API_KEY}"
ISS_POSITION_URL = "http://api.open-notify.org/iss-now.json"
ISS_STREAM_URL = "https://www.youtube.com/embed/OCem0E-0Q6Y"
REQUEST_TIMEOUT = 10