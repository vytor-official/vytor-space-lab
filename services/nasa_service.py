import requests
from config.settings import NASA_APOD_URL, REQUEST_TIMEOUT

def get_apod():
    try:
        response = requests.get(NASA_APOD_URL, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        data = response.json()

        if not isinstance(data, dict):
            return {}

        if data.get("media_type") != "image":
            return {
                "title": data.get("title", "NASA Astronomy Picture of the Day"),
                "url": "",
                "explanation": data.get("explanation", "No image available today.")
            }

        return data
    except Exception:
        return {}