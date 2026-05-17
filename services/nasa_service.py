import requests
from config.settings import NASA_APOD_URL, REQUEST_TIMEOUT

def get_apod():
    if not NASA_APOD_URL:
        return {}

    try:
        response = requests.get(NASA_APOD_URL, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        data = response.json()

        if not isinstance(data, dict):
            return {}

        if data.get("error"):
            return {}

        return {
            "title": data.get("title", ""),
            "url": data.get("url", ""),
            "explanation": data.get("explanation", ""),
            "media_type": data.get("media_type", "")
        }

    except Exception:
        return {}