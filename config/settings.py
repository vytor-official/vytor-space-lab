import os

APP_NAME = "Vytor Space Intelligence"
NASA_API_KEY = os.getenv("NASA_API_KEY", "")
NASA_APOD_URL = f"https://api.nasa.gov/planetary/apod?api_key={NASA_API_KEY}" if NASA_API_KEY else ""
NASA_ASTEROID_URL = f"https://api.nasa.gov/neo/rest/v1/feed?api_key={NASA_API_KEY}" if NASA_API_KEY else ""
ISS_POSITION_URL = "http://api.open-notify.org/iss-now.json"
REQUEST_TIMEOUT = 10